
# Card Details Response PIN Delivery Address

Delivery address.

## Structure

`CardDetailsResponsePINDeliveryAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contact_fore_name` | `str` | Optional | Fore name of the contact person |
| `contact_middle_name` | `str` | Optional | Middle name of the contact person |
| `contact_last_name` | `str` | Optional | Last name of the contact person |
| `contact_title` | `str` | Optional | Title of the contact person Optional Max field length- 10 Note- If the Shell Card Platform configuration is set to clear the personal details captured on card orders, this value will be cleared from the record after processing the request.<br><br>**Constraints**: *Maximum Length*: `10` |
| `company_name` | `str` | Required | Company name Mandatory if IsNewDeliveryAddress and OrderReplacement are passed. True, Note- If the Shell Card Platform configuration is set to clear the personal details captured on card orders, this value will be cleared from the record after processing the request. |
| `address_id` | `int` | Required | Address Id in cards platform. |
| `address_line_1` | `str` | Required | Address line 1 Mandatory if IsNewDeliveryAddress and OrderReplacement are passed True. Max field length- 40 Note- If the Shell Card Platform configuration is set to clear the personal details captured on card orders, this value will be cleared from the record after processing the request.<br><br>**Constraints**: *Minimum Length*: `1` |
| `address_line_2` | `str` | Optional | Address line 2 Optional Max field length- 40 Note- If the Shell Card Platform configuration is set to clear the personal details captured on card orders, this value will be cleared from the record after processing the request. |
| `address_line_3` | `str` | Optional | Address line Optional Max field length- 40 Note- If the Shell Card Platform configuration is set to clear the personal details captured on card orders, this value will be cleared from the record after processing the request. |
| `zip_code` | `str` | Required | ZIP code Mandatory if IsNewDeliveryAddress and OrderReplacement are passed. True, Max field length- 10 Note- If the Shell Card Platform configuration is set to clear the personal details captured on card orders, this value will be cleared from the record after processing the request.<br><br>**Constraints**: *Maximum Length*: `10` |
| `city` | `str` | Optional | City Max field length- 40 Note- If the Shell Card Platform configuration is set to clear the personal details captured on card orders, this value will be cleared from the record after processing the request.<br><br>**Constraints**: *Maximum Length*: `40` |
| `region_id` | `int` | Optional | Region Id |
| `region` | `str` | Optional | Region Optional When region is passed, Shell Card Platform will look up for the region id for the given region.  If the option to clear personal details is set in the Shell Card Platform, then this value will be cleared from the record after processing the request . |
| `country_id` | `int` | Required | Country Id in cards platform. |
| `country_iso_code` | `str` | Required | The ISO code of the country. Mandatory if IsNewDeliveryAddress and OrderReplacement are passed. If the option to clear personal details is set in the Shell Card Platform, then this value will be cleared from the record after processing the request . |
| `country` | `str` | Required | Country name. |

## Example (as JSON)

```json
{
  "ContactForeName": "ROBERT",
  "ContactMiddleName": "M",
  "ContactLastName": "Langdon",
  "ContactTitle": "Mr.",
  "CompanyName": "PARKLEY Philippines",
  "AddressId": 1768,
  "AddressLine1": "No 345, 1st cross,",
  "AddressLine2": "10th avenue",
  "AddressLine3": "makati city",
  "ZipCode": "1630",
  "City": "manila",
  "Region": "EU",
  "CountryId": 1,
  "CountryISOCode": "PH",
  "Country": "Philippines"
}
```

