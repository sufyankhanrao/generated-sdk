
# Description and Amount

Description and amount pair used on IRS W-2, etc.

*This model accepts additional fields of type Any.*

## Structure

`DescriptionAndAmount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Description |
| `amount` | `float` | Optional | Amount |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "description": "description0",
  "amount": 4.82,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

