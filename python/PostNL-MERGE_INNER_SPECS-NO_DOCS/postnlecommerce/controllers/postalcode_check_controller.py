"""postnlecommerce.

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.authentication.multiple.single_auth import (
    Single,
)
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter

from postnlecommerce.api_helper import APIHelper
from postnlecommerce.configuration import Server
from postnlecommerce.controllers.base_controller import (
    BaseController,
)
from postnlecommerce.exceptions.barcode_response_error_exception import (
    BarcodeResponseErrorException,
)
from postnlecommerce.exceptions.barcode_response_invalid_exception import (
    BarcodeResponseInvalidException,
)
from postnlecommerce.exceptions.method_not_allowed_only_get_post_exception import (
    MethodNotAllowedOnlyGetPostException,
)
from postnlecommerce.http.http_method_enum import (
    HttpMethodEnum,
)
from postnlecommerce.models.cpc_response import (
    CpcResponse,
)


class PostalcodeCheckController(BaseController):
    """A Controller to access Endpoints in the postnlecommerce API."""

    def __init__(self, config):
        """Initialize PostalcodeCheckController object."""
        super(PostalcodeCheckController, self).__init__(config)

    def checkout_postalcode_check(self,
                                  postalcode,
                                  housenumber,
                                  housenumberaddition=None):
        """Perform a GET request to /shipment/checkout/v1/postalcodecheck.

        Please note that this API is not available on the sandbox environment.
        Request example:
        ```
        curl -X GET
        "https://api.postnl.nl/shipment/checkout/v1/postalcodecheck?postalcode=
        3571ZZ&amp;housenumber=74&amp;housenumberaddition=bis" \
         -H "Accept: application/json" \
         -H "apikey: APIKEY-HERE"
        ```

        Args:
            postalcode (str): The request query parameter.
            housenumber (str): The request query parameter.
            housenumberaddition (str, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.POSTNL)
            .path("/shipment/checkout/v1/postalcodecheck")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key("postalcode")
                         .value(postalcode))
            .query_param(Parameter()
                         .key("housenumber")
                         .value(housenumber))
            .query_param(Parameter()
                         .key("housenumberaddition")
                         .value(housenumberaddition))
            .header_param(Parameter()
                          .key("accept")
                          .value("application/json"))
            .auth(Single("APIKeyHeader")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CpcResponse.from_dictionary)
            .is_api_response(True)
            .local_error("400", "Bad request", BarcodeResponseInvalidException)
            .local_error("401", "Invalid apikey", MethodNotAllowedOnlyGetPostException)
            .local_error("405",
                "Method not allowed",
                MethodNotAllowedOnlyGetPostException)
            .local_error("429",
                "Too many requests",
                MethodNotAllowedOnlyGetPostException)
            .local_error("500", "Internal server error", BarcodeResponseErrorException),
        ).execute()
