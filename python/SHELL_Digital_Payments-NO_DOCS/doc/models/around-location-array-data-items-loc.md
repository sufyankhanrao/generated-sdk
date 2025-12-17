
# Around Location Array Data Items Loc

Object containing address details/elements

## Structure

`AroundLocationArrayDataItemsLoc`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `street` | `str` | Optional | The station’s full street address, including building number |
| `pc` | `str` | Optional | The station’s postcode |
| `city` | `str` | Optional | The city the station is located within |
| `region` | `str` | Optional | The region the station is located within |
| `country` | `str` | Required | The name of the country (in English) the station is located within |
| `ccode` | `str` | Required | The two-letter ISO 3166 country code of the country the station is located within |

## Example (as JSON)

```json
{
  "street": "80/2 Outer Ring Road.",
  "pc": "560037",
  "city": "Bangalore",
  "region": "Karnataka",
  "country": "India",
  "ccode": "IN"
}
```

