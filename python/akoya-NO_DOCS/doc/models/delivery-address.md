
# Delivery Address

Physical mail address associated with the account

*This model accepts additional fields of type Any.*

## Structure

`DeliveryAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `line_1` | `str` | Optional | Address line 1 |
| `line_2` | `str` | Optional | Address line 2 |
| `line_3` | `str` | Optional | Address line 3 |
| `city` | `str` | Optional | City |
| `region` | `str` | Optional | State, Province, Territory, Canton or Prefecture. From [Universal Postal Union](https://www.upu.int/en/Postal-Solutions/Programmes-Services/Addressing-Solutions#addressing-s42-standard) as of 2-26-2020, [S42 International Address Standards](https://www.upu.int/UPU/media/upu/documents/PostCode/S42_International-Addressing-Standards.pdf). For U.S. addresses can be 2-character code from '#/components/schemas/StateCode' |
| `postal_code` | `str` | Optional | Postal code<br><br>**Constraints**: *Maximum Length*: `16` |
| `country` | [`Iso3166CountryCode`](../../doc/models/iso-3166-country-code.md) | Optional | Country code |
| `mtype` | `str` | Optional | Type of address location. One of BUSINESS, HOME, MAILING |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "line1": "line18",
  "line2": "line20",
  "line3": "line38",
  "city": "city4",
  "region": "region2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

