
# Form 1120 SK1

Shareholder's Share of Income, Deductions, Credits, etc.

*This model accepts additional fields of type Any.*

## Structure

`Form1120SK1`

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
| `final_k_1` | `bool` | Optional | Final K-1 |
| `amended_k_1` | `bool` | Optional | Amended K-1 |
| `fiscal_year_begin` | `date` | Optional | Fiscal year begin date |
| `fiscal_year_end` | `date` | Optional | Fiscal year end date |
| `irs_center` | `str` | Optional | Box C, IRS Center where corporation filed return |
| `corporation_beginning_shares` | `float` | Optional | Box D, Corporation's total number of shares, Beginning of tax year |
| `corporation_ending_shares` | `float` | Optional | Box D, Corporation's total number of shares, End of tax year |
| `percent_ownership` | `float` | Optional | Box G, Current year allocation percentage |
| `beginning_shares` | `float` | Optional | Box H, Shareholder's number of shares, Beginning of tax year |
| `ending_shares` | `float` | Optional | Box H, Shareholder's number of shares, End of tax year |
| `beginning_loans` | `float` | Optional | Box I, Loans from shareholder, Beginning of tax year |
| `ending_loans` | `float` | Optional | Box I, Loans from shareholder, Ending of tax year |
| `ordinary_income` | `float` | Optional | Box 1, Ordinary business income (loss) |
| `net_rental_real_estate_income` | `float` | Optional | Box 2, Net rental real estate income (loss) |
| `other_rental_income` | `float` | Optional | Box 3, Other net rental income (loss) |
| `interest_income` | `float` | Optional | Box 4, Interest income |
| `ordinary_dividends` | `float` | Optional | Box 5a, Ordinary dividends |
| `qualified_dividends` | `float` | Optional | Box 5b, Qualified dividends |
| `royalties` | `float` | Optional | Box 6, Royalties |
| `net_short_term_gain` | `float` | Optional | Box 7, Net short-term capital gain (loss) |
| `net_long_term_gain` | `float` | Optional | Box 8a, Net long-term capital gain (loss) |
| `collectibles_gain` | `float` | Optional | Box 8b, Collectibles (28%) gain (loss) |
| `unrecaptured_1250_gain` | `float` | Optional | Box 8c, Unrecaptured section 1250 gain |
| `net_1231_gain` | `float` | Optional | Box 9, Net section 1231 gain (loss) |
| `other_income` | [`List[DescriptionAndAmount]`](../../doc/models/description-and-amount.md) | Optional | Box 10, Other income (loss) |
| `section_179_deduction` | `float` | Optional | Box 11, Section 179 deduction |
| `other_deductions` | [`List[CodeAndAmount]`](../../doc/models/code-and-amount.md) | Optional | Box 12, Other deductions |
| `credits` | [`List[CodeAndAmount]`](../../doc/models/code-and-amount.md) | Optional | Box 13, Credits |
| `schedule_k_3` | `bool` | Optional | Box 14, Schedule K-3 is attached |
| `amt_items` | [`List[CodeAndAmount]`](../../doc/models/code-and-amount.md) | Optional | Box 15, Alternative minimum tax (AMT) items |
| `basis_items` | [`List[CodeAndAmount]`](../../doc/models/code-and-amount.md) | Optional | Box 16, Items affecting shareholder basis |
| `other_info` | [`List[CodeAndAmount]`](../../doc/models/code-and-amount.md) | Optional | Box 17, Other information |
| `multiple_at_risk_activities` | `bool` | Optional | Box 18, More than one activity for at-risk purposes |
| `multiple_passive_activities` | `bool` | Optional | Box 19, More than one activity for passive activity purposes |
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
  "fiscalYearBegin": "2021-07-15",
  "fiscalYearEnd": "2021-07-15",
  "corrected": false,
  "accountId": "accountId6",
  "taxFormId": "taxFormId8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

