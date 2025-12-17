
# Update Card Renewal Address 2

## Structure

`UpdateCardRenewalAddress2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contact_name` | `str` | Required | Contact name<br>Note: Mandatory when ‘UseCustomerDefaultAddress’ is set to ‘false’. The field is ignored otherwise.<br><br>Max Length: 50 |
| `contact_title` | `str` | Optional | Title<br>Max Length: 50 |
| `company_name` | `str` | Required | Company name.<br>Note: Mandatory when ‘UseCustomerDefaultAddress’ is set to ‘false’. The field is ignored otherwise.<br>Max Length: 50 |
| `address_line` | `str` | Required | Address line 1,2 and 3<br>Note: Mandatory when ‘UseCustomerDefaultAddress’ is set to ‘false’. The field is ignored otherwise.<br>Max Length: 128<br>Note: -Each address line should be separated by “\r\n”. |
| `zip_code` | `str` | Required | ZipCode<br>Note: Mandatory when ‘UseCustomerDefaultAddress’ is set to ‘false’. The field is ignored otherwise.<br>Max Length: 10 |
| `city` | `str` | Optional | City<br>Note: Mandatory when ‘UseCustomerDefaultAddress’ is set to ‘false’. The field is ignored otherwise.<br>Max Length: 40 |
| `region_id` | `int` | Optional | Region id of card. |
| `country_id` | `int` | Required | Country ID<br>Note: Mandatory when ‘UseCustomerDefaultAddress’ is set to ‘false’. The field is ignored otherwise. |
| `email_address` | `str` | Optional | Email Address<br><br>Max Length: 90<br>Note: -<br>Based on the international standard that there can be<br>•	Max Length 64 before the @ (the 'Local part’) =64(minimum of 1)<br>•	Max Lenth after the (the domain) = 88 (Minimum of 2) |
| `phone_number` | `str` | Optional | Phone number<br>Optional<br>Max Length: 16 |

## Example (as JSON)

```json
{
  "ContactName": "Jack",
  "ContactTitle": "Mr",
  "CompanyName": "Travel Transport",
  "AddressLine": "Elm Street 11",
  "ZipCode": "1023EA",
  "City": "London",
  "RegionID": 2,
  "CountryID": 8,
  "EmailAddress": "testmail@gmail.com",
  "PhoneNumber": "+99999999999"
}
```

