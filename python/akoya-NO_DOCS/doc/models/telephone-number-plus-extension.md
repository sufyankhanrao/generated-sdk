
# Telephone Number Plus Extension

A telephone number that can contain optional text for an arbitrary length telephone extension number

*This model accepts additional fields of type Any.*

## Structure

`TelephoneNumberPlusExtension`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`TelephoneNumberType`](../../doc/models/telephone-number-type.md) | Optional | Type of phone number: HOME, BUSINESS, CELL, FAX |
| `country` | [`Iso3166CountryCode`](../../doc/models/iso-3166-country-code.md) | Optional | Country calling codes defined by ITU-T recommendations E.123 and E.164 |
| `number` | `str` | Optional | Telephone subscriber number defined by ITU-T recommendation E.164<br><br>**Constraints**: *Maximum Length*: `15`, *Pattern*: `\d+` |
| `extension` | `str` | Optional | An arbitrary length telephone number extension |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "type": "FAX",
  "country": "GG",
  "number": "number6",
  "extension": "extension4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

