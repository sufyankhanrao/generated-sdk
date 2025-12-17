import hashlib
import hmac
import json
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
from tests.framework_integrations.webhooks.apps.flask_webhooks_app import (
    create_app
)

from webhooksandcallbacksapi.http.request import (
    Request
)

class FlaskWebhooksTest(unittest.TestCase):
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

    @classmethod
    def setUpClass(cls):
        app = create_app()
        app.config.update(TESTING=True)
        cls.client = app.test_client()

    @staticmethod
    def _json_bytes(obj: Any) -> bytes:
        return json.dumps(obj, sort_keys=True).encode("utf-8")

    @staticmethod
    def _make_request(body_obj, add_signature_header = True) -> Request:
        raw = FlaskWebhooksTest._json_bytes(body_obj)
        request = Request(
            method="POST",
            path="/webhooks",
            url=f"https://example.test/webhooks",
            headers={"Content-Type": "application/json"},
            raw_body=raw,
        )
        if add_signature_header:
            request.headers["X-Signature"] = FlaskWebhooksTest._compute_expected_signature(
                secret_key="your-shared-secret",
                request=request,
            )
        return request

    def test_order_updated_from_webhooks_app(self):
        """
         Tests the `orderUpdated` event from webhooks application.
        """

        # arrange
        event_payload = {"orderUpdatedId": 91}
        core_req = self._make_request(event_payload)

        # act
        resp = self.client.post(
            "/webhooks",
            json=event_payload,
            headers=core_req.headers,
        )

        # assert
        self.assertEqual(resp.status_code, 200)
