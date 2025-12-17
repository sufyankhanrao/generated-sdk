
# Address 79

Array of merchant addresses.

## Structure

`Address79`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_line_1` | `str` | Required | Line 1 of address.<br><br>**Constraints**: *Maximum Length*: `100` |
| `address_line_2` | `str` | Optional | Line 2 of address.<br><br>**Constraints**: *Maximum Length*: `20` |
| `city` | `str` | Required | City of address.<br><br>**Constraints**: *Maximum Length*: `50` |
| `state_province` | `str` | Required | State or province of address.<br><br>**Constraints**: *Maximum Length*: `2` |
| `postal_code` | `str` | Required | Postal code of address.<br><br>**Constraints**: *Maximum Length*: `10` |
| `country_code` | `str` | Required | Country of address.<br><br>**Constraints**: *Maximum Length*: `2` |
| `address_type` | [`AddressTypeEnum`](../../doc/models/address-type-enum.md) | Required | Address type of address.<br><br>**Constraints**: *Maximum Length*: `20` |

## Example (as JSON)

```json
{
  "address_line_1": "121 E Main",
  "address_line_2": "Apt 707",
  "city": "Dallas",
  "state_province": "TX",
  "postal_code": "75087",
  "country_code": "US",
  "address_type": "location"
}
```

