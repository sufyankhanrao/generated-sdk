
# Form W2

Wage and Tax Statement

*This model accepts additional fields of type Any.*

## Structure

`FormW2`

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
| `control_number` | `str` | Optional | Control number |
| `wages` | `float` | Optional | Box 1, Wages, tips, other compensation |
| `federal_tax_withheld` | `float` | Optional | Box 2, Federal income tax withheld |
| `social_security_wages` | `float` | Optional | Box 3, Social security wages |
| `social_security_tax_withheld` | `float` | Optional | Box 4, Social security tax withheld |
| `medicare_wages` | `float` | Optional | Box 5, Medicare wages and tips |
| `medicare_tax_withheld` | `float` | Optional | Box 6, Medicare tax withheld |
| `social_security_tips` | `float` | Optional | Box 7, Social security tips |
| `allocated_tips` | `float` | Optional | Box 8, Allocated tips |
| `dependent_care_benefit` | `float` | Optional | Box 10, Dependent care benefits |
| `non_qualified_plan` | `float` | Optional | Box 11, Nonqualified plans |
| `codes` | [`List[CodeAndAmount]`](../../doc/models/code-and-amount.md) | Optional | Box 12, Codes and amounts |
| `statutory` | `bool` | Optional | Box 13, Statutory employee |
| `retirement_plan` | `bool` | Optional | Box 13, Retirement plan |
| `third_party_sick_pay` | `bool` | Optional | Box 13, Third-party sick pay |
| `espp_qualified` | `float` | Optional | Employee Stock Purchase Plan Qualified Disposition amount |
| `espp_non_qualified` | `float` | Optional | Employee Stock Purchase Plan Nonqualified Disposition amount |
| `other` | [`List[DescriptionAndAmount]`](../../doc/models/description-and-amount.md) | Optional | Box 14, Other descriptions and amounts |
| `state_and_local` | [`List[StateAndLocalTaxWithholding]`](../../doc/models/state-and-local-tax-withholding.md) | Optional | Boxes 15-20, State and Local tax withholding |
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

