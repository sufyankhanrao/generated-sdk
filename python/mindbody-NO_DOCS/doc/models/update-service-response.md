
# Update Service Response

A response from the Update Services API method.

## Structure

`UpdateServiceResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `services` | [`List[Service]`](../../doc/models/service.md) | Optional | List of services as response |

## Example (as JSON)

```json
{
  "Services": [
    {
      "Price": 224.3,
      "OnlinePrice": 2.82,
      "TaxIncluded": 75.84,
      "ProgramId": 204,
      "TaxRate": 192.34
    },
    {
      "Price": 224.3,
      "OnlinePrice": 2.82,
      "TaxIncluded": 75.84,
      "ProgramId": 204,
      "TaxRate": 192.34
    },
    {
      "Price": 224.3,
      "OnlinePrice": 2.82,
      "TaxIncluded": 75.84,
      "ProgramId": 204,
      "TaxRate": 192.34
    }
  ]
}
```

