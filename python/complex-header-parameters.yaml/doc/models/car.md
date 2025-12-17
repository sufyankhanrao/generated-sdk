
# Car

## Structure

`Car`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `make` | `str` | Required | - |
| `model` | `str` | Required | - |
| `doors` | `int` | Required | - |
| `engine` | [`Engine`](../../doc/models/engine.md) | Required | - |

## Example (as JSON)

```json
{
  "make": "Toyota",
  "model": "Yaris",
  "doors": 2,
  "engine": {
    "horsepower": 1500,
    "fuelType": "Petrol"
  }
}
```

