
# Factoring Schema

This class contains special combination of required and optional typed models in oneOf/anyOf cases.

## Structure

`FactoringSchema`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `any_of_dog_cat` | [Dog](../../doc/models/dog.md) \| [Cat](../../doc/models/cat.md) | Required | This is a container for any-of cases. |
| `any_of_cat_dog` | [Cat](../../doc/models/cat.md) \| [Dog](../../doc/models/dog.md) | Required | This is a container for any-of cases. |
| `any_of_squirrel_dog` | [Squirrel](../../doc/models/squirrel.md) \| [Dog](../../doc/models/dog.md) | Required | This is a container for any-of cases. |
| `one_of_cat_dog_rabbit` | [Cat](../../doc/models/cat.md) \| [Dog](../../doc/models/dog.md) \| [Rabbit](../../doc/models/rabbit.md) | Required | This is a container for one-of cases. |
| `one_of_vehicles` | [VehicleA](../../doc/models/vehicle-a.md) \| [VehicleB](../../doc/models/vehicle-b.md) | Required | This is a container for one-of cases. |

## Example (as JSON)

```json
{
  "anyOfDogCat": {
    "bark": false,
    "age": 140,
    "cute": false,
    "breed": "breed0"
  },
  "anyOfCatDog": {
    "bark": false,
    "age": 238,
    "cute": false
  },
  "anyOfSquirrelDog": {
    "squeak": false,
    "childern": 22
  },
  "oneOfCatDogRabbit": {
    "bark": false,
    "age": 238,
    "cute": false
  },
  "oneOfVehicles": {
    "NumberOfTyres": "NumberOfTyres8",
    "model": "model8"
  }
}
```

