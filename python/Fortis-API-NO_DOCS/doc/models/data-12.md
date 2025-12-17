
# Data 12

## Structure

`Data12`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `parent_id` | `str` | Optional | Location ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `primary_principal` | [`PrimaryPrincipal`](../../doc/models/primary-principal.md) | Optional | The Primary Principal. |
| `template_code` | `str` | Optional | The ID of the template to be used - this value will be provided by Fortis.<br><br>**Constraints**: *Maximum Length*: `20`, *Pattern*: `^[a-zA-Z0-9]*$` |
| `email` | `str` | Optional | Merchant email address.<br><br>**Constraints**: *Maximum Length*: `100` |
| `dba_name` | `str` | Optional | Merchant 'Doing Business As' name.<br><br>**Constraints**: *Maximum Length*: `100` |
| `location` | [`Location5`](../../doc/models/location-5.md) | Optional | The Location. |
| `app_delivery` | `str` | Optional | The delivery method of the app to the merchant.<br><br>**Constraints**: *Maximum Length*: `20` |
| `business_category` | [`BusinessCategoryEnum`](../../doc/models/business-category-enum.md) | Optional | The Category of the merchant's business |
| `business_type` | [`BusinessTypeEnum`](../../doc/models/business-type-enum.md) | Optional | The Type of a merchant's business. |
| `business_description` | `str` | Optional | Description of Goods or Services.<br><br>**Constraints**: *Maximum Length*: `200` |
| `swiped_percent` | `int` | Optional | Card present/swiped percentage<br><br>**Constraints**: `>= 0`, `<= 100` |
| `keyed_percent` | `int` | Optional | Card not present/keyed percentage<br><br>**Constraints**: `>= 0`, `<= 100` |
| `ecommerce_percent` | `int` | Optional | eCommerce percentage.<br><br>**Constraints**: `>= 0`, `<= 100` |
| `ownership_type` | [`OwnershipTypeEnum`](../../doc/models/ownership-type-enum.md) | Optional | The Ownership Type of the merchant's business.<br><br>**Constraints**: *Maximum Length*: `10` |
| `fed_tax_id` | `str` | Optional | Federal Tax ID (EIN).<br><br>**Constraints**: *Maximum Length*: `10` |
| `cc_average_ticket_range` | `int` | Optional | Average Transaction Amount Range<br><br>**Constraints**: `>= 1`, `<= 7` |
| `cc_monthly_volume_range` | `int` | Optional | Monthly Processing Volume Range<br><br>**Constraints**: `>= 1`, `<= 7` |
| `cc_high_ticket` | `int` | Optional | Highest transaction amount rounded to the next dollar<br><br>**Constraints**: `>= 0`, `<= 30000` |
| `ec_average_ticket_range` | `int` | Optional | Average Transaction Amount Range<br><br>**Constraints**: `>= 1`, `<= 7` |
| `ec_monthly_volume_range` | `int` | Optional | Monthly Processing Volume Range<br><br>**Constraints**: `>= 1`, `<= 7` |
| `ec_high_ticket` | `int` | Optional | Highest transaction amount rounded to the next dollar<br><br>**Constraints**: `>= 0`, `<= 30000` |
| `website` | `str` | Optional | Merchant's business website.<br><br>**Constraints**: *Maximum Length*: `100` |
| `bank_account` | [`BankAccount`](../../doc/models/bank-account.md) | Optional | The Bank Account. |
| `alt_bank_account` | [`AltBankAccount`](../../doc/models/alt-bank-account.md) | Optional | The Alternative Bank Account. |
| `legal_name` | `str` | Optional | Merchant legal name.<br><br>**Constraints**: *Maximum Length*: `100` |
| `contact` | [`Contact`](../../doc/models/contact.md) | Optional | The Contact. |
| `client_app_id` | `str` | Optional | Client Issues Id to track that can be used to track each submitted merchant application. This id should be generated and sent in the request payload, and will be returned in the response payload. If no id is submitted in the payload request, this field will be null in the response.<br><br>**Constraints**: *Maximum Length*: `20` |
| `app_link` | `str` | Optional | A full page or iframeable link, set in the request app_delivery field, that can be used to retrieve and resume the generated merchant application. No link will be returned if app_delivery is direct<br><br>**Constraints**: *Maximum Length*: `400` |

## Example (as JSON)

```json
{
  "parent_id": "11e95f8ec39de8fbdb0a4f1a",
  "template_code": "1234YourTemplateCode",
  "email": "jtodd@example.com",
  "dba_name": "Discount Home Goods",
  "app_delivery": "link_full_page",
  "business_category": "education",
  "swiped_percent": 0,
  "keyed_percent": 0,
  "ecommerce_percent": 100,
  "ownership_type": "llp",
  "fed_tax_id": "0000000000",
  "cc_average_ticket_range": 5,
  "cc_monthly_volume_range": 1,
  "cc_high_ticket": 1500,
  "ec_average_ticket_range": 5,
  "ec_monthly_volume_range": 2,
  "ec_high_ticket": 1500,
  "website": "http://www.example.com",
  "legal_name": "Total Home Goods, LLP",
  "client_app_id": "ABC123",
  "app_link": "https://mpa.example.com/signup/123456788",
  "primary_principal": {
    "first_name": "first_name6",
    "last_name": "last_name4",
    "middle_name": "middle_name6",
    "title": "title2",
    "date_of_birth": "date_of_birth2"
  }
}
```

