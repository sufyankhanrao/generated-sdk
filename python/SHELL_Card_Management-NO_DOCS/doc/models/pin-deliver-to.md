
# PIN Deliver To

## Structure

`PINDeliverTo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contact_name` | `str` | Optional | Contact Name<br>Max Length: 50 |
| `contact_title` | `str` | Optional | Contact Title<br>Max Length: 50 |
| `company_name` | `str` | Required | Company Name for PIN delivery.<br>Max Length: 50 |
| `address_line` | `str` | Required | Address Lines<br>Max Length: 1024 |
| `zip_code` | `str` | Required | Zip Code<br>Max Length: 10 |
| `city` | `str` | Required | City<br>Max Length: 40 |
| `region_id` | `int` | Optional | Region |
| `country_id` | `int` | Optional | Country |
| `phone_number` | `str` | Optional | Cardholder phone number for PIN delivery. |
| `email_address` | `str` | Optional | Cardholder email address for PIN delivery<br>Max Length : 90<br>Example: xxxxxx@example.com <br/>Note:Based on the international standard that there can be Max Length 64 before the @ (the 'Local part’) =64(minimum of 1) Max Lenth after the (the domain) = 88 (Minimum of 2) |
| `save_pin_reminder` | `bool` | Optional | Save PIN Reminder<br>If SavePINReminder is true, the contact address will be saved database for PIN reminder.<br><br><br/>Only allowed for PIN Advice paper delivery. |

## Example (as JSON)

```json
{
  "ContactName": "ContactName0",
  "ContactTitle": "ContactTitle6",
  "CompanyName": "CompanyName2",
  "AddressLine": "AddressLine6",
  "ZipCode": "ZipCode4",
  "City": "City0",
  "RegionID": 6,
  "CountryID": 136,
  "PhoneNumber": "PhoneNumber4"
}
```

