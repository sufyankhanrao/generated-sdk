
# Issue Response

POST UserToken/Issue successful response

## Structure

`IssueResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `token_type` | `str` | Optional | - |
| `access_token` | `str` | Optional | The authentication token value. |
| `expires` | `datetime` | Optional | Token expiration in UTC. |
| `user` | [`User`](../../doc/models/user.md) | Optional | - |

## Example (as JSON)

```json
{
  "TokenType": "TokenType2",
  "AccessToken": "AccessToken6",
  "Expires": "2016-03-13T12:52:32.123Z",
  "User": {
    "Id": 116,
    "FirstName": "FirstName8",
    "LastName": "LastName2",
    "Type": "Type6"
  }
}
```

