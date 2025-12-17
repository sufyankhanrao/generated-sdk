
# Authentication Result

*This model accepts additional fields of type Any.*

## Structure

`AuthenticationResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `access_token` | `str` | Required | - |
| `expires_in` | `int` | Required | - |
| `id_token` | `str` | Required | - |
| `refresh_token` | `str` | Required | - |
| `scope` | `str` | Required | - |
| `token_type` | `str` | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
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
}
```

