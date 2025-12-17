## Callbacks A Handler

Payment and fulfillment callback group with custom verification

## Signature Verification

This handler uses the `HMAC Signature Verifier` for request verification. Each event in this group includes an `X-Signature` header that will be validated using your shared `secret-key` to ensure request authenticity.

## Events

Events available in this group. Subscribe to receive webhook notifications when these events occur.

| Name | Description |
|  --- | --- |
| [fulfillmentCallback](../../../doc/events/callbacks/callbacks_a/fulfillment-callback.md) | Called when order processing is complete |

## SDK Usage Example

```python
from flask import (
    Flask,
    Response,
    request
)

from webhooksandcallbacksapi.events.callbacks.callbacks_a_handler import (
    CallbacksAHandler
)
from webhooksandcallbacksapi.events.signature_verification_failure import (
    SignatureVerificationFailure
)
from webhooksandcallbacksapi.events.unknown_event import (
    UnknownEvent
)
from webhooksandcallbacksapi.models.fulfillment_callback import (
    FulfillmentCallback
)
from webhooksandcallbacksapi.utilities.request_adapter import (
    to_core_request
)

app = Flask(__name__)

@app.route("/callbacks", methods=["POST"])
def Callbacks():
    # Step 1: Create the handler with your shared secret key.
    handler = CallbacksAHandler(secret_key="your-shared-secret")

    # Step 2: Convert the incoming request using to_core_request (Django/Flask)
    #         or await to_core_request_async (FastAPI).
    core_req = to_core_request(request)

    # Step 3: Verify and parse the request into a typed event.
    event = handler.verify_and_parse_event(core_req)

    # Step 4: Pattern match on the event type and handle it.
    if isinstance(event, FulfillmentCallback):
        print("fulfillmentCallback received")
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

