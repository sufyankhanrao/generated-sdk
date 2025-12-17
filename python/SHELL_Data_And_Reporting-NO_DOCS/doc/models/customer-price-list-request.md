
# Customer Price List Request

## Structure

`CustomerPriceListRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `col_co_id` | `int` | Optional | - |
| `col_co_code` | `int` | Optional | - |
| `payer_id` | `int` | Optional | Payer Id of the selected payer.<br>Optional if PayerNumber is passed else Mandatory |
| `payer_number` | `str` | Optional | Payer Number of the selected payer.<br>Optional if PayerId is passed else Mandatory |
| `account_id` | `int` | Optional | Account Id of the customer.<br>Optional |
| `account_number` | `str` | Optional | Account Number of the customer.<br>Optional |
| `customer_specific_list` | `int` | Optional | Whether customer specific price lists and customer specific discount values set on pump prices are to be returned or not. |
| `price_list_type` | `int` | Optional | Specifies the type of price lists to be included in the response.<br>Optional – default value is zero.<br><br>Allowed values:<br>0 – All<br>1 – National Only<br>2 – International Only |
| `del_co_id` | `int` | Optional | Delivering Company ID<br>Optional. |
| `from_date` | `str` | Required | Start date to fetch the price lists, discount values on pump prices and VAT rates.<br>Mandatory<br>Format: yyyyMMdd |
| `to_date` | `str` | Required | End date to fetch the price lists, discount values on pump prices and VAT rates.<br>Mandatory and greater than or equal to FromDate.<br>Maximum of 30 (configurable) day’s duration is allowed between ‘From’ and ‘To’ dates.<br>Format: yyyyMMdd |
| `include_pump_price_discounts` | `bool` | Optional | True / False.<br>A flag to request the discount information set on pump prices for the customer to be included in the response.<br>Optional<br>Default value: False |

## Example (as JSON)

```json
{
  "ColCoId": 82,
  "ColCoCode": 96,
  "PayerId": 130,
  "PayerNumber": "PayerNumber6",
  "AccountId": 190,
  "FromDate": "FromDate2",
  "ToDate": "ToDate8"
}
```

