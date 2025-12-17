
# Forgot Password Input Model

*This model accepts additional fields of type Any.*

## Structure

`ForgotPasswordInputModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `str` | Required | Registered email to recieve password. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "email": "abc@abc.com",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

