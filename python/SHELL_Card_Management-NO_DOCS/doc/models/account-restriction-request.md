
# Account Restriction Request

## Structure

`AccountRestrictionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `col_co_id` | `int` | Optional | Collecting Company Id of the selected payer.<br>Optional if ColCoCode is passed else Mandatory.<br>Example:<br>1 for Philippines<br>5 for UK |
| `col_co_code` | `int` | Optional | Collecting Company Code (Shell Code) of the selected payer.<br>Mandatory for serviced OUs such as Romania, Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other countries if ColCoID is provided.<br>Example:<br>86 for Philippines<br>5 for UK |
| `payer_id` | `int` | Optional | Payer Id of the selected payer.<br>Optional if PayerNumber is passed else Mandatory<br>Example: 123456 |
| `payer_number` | `str` | Optional | Payer Number of the selected payer.<br>Optional if PayerId is passed else Mandatory<br>Example: GB000000123 |
| `account_id` | `int` | Optional | Account ID of the customer on which the restrictions will be applied.<br>Optional if AccountNumber is passed, else Mandatory.<br>Example: 123456 |
| `account_number` | `str` | Optional | Account Number of the customer on which the restrictions will be applied.<br>Optional if AccountId is passed, else Mandatory.<br>Example: GB000000123 |
| `reset_usage_restrictions` | `bool` | Optional | True/False.<br>If true, the usage restrictions applied on the account will be removed.<br>Optional<br>Default: False |
| `usage_restrictions` | [`UsageRestrictionsCard`](../../doc/models/usage-restrictions-card.md) | Optional | - |

## Example (as JSON)

```json
{
  "ColCoId": 138,
  "ColCoCode": 152,
  "PayerId": 186,
  "PayerNumber": "PayerNumber8",
  "AccountId": 246
}
```

