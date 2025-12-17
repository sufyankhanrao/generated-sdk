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
    Base64UrlEncoder
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
from webhooksandcallbacksapi.events.webhooks.webhooks_c_handler import (
    WebhooksCHandler
)
from webhooksandcallbacksapi.http.request import (
    Request
)

class TestWebhooksCHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.handler = WebhooksCHandler("dummy_signing_key")

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
        encoded = Base64UrlEncoder().encode(digest)
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
        raw = TestWebhooksCHandler._json_bytes(body_obj)
        request = Request(
            method="POST",
            path="/webhooks",
            url=f"https://example.test/webhooks",
            headers={"Content-Type": "application/json"},
            raw_body=raw,
        )
        if add_signature_header:
            request.headers["X-Webhook-Signature"] = TestWebhooksCHandler._compute_expected_signature(
                secret_key="dummy_signing_key",
                request=request,
                resolver=TestWebhooksCHandler._canonical_message_builder,
            )
        return request

    def test_string_event_from_webhooks_c_handler(self):
        """
         Tests the `stringEvent` event from webhooksCHandler.
        """

        # arrange
        event_payload = "\"body6\""
        core_req = self._make_request(event_payload)

        # act
        event = self.handler.verify_and_parse_event(core_req)

        # assert
        assert isinstance(event, str)


    def test_int_event_from_webhooks_c_handler(self):
        """
         Tests the `intEvent` event from webhooksCHandler.
        """

        # arrange
        event_payload = 8
        core_req = self._make_request(event_payload)

        # act
        event = self.handler.verify_and_parse_event(core_req)

        # assert
        assert isinstance(event, int)


    def test_number_list_event_from_webhooks_c_handler(self):
        """
         Tests the `numberListEvent` event from webhooksCHandler.
        """

        # arrange
        event_payload = [203.64, 203.65]
        core_req = self._make_request(event_payload)

        # act
        event = self.handler.verify_and_parse_event(core_req)

        # assert
        assert isinstance(event, list) and all(isinstance(x, float) for x in event)


    def test_string_map_event_from_webhooks_c_handler(self):
        """
         Tests the `stringMapEvent` event from webhooksCHandler.
        """

        # arrange
        event_payload = {"key0": "body4", "key1": "body5"}
        core_req = self._make_request(event_payload)

        # act
        event = self.handler.verify_and_parse_event(core_req)

        # assert
        assert isinstance(event, dict) and all(isinstance(k, str) and isinstance(v, str) for k, v in event.items())


    def test_signature_verification_failure(self):
        """
         Tests the `SignatureVerificationFailure` case from WebhooksCHandler.
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
         Tests the `UnknownEvent` case from WebhooksCHandler.
        """

        # arrange
        event_payload = ""
        core_req = self._make_request(event_payload)

        # act
        event = self.handler.verify_and_parse_event(core_req)

        # assert
        assert isinstance(event, UnknownEvent)
