
# Express Sub Account Get Response

## Structure

`ExpressSubAccountGetResponse`

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
  "correlationId": "correlationId4",
  "httpStatusCode": "httpStatusCode0",
  "httpStatusMessage": "httpStatusMessage4",
  "id": "id4",
  "mid": "mid4"
}
```

