
# Holds Oaf Field

This class contains special combination of required and optional typed models in oneOf/anyOf cases.

## Structure

`HoldsOafField`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `any_of_dog_cat` | [Dog](../../doc/models/dog.md) \| [Cat](../../doc/models/cat.md) | Required | This is a container for any-of cases. |
| `inner_model` | [`HoldsModelWithOafField`](../../doc/models/holds-model-with-oaf-field.md) | Optional | - |

## Example (as JSON)

```json
{
  "anyOfDogCat": {
    "bark": false,
    "age": 140,
    "cute": false,
    "breed": "breed0"
  },
  "innerModel": {
    "innerModel": {
      "anyOfDogCat": {
        "bark": false,
        "age": 140,
        "cute": false,
        "breed": "breed0"
      },
      "innerModel": {}
    }
  }
}
```

