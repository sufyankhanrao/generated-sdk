
# Deposit Account Number Request

## Structure

`DepositAccountNumberRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationType1`](../../doc/models/pagination-type-1.md) | Optional | Used for pagination. |
| `hierarchy` | [`Entity3`](../../doc/models/entity-3.md) | Required | Refers to merchant hierarchy levels |
| `account_number` | `str` | Optional | Account number or Card number involved in the rejected transaction. <br> Passing account number in request, Entity type and Value is mandatory to pass.<br>Supports entity type as Merchant and Chain .<br><br>**Constraints**: *Maximum Length*: `19` |
| `date_range` | [`DateRangeSearch`](../../doc/models/date-range-search.md) | Required | A range of dates that includes a particular start and end date and all dates in between the range. |

## Example (as JSON)

```json
{
  "hierarchy": {
    "level": "MERCHANT",
    "values": [
      "4445001234567",
      "4445002345678"
    ],
    "chainCode": "172111"
  },
  "accountNumber": "4445123456789012",
  "dateRange": {
    "fromDate": "2021-12-01",
    "toDate": "2021-12-01"
  },
  "pagination": {
    "pageNumber": 16776215,
    "pageSize": 1000
  }
}
```

