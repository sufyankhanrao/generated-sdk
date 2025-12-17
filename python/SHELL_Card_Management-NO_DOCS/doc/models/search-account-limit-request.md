
# Search Account Limit Request

## Structure

`SearchAccountLimitRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `col_co_id` | `int` | Optional | Collecting Company Id of the selected payer.<br>Optional if ColCoCode is passed else Mandatory.<br>Example: |
| `col_co_code` | `int` | Optional | Collecting Company Code (Shell Code) of the selected payer.<br>Mandatory for serviced OUs such as Romania, Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other countries if ColCoID is provided.<br>Example:<br>86 for Philippines<br>5 for UK |
| `payer_id` | `int` | Optional | Payer Id of the selected payer.<br>Optional if PayerNumber is passed else Mandatory<br>Example: 123456 |
| `payer_number` | `str` | Optional | Payer Number of the selected payer.<br>Optional if PayerId is passed else Mandatory<br>Example: GB000000123 |
| `account_id` | `int` | Optional | Account ID of the customer.<br>Optional if AccountNumber is passed else Mandatory<br>Example: 123456 |
| `account_number` | `str` | Optional | Account Number of the customer.<br>Optional if AccountId is passed else Mandatory<br>Example: GB000000123 |

## Example (as JSON)

```json
{
  "ColCoId": 30,
  "ColCoCode": 44,
  "PayerId": 78,
  "PayerNumber": "PayerNumber0",
  "AccountId": 138
}
```

