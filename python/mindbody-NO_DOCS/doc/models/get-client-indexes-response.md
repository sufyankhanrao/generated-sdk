
# Get Client Indexes Response

## Structure

`GetClientIndexesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_indexes` | [`List[ClientIndex]`](../../doc/models/client-index.md) | Optional | Contains information about the client indexes. |

## Example (as JSON)

```json
{
  "ClientIndexes": [
    {
      "Id": 102,
      "Name": "Name0",
      "RequiredBusinessMode": false,
      "RequiredConsumerMode": false,
      "Values": [
        {
          "Active": false,
          "Id": 34,
          "Name": "Name4"
        }
      ]
    },
    {
      "Id": 102,
      "Name": "Name0",
      "RequiredBusinessMode": false,
      "RequiredConsumerMode": false,
      "Values": [
        {
          "Active": false,
          "Id": 34,
          "Name": "Name4"
        }
      ]
    },
    {
      "Id": 102,
      "Name": "Name0",
      "RequiredBusinessMode": false,
      "RequiredConsumerMode": false,
      "Values": [
        {
          "Active": false,
          "Id": 34,
          "Name": "Name4"
        }
      ]
    }
  ]
}
```

