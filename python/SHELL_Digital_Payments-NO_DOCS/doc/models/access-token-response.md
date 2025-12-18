
# Access Token Response

## Structure

`AccessTokenResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `access_token` | `str` | Optional | It is the token used for the requests that required an authenticated user. This will be used for all the callback URLs. |
| `expires_in` | `str` | Optional | validity of the access token in seconds |
| `token_type` | `str` | Optional | Type of token provided<br><br>**Default**: `'Bearer'` |

## Example (as JSON)

```json
{
  "access_token": "zn2GcAQugJQRJXcGXsmHZ8LMqVde",
  "expires_in": "3599",
  "token_type": "Bearer"
}
```

