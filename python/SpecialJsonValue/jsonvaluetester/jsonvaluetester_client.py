# -*- coding: utf-8 -*-

"""
jsonvaluetester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.configurations.global_configuration import GlobalConfiguration
from apimatic_core.decorators.lazy_property import LazyProperty
from jsonvaluetester.configuration import Configuration
from jsonvaluetester.controllers.base_controller import BaseController
from jsonvaluetester.configuration import Environment
from jsonvaluetester.controllers.json_obj_controller import JsonObjController
from jsonvaluetester.controllers.json_val_controller import JsonValController


class JsonvaluetesterClient(object):
    @LazyProperty
    def json_obj(self):
        return JsonObjController(self.global_configuration)

    @LazyProperty
    def json_val(self):
        return JsonValController(self.global_configuration)

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=3, backoff_factor=2,
                 retry_statuses=None, retry_methods=None, proxy_settings=None,
                 environment=Environment.TESTING, config=None):
        self.config = config or Configuration(
            http_client_instance=http_client_instance,
            override_http_client_configuration=override_http_client_configuration,
            http_call_back=http_call_back, timeout=timeout,
            max_retries=max_retries, backoff_factor=backoff_factor,
            retry_statuses=retry_statuses, retry_methods=retry_methods,
            proxy_settings=proxy_settings, environment=environment)

        self.global_configuration = GlobalConfiguration(self.config)\
            .global_errors(BaseController.global_errors())\
            .base_uri_executor(self.config.get_base_uri)

    @classmethod
    def from_environment(cls, dotenv_path=None, **overrides):
        return cls(config=Configuration.from_environment(dotenv_path=dotenv_path, **overrides))
