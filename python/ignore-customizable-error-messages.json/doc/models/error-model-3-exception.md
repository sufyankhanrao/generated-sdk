
# Error Model 3 Exception

## Structure

`ErrorModel3Exception`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `server_message` | `str` | Required | Represents the server's exception message |
| `server_code` | `int` | Required | Represents the server's error code |
| `secret_message_for_endpoint` | `str` | Required | Represents the specific endpoint info |

## Example (as JSON)

```json
{
  "ServerMessage": "ServerMessage6",
  "ServerCode": 192,
  "SecretMessageForEndpoint": "SecretMessageForEndpoint6"
}
```

