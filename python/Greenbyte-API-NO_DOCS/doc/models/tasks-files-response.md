
# Tasks Files Response

## Structure

`TasksFilesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `file_id` | `int` | Required | The id of a file.<br><br>**Constraints**: `>= 1` |
| `file_name` | `str` | Required | - |
| `timestamp_uploaded` | `datetime` | Required | The timestamp when the file was uploaded. |
| `uploaded_by` | [`User`](../../doc/models/user.md) | Required | - |
| `description` | `str` | Optional | - |
| `category` | [`TaskFileCategoryEnum`](../../doc/models/task-file-category-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "fileId": 130,
  "fileName": "250.png",
  "timestampUploaded": "01/08/2020 00:00:00",
  "uploadedBy": {
    "firstName": "firstName0",
    "lastName": "lastName8"
  },
  "description": "A photo of the nacelle",
  "category": "Pictures"
}
```

