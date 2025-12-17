## Webhooks No Verification Handler

Demo group with no payload verification (unsigned webhooks).

## Events

Events available in this group. Subscribe to receive webhook notifications when these events occur.

| Name | Description |
|  --- | --- |
| [auditLogEvent](../../../doc/events/webhooks/webhooks_no_verification/audit-log-event.md) | Demonstrates an event without signature verification. |
| [rootLevelPrimitiveOneOfEvent](../../../doc/events/webhooks/webhooks_no_verification/root-level-primitive-one-of-event.md) | Root-level oneOf across primitives and collections of primitives/enums. |

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
from webhooksandcallbacksapi.models.audit_log_event import (
    AuditLogEvent
)
from webhooksandcallbacksapi.utilities.request_adapter import (
    to_core_request
)

app = Flask(__name__)

@app.route("/webhooks", methods=["POST"])
def Webhooks():
    # Step 1: Convert the incoming request using to_core_request (Django/Flask)
    #         or await to_core_request_async (FastAPI).
    core_req = to_core_request(request)

    # Step 2: Parse the request into a typed event.
    event = WebhooksNoVerificationHandler.parse_event(core_req)

    # Step 3: Pattern match on the event type and handle it.
    if isinstance(event, AuditLogEvent):
        print("auditLogEvent received")
        # TODO: add handling logic
    elif isinstance(event, str) or isinstance(event, int) or isinstance(event, list) and all(isinstance(x, str) for x in event) or isinstance(event, list) and all(isinstance(x, int) for x in event):
        print("rootLevelPrimitiveOneOfEvent received")
        # TODO: add handling logic
    elif isinstance(event, UnknownEvent):
        print("Unknown event")
        # TODO: add unknown event handling

    # Step 4: Return 200 OK to acknowledge receipt (adjust with other codes if needed).
    return Response(status=200)
```

