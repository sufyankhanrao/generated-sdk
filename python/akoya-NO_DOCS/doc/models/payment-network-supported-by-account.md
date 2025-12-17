
# Payment Network Supported by Account

This provides details required to execute a transaction against the account within the payment network

*This model accepts additional fields of type Any.*

## Structure

`PaymentNetworkSupportedByAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_id` | `str` | Optional | Bank identifier used by the payment network ie. Routing Number |
| `identifier` | `str` | Optional | The number used to identify the account within the payment network. If identifierType is ACCOUNT_NUMBER, this is the account number. |
| `identifier_type` | `str` | Optional | Type of identifier |
| `mtype` | `str` | Optional | Type of payment network |
| `transfer_in` | `bool` | Optional | Can transfer funds to the account using this information |
| `transfer_out` | `bool` | Optional | Can transfer funds from the account using this information |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
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
```

