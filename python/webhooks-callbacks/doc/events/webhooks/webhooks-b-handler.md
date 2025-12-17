## Webhooks B Handler

Multi-event webhook group with oneOf payload structures. Uses a message template that also includes a request header pointer.

## Signature Verification

This handler uses the `HMAC Signature Verifier` for request verification. Each event in this group includes an `X-Webhook-Signature` header that will be validated using your shared `secret-key` to ensure request authenticity.

## Events

Events available in this group. Subscribe to receive webhook notifications when these events occur.

| Name | Description |
|  --- | --- |
| [userNotificationEvent](../../../doc/events/webhooks/webhooks_b/user-notification-event.md) | Triggered when user-related notifications occur |
| [systemNotificationEvent](../../../doc/events/webhooks/webhooks_b/system-notification-event.md) | Triggered when system-wide notifications occur |
| [inventoryChangeEvent](../../../doc/events/webhooks/webhooks_b/inventory-change-event.md) | Triggered when inventory stock levels change |

## SDK Usage Example

```python
from flask import (
    Flask,
    Response,
    request
)

from webhooksandcallbacksapi.events.signature_verification_failure import (
    SignatureVerificationFailure
)
from webhooksandcallbacksapi.events.unknown_event import (
    UnknownEvent
)
from webhooksandcallbacksapi.events.webhooks.webhooks_b_handler import (
    WebhooksBHandler
)
from webhooksandcallbacksapi.models.inventory_stock_decrease_event import (
    InventoryStockDecreaseEvent
)
from webhooksandcallbacksapi.models.inventory_stock_depleted_event import (
    InventoryStockDepletedEvent
)
from webhooksandcallbacksapi.models.inventory_stock_increase_event import (
    InventoryStockIncreaseEvent
)
from webhooksandcallbacksapi.models.system_alert_notification_event import (
    SystemAlertNotificationEvent
)
from webhooksandcallbacksapi.models.system_maintenance_notification_event import (
    SystemMaintenanceNotificationEvent
)
from webhooksandcallbacksapi.models.system_performance_notification_event import (
    SystemPerformanceNotificationEvent
)
from webhooksandcallbacksapi.models.user_action_notification_event import (
    UserActionNotificationEvent
)
from webhooksandcallbacksapi.models.user_preference_notification_event import (
    UserPreferenceNotificationEvent
)
from webhooksandcallbacksapi.models.user_status_notification_event import (
    UserStatusNotificationEvent
)
from webhooksandcallbacksapi.utilities.request_adapter import (
    to_core_request
)

app = Flask(__name__)

@app.route("/webhooks", methods=["POST"])
def Webhooks():
    # Step 1: Create the handler with your shared secret key.
    handler = WebhooksBHandler(secret_key="your-shared-secret")

    # Step 2: Convert the incoming request using to_core_request (Django/Flask)
    #         or await to_core_request_async (FastAPI).
    core_req = to_core_request(request)

    # Step 3: Verify and parse the request into a typed event.
    event = handler.verify_and_parse_event(core_req)

    # Step 4: Pattern match on the event type and handle it.
    if isinstance(event, UserActionNotificationEvent) or isinstance(event, UserStatusNotificationEvent) or isinstance(event, UserPreferenceNotificationEvent):
        print("userNotificationEvent received")
        # TODO: add handling logic
    elif isinstance(event, SystemAlertNotificationEvent) or isinstance(event, SystemMaintenanceNotificationEvent) or isinstance(event, SystemPerformanceNotificationEvent):
        print("systemNotificationEvent received")
        # TODO: add handling logic
    elif isinstance(event, InventoryStockIncreaseEvent) or isinstance(event, InventoryStockDecreaseEvent) or isinstance(event, InventoryStockDepletedEvent):
        print("inventoryChangeEvent received")
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

