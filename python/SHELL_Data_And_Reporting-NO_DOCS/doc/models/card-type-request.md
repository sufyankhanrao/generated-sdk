
# Card Type Request

## Structure

`CardTypeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `col_co_id` | `int` | Optional | Collecting Company Id of the selected payer.<br>Optional if ColCoCode is passed else Mandatory. |
| `col_co_code` | `int` | Optional | Collecting Company Code (Shell Code) of the selected payer.<br>Mandatory for serviced OUs such as Romania, Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other countries if ColCoID is provided. |
| `payer_id` | `int` | Optional | Payer Id of the selected payer. |
| `payer_number` | `str` | Optional | Payer Number of the selected payer. |
| `account_id` | `int` | Optional | Account Id of the customer.<br>Optional if AccountNumber is passed else Mandatory. |
| `account_number` | `str` | Optional | Account Number of the customer.<br>Optional if AccountId is passed else Mandatory<br>Example: GB000000124 |
| `include_usage_restrictions` | `bool` | Optional | Include usage restrictions in the response.<br>Optional field– default value is False.<br>Possible values: True/False |
| `include_purchase_categories` | `bool` | Optional | Include purchase categories in the response.<br>Optional field– default value is False.<br>Possible values: True/False |

## Example (as JSON)

```json
{
  "ColCoId": 14,
  "ColCoCode": 14,
  "PayerId": 2343,
  "PayerNumber": "GB000000124",
  "AccountId": 343,
  "AccountNumber": "GB000000124"
}
```

