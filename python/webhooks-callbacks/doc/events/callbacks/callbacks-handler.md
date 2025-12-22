## Callbacks Handler



## Events

Events available in this group. Subscribe to receive webhook notifications when these events occur.

| Name | Description |
|  --- | --- |
| [paymentCallback](../../../doc/events/callbacks/callbacks/payment-callback.md) | Called when payment processing is complete |

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
def Callbacks():
    # Step 1: Convert the incoming request using to_core_request (Django/Flask)
    #         or await to_core_request_async (FastAPI).
    core_req = to_core_request(request)

    # Step 2: Parse the request into a typed event.
    event = CallbacksHandler.parse_event(core_req)

    # Step 3: Pattern match on the event type and handle it.
    if isinstance(event, PaymentCallback):
        print("paymentCallback received")
        # TODO: add handling logic
    elif isinstance(event, UnknownEvent):
        print("Unknown event")
        # TODO: add unknown event handling

    # Step 4: Return 200 OK to acknowledge receipt (adjust with other codes if needed).
    return Response(status=200)
```

