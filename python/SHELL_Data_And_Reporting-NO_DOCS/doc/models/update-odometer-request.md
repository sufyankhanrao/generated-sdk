
# Update Odometer Request

## Structure

`UpdateOdometerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `col_co_id` | `int` | Optional | Collecting Company Id  of the selected payer.<br>Optional if ColCoCode is passed else Mandatory.<br>Example:<br>1 for Philippines<br>5 for UK |
| `col_co_code` | `int` | Optional | Collecting Company Code (Shell Code) of the selected payer.<br>Mandatory for serviced OUs such as Romania, Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other countries if ColCoID is provided. |
| `payer_id` | `int` | Optional | Payer Id (i.e. Customer Id of the Payment Customer in Cards Platform) of the selected payer.<br>Optional if PayerNumber is passed else Mandatory |
| `account_id` | `int` | Optional | Account Id (i.e. Customer Id of the Sub Account in GFN) of the selected account.<br>Optional if AccountNumber is passed else Mandatory |
| `account_number` | `str` | Optional | Account Number (ex: GB000000123) of the selected account.<br>Optional if AccountId is passed else Mandatory |
| `update_odometers` | [`List[UpdateOdometer]`](../../doc/models/update-odometer.md) | Optional | - |
| `notify_caller` | `bool` | Optional | True/False.<br>Optional.<br>Default: False<br>If true, the caller would be notified back with the status as success or failure after the update odometer is processed. |
| `caller` | `str` | Optional | The caller to be notified with the status of the update odometer.<br>Mandatory, if NotifyCaller is true. |

## Example (as JSON)

```json
{
  "ColCoId": 62,
  "ColCoCode": 76,
  "PayerId": 110,
  "AccountId": 170,
  "AccountNumber": "AccountNumber4"
}
```

