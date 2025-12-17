
# Array of Account Payment Networks

An optionally paginated array of payment networks supported by the account

*This model accepts additional fields of type Any.*

## Structure

`ArrayOfAccountPaymentNetworks`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_networks` | [`List[PaymentNetworkSupportedByAccount]`](../../doc/models/payment-network-supported-by-account.md) | Optional | Array of payment networks |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "paymentNetworks": [
    {
      "bankId": "bankId0",
      "identifier": "identifier2",
      "identifierType": "identifierType4",
      "type": "type0",
      "transferIn": false,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    {
      "bankId": "bankId0",
      "identifier": "identifier2",
      "identifierType": "identifierType4",
      "type": "type0",
      "transferIn": false,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    {
      "bankId": "bankId0",
      "identifier": "identifier2",
      "identifierType": "identifierType4",
      "type": "type0",
      "transferIn": false,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

