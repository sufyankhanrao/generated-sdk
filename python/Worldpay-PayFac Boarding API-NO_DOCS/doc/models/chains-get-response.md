
# Chains Get Response

## Structure

`ChainsGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `chains_codes` | [`List[Chain]`](../../doc/models/chain.md) | Optional | - |

## Example (as JSON)

```json
{
  "correlationId": "0acfc8fe1816421ab7376337d5729b94",
  "httpStatusCode": "200",
  "httpStatusMessage": "OK",
  "chainsCodes": [
    {
      "chainCode": "chainCode6",
      "chainName": "chainName2"
    },
    {
      "chainCode": "chainCode6",
      "chainName": "chainName2"
    }
  ]
}
```

