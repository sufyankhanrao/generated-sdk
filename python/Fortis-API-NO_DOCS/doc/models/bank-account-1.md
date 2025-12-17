
# Bank Account 1

Array of bank account objects.

## Structure

`BankAccount1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_name` | `str` | Required | Account holder name.<br><br>**Constraints**: *Maximum Length*: `40` |
| `routing_number` | `str` | Required | Nine-digit Bank routing number.<br><br>**Constraints**: *Maximum Length*: `9` |
| `account_number` | `str` | Required | Account number.<br><br>**Constraints**: *Maximum Length*: `17` |
| `is_primary` | `bool` | Optional | Flag indicating whether or not the account is the primary account. Only one account can be marked as primary. |
| `account_type` | [`AccountType6Enum`](../../doc/models/account-type-6-enum.md) | Required | Account type. Either "checking" or "savings"<br><br>**Constraints**: *Maximum Length*: `10` |
| `alt_deposit_types` | `List[str]` | Optional | Array of deposit types. ('fees', 'adjustments', 'returns') |

## Example (as JSON)

```json
{
  "account_holder_name": "James Bond",
  "routing_number": "111111111",
  "account_number": "1234567",
  "is_primary": true,
  "account_type": "checking",
  "alt_deposit_types": [
    "alt_deposit_types0",
    "alt_deposit_types9"
  ]
}
```

