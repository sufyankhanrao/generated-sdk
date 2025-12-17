
# Summary Date

## Structure

`SummaryDate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `credits_count` | `int` | Optional | Refers to count of credits.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `credited_amount` | `float` | Optional | Refers to an entry that shows that money has been received.Currency is in USD.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `debits_count` | `int` | Optional | Refers to count of debits.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `debited_amount` | `float` | Optional | Refers to an entry that shows that money has been deducted.Currency is in USD.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `net_amount` | `float` | Optional | Refers to the Amount left over after all deductions are made.<br><br>NetAmount= CreditedAmount - DebitedAmount.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `date` | `str` | Optional | Date when transaction was deposited.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |

## Example (as JSON)

```json
{
  "creditsCount": 2,
  "creditedAmount": 33.5,
  "debitsCount": 3,
  "debitedAmount": 32.4,
  "netAmount": 1.11,
  "date": "2019-08-06"
}
```

