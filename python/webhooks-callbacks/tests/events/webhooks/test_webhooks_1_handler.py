from typing import Any

import unittest

from webhooksandcallbacksapi.api_helper import (
    APIHelper
)
from webhooksandcallbacksapi.events.unknown_event import (
    UnknownEvent
)
from webhooksandcallbacksapi.events.webhooks.webhooks_1_handler import (
    Webhooks1Handler
)
from webhooksandcallbacksapi.http.request import (
    Request
)
from webhooksandcallbacksapi.models.order_created_event import (
    OrderCreatedEvent
)

class TestWebhooks1Handler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @staticmethod
    def _json_bytes(obj: Any) -> bytes:
        return APIHelper.json_serialize(obj).encode("utf-8")

    @staticmethod
    def _make_request(body_obj, add_signature_header = True) -> Request:
        raw = TestWebhooks1Handler._json_bytes(body_obj)
        request = Request(
            method="POST",
            path="/webhooks",
            url=f"https://example.test/webhooks",
            headers={"Content-Type": "application/json"},
            raw_body=raw,
        )
        return request

    def test_order_created_from_webhooks_1_handler(self):
        """
         Tests the `orderCreated` event from Webhooks1Handler.
        """

        # arrange
        event_payload = {"orderCreatedId": 9}
        core_req = self._make_request(event_payload)

        # act
        event = Webhooks1Handler.parse_event(core_req)

        # assert
        assert isinstance(event, OrderCreatedEvent)


    def test_unknown_event(self):
        """
         Tests the `UnknownEvent` case from Webhooks1Handler.
        """

        # arrange
        event_payload = ""
        core_req = self._make_request(event_payload)

        # act
        event = Webhooks1Handler.parse_event(core_req)

        # assert
        assert isinstance(event, UnknownEvent)
