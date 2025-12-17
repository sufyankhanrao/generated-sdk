
# Bank Account

## Structure

`BankAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dda_type` | [`DdaTypeEnum`](../../doc/models/dda-type-enum.md) | Optional | Direct deposit account type.<br><br>**Constraints**: *Maximum Length*: `8` |
| `ach_type` | [`AchTypeEnum`](../../doc/models/ach-type-enum.md) | Optional | Check deposit type<br><br>**Constraints**: *Maximum Length*: `19` |
| `account_number` | `str` | Optional | Direct deposit account number.  Maximum 17 characters.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `17` |
| `routing_number` | `str` | Optional | Bank routing number. Must be 9 characters and pass ACH Mod-10 validation.<br><br>**Constraints**: *Minimum Length*: `9`, *Maximum Length*: `9` |
| `bank_name` | `str` | Optional | Bank name used for credit card processing services.<br><br>**Constraints**: *Maximum Length*: `36` |

## Example (as JSON)

```json
{
  "ddaType": "CHECKING",
  "accountNumber": "*****1545",
  "routingNumber": "102000076",
  "bankName": "Bank name",
  "achType": "COMMERCIAL CHECKING"
}
```

