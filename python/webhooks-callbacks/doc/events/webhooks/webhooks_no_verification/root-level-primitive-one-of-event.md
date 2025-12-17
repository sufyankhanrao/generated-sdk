
# Root Level Primitive One of Event

Root-level oneOf across primitives and collections of primitives/enums.

## Headers

This event's request contains the following headers.

| Name |
|  --- |
| Content-Type |

## Payload Type

This event's request payload is of type [RootLevelPrimitiveOneOfEventRequestEnum | int | List[RootLevelPrimitiveOneOfEventRequest1Enum] | List[int]](../../../../doc/models/containers/root-level-one-of-primitive-event-root-level-primitive-one-of-body.md).

## Payload Example

```json
"on"
```

## SDK Usage Example

```python
from flask import (
    Flask,
    Response,
    request
)

from webhooksandcallbacksapi.events.unknown_event import (
    UnknownEvent
)
from webhooksandcallbacksapi.events.webhooks.webhooks_no_verification_handler import (
    WebhooksNoVerificationHandler
)
from webhooksandcallbacksapi.utilities.request_adapter import (
    to_core_request
)

app = Flask(__name__)

@app.route("/webhooks", methods=["POST"])
def Webhooks() -> Response:
    # Step 1: Convert the incoming request using to_core_request (Django/Flask)
    #         or await to_core_request_async (FastAPI).
    core_req = to_core_request(request)

    # Step 2: Parse the request into a typed event.
    event = WebhooksNoVerificationHandler.parse_event(core_req)

    # Step 3: Pattern match for rootLevelPrimitiveOneOfEvent only.
    if isinstance(event, str) or isinstance(event, int) or isinstance(event, list) and all(isinstance(x, str) for x in event) or isinstance(event, list) and all(isinstance(x, int) for x in event):
        print("rootLevelPrimitiveOneOfEvent received")
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
| 200 | Event processed successfully |
| 422 | Event processing failed |

