
# Search Auth Transactions Response

Search results for authorization transaction.

## Structure

`SearchAuthTransactionsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationResponse1`](../../doc/models/pagination-response-1.md) | Optional | Used for pagination |
| `authorizations` | [`List[Authorization]`](../../doc/models/authorization.md) | Optional | Resource is used to authorization details. |

## Example (as JSON)

```json
{
  "pagination": {
    "pageNumber": 16776215,
    "pageSize": 1000,
    "totalRowCount": 9999998999,
    "totalReturnedCount": 9999998999
  },
  "authorizations": [
    {
      "transactionId": "transactionId2",
      "transactionDateTime": "transactionDateTime6",
      "processDate": "processDate2",
      "transactionStatus": null,
      "transactionType": null
    },
    {
      "transactionId": "transactionId2",
      "transactionDateTime": "transactionDateTime6",
      "processDate": "processDate2",
      "transactionStatus": null,
      "transactionType": null
    },
    {
      "transactionId": "transactionId2",
      "transactionDateTime": "transactionDateTime6",
      "processDate": "processDate2",
      "transactionStatus": null,
      "transactionType": null
    }
  ]
}
```

