
# Summaryofbundler Request

## Structure

`SummaryofbundlerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `col_co_id` | `int` | Optional | Collecting Company Id of the selected payer.<br>Optional if ColCoCode is passed else Mandatory.<br>Example:<br>1 for Philippines<br>5 for UK |
| `col_co_code` | `int` | Optional | Collecting Company Code (Shell Code) of the selected payer.<br>Mandatory for serviced OUs such as Romania, Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other countries if ColCoID is provided.<br>Example:<br>86 for Philippines<br>5 for UK |
| `payer_id` | `int` | Optional | Payer Id  of the selected payer.<br>Optional if PayerNumber is passed else Mandatory<br>Example: 123456 |
| `payer_number` | `str` | Optional | Payer Number of the selected payer.<br>Optional if PayerId is passed else Mandatory<br>Example: GB000000123 |
| `account_id` | `int` | Optional | Account Id of the customer.<br>Optional if Account Number is passed else Mandatory<br>Example: 123456 |
| `account_number` | `str` | Optional | Account Number of the customer.<br>Optional if Account Id is passed else Mandatory<br>Example: GB000000123 |
| `bundle_id` | `List[str]` | Optional | List of Bundle Id associated with account<br>Optional.<br>When not present all the bundles in the given account will be returned in the response. |

## Example (as JSON)

```json
{
  "ColCoId": 148,
  "ColCoCode": 162,
  "PayerId": 196,
  "PayerNumber": "PayerNumber6",
  "AccountId": 0
}
```

