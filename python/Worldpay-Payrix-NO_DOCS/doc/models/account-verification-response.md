
# Account Verification Response

## Structure

`AccountVerificationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `account` | `str` | Optional | The identifier of the Account that you want to verify. |
| `mtype` | [`AccountVerificationTypeEnum`](../../doc/models/account-verification-type-enum.md) | Optional | The type of account verification you want to perform.<br><br><details><br><summary>Valid Values</summary><br>- `debit` - **Makes two challenge debits (debit1 and debit2).**<br>- `credentials` - **Uses a bank account credential (username/password).**<br></details><br> |
| `debit_1` | `int` | Optional | The first verification amount debited in cents. |
| `debit_2` | `int` | Optional | The second verification amount debited in cents. |
| `trials` | `int` | Optional | The number of verification challenge responses attempted. |
| `toaccount` | `str` | Optional | Account that will be deposited with both amounts: debit1 and debit2. |

## Example (as JSON)

```json
{
  "id": "id6",
  "created": "created6",
  "modified": "modified6",
  "creator": "String5",
  "modifier": "modifier0"
}
```

