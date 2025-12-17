
# Monthly Summary Chain Details

## Structure

`MonthlySummaryChainDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `chain_code` | `str` | Optional | The Chain Code is the level of the merchant hierarchy that groups merchant identifiers (MIDs) and any related roll-up values under a common identifier for settlement, billing and reporting. Chain Code is the primary identifier for merchants boarded in MDB (Merchant Database) system.<br><br>**Constraints**: *Maximum Length*: `6` |
| `total_chargeback_sales_count` | `int` | Optional | Count of all chargeback sales<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `total_chargeback_sales_amount` | `float` | Optional | Sum of all chargeback Sales<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_transaction_amount` | `float` | Optional | Total amount of chargebacks<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_transaction_count` | `int` | Optional | total count of transaction<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `process_month_start` | `str` | Optional | Refers to the starting month<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7`, *Pattern*: `^[0-9]{4}-[0-9]{2}$` |
| `process_month_end` | `str` | Optional | Refers to the ending month<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7`, *Pattern*: `^[0-9]{4}-[0-9]{2}$` |

## Example (as JSON)

```json
{
  "chainCode": "AB1234",
  "totalChargebackSalesCount": 2356,
  "totalChargebackSalesAmount": 335594.56,
  "totalTransactionAmount": 962955.24,
  "totalTransactionCount": 20,
  "processMonthStart": "2022-12",
  "processMonthEnd": "2023-02"
}
```

