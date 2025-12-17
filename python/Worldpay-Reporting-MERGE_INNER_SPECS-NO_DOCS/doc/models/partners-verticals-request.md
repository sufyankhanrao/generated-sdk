
# Partners Verticals Request

## Structure

`PartnersVerticalsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `independent_sales_channel_codes` | `List[str]` | Required | Independent sales channel value provides a secondary entity under the independent sales organization hierarchy level.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `5`, *Maximum Length*: `256` |
| `month_range` | [`MonthRange`](../../doc/models/month-range.md) | Required | Month Range for which the transaction is processed. |
| `verticals` | [`List[VerticalEnum]`](../../doc/models/vertical-enum.md) | Optional | Indicates a specific industry or market carried out by the Organization.<br><br>**Constraints**: *Maximum Length*: `11` |
| `sort_results_by` | [`SortPartnerVertical`](../../doc/models/sort-partner-vertical.md) | Optional | Used to sort the results. |

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
    "TRAVEL",
    "B2B"
  ],
  "sortResultsBy": {
    "fieldName": "PROCESS_REVENUE",
    "orderBy": "ASC"
  }
}
```

