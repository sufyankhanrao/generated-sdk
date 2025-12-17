
# Open Order Entity

Information on an open order.

*This model accepts additional fields of type Any.*

## Structure

`OpenOrderEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `str` | Optional | Long term persistent identity of the order. Id for this order transaction. |
| `security_id` | `str` | Optional | Unique identifier of the security. |
| `security_id_type` | [`SecurityIdType`](../../doc/models/security-id-type.md) | Optional | Security identifier type |
| `symbol` | `str` | Optional | Market symbol |
| `description` | `str` | Optional | Description of order |
| `units` | `float` | Optional | Number of units (shares, bonds, etc.) |
| `order_type` | [`OrderType`](../../doc/models/order-type.md) | Optional | Type of order. |
| `order_date` | `datetime` | Optional | Order date |
| `unit_price` | `float` | Optional | Unit price |
| `unit_type` | [`UnitType`](../../doc/models/unit-type.md) | Optional | Type of unit. |
| `order_duration` | [`OrderDuration`](../../doc/models/order-duration.md) | Optional | This order is good for DAY, GOODTILLCANCEL, IMMEDIATE |
| `sub_account` | [`SubAccount`](../../doc/models/sub-account.md) | Optional | - |
| `limit_price` | `float` | Optional | Limit Price |
| `stop_price` | `float` | Optional | Stop price |
| `inv_401_k_source` | [`Inv401KSource`](../../doc/models/inv-401-k-source.md) | Optional | For 401(k) accounts, source of money for this order. Default if not present is OTHERNONVEST. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "orderId": "orderId4",
  "securityId": "securityId6",
  "securityIdType": "VALOR",
  "symbol": "symbol0",
  "description": "description2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

