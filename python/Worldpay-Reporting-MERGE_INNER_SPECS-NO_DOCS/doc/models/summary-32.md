
# Summary 32

## Structure

`Summary32`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sale_count` | `int` | Optional | Count of sales for individual card network over a given period of time.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `sale_amount` | `float` | Optional | Amount of sales for individual card network over a given period of time.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `return_count` | `int` | Optional | Count of returns for individual card network over a given period of time.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `return_amount` | `float` | Optional | Amount of returns for individual card network over a given period of time.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `net_amount` | `float` | Optional | Refers to the Amount left over after All deductions are made. (for All Credit cards like Visa, Mastercard, Amex, Discover)<br>Net Amount = Sales Amount - 0 (for Debit transactions).<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `merchant_id` | `str` | Optional | The Merchant hierarchy level is the last level in the Vertical Hierarchy. MID is the unique identifier assigned for a processing location, business type, MCC Code that requires a specific value to define merchant authorizations, settlement, reporting, pricing and billing levels.<br><br>**Constraints**: *Maximum Length*: `16` |

## Example (as JSON)

```json
{
  "saleCount": 10,
  "saleAmount": 120.34,
  "returnCount": 11,
  "returnAmount": 20.56,
  "netAmount": 100.23,
  "merchantId": "4445123456789"
}
```

