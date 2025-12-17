
# Form 1099 B

Proceeds From Broker and Barter Exchange Transactions

*This model accepts additional fields of type Any.*

## Structure

`Form1099B`

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
| `state_and_local` | [`List[StateAndLocalTaxWithholding]`](../../doc/models/state-and-local-tax-withholding.md) | Optional | Boxes 14-16, State and Local tax withholding |
| `federal_tax_withheld` | `float` | Optional | Box 4, Federal income tax withheld |
| `profit_on_closed_contracts` | `float` | Optional | Box 8, Profit or (loss) realized in current year on closed contracts |
| `unrealized_profit_open_contracts_begin` | `float` | Optional | Box 9, Unrealized profit or loss on open contracts at end of last year |
| `unrealized_profit_open_contracts_end` | `float` | Optional | Box 10, Unrealized profit or loss on open contracts at end of current year |
| `aggregate_profit_on_contracts` | `float` | Optional | Box 11, Aggregate profit or (loss) on contracts |
| `bartering` | `float` | Optional | Box 13, Bartering |
| `security_details` | [`List[SecurityDetailIrsForm1099B]`](../../doc/models/security-detail-irs-form-1099-b.md) | Optional | Boxes 1-3, 5-7, 12, Security details |
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
  "accountId": "accountId8",
  "taxFormId": "taxFormId6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

