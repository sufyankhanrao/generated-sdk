
# Payment Callback

Called when payment processing is complete

## Headers

This event's request contains the following headers.

| Name | Description |
|  --- | --- |
| X-Correlation-Id | Correlation ID for request tracing across services. |
| X-Client-Version | Client application version sending the request. |
| Content-Type |  |

## Payload Type

This event's request payload is of type [PaymentCallback](../../../../doc/models/payment-callback.md).

## Payload Example

```json
{
  "orderId": "order_789",
  "paymentStatus": "success",
  "transactionId": "txn_abc123",
  "amount": 59.98,
  "currency": "USD",
  "timestamp": "2025-09-19T10:35:00Z",
  "failureReason": "failureReason2"
}
```

## SDK Usage Example

```python
from flask import (
    Flask,
    Response,
    request,
)

from webhooksandcallbacksapi.events.callbacks.callbacks_handler import (
    CallbacksHandler,
)
from webhooksandcallbacksapi.events.unknown_event import (
    UnknownEvent,
)
from webhooksandcallbacksapi.models.payment_callback import (
    PaymentCallback,
)
from webhooksandcallbacksapi.utilities.request_adapter import (
    to_core_request,
)

app = Flask(__name__)

@app.route("/callbacks", methods=[
    "POST",
])
def Callbacks() -> Response:
    # Step 1: Convert the incoming request using to_core_request (Django/Flask)
    #         or await to_core_request_async (FastAPI).
    core_req = to_core_request(request)

    # Step 2: Parse the request into a typed event.
    event = CallbacksHandler.parse_event(core_req)

    # Step 3: Pattern match for paymentCallback only.
    if isinstance(event, PaymentCallback):
        print("paymentCallback received")
        # TODO: add handling logic
    elif isinstance(event, UnknownEvent):
        print("Unknown event")
        # TODO: add unknown event handling

    # Step 4: Return 200 OK to acknowledge receipt (adjust with other codes if needed).
    return Response(status=200)
```

## Accepted Server Responses

The server should responds with one of the following status codes:

| Status Code | Description |
|  --- | --- |
| 200 | Callback received successfully |
| 400 | Invalid callback data |

