
# Response Transaction Bin Info

## Structure

`ResponseTransactionBinInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type94Enum`](../../doc/models/type-94-enum.md) | Optional | Resource Type<br><br>**Default**: `'TransactionBinInfo'` |
| `data` | [`Data23`](../../doc/models/data-23.md) | Optional | - |

## Example (as JSON)

```json
{
  "type": "TransactionBinInfo",
  "data": {
    "issuer_bank_name": "issuer_bank_name6",
    "country_code": "country_code0",
    "detail_card_product": "detail_card_product2",
    "detail_card_indicator": "detail_card_indicator2",
    "fsa_indicator": "fsa_indicator8"
  }
}
```

