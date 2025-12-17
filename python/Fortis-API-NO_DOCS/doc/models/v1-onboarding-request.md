
# V1 Onboarding Request

## Structure

`V1OnboardingRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `parent_id` | `str` | Optional | Location ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `primary_principal` | [`PrimaryPrincipal1`](../../doc/models/primary-principal-1.md) | Required | The Primary Principal. |
| `template_code` | `str` | Required | The ID of the template to be used - this value will be provided by Fortis.<br><br>**Constraints**: *Maximum Length*: `20`, *Pattern*: `^[a-zA-Z0-9]*$` |
| `email` | `str` | Required | Merchant email address.<br><br>**Constraints**: *Maximum Length*: `100` |
| `dba_name` | `str` | Required | Merchant 'Doing Business As' name.<br><br>**Constraints**: *Maximum Length*: `100` |
| `location` | [`Location20`](../../doc/models/location-20.md) | Required | The Location. |
| `app_delivery` | [`AppDeliveryEnum`](../../doc/models/app-delivery-enum.md) | Required | The delivery method of the app to the merchant.<br><br>**Constraints**: *Maximum Length*: `12` |
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
| `bank_account` | [`BankAccount`](../../doc/models/bank-account.md) | Required | The Bank Account. |
| `alt_bank_account` | [`AltBankAccount`](../../doc/models/alt-bank-account.md) | Required | The Alternative Bank Account. |
| `legal_name` | `str` | Optional | Merchant legal name.<br><br>**Constraints**: *Maximum Length*: `100` |
| `contact` | [`Contact11`](../../doc/models/contact-11.md) | Required | The Contact. |
| `client_app_id` | `str` | Optional | Client Issues Id to track that can be used to track each submitted merchant application. This id should be generated and sent in the request payload, and will be returned in the response payload. If no id is submitted in the payload request, this field will be null in the response.<br><br>**Constraints**: *Maximum Length*: `50` |

## Example (as JSON)

```json
{
  "parent_id": "11e95f8ec39de8fbdb0a4f1a",
  "primary_principal": {
    "first_name": "Bob",
    "last_name": "Fairview",
    "middle_name": "Nathaniel",
    "title": "Dr",
    "date_of_birth": "2021-12-01",
    "address_line_1": "1354 Oak St.",
    "address_line_2": "Unit 203",
    "city": "Dover",
    "state_province": "DE",
    "postal_code": "55022",
    "ownership_percent": 100,
    "phone_number": "555-555-1234"
  },
  "template_code": "1234YourTemplateCode",
  "email": "email@domain.com",
  "dba_name": "Discount Home Goods",
  "location": {
    "address_line_1": "1200 West Hartford Pkwy",
    "address_line_2": "Suite 2000",
    "city": "Dover",
    "state_province": "DE",
    "postal_code": "55022",
    "phone_number": "555-555-1212"
  },
  "app_delivery": null,
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
  "bank_account": {
    "routing_number": "011103093",
    "account_number": "01234567890123",
    "account_holder_name": "Bob Fairview"
  },
  "alt_bank_account": {
    "routing_number": "011103093",
    "account_number": "01234567890123",
    "account_holder_name": "Bob Fairview",
    "deposit_type": "fees_adjustments"
  },
  "legal_name": "Total Home Goods, LLP",
  "contact": {
    "first_name": "Jeffery",
    "last_name": "Todd",
    "email": "jtodd@example.com",
    "phone_number": "555-555-3456"
  },
  "client_app_id": "ABC123",
  "business_type": "books_mags_music_and_video",
  "business_description": "business_description0"
}
```

