
# Acknowledge Request

Acknowledge Request

## Structure

`AcknowledgeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `http_status_code` | `str` | Required | Http response status Code<br><br>**Constraints**: *Maximum Length*: `3` |
| `http_status_message` | `str` | Required | Http response status Message<br><br>**Constraints**: *Maximum Length*: `256` |
| `errors` | [`List[Errors]`](../../doc/models/errors.md) | Optional | Error Message |

## Example (as JSON)

```json
{
  "httpStatusCode": "200",
  "httpStatusMessage": "OK",
  "errors": [
    {
      "errorMessage": "errorMessage8",
      "target": "target2"
    },
    {
      "errorMessage": "errorMessage8",
      "target": "target2"
    }
  ]
}
```

