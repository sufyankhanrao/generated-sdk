
# Summary 61

## Structure

`Summary61`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `credits_count` | `int` | Optional | Refers to count of credits.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `credited_amount` | `float` | Optional | Refers to an entry that shows that money has been received.Currency is in USD.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `debits_count` | `int` | Optional | Refers to count of debits.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `debited_amount` | `float` | Optional | Refers to an entry that shows that money has been deducted.Currency is in USD.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `net_amount` | `float` | Optional | Refers to the Amount left over after all deductions are made.<br><br>NetAmount= CreditedAmount - DebitedAmount.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `account_number` | `str` | Optional | Account number or Card number involved in the rejected transaction<br><br>**Constraints**: *Maximum Length*: `19` |
| `account_type` | `str` | Optional | Indicates to type of account<br><br>**Constraints**: *Maximum Length*: `255` |
| `chain_code` | `str` | Optional | The Chain Code is the level of the merchant hierarchy that groups merchant identifiers (MIDs) and any related roll-up values under a common identifier for settlement, billing and reporting. Chain Code is the primary identifier for merchants boarded in MDB (Merchant Database) system.<br><br>**Constraints**: *Maximum Length*: `6` |
| `merchant_id` | `str` | Optional | The Merchant hierarchy level is the last level in the Vertical Hierarchy. MID is the unique identifier assigned for a processing location, business type, MCC Code that requires a specific value to define merchant authorizations, settlement, reporting, pricing and billing levels.<br><br>**Constraints**: *Maximum Length*: `20` |

## Example (as JSON)

```json
{
  "creditsCount": 2,
  "creditedAmount": 33.5,
  "debitsCount": 3,
  "debitedAmount": 32.4,
  "netAmount": 1.11,
  "accountNumber": "4445123456789012",
  "accountType": "FED",
  "chainCode": "172111",
  "merchantId": "4445091034215"
}
```

