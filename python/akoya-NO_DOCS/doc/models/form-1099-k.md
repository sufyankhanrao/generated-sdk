
# Form 1099 K

Merchant Card and Third-Party Network Payments

*This model accepts additional fields of type Any.*

## Structure

`Form1099K`

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
| `payment_settlement_entity` | `bool` | Optional | Check to indicate if FILER is a Payment Settlement Entity (PSE) |
| `electronic_payment_facilitator` | `bool` | Optional | Check to indicate if FILER is an Electronic Payment Facilitator (EPF) / Other third party |
| `payment_card` | `bool` | Optional | Check to indicate transactions reported are: Payment card |
| `third_party_network` | `bool` | Optional | Check to indicate transactions reported are: Third party network |
| `pse_name` | `str` | Optional | PSE's name |
| `pse_phone` | [`TelephoneNumberPlusExtension`](../../doc/models/telephone-number-plus-extension.md) | Optional | PSE's phone number |
| `account_number` | `str` | Optional | Account number |
| `gross_amount` | `float` | Optional | Box 1a, Gross amount of payment card/third party network transactions |
| `card_not_present` | `float` | Optional | Box 1b, Card Not Present Transactions |
| `merchant_category_code` | `str` | Optional | Box 2, Merchant category code |
| `number_of_transactions` | `float` | Optional | Box 3, Number of purchase transactions |
| `federal_tax_withheld` | `float` | Optional | Box 4, Federal income tax withheld |
| `month_amounts` | [`List[MonthAndAmount]`](../../doc/models/month-and-amount.md) | Optional | Box 5, Monthly amounts |
| `state_and_local` | [`List[StateAndLocalTaxWithholding]`](../../doc/models/state-and-local-tax-withholding.md) | Optional | Boxes 6-8, State and Local tax withholding |
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
  "accountId": "accountId4",
  "taxFormId": "taxFormId8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

