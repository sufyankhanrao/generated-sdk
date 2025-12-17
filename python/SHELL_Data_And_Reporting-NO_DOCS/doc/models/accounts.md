
# Accounts

## Structure

`Accounts`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `int` | Optional | Account Id of the customer.<br>Optional, if AccountNumber is passed, else mandatory. |
| `account_number` | `str` | Optional | Account Number of the customer.<br>Optional, if AccountId is passed, else mandatory. |

## Example (as JSON)

```json
{
  "AccountId": 3453,
  "AccountNumber": "GB000000124"
}
```

