"""testerfilesandmultipart.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter

from testerfilesandmultipart.api_helper import (
    APIHelper,
)
from testerfilesandmultipart.configuration import (
    Server,
)
from testerfilesandmultipart.controllers.base_controller import (
    BaseController,
)
from testerfilesandmultipart.http.http_method_enum import (
    HttpMethodEnum,
)
from testerfilesandmultipart.models.server_response import (
    ServerResponse,
)


class FormParamsController(BaseController):
    """A Controller to access Endpoints in the testerfilesandmultipart API."""

    def __init__(self, config):
        """Initialize FormParamsController object."""
        super(FormParamsController, self).__init__(config)

    def send_multiple_files(self,
                            file,
                            file_1):
        """Perform a POST request to /form/multipleFiles.

        Args:
            file (typing.BinaryIO): The request form parameter.
            file_1 (typing.BinaryIO): The request form parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/form/multipleFiles")
            .http_method(HttpMethodEnum.POST)
            .multipart_param(Parameter()
                             .key("file")
                             .value(file)
                             .default_content_type("application/octet-stream")
                             .is_required(True))
            .multipart_param(Parameter()
                             .key("file1")
                             .value(file_1)
                             .default_content_type("application/octet-stream")
                             .is_required(True))
            .header_param(Parameter()
                          .key("accept")
                          .value("application/json")),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_collected_files(self,
                             options=dict()):
        """Perform a POST request to /form/multipleFiles.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::
                    file -- typing.BinaryIO -- The request form parameter.
                    file_1 -- typing.BinaryIO -- The request form parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/form/multipleFiles")
            .http_method(HttpMethodEnum.POST)
            .multipart_param(Parameter()
                             .key("file")
                             .value(options.get("file", None))
                             .default_content_type("application/octet-stream")
                             .is_required(True))
            .multipart_param(Parameter()
                             .key("file1")
                             .value(options.get("file_1", None))
                             .default_content_type("application/octet-stream")
                             .is_required(True))
            .header_param(Parameter()
                          .key("accept")
                          .value("application/json")),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()
