"""postnlecommerce.

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.configurations.global_configuration import (
    GlobalConfiguration,
)
from apimatic_core.decorators.lazy_property import (
    LazyProperty,
)

from postnlecommerce.configuration import (
    Configuration,
    Environment,
)
from postnlecommerce.controllers.barcode_controller import (
    BarcodeController,
)
from postnlecommerce.controllers.base_controller import (
    BaseController,
)
from postnlecommerce.controllers.checkout_controller import (
    CheckoutController,
)
from postnlecommerce.controllers.confirming_controller import (
    ConfirmingController,
)
from postnlecommerce.controllers.deliverydate_controller import (
    DeliverydateController,
)
from postnlecommerce.controllers.labelling_controller import (
    LabellingController,
)
from postnlecommerce.controllers.locations_controller import (
    LocationsController,
)
from postnlecommerce.controllers.postalcode_check_controller import (
    PostalcodeCheckController,
)
from postnlecommerce.controllers.shipment_controller import (
    ShipmentController,
)
from postnlecommerce.controllers.shipping_status_controller import (
    ShippingStatusController,
)
from postnlecommerce.controllers.timeframes_controller import (
    TimeframesController,
)
from postnlecommerce.http.auth.custom_header_authentication import (
    CustomHeaderAuthentication,
)


class PostnlecommerceClient(object):
    """Client that provide access to the PostnlecommerceClient APIs."""

    @LazyProperty
    def barcode(self):
        """Provide access to the BarcodeController endpoints."""
        return BarcodeController(self.global_configuration)

    @LazyProperty
    def checkout(self):
        """Provide access to the CheckoutController endpoints."""
        return CheckoutController(self.global_configuration)

    @LazyProperty
    def confirming(self):
        """Provide access to the ConfirmingController endpoints."""
        return ConfirmingController(self.global_configuration)

    @LazyProperty
    def deliverydate(self):
        """Provide access to the DeliverydateController endpoints."""
        return DeliverydateController(self.global_configuration)

    @LazyProperty
    def labelling(self):
        """Provide access to the LabellingController endpoints."""
        return LabellingController(self.global_configuration)

    @LazyProperty
    def locations(self):
        """Provide access to the LocationsController endpoints."""
        return LocationsController(self.global_configuration)

    @LazyProperty
    def postalcode_check(self):
        """Provide access to the PostalcodeCheckController endpoints."""
        return PostalcodeCheckController(self.global_configuration)

    @LazyProperty
    def shipment(self):
        """Provide access to the ShipmentController endpoints."""
        return ShipmentController(self.global_configuration)

    @LazyProperty
    def shipping_status(self):
        """Provide access to the ShippingStatusController endpoints."""
        return ShippingStatusController(self.global_configuration)

    @LazyProperty
    def timeframes(self):
        """Provide access to the TimeframesController endpoints."""
        return TimeframesController(self.global_configuration)

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=3, backoff_factor=2,
                 retry_statuses=None, retry_methods=None, proxy_settings=None,
                 environment=Environment.PRODUCTION_SERVER, apikey=None,
                 custom_header_authentication_credentials=None, config=None):
        """Initialize a new instance of PostnlecommerceClient."""
        self.config = config or Configuration(
            http_client_instance=http_client_instance,
            override_http_client_configuration=override_http_client_configuration,
            http_call_back=http_call_back, timeout=timeout,
            max_retries=max_retries, backoff_factor=backoff_factor,
            retry_statuses=retry_statuses, retry_methods=retry_methods,
            proxy_settings=proxy_settings, environment=environment,
            apikey=apikey,
            custom_header_authentication_credentials=custom_header_authentication_credentials)

        self.global_configuration = GlobalConfiguration(self.config)\
            .global_errors(BaseController.global_errors())\
            .base_uri_executor(self.config.get_base_uri)\
            .user_agent(BaseController.user_agent(),
                BaseController.user_agent_parameters())

        self.auth_managers = {
            "APIKeyHeader": CustomHeaderAuthentication(
                self.config.custom_header_authentication_credentials),
        }
        self.global_configuration =\
            self.global_configuration.auth_managers(self.auth_managers)

    @classmethod
    def from_environment(cls, dotenv_path=None, **overrides):
        """Create a client instance using environment variables.

        Returns:
            PostnlecommerceClient instance.

        """
        return cls(config=Configuration
            .from_environment(dotenv_path=dotenv_path, **overrides))
