
# Revenue by Party Request

## Structure

`RevenueByPartyRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `independent_sales_channel_codes` | `List[str]` | Required | Independent sales channel value provides a secondary entity under the independent sales organization hierarchy level.<br><br>**Constraints**: *Maximum Length*: `256` |
| `parties` | [`List[PartyEnum]`](../../doc/models/party-enum.md) | Optional | Individual or entity that is involved in a transaction.<br><br>**Constraints**: *Maximum Length*: `256` |
| `month_range` | [`MonthRange`](../../doc/models/month-range.md) | Required | Month Range for which the transaction is processed. |
| `sort_results_by` | [`SortResultsBy`](../../doc/models/sort-results-by.md) | Optional | Used to sort the results. |

## Example (as JSON)

```json
{
  "independentSalesChannelCodes": [
    "MTBCON",
    "MTBNEW"
  ],
  "monthRange": {
    "startMonth": "2022-01",
    "endMonth": "2022-06"
  },
  "parties": [
    "ACQUIRE_NON_CORE",
    "GATEWAY",
    "INTERCHANGE"
  ],
  "sortResultsBy": {
    "fieldName": "BATCH_NUMBER",
    "orderBy": "ASC"
  }
}
```

