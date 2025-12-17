
# Express Sub Account Post Response

## Structure

`ExpressSubAccountPostResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `id` | `str` | Optional | - |
| `mid` | `str` | Optional | - |
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

