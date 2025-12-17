
# Summary Responses

## Structure

`SummaryResponses`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_approved_count` | `int` | Optional | Count of Approved Transactions.<br><br>**Constraints**: `<= 10` |
| `total_approved_amount` | `float` | Optional | Sum of Amount of Approved Transactions.<br><br>**Constraints**: `<= 15` |
| `total_declined_count` | `int` | Optional | Count of Declined Transactions.<br><br>**Constraints**: `<= 10` |
| `total_declined_amount` | `float` | Optional | Sum of Amount of Declined Transactions.<br><br>**Constraints**: `<= 15` |
| `total_approved_count_percent` | `float` | Optional | Ratio of Count of Approved Transactions to the Count of Total Transctions.<br><br>**Constraints**: `<= 15` |
| `total_approved_amount_percent` | `float` | Optional | Ratio of the Sum of Amount of Approved Transactions to the Sum of Amount of Total Transctions.<br><br>**Constraints**: `<= 15` |
| `total_declined_count_percent` | `float` | Optional | Ratio of Count of Declined Transactions to the Count of Total Transctions.<br><br>**Constraints**: `<= 15` |
| `total_declined_amount_percent` | `float` | Optional | Ratio of the Sum of Amount of Declined Transactions to the Sum of Amount of Total Transctions.<br><br>**Constraints**: `<= 15` |
| `total_count` | `int` | Optional | Sum of the Count of Approved Transactions and Count of declined Transactions.<br><br>**Constraints**: `<= 10` |
| `total_amount` | `float` | Optional | Sum of the Amount of Approved Transactions and Amount of declined Transactions.<br><br>**Constraints**: `<= 15` |

## Example (as JSON)

```json
{
  "totalApprovedCount": 10,
  "totalDeclinedAmountPercent": 14.65,
  "totalApprovedAmount": 15.0,
  "totalDeclinedCount": 10,
  "totalDeclinedAmount": 15.0,
  "totalApprovedCountPercent": 15.0
}
```

