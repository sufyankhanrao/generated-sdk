
# Form 1095 A

Health Insurance Marketplace Statement

*This model accepts additional fields of type Any.*

## Structure

`Form1095A`

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
| `marketplace_id` | `str` | Optional | Box 1, Marketplace identifier |
| `marketplace_policy_number` | `str` | Optional | Box 2, Marketplace-assigned policy number |
| `policy_issuer_name` | `str` | Optional | Box 3, Policy issuer's name |
| `recipient_date_of_birth` | `date` | Optional | Box 6, Recipient's date of birth |
| `spouse_name` | `str` | Optional | Box 7, Recipient's spouse's name |
| `spouse_tin` | `str` | Optional | Box 8, Recipient's spouse's SSN |
| `spouse_date_of_birth` | `date` | Optional | Box 9, Recipient's spouse's date of birth |
| `policy_start_date` | `date` | Optional | Box 10, Policy start date |
| `policy_termination_date` | `date` | Optional | Box 11, Policy termination date |
| `covered_individuals` | [`List[HealthInsuranceMarketplaceCoveredIndividual]`](../../doc/models/health-insurance-marketplace-covered-individual.md) | Optional | Boxes 16+, Covered Individuals |
| `coverages` | [`List[HealthInsuranceCoverage]`](../../doc/models/health-insurance-coverage.md) | Optional | Boxes 21-33, Coverage Information |
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
  "recipientDateOfBirth": "2021-07-15",
  "spouseDateOfBirth": "2021-07-15",
  "policyStartDate": "2021-07-15",
  "policyTerminationDate": "2021-07-15",
  "corrected": false,
  "accountId": "accountId2",
  "taxFormId": "taxFormId0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

