from typing import Any

import unittest

from webhooksandcallbacksapi.api_helper import (
    APIHelper
)
from webhooksandcallbacksapi.events.callbacks.callbacks_handler import (
    CallbacksHandler
)
from webhooksandcallbacksapi.events.unknown_event import (
    UnknownEvent
)
from webhooksandcallbacksapi.http.request import (
    Request
)
from webhooksandcallbacksapi.models.payment_callback import (
    PaymentCallback
)

class TestCallbacksHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @staticmethod
    def _json_bytes(obj: Any) -> bytes:
        return APIHelper.json_serialize(obj).encode("utf-8")

    @staticmethod
    def _make_request(body_obj, add_signature_header = True) -> Request:
        raw = TestCallbacksHandler._json_bytes(body_obj)
        request = Request(
            method="POST",
            path="/callbacks",
            url=f"https://example.test/callbacks",
            headers={"Content-Type": "application/json"},
            raw_body=raw,
        )
        return request

    def test_payment_callback_from_callbacks_handler(self):
        """
         Tests the `paymentCallback` event from CallbacksHandler.
        """

        # arrange
        event_payload = {
            "orderId": "order_789",
            "paymentStatus": "success",
            "transactionId": "txn_abc123",
            "amount": 59.98,
            "currency": "USD",
            "timestamp": "2025-09-19T10:35:00Z"
        }
        core_req = self._make_request(event_payload)

        # act
        event = CallbacksHandler.parse_event(core_req)

        # assert
        assert isinstance(event, PaymentCallback)


    def test_unknown_event(self):
        """
         Tests the `UnknownEvent` case from CallbacksHandler.
        """

        # arrange
        event_payload = ""
        core_req = self._make_request(event_payload)

        # act
        event = CallbacksHandler.parse_event(core_req)

        # assert
        assert isinstance(event, UnknownEvent)
