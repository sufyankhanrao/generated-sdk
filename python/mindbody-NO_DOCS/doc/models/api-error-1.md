
# Api Error 1

## Structure

`ApiError1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `str` | Optional | The text of the message. Each message is specific to the error that caused it.<br>For example, if the the error type is `InvalidFileFormat`,<br>the message could say "The photo you attempted to upload is not a supported file type." |
| `code` | `str` | Optional | The type of error that occurred, for example, `ClientNotFound` or `InvalidClassId`. |

## Example (as JSON)

```json
{
  "Message": "Message4",
  "Code": "Code8"
}
```

