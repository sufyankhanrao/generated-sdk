
# Summary 4

## Structure

`Summary4`

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
| `merchant_id` | `str` | Optional | The Merchant hierarchy level is the last level in the Vertical Hierarchy. MID is the unique identifier assigned for a processing location, business type, MCC Code that requires a specific value to define merchant authorizations, settlement, reporting, pricing and billing levels.<br><br>**Constraints**: *Maximum Length*: `16` |

## Example (as JSON)

```json
{
  "approvedCount": 10,
  "declinedAmountPercent": 14.65,
  "merchantId": "4445091034215",
  "approvedAmount": 15.0,
  "declinedCount": 8,
  "declinedAmount": 15.0,
  "approvedCountPercent": 15.0
}
```

