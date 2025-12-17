
# ACH Rejects Search Response

ACH Reject search response details

## Structure

`ACHRejectsSearchResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationResponse1`](../../doc/models/pagination-response-1.md) | Optional | Pagination response details |
| `depositerrors` | [`List[RejRealTimeTransaction]`](../../doc/models/rej-real-time-transaction.md) | Optional | deposit error details |

## Example (as JSON)

```json
{
  "pagination": {
    "pageNumber": 16776215,
    "pageSize": 1000,
    "totalRowCount": 9999998999,
    "totalReturnedCount": 9999998999
  },
  "depositerrors": [
    {
      "returnDate": "returnDate6",
      "effectiveDate": "effectiveDate8",
      "fundingMethod": "fundingMethod8",
      "rejectionReason": {
        "code": "code8",
        "description": "description0"
      },
      "routingNumber": 100000000
    },
    {
      "returnDate": "returnDate6",
      "effectiveDate": "effectiveDate8",
      "fundingMethod": "fundingMethod8",
      "rejectionReason": {
        "code": "code8",
        "description": "description0"
      },
      "routingNumber": 100000000
    }
  ]
}
```

