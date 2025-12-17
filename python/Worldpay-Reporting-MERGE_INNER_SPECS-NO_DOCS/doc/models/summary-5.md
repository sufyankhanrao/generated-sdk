
# Summary 5

## Structure

`Summary5`

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
| `chain_code` | `str` | Optional | The Chain Code is the level of the merchant hierarchy that groups merchant identifiers (MIDs) and any related roll-up values under a common identifier for settlement, billing and reporting. Chain Code is the primary identifier for merchants boarded in MDB (Merchant Database) system.<br><br>**Constraints**: *Maximum Length*: `6` |

## Example (as JSON)

```json
{
  "approvedCount": 10,
  "declinedAmountPercent": 14.65,
  "chainCode": "1X0010",
  "approvedAmount": 15.0,
  "declinedCount": 10,
  "declinedAmount": 15.0,
  "approvedCountPercent": 15.0
}
```

