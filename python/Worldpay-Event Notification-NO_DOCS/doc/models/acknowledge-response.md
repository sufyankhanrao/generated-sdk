
# Acknowledge Response

## Structure

`AcknowledgeResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `http_status_code` | `str` | Required | Http response status Code<br><br>**Constraints**: *Maximum Length*: `3` |
| `http_status_message` | `str` | Required | Http response status Message<br><br>**Constraints**: *Maximum Length*: `256` |

## Example (as JSON)

```json
{
  "httpStatusCode": "200",
  "httpStatusMessage": "OK"
}
```

