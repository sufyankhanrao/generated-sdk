
# Summary 62

## Structure

`Summary62`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sale_count` | `int` | Optional | Count of sales for individual card network over a given period of time.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `sale_amount` | `float` | Optional | Amount of sales for individual card network over a given period of time.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `return_count` | `int` | Optional | Count of returns for individual card network over a given period of time.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `return_amount` | `float` | Optional | Amount of returns for individual card network over a given period of time.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `net_amount` | `float` | Optional | Refers to the Amount left over after All deductions are made. (for All Credit cards like Visa, Mastercard, Amex, Discover)<br>Net Amount = Sales Amount - 0 (for Debit transactions).<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `chain_code` | `str` | Optional | The Chain Code is the level of the merchant hierarchy that groups merchant identifiers (MIDs) and any related roll-up values under a common identifier for settlement, billing and reporting. Chain Code is the primary identifier for merchants boarded in MDB (Merchant Database) system.<br><br>**Constraints**: *Maximum Length*: `6` |

## Example (as JSON)

```json
{
  "saleCount": 10,
  "saleAmount": 120.34,
  "returnCount": 11,
  "returnAmount": 20.56,
  "netAmount": 100.23,
  "chainCode": "AB1234"
}
```

