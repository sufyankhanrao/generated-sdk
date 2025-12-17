
# Form 1099 Div

Dividends and Distributions

*This model accepts additional fields of type Any.*

## Structure

`Form1099Div`

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
| `account_number` | `str` | Optional | Account number |
| `ordinary_dividends` | `float` | Optional | Box 1a, Total ordinary dividends |
| `qualified_dividends` | `float` | Optional | Box 1b, Qualified dividends |
| `total_capital_gain` | `float` | Optional | Box 2a, Total capital gain distributions |
| `unrecaptured_1250_gain` | `float` | Optional | Box 2b, Unrecaptured Section 1250 gain |
| `section_1202_gain` | `float` | Optional | Box 2c, Section 1202 gain |
| `collectibles_gain` | `float` | Optional | Box 2d, Collectibles (28%) gain |
| `section_897_dividends` | `float` | Optional | Box 2e, Section 897 ordinary dividends |
| `section_897_capital_gain` | `float` | Optional | Box 2f, Section 897 capital gain |
| `non_taxable_distribution` | `float` | Optional | Box 3, Nondividend distributions |
| `federal_tax_withheld` | `float` | Optional | Box 4, Federal income tax withheld |
| `section_199_a_dividends` | `float` | Optional | Box 5, Section 199A dividends |
| `investment_expenses` | `float` | Optional | Box 6, Investment expenses |
| `foreign_tax_paid` | `float` | Optional | Box 7, Foreign tax paid |
| `foreign_country` | `str` | Optional | Box 8, Foreign country or U.S. possession |
| `cash_liquidation` | `float` | Optional | Box 9, Cash liquidation distributions |
| `non_cash_liquidation` | `float` | Optional | Box 10, Noncash liquidation distributions |
| `foreign_account_tax_compliance` | `bool` | Optional | Box 11, FATCA filing requirement |
| `tax_exempt_interest_dividend` | `float` | Optional | Box 12, Exempt-interest dividends |
| `specified_pab_interest_dividend` | `float` | Optional | Box 13, Specified private activity bond interest dividends |
| `state_and_local` | [`List[StateAndLocalTaxWithholding]`](../../doc/models/state-and-local-tax-withholding.md) | Optional | Boxes 14-16, State and Local tax withholding |
| `foreign_incomes` | [`List[DescriptionAndAmount]`](../../doc/models/description-and-amount.md) | Optional | Foreign income information |
| `state_tax_exempt_incomes` | [`List[DescriptionAndAmount]`](../../doc/models/description-and-amount.md) | Optional | Tax exempt income state information |
| `second_tin_notice` | `bool` | Optional | Second TIN Notice |
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
  "accountId": "accountId2",
  "taxFormId": "taxFormId0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

