
# Delivery Addresses

## Structure

`DeliveryAddresses`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_id` | `int` | Optional | Address Id |
| `address_line_1` | `str` | Optional | AddressLine1 |
| `address_line_2` | `str` | Optional | AddressLine2 |
| `address_line_3` | `str` | Optional | AddressLine3 |
| `city` | `str` | Optional | City |
| `company_name` | `str` | Optional | Account Name |
| `contact_fore_name` | `str` | Optional | Contact fore name of the delivery address. |
| `contact_last_name` | `str` | Optional | Contact last name of the delivery address. |
| `contact_middle_name` | `str` | Optional | Contact middle name of the delivery address. |
| `contact_title` | `str` | Optional | ContactTitle |
| `country` | `str` | Optional | Country |
| `country_id` | `int` | Optional | Country Id |
| `country_iso_code` | `str` | Optional | Country ISO code |
| `fax` | `str` | Optional | Fax number of the address contact. |
| `region` | `str` | Optional | Region of the Card Delivery address |
| `region_id` | `int` | Optional | Region Id of the address. |
| `telephone` | `str` | Optional | Telephone number of the address contact |
| `zip_code` | `str` | Optional | Delivery Zip code |
| `address_type` | `int` | Optional | Delivery address type.<br>Possible Values:<br>1 – Card and PIN delivery address<br>2 – Card delivery address<br>3 – PIN delivery address |

## Example (as JSON)

```json
{
  "AddressId": 1,
  "AddressLine1": "AddressLine1",
  "AddressLine2": "AddressLine2",
  "AddressLine3": "AddressLine3",
  "City": "germany",
  "CompanyName": "5.11.3 DE",
  "ContactForeName": "5.11.13 DE",
  "ContactLastName": "SAM",
  "ContactMiddleName": "SAM",
  "ContactTitle": "Mr",
  "Country": "Germany",
  "CountryId": 9,
  "CountryISOCode": "DE",
  "Fax": "657875",
  "Region": "Germany",
  "RegionId": 133,
  "Telephone": "78787786868",
  "ZipCode": "E14 5HQ",
  "AddressType": 1
}
```

