# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.configurations.global_configuration import GlobalConfiguration
from apimatic_core.decorators.lazy_property import LazyProperty
from tester.configuration import Configuration
from tester.controllers.base_controller import BaseController
from tester.configuration import Environment
from tester.controllers.response_types_controller\
    import ResponseTypesController
from tester.controllers.form_params_controller import FormParamsController
from tester.controllers.body_params_controller import BodyParamsController
from tester.controllers.error_codes_controller import ErrorCodesController
from tester.controllers.query_param_controller import QueryParamController
from tester.controllers.echo_controller import EchoController
from tester.controllers.header_controller import HeaderController
from tester.controllers.template_params_controller\
    import TemplateParamsController
from tester.controllers.query_params_controller import QueryParamsController


class TesterClient(object):
    @LazyProperty
    def response_types(self):
        return ResponseTypesController(self.global_configuration)

    @LazyProperty
    def form_params(self):
        return FormParamsController(self.global_configuration)

    @LazyProperty
    def body_params(self):
        return BodyParamsController(self.global_configuration)

    @LazyProperty
    def error_codes(self):
        return ErrorCodesController(self.global_configuration)

    @LazyProperty
    def query_param(self):
        return QueryParamController(self.global_configuration)

    @LazyProperty
    def echo(self):
        return EchoController(self.global_configuration)

    @LazyProperty
    def header(self):
        return HeaderController(self.global_configuration)

    @LazyProperty
    def template_params(self):
        return TemplateParamsController(self.global_configuration)

    @LazyProperty
    def query_params(self):
        return QueryParamsController(self.global_configuration)

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=None, retry_methods=None, proxy_settings=None,
                 environment=Environment.TESTING, port='80', suites=1,
                 config=None):
        self.config = config or Configuration(
            http_client_instance=http_client_instance,
            override_http_client_configuration=override_http_client_configuration,
            http_call_back=http_call_back, timeout=timeout,
            max_retries=max_retries, backoff_factor=backoff_factor,
            retry_statuses=retry_statuses, retry_methods=retry_methods,
            proxy_settings=proxy_settings, environment=environment, port=port,
            suites=suites)

        self.global_configuration = GlobalConfiguration(self.config)\
            .global_errors(BaseController.global_errors())\
            .base_uri_executor(self.config.get_base_uri)

    @classmethod
    def from_environment(cls, dotenv_path=None, **overrides):
        return cls(config=Configuration.from_environment(dotenv_path=dotenv_path, **overrides))
