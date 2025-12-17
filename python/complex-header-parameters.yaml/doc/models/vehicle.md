
# Vehicle

## Structure

`Vehicle`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `make` | `str` | Required | - |
| `model` | `str` | Required | - |
| `year` | `int` | Required | - |
| `engine` | [`Engine`](../../doc/models/engine.md) | Required | - |

## Example (as JSON)

```json
{
  "make": "Toyota",
  "model": "Camry",
  "year": 2022,
  "engine": {
    "horsepower": 3000,
    "fuelType": "Petrol"
  }
}
```

