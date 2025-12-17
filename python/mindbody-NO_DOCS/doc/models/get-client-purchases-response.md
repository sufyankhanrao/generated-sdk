
# Get Client Purchases Response

## Structure

`GetClientPurchasesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `purchases` | [`List[ClientPurchaseRecord]`](../../doc/models/client-purchase-record.md) | Optional | Contains information that describes the item sold and the payment. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "Purchases": [
    {
      "Sale": {
        "Id": 174,
        "SaleDate": "2016-03-13T12:52:32.123Z",
        "SaleTime": "SaleTime0",
        "SaleDateTime": "2016-03-13T12:52:32.123Z",
        "OriginalSaleDateTime": "2016-03-13T12:52:32.123Z"
      },
      "Description": "Description6",
      "AccountPayment": false,
      "Price": 130.6,
      "AmountPaid": 155.16
    },
    {
      "Sale": {
        "Id": 174,
        "SaleDate": "2016-03-13T12:52:32.123Z",
        "SaleTime": "SaleTime0",
        "SaleDateTime": "2016-03-13T12:52:32.123Z",
        "OriginalSaleDateTime": "2016-03-13T12:52:32.123Z"
      },
      "Description": "Description6",
      "AccountPayment": false,
      "Price": 130.6,
      "AmountPaid": 155.16
    },
    {
      "Sale": {
        "Id": 174,
        "SaleDate": "2016-03-13T12:52:32.123Z",
        "SaleTime": "SaleTime0",
        "SaleDateTime": "2016-03-13T12:52:32.123Z",
        "OriginalSaleDateTime": "2016-03-13T12:52:32.123Z"
      },
      "Description": "Description6",
      "AccountPayment": false,
      "Price": 130.6,
      "AmountPaid": 155.16
    }
  ]
}
```

