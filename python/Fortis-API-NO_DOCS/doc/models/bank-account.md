
# Bank Account

The Bank Account.

## Structure

`BankAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `routing_number` | `str` | Optional | Nine-digit Bank routing number.<br><br>**Constraints**: *Maximum Length*: `9` |
| `account_number` | `str` | Optional | Bank account number.<br><br>**Constraints**: *Maximum Length*: `17` |
| `account_holder_name` | `str` | Optional | Name on bank account.<br><br>**Constraints**: *Maximum Length*: `40` |

## Example (as JSON)

```json
{
  "routing_number": "011103093",
  "account_number": "01234567890123",
  "account_holder_name": "Bob Fairview"
}
```

