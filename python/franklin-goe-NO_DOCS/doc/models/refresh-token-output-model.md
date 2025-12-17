
# Refresh Token Output Model

*This model accepts additional fields of type Any.*

## Structure

`RefreshTokenOutputModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authentication_result` | [`AuthenticationResult`](../../doc/models/authentication-result.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "AuthenticationResult": {
    "AccessToken": "AccessToken8",
    "ExpiresIn": 78,
    "IdToken": "IdToken0",
    "RefreshToken": "RefreshToken4",
    "Scope": "Scope8",
    "TokenType": "TokenType0",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

