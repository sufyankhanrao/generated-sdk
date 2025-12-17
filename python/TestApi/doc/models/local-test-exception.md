
# Local Test Exception

To test specific local exceptions.

## Structure

`LocalTestException`

## Inherits From

[`GlobalTestException`](../../doc/models/global-test-exception.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `secret_message_for_endpoint` | `str` | Required | Represents the specific endpoint info |
| `error_days` | [`Days1Enum`](../../doc/models/days-1-enum.md) | Optional | Represents the optional error days<br><br>**Default**: `'Friday'` |

## Example (as JSON)

```json
{
  "SecretMessageForEndpoint": "SecretMessageForEndpoint8",
  "errorDays": "Friday",
  "ServerMessage": "ServerMessage8",
  "ServerCode": 212
}
```

