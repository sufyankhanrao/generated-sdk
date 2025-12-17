from typing import Any

import unittest

from webhooksandcallbacksapi.api_helper import (
    APIHelper
)
from webhooksandcallbacksapi.events.unknown_event import (
    UnknownEvent
)
from webhooksandcallbacksapi.events.webhooks.webhooks_no_verification_handler import (
    WebhooksNoVerificationHandler
)
from webhooksandcallbacksapi.http.request import (
    Request
)
from webhooksandcallbacksapi.models.audit_log_event import (
    AuditLogEvent
)

class TestWebhooksNoVerificationHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @staticmethod
    def _json_bytes(obj: Any) -> bytes:
        return APIHelper.json_serialize(obj).encode("utf-8")

    @staticmethod
    def _make_request(body_obj, add_signature_header = True) -> Request:
        raw = TestWebhooksNoVerificationHandler._json_bytes(body_obj)
        request = Request(
            method="POST",
            path="/webhooks",
            url=f"https://example.test/webhooks",
            headers={"Content-Type": "application/json"},
            raw_body=raw,
        )
        return request

    def test_audit_log_event_from_webhooks_no_verification_handler(self):
        """
         Tests the `auditLogEvent` event from webhooksNoVerificationHandler.
        """

        # arrange
        event_payload = {}
        core_req = self._make_request(event_payload)

        # act
        event = WebhooksNoVerificationHandler.parse_event(core_req)

        # assert
        assert isinstance(event, AuditLogEvent)


    def test_root_level_primitive_one_of_event_from_webhooks_no_verification_handler(
        self,
    ):
        """
         Tests the `rootLevelPrimitiveOneOfEvent` event from
        webhooksNoVerificationHandler.
        """

        # arrange
        event_payload = "\"on\""
        core_req = self._make_request(event_payload)

        # act
        event = WebhooksNoVerificationHandler.parse_event(core_req)

        # assert
        assert isinstance(event, str) or isinstance(event, int) or isinstance(event, list) and all(isinstance(x, str) for x in event) or isinstance(event, list) and all(isinstance(x, int) for x in event)


    def test_unknown_event(self):
        """
         Tests the `UnknownEvent` case from WebhooksNoVerificationHandler.
        """

        # arrange
        event_payload = ""
        core_req = self._make_request(event_payload)

        # act
        event = WebhooksNoVerificationHandler.parse_event(core_req)

        # assert
        assert isinstance(event, UnknownEvent)
