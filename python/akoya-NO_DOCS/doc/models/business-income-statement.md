
# Business Income Statement

Business Income Statement for IRS Form 1040 Schedule C

*This model accepts additional fields of type Any.*

## Structure

`BusinessIncomeStatement`

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
| `business_name` | `str` | Optional | Box C, Business name |
| `sales` | `float` | Optional | Box 1, Gross receipts or sales |
| `returns` | `float` | Optional | Box 2, Returns and allowances |
| `other_income` | [`List[DescriptionAndAmount]`](../../doc/models/description-and-amount.md) | Optional | Box 8, Other income |
| `advertising` | `float` | Optional | Box 8, Advertising |
| `car_and_truck` | `float` | Optional | Box 9, Car and truck expenses |
| `commissions` | `float` | Optional | Box 10, Commissions and fees |
| `contract_labor` | `float` | Optional | Box 11, Contract labor |
| `depletion` | `float` | Optional | Box 12, Depletion |
| `depreciation` | `float` | Optional | Box 13, Depreciation |
| `employee_benefits` | `float` | Optional | Box 14, Employee benefit programs |
| `insurance` | `float` | Optional | Box 15, Insurance |
| `mortgage_interest` | `float` | Optional | Box 16a, Mortgage interest |
| `other_interest` | `float` | Optional | Box 16b, Other interest |
| `legal` | `float` | Optional | Box 17, Legal and professional services |
| `office` | `float` | Optional | Box 18, Office expense |
| `pension` | `float` | Optional | Box 19, Pension and profit-sharing plans |
| `equipment_rent` | `float` | Optional | Box 20a, Equipment rent |
| `other_rent` | `float` | Optional | Box 20b, Other rent |
| `repairs` | `float` | Optional | Box 21, Repairs and maintenance |
| `supplies` | `float` | Optional | Box 22, Supplies |
| `taxes` | `float` | Optional | Box 23, Taxes and licenses |
| `travel` | `float` | Optional | Box 24a, Travel |
| `meals` | `float` | Optional | Box 24b, Deductible meals |
| `utilities` | `float` | Optional | Box 25, Utilities |
| `wages` | `float` | Optional | Box 26, Wages |
| `other_expenses` | [`List[DescriptionAndAmount]`](../../doc/models/description-and-amount.md) | Optional | Box 27, Other expenses |
| `beginning_inventory` | `float` | Optional | Box 35, Inventory at beginning of year |
| `purchases` | `float` | Optional | Box 36, Purchases |
| `cost_of_labor` | `float` | Optional | Box 37, Cost of labor |
| `materials` | `float` | Optional | Box 38, Materials and supplies |
| `other_costs` | [`List[DescriptionAndAmount]`](../../doc/models/description-and-amount.md) | Optional | Box 39, Other costs |
| `ending_inventory` | `float` | Optional | Box 41, Inventory at end of year |
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
  "accountId": "accountId4",
  "taxFormId": "taxFormId2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

