
# Form 1098 C

Contributions of Motor Vehicles, Boats, and Airplanes

*This model accepts additional fields of type Any.*

## Structure

`Form1098C`

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
| `date_of_contribution` | `date` | Optional | Box 1, Date of contribution |
| `odometer_mileage` | `int` | Optional | Box 2a, Odometer mileage |
| `car_year` | `int` | Optional | Box 2b, Year |
| `make` | `str` | Optional | Box 2c, Make |
| `model` | `str` | Optional | Box 2d, Model |
| `vin` | `str` | Optional | Box 3, Vehicle or other identification number |
| `arms_length_transaction` | `bool` | Optional | Box 4a, Donee certifies that vehicle was sold in arm's length transaction to unrelated party |
| `date_of_sale` | `date` | Optional | Box 4b, Date of sale |
| `gross_proceeds` | `float` | Optional | Box 4c, Gross proceeds from sale (see instructions) |
| `not_transferred_before` | `bool` | Optional | Box 5a, Donee certifies that vehicle will not be transferred for money, other property, or services before completion of material improvements or significant intervening use |
| `needy_individual` | `bool` | Optional | Box 5b, Donee certifies that vehicle is to be transferred to a needy individual for significantly below fair market value in furtherance of donee's charitable purpose |
| `description_of_improvements` | `str` | Optional | Box 5c, Donee certifies the following detailed description of material improvements or significant intervening use and duration of use |
| `goods_in_exchange` | `bool` | Optional | Box 6a, Did you provide goods or services in exchange for the vehicle? Yes |
| `value_of_exchange` | `float` | Optional | Box 6b, Value of goods and services provided in exchange for the vehicle |
| `intangible_religious` | `bool` | Optional | Box 6c, If this box is checked, donee certifies that the goods and services consisted solely of intangible religious benefits |
| `description_of_goods` | `str` | Optional | Box 6c, Describe the goods and services, if any, that were provided |
| `max_deduction_applies` | `bool` | Optional | Box 7, Under the law, the donor may not claim a deduction of more than $500 for this vehicle if this box is checked |
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
  "dateOfContribution": "2021-07-15",
  "dateOfSale": "2021-07-15",
  "corrected": false,
  "accountId": "accountId6",
  "taxFormId": "taxFormId6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

