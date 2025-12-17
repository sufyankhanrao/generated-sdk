
# Form 1099 R

Distributions from Pensions, Annuities, Retirement or Profit-Sharing Plans, IRAs, Insurance Contracts, etc.

*This model accepts additional fields of type Any.*

## Structure

`Form1099R`

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
| `allocable_to_irr` | `float` | Optional | Box 10, Amount allocable to IRR within 5 years |
| `first_year_of_roth` | `int` | Optional | Box 11, First year of designated Roth contributions. A four-digit year. (Like `TaxYear` definition, but lower minimum since first year of Roth IRAs was 1997)<br><br>**Constraints**: `>= 1997`, `<= 2050` |
| `recipient_account_number` | `str` | Optional | Account number |
| `gross_distribution` | `float` | Optional | Box 1, Gross distribution |
| `taxable_amount` | `float` | Optional | Box 2a, Taxable amount |
| `taxable_amount_not_determined` | `bool` | Optional | Box 2b, Taxable amount not determined |
| `total_distribution` | `bool` | Optional | Box 2c, Total distribution |
| `capital_gain` | `float` | Optional | Box 3, Capital gain |
| `federal_tax_withheld` | `float` | Optional | Box 4, Federal income tax withheld |
| `employee_contributions` | `float` | Optional | Box 5, Employee contributions |
| `net_unrealized_appreciation` | `float` | Optional | Box 6, Net unrealized appreciation |
| `distribution_codes` | `List[str]` | Optional | Box 7, Distribution codes |
| `ira_sep_simple` | `bool` | Optional | Box 7b, IRA/SEP/SIMPLE |
| `other_amount` | `float` | Optional | Box 8, Other |
| `other_percent` | `float` | Optional | Box 8, Other percent |
| `your_percent_of_total` | `float` | Optional | Box 9a, Your percent of total distribution |
| `total_employee_contributions` | `float` | Optional | Box 9b, Total employee contributions |
| `foreign_account_tax_compliance` | `bool` | Optional | Box 12, FATCA filing requirement |
| `date_of_payment` | `date` | Optional | Box 13, Date of payment |
| `state_and_local` | [`List[StateAndLocalTaxWithholding]`](../../doc/models/state-and-local-tax-withholding.md) | Optional | Boxes 14-19, State and Local tax withholding |
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
  "firstYearOfRoth": 2020,
  "dateOfPayment": "2021-07-15",
  "corrected": false,
  "accountId": "accountId8",
  "taxFormId": "taxFormId6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

