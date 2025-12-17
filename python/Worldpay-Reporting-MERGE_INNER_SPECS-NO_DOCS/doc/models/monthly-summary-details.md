
# Monthly Summary Details

## Structure

`MonthlySummaryDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Optional | The Merchant hierarchy level is the last level in the Vertical Hierarchy. MID is the unique identifier assigned for a processing location, business type, MCC Code that requires a specific value to define merchant authorizations, settlement, reporting, pricing and billing levels.<br><br>**Constraints**: *Maximum Length*: `16` |
| `total_sales_amount` | `float` | Optional | Sum of credit card sales amount and debit card sales amount.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_sales_count` | `int` | Optional | Sum of credit card sales count and debit card sales count.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `total_settled_sales_amount` | `float` | Optional | Sum of net credit sales amount and net debit sales amount.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `credit_sales_amount` | `float` | Optional | Amount of credit card sales.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `credit_sales_count` | `int` | Optional | Count of credit card sales.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `credit_returns_amount` | `float` | Optional | Amount of credit card returns.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `credit_returns_count` | `int` | Optional | Count of credit card returns.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `net_credit_sales_amount` | `float` | Optional | Credit card sales amount - Credit card returns amount.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `debit_sales_amount` | `float` | Optional | Debit card sales amount.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `debit_sales_count` | `int` | Optional | Debit card sales count.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `debit_returns_amount` | `float` | Optional | Debit card returns amount.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `debit_returns_count` | `int` | Optional | Debit card returns amount.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `net_debit_sales_amount` | `float` | Optional | Debit card sales amount - 0.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `gift_sales_amount` | `float` | Optional | Amount of gift sales.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `gift_sales_count` | `int` | Optional | Count of gift sales.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `chargeback_sales_amount` | `float` | Optional | Amount of chargeback sales amount<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `chargeback_sales_count` | `int` | Optional | Count of chargeback sales amount<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `process_month` | `str` | Optional | Refers to the process month<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7`, *Pattern*: `^[0-9]{4}-[0-9]{2}$` |
| `merchant_category_code` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Code and description define the category of merchant. |

## Example (as JSON)

```json
{
  "merchantId": "4445191034215",
  "totalSalesAmount": 96295675.24,
  "totalSalesCount": 335594,
  "totalSettledSalesAmount": 96295675.24,
  "creditSalesAmount": 58.59,
  "creditSalesCount": 20,
  "creditReturnsAmount": 58.59,
  "creditReturnsCount": 20,
  "netCreditSalesAmount": 58.59,
  "debitSalesAmount": 32734704.99,
  "debitSalesCount": 20,
  "debitReturnsAmount": 58.59,
  "debitReturnsCount": 20,
  "netDebitSalesAmount": 58.59,
  "giftSalesAmount": 58.59,
  "giftSalesCount": 20,
  "chargebackSalesAmount": 58.59,
  "chargebackSalesCount": 20,
  "processMonth": "2022-12"
}
```

