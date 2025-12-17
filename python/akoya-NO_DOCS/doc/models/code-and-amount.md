
# Code and Amount

Code and amount pair used on IRS W-2, K-1, etc.

*This model accepts additional fields of type Any.*

## Structure

`CodeAndAmount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | Code |
| `amount` | `float` | Optional | Amount |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "code": "code2",
  "amount": 40.84,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

