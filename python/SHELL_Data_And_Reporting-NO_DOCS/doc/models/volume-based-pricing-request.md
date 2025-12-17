
# Volume Based Pricing Request

## Structure

`VolumeBasedPricingRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `col_co_id` | `int` | Optional | Collecting Company Id of the selected payer.<br>Optional if ColCoCode is passed else Mandatory.<br>Example:<br>1 for Philippines<br>5 for UK |
| `col_co_code` | `int` | Optional | Collecting Company Code of the selected payer.<br>Mandatory for serviced OUs such as Romania, Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other countries if ColCoID is provided.<br>Example:<br>86 for Philippines<br>5 for UK |
| `payer_id` | `int` | Optional | Payer Id of the selected payer.<br>Optional if PayerNumber is passed else Mandatory |
| `payer_number` | `str` | Optional | Payer Number of the selected payer.<br>Optional if PayerId is passed else Mandatory |
| `include_history` | `bool` | Optional | The API will return the details of the previously calculated/paid bonus and fuel consumption (Volume) in the response when this flag is ‘True’. |

## Example (as JSON)

```json
{
  "ColCoId": 96,
  "ColCoCode": 110,
  "PayerId": 144,
  "PayerNumber": "PayerNumber2",
  "IncludeHistory": false
}
```

