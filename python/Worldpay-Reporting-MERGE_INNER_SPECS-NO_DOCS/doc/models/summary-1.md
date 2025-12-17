
# Summary 1

## Structure

`Summary1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `approved_count` | `int` | Optional | Count of Approved Transactions.<br><br>**Constraints**: `<= 10` |
| `approved_amount` | `float` | Optional | Sum of Amount of Approved Transactions.<br><br>**Constraints**: `<= 15` |
| `declined_count` | `int` | Optional | Count of Declined Transactions.<br><br>**Constraints**: `<= 10` |
| `declined_amount` | `float` | Optional | Sum of Amount of Declined Transactions.<br><br>**Constraints**: `<= 15` |
| `approved_count_percent` | `float` | Optional | Ratio of Count of Approved Transactions to the Count of Total Transctions.<br><br>**Constraints**: `<= 15` |
| `approved_amount_percent` | `float` | Optional | Ratio of the Sum of Amount of Approved Transactions to the Sum of Amount of Total Transctions.<br><br>**Constraints**: `<= 15` |
| `declined_count_percent` | `float` | Optional | Ratio of Count of Declined Transactions to the Count of Total Transctions.<br><br>**Constraints**: `<= 15` |
| `declined_amount_percent` | `float` | Optional | Ratio of the Sum of Amount of Declined Transactions to the Sum of Amount of Total Transctions.<br><br>**Constraints**: `<= 15` |
| `transaction_date` | `str` | Optional | The transaction date is the specific day when a financial transaction, such as a purchase or sale, takes place officially.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |

## Example (as JSON)

```json
{
  "approvedCount": 10,
  "declinedAmountPercent": 14.65,
  "transactionDate": "2021-12-21",
  "approvedAmount": 15.0,
  "declinedCount": 10,
  "declinedAmount": 15.0,
  "approvedCountPercent": 15.0
}
```

