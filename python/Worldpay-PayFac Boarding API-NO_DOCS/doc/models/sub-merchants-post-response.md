
# Sub Merchants Post Response

## Structure

`SubMerchantsPostResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `id` | `str` | Optional | Resource Identifier |
| `mid` | `str` | Optional | - |
| `accepted_cards` | [`List[AcceptedCard]`](../../doc/models/accepted-card.md) | Optional | Method of Payment or Card Type related attributes. Only the attributes specific to the Card type needs to be included. |
| `express_sub_account` | [`ExpressSubAccount`](../../doc/models/express-sub-account.md) | Optional | Express gateway information |

## Example (as JSON)

```json
{
  "correlationId": "correlationId0",
  "httpStatusCode": "httpStatusCode4",
  "httpStatusMessage": "httpStatusMessage0",
  "id": "id0",
  "mid": "mid0"
}
```

