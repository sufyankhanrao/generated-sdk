
# Budle Details Request

## Structure

`BudleDetailsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `col_co_id` | `int` | Optional | Collecting Company Id  of the selected payer.<br>Optional if ColCoCode is passed else Mandatory.<br>Example:<br>1 for Philippines<br>5 for UK |
| `col_co_code` | `int` | Optional | Collecting Company Code (Shell Code) of the selected payer.<br>Mandatory for serviced OUs such as Romania, Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other countries if ColCoID is provided.<br>Example:<br>86 for Philippines<br>5 for UK |
| `payer_id` | `str` | Optional | Payer Id of the selected payer.<br>Optional if PayerNumber is passed else Mandatory<br>Example: 123456 |
| `payer_number` | `str` | Optional | Payer Number of the selected payer.<br>Optional if PayerId is passed else Mandatory<br>Example: GB000000123 |
| `account_id` | `int` | Optional | Account Id of the customer.<br>Optional if Account Number is passed else Mandatory<br>Example: 123456 |
| `account_number` | `str` | Optional | Account Number of the customer.<br>Optional if Account Id is passed else Mandatory<br>Example: GB000000123 |
| `bundle_id` | `str` | Optional | Bundle Id associated with account<br>Mandatory.<br>Example: 835662721 |

## Example (as JSON)

```json
{
  "ColCoId": 28,
  "ColCoCode": 42,
  "PayerId": "PayerId6",
  "PayerNumber": "PayerNumber8",
  "AccountId": 136
}
```

