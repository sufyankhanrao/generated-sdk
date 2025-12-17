
# Customer Detail Request

## Structure

`CustomerDetailRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `col_co_id` | `int` | Optional | Collecting Company Id (in GFN) of the selected payer.<br>Optional if ColCoCode is passed else Mandatory.<br>Example:<br>1-Philippines<br>5-UK |
| `col_co_code` | `int` | Optional | Collecting Company Code (Shell Code) of the selected payer.<br>Mandatory for serviced OUs such as Romania, Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other countries if ColCoID is provided.<br>Example:<br>86-Philippines<br>5-UK |
| `payer_id` | `int` | Optional | Payer Id (i.e., Customer Id of the Payment Customer in H3 Cards Platform) of the selected payer.<br>Optional if PayerNumber is passed else Mandatory<br>Example: 123456 |
| `payer_number` | `str` | Optional | Payer Number of the selected payer.<br>Optional if PayerId is passed else Mandatory<br>Example: GB000000123 |
| `account_id` | `int` | Optional | Account ID of the customer.<br>Optional if AccountNumber is passed else Mandatory. |
| `account_number` | `str` | Optional | Account Number of the customer.<br>Optional if AccountId is passed else Mandatory. |

## Example (as JSON)

```json
{
  "ColCoId": 14,
  "ColCoCode": 14,
  "PayerId": 12345,
  "PayerNumber": "GB000000123",
  "AccountNumber": "GB000000124",
  "AccountId": 100
}
```

