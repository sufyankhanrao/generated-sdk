
# Summary 31

## Structure

`Summary31`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `credits_count` | `int` | Optional | Refers to count of credits.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `credited_amount` | `float` | Optional | Refers to an entry that shows that money has been received.Currency is in USD.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `debits_count` | `int` | Optional | Refers to count of debits.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `debited_amount` | `float` | Optional | Refers to an entry that shows that money has been deducted.Currency is in USD.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `net_amount` | `float` | Optional | Refers to the Amount left over after all deductions are made.<br><br>NetAmount= CreditedAmount - DebitedAmount.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `chain_code` | `str` | Optional | The Chain Code is the level of the merchant hierarchy that groups merchant identifiers (MIDs) and any related roll-up values under a common identifier for settlement, billing and reporting. Chain Code is the primary identifier for merchants boarded in MDB (Merchant Database) system.<br><br>**Constraints**: *Maximum Length*: `6` |

## Example (as JSON)

```json
{
  "creditsCount": 2,
  "creditedAmount": 33.5,
  "debitsCount": 3,
  "debitedAmount": 32.4,
  "netAmount": 1.11,
  "chainCode": "172111"
}
```

