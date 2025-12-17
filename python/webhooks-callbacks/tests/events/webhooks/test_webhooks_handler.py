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
    HexEncoder
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
from webhooksandcallbacksapi.events.webhooks.webhooks_handler import (
    WebhooksHandler
)
from webhooksandcallbacksapi.http.request import (
    Request
)
from webhooksandcallbacksapi.models.order_updated_event import (
    OrderUpdatedEvent
)
from webhooksandcallbacksapi.models.payment_completed_event import (
    PaymentCompletedEvent
)
from webhooksandcallbacksapi.models.primitive_collection_event import (
    PrimitiveCollectionEvent
)

class TestWebhooksHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.handler = WebhooksHandler("dummy_signing_key")

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

        digest = hmac.new(secret_key.encode("utf-8"), message, hashlib.sha256).digest()
        encoded = HexEncoder().encode(digest)
        signature_value_template = "{digest}"
        if "{digest}" in signature_value_template:
            return signature_value_template.replace("{digest}", encoded)
        else:
            return signature_value_template

    @staticmethod
    def _json_bytes(obj: Any) -> bytes:
        return APIHelper.json_serialize(obj).encode("utf-8")

    @staticmethod
    def _make_request(body_obj, add_signature_header = True) -> Request:
        raw = TestWebhooksHandler._json_bytes(body_obj)
        request = Request(
            method="POST",
            path="/webhooks",
            url=f"https://example.test/webhooks",
            headers={"Content-Type": "application/json"},
            raw_body=raw,
        )
        if add_signature_header:
            request.headers["X-Signature"] = TestWebhooksHandler._compute_expected_signature(
                secret_key="dummy_signing_key",
                request=request,
            )
        return request

    def test_order_updated_from_webhooks_handler(self):
        """
         Tests the `orderUpdated` event from webhooksHandler.
        """

        # arrange
        event_payload = {"orderUpdatedId": 91}
        core_req = self._make_request(event_payload)

        # act
        event = self.handler.verify_and_parse_event(core_req)

        # assert
        assert isinstance(event, OrderUpdatedEvent)


    def test_payment_completed_from_webhooks_handler(self):
        """
         Tests the `paymentCompleted` event from webhooksHandler.
        """

        # arrange
        event_payload = {"paymentId": 91}
        core_req = self._make_request(event_payload)

        # act
        event = self.handler.verify_and_parse_event(core_req)

        # assert
        assert isinstance(event, PaymentCompletedEvent)


    def test_primitive_collection_event_from_webhooks_handler(self):
        """
         Tests the `primitiveCollectionEvent` event from webhooksHandler.
        """

        # arrange
        event_payload = {"ids": [69, 70, 71]}
        core_req = self._make_request(event_payload)

        # act
        event = self.handler.verify_and_parse_event(core_req)

        # assert
        assert isinstance(event, PrimitiveCollectionEvent)


    def test_signature_verification_failure(self):
        """
         Tests the `SignatureVerificationFailure` case from WebhooksHandler.
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
         Tests the `UnknownEvent` case from WebhooksHandler.
        """

        # arrange
        event_payload = ""
        core_req = self._make_request(event_payload)

        # act
        event = self.handler.verify_and_parse_event(core_req)

        # assert
        assert isinstance(event, UnknownEvent)
