
# Form 1042 S

Foreign Person's U.S. Source Income Subject to Withholding

*This model accepts additional fields of type Any.*

## Structure

`Form1042S`

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
| `form_id` | `str` | Optional | Unique form identifier |
| `amended` | `bool` | Optional | Amended |
| `amendment_number` | `int` | Optional | Amendment number |
| `income_type_code` | `str` | Optional | Box 1, Income code |
| `gross_income` | `float` | Optional | Box 2, Gross income |
| `chapter_indicator` | `str` | Optional | Box 3, Chapter indicator |
| `ch_3_exemption_code` | `str` | Optional | Box 3a, Exemption code |
| `ch_3_tax_rate` | `float` | Optional | Box 3b, Tax rate |
| `ch_4_exemption_code` | `str` | Optional | Box 4a, Exemption code |
| `ch_4_tax_rate` | `float` | Optional | Box 4b, Tax rate |
| `withholding_allowance` | `float` | Optional | Box 5, Withholding allowance |
| `net_income` | `float` | Optional | Box 6, Net income |
| `federal_tax_withheld` | `float` | Optional | Box 7a, Federal tax withheld |
| `escrow_procedures_applied` | `bool` | Optional | Box 7b, Check if federal tax withheld was not deposited with the IRS because escrow procedures were applied |
| `subsequent_year` | `bool` | Optional | Box 7c, Check if withholding occurred in subsequent year with respect to a partnership interest |
| `other_agents_tax_withheld` | `float` | Optional | Box 8, Tax withheld by other agents |
| `recipient_repaid_amount` | `float` | Optional | Box 9, Overwithheld tax repaid to recipient pursuant to adjustment procedures |
| `total_tax_withholding_credit` | `float` | Optional | Box 10, Total withholding credit |
| `withholding_agent_tax_paid` | `float` | Optional | Box 11, Tax paid by withholding agent (amounts not withheld) |
| `withholding_agent` | [`Form1042SAgent`](../../doc/models/form-1042-s-agent.md) | Optional | Boxes 12a-i, Withholding agent |
| `form_1042_recipient` | [`Form1042SRecipient`](../../doc/models/form-1042-s-recipient.md) | Optional | Boxes 13a-j, 13l, Recipient for Form 1042-S |
| `account_number` | `str` | Optional | Box 13k, Recipient account number |
| `primary` | [`Form1042SAgent`](../../doc/models/form-1042-s-agent.md) | Optional | Boxes 14a-b, Primary Withholding Agent |
| `prorata_basis_reporting` | `bool` | Optional | Box 15, Check if pro-rata basis reporting |
| `intermediary` | [`Form1042SAgent`](../../doc/models/form-1042-s-agent.md) | Optional | Boxes 15a-i, Intermediary or flow thru entity |
| `payer` | [`Form1042SAgent`](../../doc/models/form-1042-s-agent.md) | Optional | Boxes 16a-e, Payer |
| `state_and_local` | [`StateAndLocalTaxWithholding`](../../doc/models/state-and-local-tax-withholding.md) | Optional | Box 17, State and Local tax withholding |
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
  "accountId": "accountId6",
  "taxFormId": "taxFormId6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

