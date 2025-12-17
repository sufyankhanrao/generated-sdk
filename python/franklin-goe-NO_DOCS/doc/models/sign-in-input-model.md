
# Sign in Input Model

*This model accepts additional fields of type Any.*

## Structure

`SignInInputModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `str` | Required | Email to login. |
| `password` | `str` | Required | Password to login. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "email": "abc@abc.com",
  "password": "Gpattm@#124",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

