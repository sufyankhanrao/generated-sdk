
# Holds Model With Oaf Field

This class contains a field of type model that contains a field.

## Structure

`HoldsModelWithOafField`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `inner_model` | [`HoldsOafField`](../../doc/models/holds-oaf-field.md) | Required | - |

## Example (as JSON)

```json
{
  "innerModel": {
    "anyOfDogCat": {
      "bark": false,
      "age": 140,
      "cute": false,
      "breed": "breed0"
    },
    "innerModel": {
      "innerModel": {}
    }
  }
}
```

