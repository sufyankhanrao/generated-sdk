
# Error Exception

Error details.

## Structure

`ErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `str` | Optional | Indicates the error of code<br><br>**Constraints**: *Maximum Length*: `256` |
| `error_type` | `str` | Optional | Indicates the type of error<br><br>**Constraints**: *Maximum Length*: `256` |
| `error_message` | `str` | Optional | Indicates the message error<br><br>**Constraints**: *Maximum Length*: `256` |
| `target` | `str` | Optional | Indicates the target<br><br>**Constraints**: *Maximum Length*: `256` |

## Example (as JSON)

```json
{
  "errorCode": "ERROR_CODE",
  "errorType": "Error Type here",
  "errorMessage": "Error message here.",
  "target": "Target field name."
}
```

