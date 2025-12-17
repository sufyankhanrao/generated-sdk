
# Entity Refs Response Item

## Structure

`EntityRefsResponseItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[EntityRefsResponse]`](../../doc/models/entity-refs-response.md) | Optional | The data object that the API returns for this request. |
| `details` | [`Details`](../../doc/models/details.md) | Optional | An object describing the response, including the request ID and pagination indicators. |
| `errors` | [`List[ErrorItem]`](../../doc/models/error-item.md) | Optional | An array of zero or more errors that occurred when the API processed the request. |

## Example (as JSON)

```json
{
  "data": [
    {
      "id": "id0",
      "created": "created0",
      "modified": "modified8",
      "creator": "String9",
      "modifier": "modifier4"
    }
  ],
  "details": {
    "requestId": "requestId2",
    "totals": {
      "key1": "val1",
      "key2": "val2"
    },
    "page": {
      "current": 164,
      "last": 78,
      "hasMore": false
    }
  },
  "errors": [
    {
      "code": 144,
      "severity": 6,
      "msg": "msg6",
      "field": "field4",
      "errorCode": "errorCode6"
    },
    {
      "code": 144,
      "severity": 6,
      "msg": "msg6",
      "field": "field4",
      "errorCode": "errorCode6"
    }
  ]
}
```

