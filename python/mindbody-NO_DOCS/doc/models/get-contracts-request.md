
# Get Contracts Request

## Structure

`GetContractsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contract_ids` | `List[int]` | Optional | When included, the response only contains details about the specified contract IDs. |
| `sold_online` | `bool` | Optional | When `true`, the response only contains details about contracts and AutoPay options that can be sold online.<br>When `false`, all contracts are returned.<br>Default: **false** |
| `location_id` | `int` | Required | The ID of the location that has the requested contracts and AutoPay options. |
| `consumer_id` | `int` | Optional | The ID of the client. |
| `promo_code` | `str` | Optional | PromoCode to apply |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ContractIds": [
    10
  ],
  "SoldOnline": false,
  "LocationId": 104,
  "ConsumerId": 74,
  "PromoCode": "PromoCode0",
  "Limit": 154
}
```

