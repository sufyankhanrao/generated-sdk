"""retriestester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.configurations.endpoint_configuration import (
    EndpointConfiguration,
)
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter

from retriestester.api_helper import APIHelper
from retriestester.configuration import Server
from retriestester.controllers.base_controller import (
    BaseController,
)
from retriestester.http.http_method_enum import (
    HttpMethodEnum,
)
from retriestester.models.server_response import (
    ServerResponse,
)


class APIController(BaseController):
    """A Controller to access Endpoints in the retriestester API."""

    def __init__(self, config):
        """Initialize APIController object."""
        super(APIController, self).__init__(config)

    def try_api_call(self,
                     case,
                     max_retries=None,
                     timeout=None):
        """Perform a GET request to /retries/tryApiCall/{case}.

        Args:
            case (str): Try api call for this case
            max_retries (int, optional): Maximum number of allowed retries
            timeout (int, optional): Timeout for all requests in seconds

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
            .path("/retries/tryApiCall/{case}")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key("case")
                            .value(case)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key("maxRetries")
                          .value(max_retries))
            .header_param(Parameter()
                          .key("timeout")
                          .value(timeout))
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

    def try_post_api_call(self,
                          max_retries=None,
                          timeout=None):
        """Perform a POST request to /retries/tryPostApi.

        Args:
            max_retries (int, optional): Maximum number of allowed retries
            timeout (int, optional): Timeout for all requests in seconds

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
            .path("/retries/tryPostApi")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key("maxRetries")
                          .value(max_retries))
            .header_param(Parameter()
                          .key("timeout")
                          .value(timeout))
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

    def retry_post_api_call(self,
                            max_retries=None,
                            timeout=None):
        """Perform a POST request to /retries/retryPostApi.

        Args:
            max_retries (int, optional): Maximum number of allowed retries
            timeout (int, optional): Timeout for all requests in seconds

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
            .path("/retries/retryPostApi")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key("maxRetries")
                          .value(max_retries))
            .header_param(Parameter()
                          .key("timeout")
                          .value(timeout))
            .header_param(Parameter()
                          .key("accept")
                          .value("application/json")),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).endpoint_configuration(
            EndpointConfiguration()
            .to_retry(True),
        ).execute()

    def retry_api_call(self,
                       max_retries=None,
                       retry_after=None,
                       timeout=None):
        """Perform a GET request to /retries/retryApiCallAfter.

        Args:
            max_retries (int, optional): Maximum number of allowed retries
            retry_after (int, optional): Retry after in seconds
            timeout (int, optional): Timeout for all requests in seconds

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
            .path("/retries/retryApiCallAfter")
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key("maxRetries")
                          .value(max_retries))
            .header_param(Parameter()
                          .key("retryAfter")
                          .value(retry_after))
            .header_param(Parameter()
                          .key("timeout")
                          .value(timeout))
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

    def dont_retry_api_call(self,
                            max_retries=None,
                            timeout=None):
        """Perform a GET request to /retries/dontRetryApi.

        Args:
            max_retries (int, optional): Maximum number of allowed retries
            timeout (int, optional): Timeout for all requests in seconds

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
            .path("/retries/dontRetryApi")
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key("maxRetries")
                          .value(max_retries))
            .header_param(Parameter()
                          .key("timeout")
                          .value(timeout))
            .header_param(Parameter()
                          .key("accept")
                          .value("application/json")),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).endpoint_configuration(
            EndpointConfiguration()
            .to_retry(False),
        ).execute()

    def retry_send_file(self,
                        file,
                        max_retries=None,
                        retry_after=None,
                        timeout=None):
        """Perform a PUT request to /retries/tryPutApi.

        Args:
            file (typing.BinaryIO): The request body parameter.
            max_retries (int, optional): Maximum number of allowed retries
            retry_after (int, optional): Retry after in seconds
            timeout (int, optional): Timeout for all requests in seconds

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
            .path("/retries/tryPutApi")
            .http_method(HttpMethodEnum.PUT)
            .body_param(Parameter()
                        .value(file)
                        .is_required(True))
            .header_param(Parameter()
                          .key("maxRetries")
                          .value(max_retries))
            .header_param(Parameter()
                          .key("retryAfter")
                          .value(retry_after))
            .header_param(Parameter()
                          .key("timeout")
                          .value(timeout))
            .header_param(Parameter()
                          .key("content-type")
                          .value("application/octet-stream"))
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
