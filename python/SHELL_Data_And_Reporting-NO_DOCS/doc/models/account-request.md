
# Account Request

## Structure

`AccountRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Optional | Account Status.<br>Optional if StatusList is passed, else mandatory.<br>Ignored if StatusList is passed.<br>Allowed values:<br>•	ALL<br>•	ACTIVE<br>•	BLOCKED<br>•	CANCELLED<br>•	CREDITLOCK<br>•	DELINQUENCYLOCK |
| `include_card_summary` | `bool` | Optional | Include card summary details in the response.<br><br>When passed as false, the card summary related parameters on response will be set to null.<br><br>Optional – default value: true.<br><br>**Default**: `True` |
| `payer_id` | `int` | Optional | Payer id of the customer.<br>Optional if PayerNumber is passed, else Mandatory. |
| `payer_number` | `str` | Optional | PayerNumber of the customer.<br>Optional if PayerId is passed, else Mandatory. |
| `page_size` | `int` | Optional | Page Size – Number of records to show on a page.<br>Optional<br>Default value 50 |
| `request_id` | `str` | Optional | API Request Id |
| `col_co_code` | `int` | Optional | Collecting Company Code (Shell Code) of the selected payer.<br>ColCoCode or ColCoCountryCode  is Mandatory for serviced OUs such as Romania, Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other countries if ColCoID is provided. |
| `col_co_country_code` | `str` | Optional | The 2-character ISO Code for the customer and card owning country.<br>ColCoCode or ColCoCountryCode  is Mandatory for serviced OUs such as Romania, Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other countries if ColCoID is provided. |
| `current_page` | `int` | Optional | Page Number (as shown to the users)<br>Optional<br>Default value 1 |
| `invoice_points_only` | `bool` | Optional | Optional – default value: false.<br>When passed as true, the API will return accounts that are configured as Invoice Point only.<br><br>**Default**: `False` |
| `col_co_id` | `int` | Optional | Collecting Company Id (in GFN) of the selected payer.<br>Optional if ColCoCode or ColCoCountryCode  is passed else Mandatory. |
| `return_tolls_customer_id` | `bool` | Optional | Return e-Toll Customer details When True. |
| `accounts` | [`List[Accounts]`](../../doc/models/accounts.md) | Optional | - |
| `account_name` | `str` | Optional | Account Name of the customer.<br>Optional.<br>Minimum of 4 characters should be provided else not considered.<br>Accounts those have the entered value at any part of the Name will be returned. |
| `status_list` | `List[str]` | Optional | Account Statuses.<br>Optional<br>Multiple statuses are allowed to be included in the search criteria.<br>Allowed values:<br>•	ACTIVE<br>•	BLOCKED<br>•	CANCELLED<br>•	CREDITLOCK<br>•	DELINQUENCYLOCK |

## Example (as JSON)

```json
{
  "Status": "ALL",
  "IncludeCardSummary": true,
  "PayerId": 9,
  "PayerNumber": "GB00000111",
  "PageSize": 10,
  "RequestId": "b9eb91b6-65d4-4196-f910-6b0846875e70",
  "ColCoCode": 14,
  "ColCoCountryCode": "14",
  "CurrentPage": 1,
  "InvoicePointsOnly": false,
  "ColCoId": 14,
  "AccountName": "test"
}
```

