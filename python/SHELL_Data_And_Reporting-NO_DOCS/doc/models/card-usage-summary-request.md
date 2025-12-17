
# Card Usage Summary Request

## Structure

`CardUsageSummaryRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `col_co_id` | `int` | Optional | Collecting Company Id of the selected payer.<br>Optional if ColCoCode is passed else Mandatory.<br>Example:<br>1 for Philippines<br>5 for UK |
| `col_co_code` | `int` | Optional | Collecting Company Code  of the selected payer.<br>Mandatory for serviced OUs such as Romania, Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other countries if ColCoID is provided.<br>Example:<br>86 for Philippines<br>5 for UK |
| `payer_id` | `int` | Optional | Payer Id of the selected payer.<br>Optional if PayerNumber is passed else Mandatory |
| `payer_number` | `str` | Optional | Payer Number of the selected payer.<br>Optional if PayerId is passed else Mandatory |
| `account_id` | `int` | Optional | Account ID of the customer.<br>Optional if account number is passed else mandatory. |
| `account_number` | `str` | Optional | Account Number of the customer.<br>Optional if Account ID is passed else mandatory. |
| `card_id` | `int` | Optional | Card Id of the card.<br>Optional if PAN is passed, else Mandatory. |
| `pan` | `str` | Optional | PAN of the card.<br>Optional if CardId is passed, else Mandatory. |
| `card_expiry_date` | `str` | Optional | Expiry date of the card.<br>Mandatory if Card ID is not provided, else optional.<br>Format: yyyyMMdd<br>Example: 20170930 |

## Example (as JSON)

```json
{
  "ColCoId": 100,
  "ColCoCode": 114,
  "PayerId": 148,
  "PayerNumber": "PayerNumber8",
  "AccountId": 208
}
```

