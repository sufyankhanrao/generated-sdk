
# Location 5

The Location.

## Structure

`Location5`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_line_1` | `str` | Optional | Merchant's business address line 1.<br><br>**Constraints**: *Maximum Length*: `100` |
| `address_line_2` | `str` | Optional | Merchant's business address line 2.<br><br>**Constraints**: *Maximum Length*: `20` |
| `city` | `str` | Optional | Merchant's business city.<br><br>**Constraints**: *Maximum Length*: `50` |
| `state_province` | `str` | Optional | Merchant's business two-digit state or province code.<br><br>**Constraints**: *Maximum Length*: `2` |
| `postal_code` | `str` | Optional | Merchant's business postal code.<br><br>**Constraints**: *Maximum Length*: `10` |
| `phone_number` | `str` | Optional | Merchant's business phone number.<br><br>**Constraints**: *Maximum Length*: `20` |

## Example (as JSON)

```json
{
  "address_line_1": "1200 West Hartford Pkwy",
  "address_line_2": "Suite 2000",
  "city": "Dover",
  "state_province": "DE",
  "postal_code": "55022",
  "phone_number": "555-555-1212"
}
```

