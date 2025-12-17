
# Change Password Output Model

*This model accepts additional fields of type Any.*

## Structure

`ChangePasswordOutputModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `success` | `bool` | Required | Returns ‘true’ when successful and ‘false’ when failed. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "success": false,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

