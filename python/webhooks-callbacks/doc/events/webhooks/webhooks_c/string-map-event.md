
# String Map Event



## Signature Verification

This event uses the `HMAC Signature Verifier` for request verification. The event includes an `X-Webhook-Signature` header that will be validated using your shared `secret-key` to ensure request authenticity.

## Headers

This event's request contains the following headers.

| Name |
|  --- |
| Content-Type |

## Payload Type

This event's request payload is of type [Dict[str, str]].

## Payload Example

```json
{
  "key0": "body4",
  "key1": "body5"
}
```

## SDK Usage Example

```python
from flask import (
    Flask,
    Response,
    request,
)

from webhooksandcallbacksapi.events.signature_verification_failure import (
    SignatureVerificationFailure,
)
from webhooksandcallbacksapi.events.unknown_event import (
    UnknownEvent,
)
from webhooksandcallbacksapi.events.webhooks.webhooks_c_handler import (
    WebhooksCHandler,
)
from webhooksandcallbacksapi.utilities.request_adapter import (
    to_core_request,
)

app = Flask(__name__)

@app.route("/webhooks", methods=[
    "POST",
])
def Webhooks() -> Response:
    # Step 1: Create the handler with your shared secret key.
    handler = WebhooksCHandler(secret_key="your-shared-secret")

    # Step 2: Convert the incoming request using to_core_request (Django/Flask)
    #         or await to_core_request_async (FastAPI).
    core_req = to_core_request(request)

    # Step 3: Verify and parse the request into a typed event.
    event = handler.verify_and_parse_event(core_req)

    # Step 4: Pattern match for stringMapEvent only.
    if (
        isinstance(event, dict) and
        all(isinstance(k, str) and isinstance(v, str) for k, v in event.items())
    ):
        print("stringMapEvent received")
        # TODO: add handling logic
    elif isinstance(event, SignatureVerificationFailure):
        print("Signature verification failed")
        # TODO: add signature verification failure handling
    elif isinstance(event, UnknownEvent):
        print("Unknown event")
        # TODO: add unknown event handling

    # Step 5: Return 200 OK to acknowledge receipt (adjust with other codes if needed).
    return Response(status=200)
```

## Accepted Server Responses

The server should responds with one of the following status codes:

| Status Code | Description |
|  --- | --- |
| 200 | Event processed successfully |

