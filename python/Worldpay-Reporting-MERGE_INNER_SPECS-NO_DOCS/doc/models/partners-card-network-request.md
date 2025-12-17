
# Partners Card Network Request

## Structure

`PartnersCardNetworkRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `independent_sales_channel_codes` | `List[str]` | Required | Independent sales channel value provides a secondary entity under the independent sales organization hierarchy level.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `5`, *Maximum Length*: `256` |
| `month_range` | [`MonthRange`](../../doc/models/month-range.md) | Required | Month Range for which the transaction is processed. |
| `card_networks` | [`List[CardNetwork1Enum]`](../../doc/models/card-network-1-enum.md) | Optional | Brand or Network to which the card is associated.<br><br>**Constraints**: *Maximum Length*: `19` |
| `sort_results_by` | [`SortPartnerCardNetwork`](../../doc/models/sort-partner-card-network.md) | Optional | Used to sort the results. |

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
  "cardNetworks": [
    "EBT",
    "DISCOVER",
    "DINERS_CLUB"
  ],
  "sortResultsBy": {
    "fieldName": "PROCESS_REVENUE",
    "orderBy": "ASC"
  }
}
```

