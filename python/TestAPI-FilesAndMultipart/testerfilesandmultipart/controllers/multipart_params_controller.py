# -*- coding: utf-8 -*-

"""
testerfilesandmultipart

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from testerfilesandmultipart.api_helper import APIHelper
from testerfilesandmultipart.configuration import Server
from testerfilesandmultipart.http.api_response import ApiResponse
from testerfilesandmultipart.utilities.file_wrapper import FileWrapper
from testerfilesandmultipart.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from testerfilesandmultipart.http.http_method_enum import HttpMethodEnum
from testerfilesandmultipart.models.server_response import ServerResponse


class MultipartParamsController(BaseController):

    """A Controller to access Endpoints in the testerfilesandmultipart API."""
    def __init__(self, config):
        super(MultipartParamsController, self).__init__(config)

    def send_multipart_with_json(self,
                                 options=dict()):
        """Does a POST request to /multipart/multipartwithjson.

        Make a multipart request with a file, a json parameter and form
        parameters.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    file -- typing.BinaryIO -- The request form parameter.
                    integers -- int -- The request form parameter.
                    models -- List[Employee] -- The request form parameter.
                    strings -- str -- The request form parameter.

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
            .path('/multipart/multipartwithjson')
            .http_method(HttpMethodEnum.POST)
            .multipart_param(Parameter()
                             .key('file')
                             .value(options.get('file', None))
                             .default_content_type('image/png')
                             .is_required(True))
            .form_param(Parameter()
                        .key('integers')
                        .value(options.get('integers', None))
                        .is_required(True))
            .multipart_param(Parameter()
                             .key('models')
                             .value(APIHelper.json_serialize(options.get('models', None)))
                             .default_content_type('application/json')
                             .is_required(True))
            .form_param(Parameter()
                        .key('strings')
                        .value(options.get('strings', None))
                        .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()
