import hashlib
import hmac
from typing import (
    Any,
    Callable,
    Optional,
    Union
)

import unittest
from apimatic_core.security.signature_verifiers.hmac_signature_verifier import (
    Base64Encoder
)

from webhooksandcallbacksapi.api_helper import (
    APIHelper
)
from webhooksandcallbacksapi.events.signature_verification_failure import (
    SignatureVerificationFailure
)
from webhooksandcallbacksapi.events.unknown_event import (
    UnknownEvent
)
from webhooksandcallbacksapi.events.webhooks.webhooks_b_handler import (
    WebhooksBHandler
)
from webhooksandcallbacksapi.http.request import (
    Request
)
from webhooksandcallbacksapi.models.inventory_stock_decrease_event import (
    InventoryStockDecreaseEvent
)
from webhooksandcallbacksapi.models.inventory_stock_depleted_event import (
    InventoryStockDepletedEvent
)
from webhooksandcallbacksapi.models.inventory_stock_increase_event import (
    InventoryStockIncreaseEvent
)
from webhooksandcallbacksapi.models.system_alert_notification_event import (
    SystemAlertNotificationEvent
)
from webhooksandcallbacksapi.models.system_maintenance_notification_event import (
    SystemMaintenanceNotificationEvent
)
from webhooksandcallbacksapi.models.system_performance_notification_event import (
    SystemPerformanceNotificationEvent
)
from webhooksandcallbacksapi.models.user_action_notification_event import (
    UserActionNotificationEvent
)
from webhooksandcallbacksapi.models.user_preference_notification_event import (
    UserPreferenceNotificationEvent
)
from webhooksandcallbacksapi.models.user_status_notification_event import (
    UserStatusNotificationEvent
)

class TestWebhooksBHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.handler = WebhooksBHandler("dummy_signing_key")

    @staticmethod
    def _compute_expected_signature(
        secret_key: str,
        request: Request,
        resolver: Optional[Callable[[Request], Union[bytes, None]]] = None,
    ) -> str:
        if resolver is None:
            message = getattr(request, "raw_body", None)
        else:
            message = resolver(request)

        digest = hmac.new(secret_key.encode("utf-8"), message, hashlib.sha512).digest()
        encoded = Base64Encoder().encode(digest)
        signature_value_template = "v1={digest}"
        if "{digest}" in signature_value_template:
            return signature_value_template.replace("{digest}", encoded)
        else:
            return signature_value_template

    @staticmethod
    def _canonical_message_builder(request: Request) -> Optional[bytes]:
        """
         Builds the canonical message from the request for the signature
        verification.

        :param request: The incoming HTTP request.
        :type request: Request

        :return: The canonical message as bytes, or None if the message could
                 not be constructed.
        :rtype: Optional[bytes]
        """

        payload = request.raw_body.decode()
        method = request.method
        x_timestamp = request.headers.get('X-Timestamp', None)
        return f"{method}|{x_timestamp}|{payload}".encode()

    @staticmethod
    def _json_bytes(obj: Any) -> bytes:
        return APIHelper.json_serialize(obj).encode("utf-8")

    @staticmethod
    def _make_request(body_obj, add_signature_header = True) -> Request:
        raw = TestWebhooksBHandler._json_bytes(body_obj)
        request = Request(
            method="POST",
            path="/webhooks",
            url=f"https://example.test/webhooks",
            headers={"Content-Type": "application/json"},
            raw_body=raw,
        )
        if add_signature_header:
            request.headers["X-Webhook-Signature"] = TestWebhooksBHandler._compute_expected_signature(
                secret_key="dummy_signing_key",
                request=request,
                resolver=TestWebhooksBHandler._canonical_message_builder,
            )
        return request

    def test_user_notification_event_from_webhooks_b_handler(self):
        """
         Tests the `userNotificationEvent` event from webhooksBHandler.
        """

        # arrange
        event_payload = {"userActionNotificationEventType": "user.action"}
        core_req = self._make_request(event_payload)

        # act
        event = self.handler.verify_and_parse_event(core_req)

        # assert
        assert isinstance(event, UserActionNotificationEvent) or isinstance(event, UserStatusNotificationEvent) or isinstance(event, UserPreferenceNotificationEvent)


    def test_system_notification_event_from_webhooks_b_handler(self):
        """
         Tests the `systemNotificationEvent` event from webhooksBHandler.
        """

        # arrange
        event_payload = {"systemAlertNotificationEventType": "system.alert"}
        core_req = self._make_request(event_payload)

        # act
        event = self.handler.verify_and_parse_event(core_req)

        # assert
        assert isinstance(event, SystemAlertNotificationEvent) or isinstance(event, SystemMaintenanceNotificationEvent) or isinstance(event, SystemPerformanceNotificationEvent)


    def test_inventory_change_event_from_webhooks_b_handler(self):
        """
         Tests the `inventoryChangeEvent` event from webhooksBHandler.
        """

        # arrange
        event_payload = {"inventoryStockIncreaseEventType": "stock.increase"}
        core_req = self._make_request(event_payload)

        # act
        event = self.handler.verify_and_parse_event(core_req)

        # assert
        assert isinstance(event, InventoryStockIncreaseEvent) or isinstance(event, InventoryStockDecreaseEvent) or isinstance(event, InventoryStockDepletedEvent)


    def test_signature_verification_failure(self):
        """
         Tests the `SignatureVerificationFailure` case from WebhooksBHandler.
        """

        # arrange
        event_payload = {"key": "value"}
        core_req = self._make_request(event_payload, False)

        # act
        event = self.handler.verify_and_parse_event(core_req)

        # assert
        assert isinstance(event, SignatureVerificationFailure)


    def test_unknown_event(self):
        """
         Tests the `UnknownEvent` case from WebhooksBHandler.
        """

        # arrange
        event_payload = ""
        core_req = self._make_request(event_payload)

        # act
        event = self.handler.verify_and_parse_event(core_req)

        # assert
        assert isinstance(event, UnknownEvent)
