
# Accounts Put Request Schema Properties

An object representing details of the Account, including the type of Account (method), Account number, and routing code.

## Structure

`AccountsPutRequestSchemaProperties`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `method` | [`AccountMethodEnum`](../../doc/models/account-method-enum.md) | Optional | The type of the Account.<br><br><details><br><summary>Valid Values</summary><br>- `8` - **Checking**<br>- `9` - **Savings**<br>- `10` - **Corporate Checking**<br>- `11` - **Corporate Savings**<br></details><br> |
| `number` | `str` | Optional | The number of the bank account. |
| `routing` | `str` | Optional | The routing number of the bank account. This field is stored as a text string and must be between 5 and 20 characters long. |

## Example (as JSON)

```json
{
  "method": 10,
  "number": "number4",
  "routing": "routing2"
}
```

