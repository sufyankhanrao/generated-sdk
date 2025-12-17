
# Address

## Structure

`Address`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_id` | `int` | Optional | Address Id in cards platform. |
| `address_line_1` | `str` | Optional | Address line1 |
| `address_line_2` | `str` | Optional | Address line2 |
| `address_line_3` | `str` | Optional | AddressLine3 |
| `zip_code` | `str` | Optional | ZipCode |
| `city` | `str` | Optional | City |
| `region_id` | `int` | Optional | Region Id of the address. |
| `country_iso_code` | `str` | Optional | Country ISO code of the address |
| `country` | `str` | Optional | Country for the address |
| `telephone` | `str` | Optional | Telephone number of the address contact |
| `email_address` | `str` | Optional | Email address of the address contact |
| `fax` | `str` | Optional | Fax number of the address contact |

## Example (as JSON)

```json
{
  "AddressId": 1,
  "AddressLine1": "test street",
  "AddressLine2": "Address line2",
  "AddressLine3": "AddressLine3",
  "ZipCode": "667 78",
  "City": "LUMPUR",
  "RegionId": 1234,
  "CountryISOCode": "CZ",
  "Country": "Germany",
  "Telephone": "3245872364823",
  "EmailAddress": "testmail@gmail.com",
  "Fax": "3245872364823"
}
```

