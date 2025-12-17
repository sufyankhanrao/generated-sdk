
# M400 Error

## Structure

`M400Error`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `str` | Optional | - |
| `error_message` | `str` | Optional | - |
| `target` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "errorCode": "PARAMETER_VALIDATION_ERROR",
  "errorMessage": "<Field Name> exceeds maximum length",
  "target": "<Field Name>"
}
```

