
# Address

Address of contact

## Structure

`Address`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Optional | City of contact<br><br>**Constraints**: *Maximum Length*: `36`, *Pattern*: `^[\w\#\,\.\-\'\&\s\/]+$` |
| `state` | `str` | Optional | State of contact<br><br>**Constraints**: *Maximum Length*: `24` |
| `postal_code` | `str` | Optional | Postal code of contact<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `10`, *Pattern*: `^[a-zA-Z0-9\-\s]+$` |
| `country` | [`CountryEnum`](../../doc/models/country-enum.md) | Optional | An alpha 2 format country code of US or CA. |
| `street` | `str` | Optional | Street of contact<br><br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[\w\#\,\.\-\'\&\s\/]+$` |

## Example (as JSON)

```json
{
  "city": "Novi",
  "state": "Michigan",
  "postal_code": "48375",
  "country": "US",
  "street": "street8"
}
```

