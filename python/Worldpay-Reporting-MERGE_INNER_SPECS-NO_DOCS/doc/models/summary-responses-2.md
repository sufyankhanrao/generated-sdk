
# Summary Responses 2

## Structure

`SummaryResponses2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_sale_count` | `int` | Optional | Indicates the total count of sales over a given period of time.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `total_sale_amount` | `float` | Optional | Indicates the total amount of sales over a given period of time.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_return_count` | `int` | Optional | Indicates the total count of returns over a given period of time.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `total_return_amount` | `float` | Optional | Indicates the total amount of returns over a given period of time.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_net_amount` | `float` | Optional | Refers to the Amount left over after All deductions are made.<br>Total Net Amount = Total Sales Amount - Total Return Amount (for All Credit cards like Visa, Mastercard, Amex, Discover)<br>Total Net Amount = Total Sales Amount - 0 (for Debit transactions).<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "totalSaleCount": 200,
  "totalSaleAmount": 2000.11,
  "totalReturnCount": 218,
  "totalReturnAmount": 844.28,
  "totalNetAmount": 1155.72
}
```

