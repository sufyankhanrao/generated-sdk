
# Addresses Get Response

## Structure

`AddressesGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `addresses` | [`List[Address]`](../../doc/models/address.md) | Optional | - |

## Example (as JSON)

```json
{
  "correlationId": "correlationId0",
  "httpStatusCode": "httpStatusCode4",
  "httpStatusMessage": "httpStatusMessage0",
  "addresses": [
    {
      "addressLine1": "addressLine16",
      "addressLine2": "addressLine24",
      "city": "city4",
      "state": "GA",
      "country": "US",
      "postalCode": "postalCode4",
      "postalCodeExtension": "postalCodeExtension2",
      "type": "Mailing"
    }
  ]
}
```

