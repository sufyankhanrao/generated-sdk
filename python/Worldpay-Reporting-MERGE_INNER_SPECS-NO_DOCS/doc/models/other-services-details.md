
# Other Services Details

Other service details.

## Structure

`OtherServicesDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dcc_currency_conversion_rate` | `float` | Optional | DCC Currency conversion is a service offered by a merchant or acquirer that enables for card holder.<br><br>**Constraints**: `>= 0`, `<= 999999.99` |
| `dcc_settlement_markup_rate` | `float` | Optional | This field indicates the standard foreign exchange transaction fee for cards.<br><br>**Constraints**: `>= 0`, `<= 999999.99` |
| `stand_in_indicator` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Indicates whether standin option is available or not. |
| `stand_in_level` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Stand in level details. |

## Example (as JSON)

```json
{
  "dccCurrencyConversionRate": 2.65,
  "dccSettlementMarkupRate": 0.0,
  "standInIndicator": {
    "code": "code8",
    "shortDescription": "shortDescription4",
    "longDescription": "longDescription0"
  },
  "standInLevel": {
    "code": "code6",
    "shortDescription": "shortDescription6",
    "longDescription": "longDescription8"
  }
}
```

