
# Address 2

Address

## Structure

`Address2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Optional | City name<br><br>**Constraints**: *Maximum Length*: `36`, *Pattern*: `^[\w\#\,\.\-\'\&\s\/]+$` |
| `state` | `str` | Optional | State name<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `postal_code` | `str` | Optional | Postal code<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `10`, *Pattern*: `^[a-zA-Z0-9\-\s]+$` |
| `country` | [`CountryEnum`](../../doc/models/country-enum.md) | Optional | An alpha 2 format country code of US or CA. |
| `street` | `str` | Optional | Street<br><br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[\w\#\,\.\-\'\&\s\/]+$` |

## Example (as JSON)

```json
{
  "city": "Novi",
  "state": "MI",
  "postal_code": "48375",
  "country": "US",
  "street": "street0"
}
```

