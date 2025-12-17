
# Form 1099 Misc

Miscellaneous Income

*This model accepts additional fields of type Any.*

## Structure

`Form1099Misc`

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
| `rents` | `float` | Optional | Box 1, Rents |
| `royalties` | `float` | Optional | Box 2, Royalties |
| `other_income` | `float` | Optional | Box 3, Other income |
| `federal_tax_withheld` | `float` | Optional | Box 4, Federal income tax withheld |
| `fishing_boat_proceeds` | `float` | Optional | Box 5, Fishing boat proceeds |
| `medical_health_payment` | `float` | Optional | Box 6, Medical and health care payments |
| `payer_direct_sales` | `bool` | Optional | Box 7, Payer made direct sales of $5,000 or more of consumer products to a buyer (recipient) for resale |
| `substitute_payments` | `float` | Optional | Box 8, Substitute payments in lieu of dividends or interest |
| `crop_insurance` | `float` | Optional | Box 9, Crop insurance proceeds |
| `second_tin_notice` | `bool` | Optional | Second TIN Notice |
| `gross_attorney` | `float` | Optional | Box 10, Gross proceeds paid to an attorney |
| `fish_purchased` | `float` | Optional | Box 11, Fish purchased for resale |
| `section_409_a_deferrals` | `float` | Optional | Box 12, Section 409A deferrals |
| `foreign_account_tax_compliance` | `bool` | Optional | Box 13, FATCA filing requirement |
| `excess_golden` | `float` | Optional | Box 14, Excess golden parachute payments |
| `non_qualified_deferred_compensation` | `float` | Optional | Box 15, Nonqualified Deferred Compensation |
| `state_and_local` | [`List[StateAndLocalTaxWithholding]`](../../doc/models/state-and-local-tax-withholding.md) | Optional | Boxes 16-18, State and Local tax withholding |
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

