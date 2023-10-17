import requests
import geopandas as gpd
import os
import logging
import shutil
import math
from typing import Optional, Tuple, Any, List, Callable
from georeader.logic.ogr.data_source import OGR_DataSource
from georeader.handlers.base_handler import BaseHandler
from georeader.logic.thread_helper import get_session, threadpool_download
from owslib.wfs import WebFeatureService
from georeader.handlers.helpers.directory_helper import DirectoryHelper
from georeader.logic.converters import Converters
from georeader.logic.main_helpers import (
    remove_key,
    match_on,
)
from georeader.logic.error_exceptions import NotValid

LOGGER = logging.getLogger("__name__")


class WFSHandler(BaseHandler, DirectoryHelper):

    handler_type = "wfs"
    source_type = "service"

    def __init__(self, url):
        super().__init__(tmp_dir=None)
        self.url = url
        self.version = None
        self._data_source = None
        self._metadata = {}
        if "?" in self.url:
            self.base_url = self.url.split("?")[0]
        else:
            self.base_url = self.url
        self.token = self._get_key_from_url()
        self.create_working_dir()
        if not self.check_valid():
            raise NotValid(
                self.check_valid, f"{url} does not appear to be a valid WFS service"
            )
        LOGGER.debug("initializing WFSHandler")
        LOGGER.debug(vars(self))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.delete_working_dir()

    def get_dataframe(self, type_name: str = None):
        if self.version == "2.0.0":
            if self.check_if_layer_in_service(type_name):
                return self._get_dataframe_2(type_name)
            else:
                raise Exception(
                    f"Could not find any service matching type name {type_name}"
                )
        if self.version == "1.1.0" or self.version == "1.0.0":
            if self.check_if_layer_in_service(type_name):
                return self._get_dataframe_1(type_name)
            else:
                raise Exception(
                    f"Could not find any service matching type name {type_name}"
                )
        else:
            logging.error("could not get version type.")
            raise Exception("could not get version type.")

    def _get_key_from_url(self) -> dict:
        """uses regex to look through url and find possible authkey to pull out.

        Returns:
            tuple: key and value
        """
        tokens = ["authkey", "id", "token", "authentication", "key"]
        for token in tokens:
            match = match_on(token, self.url)
            if match:
                pos_1, pos_2 = match.regs[0][0], match.regs[0][1]
                authkey = self.url[pos_1:pos_2]
                key = authkey.split("=")[0]
                val = authkey.split("=")[1]
                return {key: val}
        return {}

    def check_if_layer_in_service(self, type_name: str) -> bool:
        matched = []
        for layer in self.get_layers():
            if type_name == layer['name']:
                return True
            if type_name == layer['name'].split(":")[1]:
                matched.append(layer['name'])
        if len(matched) > 1:
            LOGGER.warning(f"service has more than one service that match {type_name}")
        if len(matched) > 0:
            return True
        else:
            return False

    def check_valid(self) -> bool:
        """try allowed version return most recent verison."""
        for version in ("2.0.0", "1.1.0", "1.0.0"):
            try:
                params: dict = {
                    "version": version,
                    "service": "wfs",
                }
                params = {**params, **self.token}
                request_url = (
                    requests.Request("GET", self.base_url, params=params).prepare().url
                )
                data_source = OGR_DataSource(_input=request_url, _type="WFS")
                if data_source.data_source is None:
                    return False
                for type_name in data_source.get_all_layer_names():
                    self._metadata[type_name] = {
                        "name": type_name,
                        "schema": None,
                        "feature_count": None,
                        "extent": None,
                        "geom_type": None,
                        "crs_code": None,
                    }
                self._data_source = data_source
                self.version = version
                return True
            except Exception as e:
                logging.error(e)
        return False

    def build_params(
        self,
        type_name=None,
        request=None,
        output_format="GML3",
        xmlns=None,
        result_type=None,
        srs=None,
        bbox=None,

    ):
        """
            The build_params function is used to build the parameters for a WFS request.

            Args:
                self: Refer to the object itself
                type_name: Identify the layer to be queried
                request: Specify the type of request to be made
                output_format: Specify the output format of the response
                xmlns: Specify the namespace of the request
                result_type: Specify the type of result that you want to get back from the wfs
                srs: Specify the spatial reference system of the output
                bbox: Specify the bounding box of the area to be queried
                : Specify the type of request

            Returns:
                A dictionary of parameters
        """
        params = {
            "version": "2.0.0",
            "request": request,
            "typename": type_name,
            "resultType": result_type,
            "outputFormat": output_format,
            "xmlns": xmlns,
            "service": "wfs",
            "SRSNAME": srs,
            "bbox": bbox
        }
        params = {**params, **self.token}
        for key in params.keys():
            if params[key] is None:
                params = remove_key(params, key)
        return params

    def get_layers(self) -> Optional[List[Any]]:
        """user owslib to get layers from wfs service.

        Returns:
            [type]: [description]
        """
        try:
            return [{"name": x} for x in self._metadata.keys()]
        except Exception as e:
            LOGGER.warning(
                f"failed to fetch layer from url invalid wfs: {self.url()}, {e}"
            )
        return None

    def get_layer_count(self) -> int:
        """returns layer count
        Returns:
            Int: total layer count
        """
        return self._data_source.get_layer_count()

    def get_geom_type(self, layer_name: str = None) -> str:
        """returns geom type for layer
        Returns:
            str: name of geom type e.g polygon, point...
        """
        return self.get_metadata_attribute("geom_type", layer_name)

    def get_crs_code(self, layer_name: str = None) -> str:
        """returns CRS code for layer.
        Args:
            layer_name:

        Returns:

        """
        return self.get_metadata_attribute("crs_code", layer_name)

    def get_extent(self, layer_name: str = None) -> Tuple[float]:
        """return extent for layer.
        Args:
            layer_name (str, optional): [description]. Defaults to None.
        Returns:
            Tuple: return max bounds of layer.
        """
        return self.get_metadata_attribute("extent", layer_name)

    def format_url(self) -> str:
        """
        returns:
            [type]: [description]
        """
        tokens = ["authkey", "id", "token", "authentication", "key"]
        authkey = None
        local_url = self.url
        for token in tokens:
            match = match_on(token, self.url)
            if match:
                pos_1, pos_2 = match.regs[0][0], match.regs[0][1]
                authkey = self.url[pos_1:pos_2]
                break
        if "?" in self.url:
            local_url = local_url.split("?")[0]
        local_url = f"{local_url}?service=wfs"
        if authkey is not None:
            local_url = f"{local_url}&{authkey}"
        return local_url

    def get_accepted_formats(self) -> list:
        """get supported formats from wfs service

        Returns:
            list: list of supported format strings.
        """
        web_feature_service = WebFeatureService(url=self.url, version=self.version)
        formats = (
            web_feature_service.getOperationByName("GetFeature")
            .parameters.get("outputFormat", {})
            .get("values")
        )
        return [f.lower() for f in formats]

    def get_schema(self, layer_name: str) -> List[str]:
        """returns schema for layer. if only one layer is present no name is needed, if there are more than one layers,
        layer name or id must be provided.
        Args:
            layer_name (str, optional): [description]. Defaults to None.
        Returns:
            list: list: return list of attribute names.
        """
        return self.get_metadata_attribute("schema", layer_name)

    def get_capabilities_data(self):
        """does a getCapabilities request to wfs service.

        Returns:
            [requests.response]: [description]
        """
        params = self.build_params(request="getCapabilities", output_format="gml")
        resp = requests.get(self.base_url, params=params)
        return resp

    def get_feature_count(self, layer_name: str) -> int:
        """get the total number of features within layer.
        Args:
            layer_name (str): the name of the layer to get feature count for.
        Returns:
            int: total features
        """
        return self.get_metadata_attribute("feature_count", layer_name)

    def get_extent(self, layer_name: str = None) -> Tuple[float]:
        """return extent for layer.
        Args:
            layer_name (str, optional): [description]. Defaults to None.
        Returns:
            Tuple: return max bounds of layer.
        """
        return self.get_metadata_attribute("extent", layer_name)

    def download_data_in_chunks(self, type_name, output_format=None):
        """downloads layer data in chunks
        Args:
            type_name (str): name of layer to download.
            output_format ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        params = self.build_params(
            request="getFeature", type_name=type_name, output_format=output_format
        )
        request_url = (
            requests.Request("GET", self.base_url, params=params).prepare().url
        )
        if output_format == "json":
            local_filename = f"{self.working_dir}/{self.tmp_id}-{type_name}.json"
        else:
            local_filename = f"{self.working_dir}/{self.tmp_id}-{type_name}.xml"
        with requests.get(request_url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, "wb") as f:
                for chunk in r.iter_content(chunk_size=16384):
                    f.write(chunk)
        return local_filename

    def download_data(self, type_name: str, output_format: str = None):
        """download all features in one request.

        Args:
            type_name (str): name of layer within wfs.
            output_format (str, optional): [description]. Defaults to None.

        Raises:
            Exception: raised when

        Returns:
            [type]: [description]
        """
        params = self.build_params(
            request="getFeature", type_name=type_name, output_format=output_format
        )
        request_url = (
            requests.Request("GET", self.base_url, params=params).prepare().url
        )
        try:
            resp = requests.get(request_url)
            LOGGER.info(f"downloading data from {request_url}")
        except Exception as e:
            logging.error(e)
            raise Exception(e)
        if resp.status_code == 200:
            if output_format == "json":
                local_filename = f"{self.working_dir}/{self.tmp_id}-{type_name}.json"
            elif output_format == "shape-zip":
                local_filename = f"{self.working_dir}/{self.tmp_id}-{type_name}.zip"
            else:
                local_filename = f"{self.working_dir}/{self.tmp_id}-{type_name}.xml"
            f = open(local_filename, "wb")
            f.write(resp.content)
            f.close()
            return local_filename
        else:
            self.delete_working_dir()
            raise Exception(
                f"failed to fetch data from service, error code: {resp.status_code }"
            )

    def _get_dataframe_1(self, type_name: str, request_format=None):
        """downloads data and converts it into a geo data frame

        Args:
            type_name (string): name of wfs feature
            request_format (string, optional): format data will be downloaded in, if none is provided
                it will automatically choose the fastest possible method for downloading. supported formats
                are shape-files, gml3, gml and json. please check the wfs you are using supports the format
                you are trying to use. Defaults to None.

        Raises:
            ValueError: raised if invalid request format is passed.

        Returns:
            geopandas.geodataframe: geopandas dataframe.
        """
        # if request_format not in ('shape-zip', 'gml3', 'gml','json'):
        if request_format is None:
            accepted_formats = self.get_accepted_formats()
            dl_formats = ("shape-zip", "gml3", "gml")
            for dl_format in dl_formats:
                if dl_format.lower() in accepted_formats:
                    request_format = dl_format
                    break

        if request_format not in ("shape-zip", "gml3", "gml", "json"):
            raise ValueError(f"Error: {request_format} is not accepted format.")
        input_file = self.download_data(type_name, request_format)
        if request_format.lower() in ["json", "shape-zip"]:
            gdf = gpd.read_file(input_file)
        else:
            try:
                shape_file_folder = os.path.join(
                    self.working_dir, f"{type_name}-shp_file"
                )
                os.mkdir(shape_file_folder)
                output_file = os.path.join(shape_file_folder, f"{type_name}.shp")
                Converters().convert_gml_to_shape_file(
                    input_file=input_file, output_file=output_file
                )
                gdf = gpd.read_file(output_file)
                return gdf
            except Exception as e:
                LOGGER.error(e)
                raise Exception("Failed to get dataframe")
            finally:
                self.delete_working_dir()

    def _get_dataframe_2(self, type_name: str, features_per_request: int = 500):
        """Downloads data as GML in chucks, the files are converted into one shapefile that is then read into a
            geopandas dataframe and returned.

        Args:
            type_name (string): name of wfs feature
            features_per_request (int, optional): how may features to Download per request. Defaults to 100.

        Raises:
            Exception: [description]

        Returns:
            geopandas.geodataframe: geopandas dataframe.
        """
        #reset working dir

        total_feature_count = self.get_feature_count(layer_name=type_name)
        params = self.build_params(
            request="getFeature", type_name=type_name, output_format="gml3"
        )

        downloads_folder = os.path.join(self.working_dir, "gml_files")
        if os.path.exists(downloads_folder) is False:
            os.mkdir(downloads_folder)

        def get_request_urls():
            """generate download urls and filenames.

            Returns:
                [array]: list of arrays with two strings.
                example: [ (www.dl_url_1.com, /tmp/file_name_1
                 ) ]
            """
            calls = math.ceil(total_feature_count / features_per_request)
            remainder = total_feature_count % features_per_request
            request_urls = []
            for j in range(0, calls):
                offset = j * features_per_request
                if j + 1 == calls and remainder > 0:
                    chuck_params = {"startIndex": offset, "count": remainder}
                else:
                    chuck_params = {"startIndex": offset, "count": features_per_request}
                call_params = {**params, **chuck_params}
                request_url = (
                    requests.Request("GET", self.base_url, params=call_params)
                    .prepare()
                    .url
                )
                local_filename = os.path.join(
                    self.working_dir, downloads_folder, f"{type_name}-{j}.xml"
                )
                request_urls.append((request_url, local_filename))
            return request_urls

        def download_data(data):
            """download data using python threads.

            Args:
                data (list): [description]

            Raises:
                Exception: raised if request to wfs service fails
            """
            request_url = data[0]
            local_filename = data[1]
            session = get_session()
            with session.get(request_url) as resp:
                if resp.status_code == 200:
                    # Add in retires for so if one fails it doesn't stop entire download
                    with open(local_filename, "wb") as f:
                        f.write(resp.content)
                else:
                    raise Exception(
                        f"failed to fetch data from service, error code: {resp.status_code}"
                    )

        def get_data_sample():
            """takes the first feature from a layer ad writes to file.

            Raises:
                Exception: exception raised if download fails.

            Returns:
                string: returns filename of sample file.
            """
            chuck_params = {"startIndex": 0, "count": 1}
            call_params = {**params, **chuck_params}
            request_url = (
                requests.Request("GET", self.base_url, params=call_params).prepare().url
            )
            resp = requests.get(request_url)
            if resp.status_code == 200:
                local_filename = os.path.join(
                    self.working_dir, downloads_folder, f"{type_name}-sample.xml"
                )
                f = open(local_filename, "wb")
                f.write(resp.content)
                f.close()
            else:
                raise Exception(
                    f"failed to fetch data from service, error code: {resp.status_code}"
                )

            return local_filename

        # download resources using threads
        try:
            urls = get_request_urls()
            threadpool_download(download_data, urls)
            input_files = [x[1] for x in urls]
            gdf = Converters.convert_multiple_gml_to_dataframe(
                input_files=input_files,
                input_sample_file=get_data_sample(),
            )
            return gdf
        except Exception as e:
            LOGGER.error(e)
            raise Exception("Failed to get dataframe")
        finally:
            if os.path.exists(downloads_folder):
                shutil.rmtree(downloads_folder)

    def get_metadata_attribute(self, attribute: str, layer_name: str = None) -> Any:
        """get data for attribute in metadata
        Args:
            attribute (str): name of attribute you want to access
            layer_name (str, optional): name of layer if more than one layer exists. Defaults to None.

        Raises:
            Exception: "file contains more than one layer, provide name of layer"
            Exception: "file has no layer called <layer_name>"

        Returns:
            Any: value of the attribute requested.
        """

        def _return_attr(_layer_name: str, _attribute: str) -> Any:
            if self._metadata[_layer_name][_attribute] is None:
                self._metadata[_layer_name][_attribute] = self._get_action(
                    _layer_name, _attribute
                )()
            return self._metadata[_layer_name][_attribute]

        if self.get_layer_count() > 1 and layer_name is None:
            raise Exception("file contains more than one layer, provide name of layer")
        elif self.get_layer_count() == 1:
            layer_name = next(iter(self._metadata))
            return _return_attr(layer_name, attribute)
        elif layer_name is not None:
            if layer_name in [x['name'] for x in self.get_layers()]:
                return _return_attr(layer_name, attribute)
            else:
                raise Exception(f"file has no layer called {layer_name}")

    def _get_action(self, layer_name: str, action: str) -> Callable:
        layer = self._data_source.get_layer_by_name(layer_name)

        actions = {
            "schema": layer.get_schema,
            "feature_count": layer.get_feature_count,
            "extent": layer.get_extent,
            "geom_type": layer.get_geom_type,
            "crs_code": layer.get_crs_code,
        }
        return actions[action]

    def write_to_postgis_db(self,
                            layer_name: str,
                            table_name: str,
                            schema: str,
                            connection_str: str,
                            crs: int = None,
                            overwrite: bool = False,
                            force_type: int = None):

        if layer_name is None:
            raise Exception("provide name of layer")
        else:
            params = self.build_params(
                request="getFeature", type_name=layer_name, output_format="gml3"
            )
            request_url = requests.Request("GET", self.base_url, params=params).prepare().url
            data_source = OGR_DataSource(_input=request_url, _type="WFS")
            ogr_layer = data_source.get_layer_by_name(layer_name)
            ogr_layer.write_to_postgis_db(
                table_name=table_name,
                schema=schema,
                connection_string=connection_str,
                crs=crs,
                overwrite=overwrite,
                force_type=force_type
            )
