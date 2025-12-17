
# Revenue by Verticals Request

## Structure

`RevenueByVerticalsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `independent_sales_channel_codes` | `List[str]` | Required | Independent sales channel value provides a secondary entity under the independent sales organization hierarchy level.<br><br>**Constraints**: *Maximum Length*: `256` |
| `verticals` | [`List[VerticalEnum]`](../../doc/models/vertical-enum.md) | Optional | Indicates a specific industry or market carried out by the Organization<br><br>**Constraints**: *Maximum Length*: `15` |
| `month_range` | [`MonthRange`](../../doc/models/month-range.md) | Required | Month Range for which the transaction is processed. |
| `sort_results_by` | [`SortRevenueVertical`](../../doc/models/sort-revenue-vertical.md) | Optional | Used to sort the results. |

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
  "verticals": [
    "B2B",
    "DRUG_STORES"
  ],
  "sortResultsBy": {
    "fieldName": "TOTAL_EFFECTIVE_RATE",
    "orderBy": "ASC"
  }
}
```

