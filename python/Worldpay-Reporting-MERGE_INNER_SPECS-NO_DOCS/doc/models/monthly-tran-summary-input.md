
# Monthly Tran Summary Input

## Structure

`MonthlyTranSummaryInput`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationType2`](../../doc/models/pagination-type-2.md) | Optional | Used for pagination. |
| `sort_results_by` | [`SortResultsBy`](../../doc/models/sort-results-by.md) | Optional | Sort results by option for real time authorization transactions. |
| `merchant_id` | `str` | Optional | The Merchant hierarchy level is the last level in the Vertical Hierarchy. MID is the unique identifier assigned for a processing location, business type, MCC Code that requires a specific value to define merchant authorizations, settlement, reporting, pricing and billing levels.<br><br>**Constraints**: *Maximum Length*: `16` |
| `chain_code` | `str` | Optional | The Chain Code is the level of the merchant hierarchy that groups merchant identifiers (MIDs) and any related roll-up values under a common identifier for settlement, billing and reporting. Chain Code is the primary identifier for merchants boarded in MDB (Merchant Database) system.<br><br>**Constraints**: *Maximum Length*: `6` |
| `month_range` | [`MonthRange`](../../doc/models/month-range.md) | Optional | Refers to the month range |

## Example (as JSON)

```json
{
  "merchantId": "4445191034215",
  "chainCode": "070110",
  "pagination": {
    "pageNumber": 106,
    "pageSize": 134
  },
  "sortResultsBy": {
    "fieldName": "BATCH_NUMBER",
    "orderBy": "ASC"
  },
  "monthRange": {
    "startMonth": "startMonth8",
    "endMonth": "endMonth6"
  }
}
```

