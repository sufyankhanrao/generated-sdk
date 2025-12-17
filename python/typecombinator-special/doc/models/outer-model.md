
# Outer Model

This class contains enum types in oneOf/anyOf cases.

## Structure

`OuterModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | [InnerModel1](../../doc/models/inner-model-1.md) \| [InnerModel2](../../doc/models/inner-model-2.md) | Required | This is a container for one-of cases. |

## Example (as JSON)

```json
{
  "model": {
    "country": "Cameroon"
  }
}
```

