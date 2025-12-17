import hashlib
import hmac
import os
from typing import (
    Any,
    Callable,
    Optional,
    Union
)

import django
from apimatic_core.security.signature_verifiers.hmac_signature_verifier import (
    HexEncoder
)
from django.test import (
    Client,
    SimpleTestCase
)

from webhooksandcallbacksapi.api_helper import (
    APIHelper
)
from webhooksandcallbacksapi.http.request import (
    Request
)

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "tests.framework_integrations.django_settings",
)

django.setup()

class DjangoCallbacksATest(SimpleTestCase):
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
        super().setUpClass()
        cls.client = Client()

    @staticmethod
    def _json_bytes(obj: Any) -> bytes:
        return APIHelper.json_serialize(obj).encode("utf-8")

    @staticmethod
    def _make_request(body_obj, add_signature_header = True) -> Request:
        raw = DjangoCallbacksATest._json_bytes(body_obj)
        request = Request(
            method="POST",
            path="/callbacks",
            url=f"https://example.test/callbacks",
            headers={"Content-Type": "application/json"},
            raw_body=raw,
        )
        if add_signature_header:
            request.headers["X-Signature"] = DjangoCallbacksATest._compute_expected_signature(
                secret_key="your-shared-secret",
                request=request,
            )
        return request

    def test_fulfillment_callback_from_callbacks_a_app(self):
        """
         Tests the `fulfillmentCallback` event from callbacksA application.
        """

        # arrange
        event_payload = {
            "orderId": "order_789",
            "fulfillmentStatus": "fulfilled",
            "trackingNumber": "TRK123456789",
            "carrier": "FedEx",
            "estimatedDelivery": "2025-09-22",
            "timestamp": "2025-09-19T14:00:00Z"
        }
        core_req = self._make_request(event_payload)

        # act
        resp = self.client.post(
            "/callbacks",
            **{"HTTP_X-Signature": core_req.headers["X-Signature"]},
            data=event_payload,
            content_type="application/json",
        )

        # assert
        self.assertEqual(resp.status_code, 200)
