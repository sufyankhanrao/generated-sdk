
# Rental Income Statement

Rental Income Statement for IRS Form 1040 Schedule E

*This model accepts additional fields of type Any.*

## Structure

`RentalIncomeStatement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tax_year` | `int` | Optional | Year for which taxes are being paid<br><br>**Constraints**: `>= 2018`, `<= 2050` |
| `corrected` | `bool` | Optional | True to indicate this is a corrected tax form |
| `account_id` | `str` | Optional | Long-term persistent identity of the source account. Not the account number |
| `tax_form_id` | `str` | Optional | Long-term persistent id for this tax form. Depending upon the data provider, this may be the same id as the enclosing tax statement id, or this may be a different id, or this id may be omitted. |
| `tax_form_date` | `date` | Optional | Date of production or delivery of the tax form |
| `additional_information` | `str` | Optional | Additional explanation text or content about this tax form |
| `tax_form_type` | [`TypeFormType`](../../doc/models/type-form-type.md) | Optional | Enumerated name of the tax form entity e.g. "TaxW2" |
| `issuer` | [`TaxParty`](../../doc/models/tax-party.md) | Optional | Issuer's name, address, phone, and TIN. Issuer data need only be transmitted on enclosing TaxStatement, if it is the same on all its included tax forms. |
| `recipient` | [`TaxParty`](../../doc/models/tax-party.md) | Optional | Recipient's name, address, phone, and TIN. Recipient data need only be transmitted on enclosing TaxStatement, if it is the same on all its included tax forms. |
| `attributes` | [`List[TaxFormAttribute]`](../../doc/models/tax-form-attribute.md) | Optional | Additional attributes for this tax form when defined fields are not available. Some specific additional attributes already defined by providers: Fields required by [IRS FIRE](https://www.irs.gov/e-file-providers/filing-information-returns-electronically-fire): Name Control, Type of Identification Number (EIN, SSN, ITIN, ATIN). (ATIN is tax ID number for pending adoptions.) Tax form provider field for taxpayer notification: Recipient Email Address. |
| `error` | [`Error`](../../doc/models/error.md) | Optional | Present if an error was encountered while retrieving this form |
| `links` | [`List[HateoasLink]`](../../doc/models/hateoas-link.md) | Optional | Links to retrieve this form as data or image, or to invoke other APIs |
| `property_address` | [`Address`](../../doc/models/address.md) | Optional | Box 1a, Physical address of property (street, city, state, ZIP code) |
| `rents` | `float` | Optional | Box 3, Rents received |
| `advertising` | `float` | Optional | Box 5, Advertising |
| `auto` | `float` | Optional | Box 6, Auto and travel |
| `cleaning` | `float` | Optional | Box 7, Cleaning and maintenance |
| `commissions` | `float` | Optional | Box 8, Commissions |
| `insurance` | `float` | Optional | Box 9, Insurance |
| `legal` | `float` | Optional | Box 10, Legal and other professional fees |
| `management_fees` | `float` | Optional | Box 11, Management fees |
| `mortgage_interest` | `float` | Optional | Box 12, Mortgage interest paid to banks, etc. |
| `other_interest` | `float` | Optional | Box 13, Other interest |
| `repairs` | `float` | Optional | Box 14, Repairs |
| `supplies` | `float` | Optional | Box 15, Supplies |
| `taxes` | `float` | Optional | Box 16, Taxes |
| `utilities` | `float` | Optional | Box 17, Utilities |
| `depreciation_expense` | `float` | Optional | Box 18, Depreciation |
| `other_expenses` | [`List[DescriptionAndAmount]`](../../doc/models/description-and-amount.md) | Optional | Box 19, Other expenses |
| `capital_expenditures` | [`List[DateAndAmount]`](../../doc/models/date-and-amount.md) | Optional | Capital expenditures, for use in calculating Depreciation |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "taxYear": 2023,
  "taxFormDate": "2021-07-15",
  "attributes": [
    {
      "name": "nameControl",
      "value": "WILC"
    },
    {
      "name": "recipientIdType",
      "value": "EIN",
      "code": "1"
    },
    {
      "name": "recipientIdType",
      "value": "SSN",
      "code": "2"
    },
    {
      "name": "recipientIdType",
      "value": "ITIN",
      "code": "2"
    },
    {
      "name": "recipientIdType",
      "value": "ATIN",
      "code": "2"
    }
  ],
  "corrected": false,
  "accountId": "accountId8",
  "taxFormId": "taxFormId4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

