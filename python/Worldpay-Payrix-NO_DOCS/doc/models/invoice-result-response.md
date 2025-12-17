
# Invoice Result Response

## Structure

`InvoiceResultResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `invoice` | `str` | Optional | The identifier of the Invoice that owns this invoiceResults resource. |
| `txn` | `str` | Optional | The identifier of the Transaction associated with this invoiceResults resource. |
| `status` | [`InvoiceResultStatusEnum`](../../doc/models/invoice-result-status-enum.md) | Optional | The status of this invoiceResult<br><br><details><br><summary>Valid Values</summary><br>- `success` - **Successfuly processed.**<br>- `failure` - **Failed to process.**<br><br></details><br> |
| `message` | `str` | Optional | A message that accompanies and describes this invoice result. This field is specified as a text string and must be between 1 and 500 characters long. |
| `shipping_first` | `str` | Optional | The shipping first name associated with this InvoiceResult. This field is stored as a text string and must be between 0 and 100 characters long. |
| `shipping_middle` | `str` | Optional | The shipping middle name associated with this InvoiceResult. This field is stored as a text string and must be between 0 and 100 characters long. |
| `shipping_last` | `str` | Optional | The shipping last name associated with this InvoiceResult. This field is stored as a text string and must be between 0 and 100 characters long. |
| `shipping_company` | `str` | Optional | The shipping name of the company associated with this InvoiceResult. This field is stored as a text string and must be between 0 and 100 characters long. |
| `shipping_address_1` | `str` | Optional | The shipping first line of the address associated with this InvoiceResult. This field is stored as a text string and must be between 0 and 500 characters long. |
| `shipping_address_2` | `str` | Optional | The shipping second line of the address associated with this InvoiceResult. This field is stored as a text string and must be between 0 and 500 characters long. |
| `shipping_city` | `str` | Optional | The shipping name of the city in the address associated with this InvoiceResult. This field is stored as a text string and must be between 0 and 500 characters long. |
| `shipping_state` | `str` | Optional | The U.S. state or Canadian province relevant to the address provided here. If the location is within the U.S. and Canada, specify the 2-character postal abbreviation for the state. If the location is outside of the U.S. and Canada, provide the full state name. This field is stored as a text string and must be between 2 and 100 characters long.<br><br><details><br><summary>U.S. States</summary><br> <br> - `AK` - **Alaska (US)**<br> <br> - `AR` - **Arkansas (US)**<br> <br> - `AL` - **Alabama (US)**<br> <br> - `AZ` - **Arizona (US)**<br> <br> - `CA` - **California (US)**<br> <br> - `CO` - **Colorado (US)**<br> <br> - `CT` - **Connecticut (US)**<br> <br> - `DE` - **Delaware (US)**<br> <br> - `FL` - **Florida (US)**<br> <br> - `GA` - **Georgia (US)**<br> <br> - `HI` - **Hawaii (US)**<br> <br> - `IA` - **Iowa (US)**<br> <br> - `ID` - **Idaho (US)**<br> <br> - `IL` - **Illinois (US)**<br> <br> - `IN` - **Indiana (US)**<br> <br> - `KY` - **Kentucky (US)**<br> <br> - `KS` - **Kansas (US)**<br> <br> - `LA` - **Louisiana (US)**<br> <br> - `MA` - **Massachusetts (US)**<br> <br> - `MD` - **Maryland (US)**<br> <br> - `ME` - **Maine (US)**<br> <br> - `MI` - **Michigan (US)**<br> <br> - `MN` - **Minnesota (US)**<br> <br> - `MO` - **Missouri (US)**<br> <br> - `MS` - **Mississippi (US)**<br> <br> - `MT` - **Montana (US)**<br> <br> - `NC` - **North Carolina (US)**<br> <br> - `ND` - **North Dakota (US)**<br> <br> - `NE` - **Nebraska (US)**<br> <br> - `NH` - **New Hampshire (US)**<br> <br> - `NJ` - **New Jersey (US)**<br> <br> - `NM` - **New Mexico (US)**<br> <br> - `NV` - **Nevada (US)**<br> <br> - `NY` - **New York (US)**<br> <br> - `OH` - **Ohio (US)**<br> <br> - `OK`- **Oklahoma (US)**<br> <br> - `OR` - **Oregon (US)**<br> <br> - `PA` - **Pennsylvania (US)**<br> <br> - `RI` - **Rhode Island (US)**<br> <br> - `SC`- **South Carolina (US)**<br> <br> - `SD` - **South Dakota (US)**<br> <br> - `TN` - **Tennessee (US)**<br> <br> - `TX` - **Texas (US)**<br> <br> - `UT` - **Utah (US)**<br> <br> - `VA` - **Virginia (US)**<br> <br> - `VT` - **Vermont (US)**<br> <br> - `WA` - **Washington (US)**<br> <br> - `WI` - **Wisconsin (US)**<br> <br> - `WV` - **West Virginia (US)**<br> <br> - `WY` - **Wyoming (US)**<br> </details><br> <details><br><summary>Canada Provinces and Territories</summary><br> <br> - `AB` - **Alberta (CAN)**<br> <br> - `BC` - **British Columbia (CAN)**<br> <br> - `MB` - **Manitoba (CAN)**<br> <br> - `ON` - **Ontario (CAN)**<br> <br> - `NS` - **Nova Scotia (CAN)**<br> <br> - `NB` - **New Brunswick (CAN)**<br> <br> - `NL` - **Newfoundland and Labrador (CAN)**<br> <br> - `NT` - **Northwest Territories (CAN)**<br> <br> - `NU` - **Nunavut (CAN)**<br> <br> - `PE` - **Prince Edward Island (CAN)**<br> <br> - `QC` - **Quebec (CAN)**<br> <br> - `SK` - **Saskatchewan (CAN)**<br> <br> - `YT` - **Yukon (CAN)**<br> </details><br> |
| `shipping_zip` | `str` | Optional | The shipping zip code in the address associated with this InvoiceResult. This field is stored as a text string and must be between 1 and 20 characters long. |
| `shipping_country` | [`ShippingCountryEnum`](../../doc/models/shipping-country-enum.md) | Optional | The shipping country associated with this InvoiceResult, valid values being the 3-letter ISO code for the country. |
| `shipping_phone` | `str` | Optional | The shipping phone number associated with this InvoiceResult. This field is stored as a text string and must be between 5 and 15 characters long. |
| `shipping_fax` | `str` | Optional | The shipping fax number associated with this InvoiceResult, stored as a text string and must be between 5 and 15 characters long. |
| `authorization` | `str` | Optional | The authorization text the customer agreed to when making this payment. |
| `authorization_data` | `str` | Optional | Replacement data for replaceable strings in the authorization text. |
| `signature` | `str` | Optional | The signature on file for the customer’s authorization acceptance. |

## Example (as JSON)

```json
{
  "id": "id6",
  "created": "created6",
  "modified": "modified4",
  "creator": "String5",
  "modifier": "modifier0"
}
```

