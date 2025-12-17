
# Error Item

## Structure

`ErrorItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `int` | Optional | The error code associated with a particular error. |
| `severity` | `int` | Optional | The severity level of a particular error.<br>Possible values are '0' (informational), '1' (warning), '2' (error) and '4' (failure). |
| `msg` | `str` | Optional | The message associated with a particular error. |
| `field` | `str` | Optional | Field name associated with error. |
| `error_code` | `str` | Optional | An identifying string code for this error. |

## Example (as JSON)

```json
{
  "code": 44,
  "severity": 150,
  "msg": "msg4",
  "field": "field2",
  "errorCode": "errorCode4"
}
```

