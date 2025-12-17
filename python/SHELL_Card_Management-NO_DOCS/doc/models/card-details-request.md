
# Card Details Request

## Structure

`CardDetailsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `col_co_code` | `int` | Optional | Collecting Company Id  of the selected payer.<br>Optional if ColCoCode is passed else Mandatory.<br>Example:<br>1-Philippines<br>5-UK |
| `col_co_id` | `int` | Optional | Collecting Company Code (Shell Code) of the selected payer.<br>Mandatory for serviced OUs such as Romania, Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other countries if ColCoID is provided.<br>Example:<br>86-Philippines<br>5-UK |
| `col_co_country_code` | `str` | Optional | ISO Country code of collecting company |
| `client_reference_id` | `str` | Optional | Customer reference number of the card.<br>Optional |
| `payer_number` | `str` | Optional | Payer Number of the selected payer. |
| `payer_id` | `int` | Optional | Payer Id (i.e. Customer Id of the Payment of the selected payer. |
| `account_number` | `str` | Optional | Account Number of the customer.<br>Optional if AccountId is passed, else mandatory. |
| `account_id` | `int` | Optional | Account ID of the customer.<br>Optional if AccountNumber is passed, else mandatory. |
| `pan` | `str` | Optional | PAN of the card.<br>Optional if CardId is passed, else Mandatory. |
| `card_id` | `int` | Optional | Card Id of the card.<br>Optional if PAN is passed, else Mandatory. |
| `token_type_id` | `int` | Optional | Token Type ID for the Card<br>Optional |
| `token_type_name` | `str` | Optional | Token Type name for the Card<br>Optional |
| `creation_date` | `str` | Optional | Card Creation Date time<br>Optional<br>Format: yyyyMMdd |
| `effective_date` | `str` | Optional | Effective date for the Card<br>Optional<br>Format: yyyyMMdd |
| `include_bundle_details` | `bool` | Optional | When the value is True, API will return bundle Id associated with card in the response, if available.<br>Note: Use ‘Null’ or ‘False’ for optimum performance. A delay in response is expected when set to ‘True’. |
| `include_intermediate_status` | `bool` | Optional | A flag which indicates if the response can contain intermediate statuses |
| `include_scheduled_card_blocks` | `bool` | Optional | A flag which indicates if the response can contain scheduled card blocks details |

## Example (as JSON)

```json
{
  "ColCoCode": 154,
  "ColCoId": 140,
  "ColCoCountryCode": "ColCoCountryCode6",
  "ClientReferenceId": "ClientReferenceId2",
  "PayerNumber": "PayerNumber8"
}
```

