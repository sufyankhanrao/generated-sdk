
# ACH Rejects Search Request

The ACH Rejects Search request is used to search for rejected ACH transactions based on the criteria provided within the API endpoint request for a given timeframe.  The From and To dates are required and are used to limit the number of transactions that fall inbetween and including those dates.

## Structure

`ACHRejectsSearchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationType1`](../../doc/models/pagination-type-1.md) | Optional | - |
| `hierarchy` | [`Entity2`](../../doc/models/entity-2.md) | Required | - |
| `date_range` | [`DateRange`](../../doc/models/date-range.md) | Required | - |
| `funding_method` | [`FundingMethodEnum`](../../doc/models/funding-method-enum.md) | Required | Refers to the method that was used for the deposit. Bank Account indicates the methods used for a payment.<br><br>**Constraints**: *Maximum Length*: `12` |
| `sort_results_by` | [`OrderByForErrorsByCategoryType`](../../doc/models/order-by-for-errors-by-category-type.md) | Optional | The sort results by field is used in request to establish the sort order for the data to be returned in ascending or descending order. |

## Example (as JSON)

```json
{
  "hierarchy": {
    "level": "MERCHANT",
    "values": [
      "4445000860700",
      "4445000860702"
    ],
    "chainCode": "OA1234"
  },
  "dateRange": {
    "fromDate": "2019-10-27",
    "toDate": "2019-11-27"
  },
  "fundingMethod": "PREPAID_CARD",
  "pagination": {
    "pageNumber": 16776215,
    "pageSize": 1000
  },
  "sortResultsBy": {
    "fieldName": "RETURN_DATE",
    "orderBy": "ASC"
  }
}
```

