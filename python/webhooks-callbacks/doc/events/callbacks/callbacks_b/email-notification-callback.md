
# Email Notification Callback

Called when email notification delivery is complete

## Signature Verification

This event uses the `HMAC Signature Verifier` for request verification. The event includes an `X-Signature` header that will be validated using your shared `secret-key` to ensure request authenticity.

## Headers

This event's request contains the following headers.

| Name |
|  --- |
| Content-Type |

## Payload Type

This event's request payload is of type [NotificationCallback](../../../../doc/models/notification-callback.md).

## Payload Example

```json
{
  "notificationType": "email",
  "subject": "Order Confirmation",
  "message": "msg_email_789"
}
```

## SDK Usage Example

```python
from flask import (
    Flask,
    Response,
    request
)

from webhooksandcallbacksapi.events.callbacks.callbacks_b_handler import (
    CallbacksBHandler
)
from webhooksandcallbacksapi.events.signature_verification_failure import (
    SignatureVerificationFailure
)
from webhooksandcallbacksapi.events.unknown_event import (
    UnknownEvent
)
from webhooksandcallbacksapi.models.notification_callback import (
    NotificationCallback
)
from webhooksandcallbacksapi.utilities.request_adapter import (
    to_core_request
)

app = Flask(__name__)

@app.route("/callbacks", methods=["POST"])
def Callbacks() -> Response:
    # Step 1: Create the handler with your shared secret key.
    handler = CallbacksBHandler(secret_key="your-shared-secret")

    # Step 2: Convert the incoming request using to_core_request (Django/Flask)
    #         or await to_core_request_async (FastAPI).
    core_req = to_core_request(request)

    # Step 3: Verify and parse the request into a typed event.
    event = handler.verify_and_parse_event(core_req)

    # Step 4: Pattern match for emailNotificationCallback only.
    if isinstance(event, NotificationCallback) and getattr(event, "notification_type", None) == "emailNotificationCallback":
        print("emailNotificationCallback received")
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
| 200 | Callback received successfully |
| 422 | Callback processing failed |

