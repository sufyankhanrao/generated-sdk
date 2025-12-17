
# Summary 22

## Structure

`Summary22`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `credits_count` | `int` | Optional | Refers to count of credits.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `credited_amount` | `float` | Optional | Refers to an entry that shows that money has been received.Currency is in USD.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `debits_count` | `int` | Optional | Refers to count of debits.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `debited_amount` | `float` | Optional | Refers to an entry that shows that money has been deducted.Currency is in USD.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `net_amount` | `float` | Optional | Refers to the Amount left over after all deductions are made.<br><br>NetAmount= CreditedAmount - DebitedAmount.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `merchant_id` | `str` | Optional | The Merchant hierarchy level is the last level in the Vertical Hierarchy. MID is the unique identifier assigned for a processing location, business type, MCC Code that requires a specific value to define merchant authorizations, settlement, reporting, pricing and billing levels.<br><br>**Constraints**: *Maximum Length*: `20` |

## Example (as JSON)

```json
{
  "creditsCount": 2,
  "creditedAmount": 33.5,
  "debitsCount": 3,
  "debitedAmount": 32.4,
  "netAmount": 1.11,
  "merchantId": "4445091034215"
}
```

