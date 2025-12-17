
# Valutec Response

## Structure

`ValutecResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `division_code` | `str` | Optional | The Division under which the submerchant is grouped. If the Division code needs to be updated for a submerchant, it can be done using PATCH /submerchants/{id} endpoint with the Division code sent in the request body |
| `gift_group_id` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "divisionCode": "001",
  "correlationId": "correlationId8",
  "httpStatusCode": "httpStatusCode2",
  "httpStatusMessage": "httpStatusMessage2",
  "giftGroupId": 112
}
```

