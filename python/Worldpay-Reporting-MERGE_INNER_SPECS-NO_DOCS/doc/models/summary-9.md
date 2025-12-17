
# Summary 9

## Structure

`Summary9`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sale_count` | `int` | Optional | Count of sales for individual card network over a given period of time.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `sale_amount` | `float` | Optional | Amount of sales for individual card network over a given period of time.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `return_count` | `int` | Optional | Count of returns for individual card network over a given period of time.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `return_amount` | `float` | Optional | Amount of returns for individual card network over a given period of time.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `net_amount` | `float` | Optional | Refers to the Amount left over after All deductions are made. (for All Credit cards like Visa, Mastercard, Amex, Discover)<br>Net Amount = Sales Amount - 0 (for Debit transactions).<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `card_type` | [`CardType7Enum`](../../doc/models/card-type-7-enum.md) | Optional | - |
| `card_network` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | - |

## Example (as JSON)

```json
{
  "saleCount": 10,
  "saleAmount": 120.34,
  "returnCount": 11,
  "returnAmount": 20.56,
  "netAmount": 100.23,
  "cardType": "CREDIT",
  "cardNetwork": {
    "code": "BML",
    "shortDescription": "Bill Me Later.",
    "longDescription": "BILL ME LATER."
  }
}
```

