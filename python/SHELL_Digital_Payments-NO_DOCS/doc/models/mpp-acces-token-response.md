
# Mpp Acces Token Response

## Structure

`MppAccesTokenResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `access_token` | `str` | Optional | It is the token used in the requests that required to authenticate an user. |
| `token_type` | `str` | Optional | type of token provided<br><br>**Default**: `'bearer'` |
| `expires_in` | `int` | Optional | validity of the access token in seconds |
| `scope` | `str` | Optional | scope for the authentication protocol<br><br>**Default**: `'basic openid'` |

## Example (as JSON)

```json
{
  "access_token": "zn2GcAQugJQRJXcGXsmHZ8LMqVde",
  "token_type": "bearer",
  "expires_in": 3599,
  "scope": "basic openid"
}
```

