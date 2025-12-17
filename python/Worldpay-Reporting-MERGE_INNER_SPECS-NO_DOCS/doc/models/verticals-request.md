
# Verticals Request

## Structure

`VerticalsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `independent_sales_channel_codes` | `List[str]` | Required | Independent sales channel value provides a secondary entity under the independent sales organization hierarchy level.<br><br>**Constraints**: *Maximum Length*: `256` |
| `verticals` | [`List[Vertical1Enum]`](../../doc/models/vertical-1-enum.md) | Optional | Indicates a specific industry or market carried out by the Organization<br><br>**Constraints**: *Maximum Length*: `15` |
| `month_range` | [`MonthRange`](../../doc/models/month-range.md) | Required | Month Range for which the transaction is processed. |
| `sort_results_by` | [`SortVerticals`](../../doc/models/sort-verticals.md) | Optional | Used to sort the results. |

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
    "RETAIL"
  ],
  "sortResultsBy": {
    "fieldName": "SETTLED_TRANSACTION_AMOUNT",
    "orderBy": "ASC"
  }
}
```

