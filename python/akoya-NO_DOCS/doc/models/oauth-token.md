
# Oauth Token

OAuth 2 Authorization endpoint response

*This model accepts additional fields of type Any.*

## Structure

`OauthToken`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id_token` | `str` | Required | ID Token |
| `token_type` | `str` | Required | Type of access token |
| `expires_in` | `int` | Optional | Time in seconds before the access token expires |
| `scope` | `str` | Optional | List of scopes granted<br>This is a space-delimited list of strings. |
| `expiry` | `int` | Optional | Time of token expiry as unix timestamp (UTC) |
| `refresh_token` | `str` | Optional | Refresh token<br>Used to get a new access token when it expires. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "id_token": "id_token6",
  "token_type": "token_type6",
  "expires_in": 74,
  "scope": "scope6",
  "expiry": 88,
  "refresh_token": "refresh_token6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

