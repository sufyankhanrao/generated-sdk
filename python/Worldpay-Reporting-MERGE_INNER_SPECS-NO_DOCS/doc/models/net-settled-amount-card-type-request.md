
# Net Settled Amount Card Type Request

Request message to get net settlement amount for card types.

## Structure

`NetSettledAmountCardTypeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `independent_sales_channel_codes` | `List[str]` | Required | Independent sales channel value provides a secondary entity under the independent sales organization hierarchy level.<br><br>**Constraints**: *Maximum Length*: `265` |
| `card_networks` | [`List[CardNetwork1Enum]`](../../doc/models/card-network-1-enum.md) | Optional | Brand or Network to which the card is associated.<br><br>**Constraints**: *Maximum Length*: `19` |
| `messaging_types` | `List[str]` | Optional | Card holder authentication method. Possible Values SIG (Signature); PIN (Pin) base transaction.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `2`, *Maximum Length*: `256` |
| `card_present` | `bool` | Optional | Indicates if card was present at the POS. Possible values True or False |
| `month_range` | [`MonthRange`](../../doc/models/month-range.md) | Required | Month Range for which the transaction is processed. |
| `sort_results_by` | [`SortSettlement`](../../doc/models/sort-settlement.md) | Optional | Used to sort the results. |

## Example (as JSON)

```json
{
  "independentSalesChannelCodes": [
    "MTBCON",
    "MTBNEW"
  ],
  "messagingTypes": [
    "PIN",
    "SIG"
  ],
  "cardPresent": true,
  "monthRange": {
    "startMonth": "2022-01",
    "endMonth": "2022-06"
  },
  "cardNetworks": [
    "AMEX",
    "WIC",
    "VOYAGER"
  ],
  "sortResultsBy": {
    "fieldName": "SETTLED_GROSS_AMOUNT",
    "orderBy": "ASC"
  }
}
```

