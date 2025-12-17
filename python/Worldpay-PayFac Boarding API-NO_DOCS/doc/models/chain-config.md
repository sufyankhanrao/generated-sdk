
# Chain Config

## Structure

`ChainConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `chain_code` | `str` | Optional | Chain code |
| `chain_name` | `str` | Optional | Name assocaited with the chain code |
| `template_mid` | `str` | Optional | Template Mid associated with the chain code - used for building terminals |
| `express_gateway_id` | `str` | Optional | Express Gateway Id associated with the chain code - used to board to express |
| `vas` | [`List[Vas]`](../../doc/models/vas.md) | Optional | Value added services associated with the chain code |

## Example (as JSON)

```json
{
  "chainCode": "0A1B2C",
  "chainName": "PayFac Chain 001",
  "templateMid": "400000000002",
  "expressGatewayId": "123456",
  "vas": [
    {
      "vas": "vas6"
    },
    {
      "vas": "vas6"
    }
  ]
}
```

