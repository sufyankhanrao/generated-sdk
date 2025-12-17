
# Addresses Type Get Response

## Structure

`AddressesTypeGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `address` | [`Address`](../../doc/models/address.md) | Optional | - |

## Example (as JSON)

```json
{
  "correlationId": "correlationId2",
  "httpStatusCode": "httpStatusCode6",
  "httpStatusMessage": "httpStatusMessage8",
  "address": {
    "addressLine1": "addressLine18",
    "addressLine2": "addressLine26",
    "city": "city6",
    "state": "NM",
    "country": "US",
    "postalCode": "postalCode8",
    "postalCodeExtension": "postalCodeExtension4",
    "type": "TerminalDeployment"
  }
}
```

