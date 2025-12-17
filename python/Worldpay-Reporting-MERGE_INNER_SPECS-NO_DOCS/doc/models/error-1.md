
# Error 1

Error Message

## Structure

`Error1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `str` | Optional | Code of error<br><br>**Constraints**: *Maximum Length*: `256` |
| `error_message` | `str` | Optional | Error Message<br><br>**Constraints**: *Maximum Length*: `256` |
| `target` | `str` | Optional | Error Target<br><br>**Constraints**: *Maximum Length*: `256` |

## Example (as JSON)

```json
{
  "errorCode": "ERROR_CODE",
  "errorMessage": "Error message here.",
  "target": "Target field name."
}
```

