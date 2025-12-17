
# Form W2 G

Certain Gambling Winnings

*This model accepts additional fields of type Any.*

## Structure

`FormW2G`

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
| `winnings` | `float` | Optional | Box 1, Reportable winnings |
| `date_won` | `date` | Optional | Box 2, Date won |
| `type_of_wager` | `str` | Optional | Box 3, Type of wager |
| `federal_tax_withheld` | `float` | Optional | Box 4, Federal income tax withheld |
| `transaction` | `str` | Optional | Box 5, Transaction |
| `race` | `str` | Optional | Box 6, Race |
| `identical_winnings` | `float` | Optional | Box 7, Winnings from identical wagers |
| `cashier` | `str` | Optional | Box 8, Cashier |
| `window` | `str` | Optional | Box 10, Window |
| `first_id` | `str` | Optional | Box 11, First I.D. |
| `second_id` | `str` | Optional | Box 12, Second I.D. |
| `state_and_local` | [`List[StateAndLocalTaxWithholding]`](../../doc/models/state-and-local-tax-withholding.md) | Optional | Boxes 13-18, State and Local tax withholding, use income fields for state (box 14) and local (box 16) winnings amounts |
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
  "dateWon": "2021-07-15",
  "corrected": false,
  "accountId": "accountId8",
  "taxFormId": "taxFormId0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

