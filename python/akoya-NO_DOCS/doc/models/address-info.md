
# Address Info

*This model accepts additional fields of type Any.*

## Structure

`AddressInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `line_1` | `str` | Optional | May contain full address if not separated |
| `city` | `str` | Optional | - |
| `state` | `str` | Optional | - |
| `postal_code` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "line1": "line12",
  "city": "city0",
  "state": "state4",
  "postalCode": "postalCode8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

