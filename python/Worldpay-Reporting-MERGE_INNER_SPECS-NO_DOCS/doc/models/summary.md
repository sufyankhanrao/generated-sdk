
# Summary

## Structure

`Summary`

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
| `card_type` | `str` | Optional | Type of card type<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `255` |
| `card_network` | [`CodeAndDescription`](../../doc/models/code-and-description.md) | Optional | Type of card network |

## Example (as JSON)

```json
{
  "approvedCount": 10,
  "declinedAmountPercent": 14.65,
  "cardType": "CREDIT",
  "approvedAmount": 15.0,
  "declinedCount": 10,
  "declinedAmount": 15.0,
  "approvedCountPercent": 15.0
}
```

