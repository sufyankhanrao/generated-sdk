
# Farm Rental Income Statement

Farm Rental Income Statement for IRS Form 4835

*This model accepts additional fields of type Any.*

## Structure

`FarmRentalIncomeStatement`

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
| `income_from_production` | `float` | Optional | Box 1, Income from production of livestock, produce, grains, and other crops |
| `coop_distributions` | `float` | Optional | Box 2a, Cooperative distributions |
| `ag_program_payments` | `float` | Optional | Box 3a, Agricultural program payments |
| `ccc_loans` | `float` | Optional | Box 4a, Commodity Credit Corporation (CCC) loans reported under election |
| `crop_insurance_proceeds` | `float` | Optional | Box 5a, Crop insurance proceeds and federal crop disaster payments |
| `other_income` | [`List[DescriptionAndAmount]`](../../doc/models/description-and-amount.md) | Optional | Box 6, Other income |
| `car_and_truck` | `float` | Optional | Box 8, Car and truck expenses |
| `chemicals` | `float` | Optional | Box 9, Chemicals |
| `conservation` | `float` | Optional | Box 10, Conservation expenses |
| `custom_hire_expenses` | `float` | Optional | Box 11, Custom hire (machine work) |
| `depreciation` | `float` | Optional | Box 12, Depreciation |
| `employee_benefit_programs` | `float` | Optional | Box 13, Employee benefit programs |
| `feed` | `float` | Optional | Box 14, Feed |
| `fertilizers` | `float` | Optional | Box 15, Fertilizers and lime |
| `freight` | `float` | Optional | Box 16, Freight and trucking |
| `fuel` | `float` | Optional | Box 17, Gasoline, fuel, and oil |
| `insurance` | `float` | Optional | Box 18, Insurance (other than health) |
| `mortgage_interest` | `float` | Optional | Box 19a, Mortgage Interest |
| `other_interest` | `float` | Optional | Box 19b, Other interest |
| `labor_hired` | `float` | Optional | Box 20, Labor hired |
| `pension` | `float` | Optional | Box 21, Pension and profit-sharing plans |
| `equipment_rent` | `float` | Optional | Box 22a, Rent or lease: Vehicles, machinery, equipment |
| `other_rent` | `float` | Optional | Box 22b, Rent or lease: Other |
| `repairs` | `float` | Optional | Box 23, Repairs and maintenance |
| `seeds` | `float` | Optional | Box 24, Seeds and plants |
| `storage` | `float` | Optional | Box 25, Storage and warehousing |
| `supplies` | `float` | Optional | Box 26, Supplies |
| `taxes` | `float` | Optional | Box 27, Taxes |
| `utilities` | `float` | Optional | Box 28, Utilities |
| `veterinary` | `float` | Optional | Box 29, Veterinary, breeding, and medicine |
| `other_expenses` | [`List[DescriptionAndAmount]`](../../doc/models/description-and-amount.md) | Optional | Box 30, Other expenses |
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

