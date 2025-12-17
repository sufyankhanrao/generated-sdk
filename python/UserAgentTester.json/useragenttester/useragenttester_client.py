# -*- coding: utf-8 -*-

"""
useragenttester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.configurations.global_configuration import GlobalConfiguration
from apimatic_core.decorators.lazy_property import LazyProperty
from useragenttester.configuration import Configuration
from useragenttester.controllers.base_controller import BaseController
from useragenttester.configuration import Environment
from useragenttester.controllers.api_controller import APIController


class UseragenttesterClient(object):
    @LazyProperty
    def client(self):
        return APIController(self.global_configuration)

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
            .base_uri_executor(self.config.get_base_uri)\
            .user_agent(BaseController.user_agent(), BaseController.user_agent_parameters())

    @classmethod
    def from_environment(cls, dotenv_path=None, **overrides):
        return cls(config=Configuration.from_environment(dotenv_path=dotenv_path, **overrides))
