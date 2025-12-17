
# Error Details

## Structure

`ErrorDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | Error code representing the error encountered |
| `title` | `str` | Optional | Error type description |
| `detail` | `str` | Optional | Detailed inforamtion about the error |
| `additional_info` | `Dict[str, str]` | Optional | Applicable when more details related to error to be returned |

## Example (as JSON)

```json
{
  "Code": "Code2",
  "Title": "Title8",
  "Detail": "Detail4",
  "AdditionalInfo": {
    "key0": "AdditionalInfo2"
  }
}
```

