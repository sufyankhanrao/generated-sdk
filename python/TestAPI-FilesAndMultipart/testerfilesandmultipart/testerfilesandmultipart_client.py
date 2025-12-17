"""testerfilesandmultipart.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.configurations.global_configuration import (
    GlobalConfiguration,
)
from apimatic_core.decorators.lazy_property import (
    LazyProperty,
)

from testerfilesandmultipart.configuration import (
    Configuration,
    Environment,
)
from testerfilesandmultipart.controllers.base_controller import (
    BaseController,
)
from testerfilesandmultipart.controllers.binary_params_controller import (
    BinaryParamsController,
)
from testerfilesandmultipart.controllers.form_params_controller import (
    FormParamsController,
)
from testerfilesandmultipart.controllers.multipart_params_controller import (
    MultipartParamsController,
)


class TesterfilesandmultipartClient(object):
    """Client that provide access to the TesterfilesandmultipartClient APIs."""

    @LazyProperty
    def form_params(self):
        """Provide access to the FormParamsController endpoints."""
        return FormParamsController(self.global_configuration)

    @LazyProperty
    def binary_params(self):
        """Provide access to the BinaryParamsController endpoints."""
        return BinaryParamsController(self.global_configuration)

    @LazyProperty
    def multipart_params(self):
        """Provide access to the MultipartParamsController endpoints."""
        return MultipartParamsController(self.global_configuration)

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=None, retry_methods=None, proxy_settings=None,
                 environment=Environment.PRODUCTION, port="80", config=None):
        """Initialize a new instance of TesterfilesandmultipartClient."""
        self.config = config or Configuration(
            http_client_instance=http_client_instance,
            override_http_client_configuration=override_http_client_configuration,
            http_call_back=http_call_back, timeout=timeout,
            max_retries=max_retries, backoff_factor=backoff_factor,
            retry_statuses=retry_statuses, retry_methods=retry_methods,
            proxy_settings=proxy_settings, environment=environment, port=port)

        self.global_configuration = GlobalConfiguration(self.config)\
            .global_errors(BaseController.global_errors())\
            .base_uri_executor(self.config.get_base_uri)

    @classmethod
    def from_environment(cls, dotenv_path=None, **overrides):
        """Create a client instance using environment variables.

        Returns:
            TesterfilesandmultipartClient instance.

        """
        return cls(config=Configuration
            .from_environment(dotenv_path=dotenv_path, **overrides))
