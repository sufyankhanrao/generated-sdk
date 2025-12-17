
# Get Commissions Response

## Structure

`GetCommissionsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `commissions` | [`List[CommissionPayrollPurchaseEvent]`](../../doc/models/commission-payroll-purchase-event.md) | Optional | Contains information about commissions earned by staff for sales within the given date range. Results are ordered by `SaleId`, then by `StaffId`. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "Commissions": [
    {
      "StaffId": 216,
      "SaleDateTime": "2016-03-13T12:52:32.123Z",
      "SaleId": 122,
      "SaleType": "SaleType6",
      "ProductId": 164
    }
  ]
}
```

