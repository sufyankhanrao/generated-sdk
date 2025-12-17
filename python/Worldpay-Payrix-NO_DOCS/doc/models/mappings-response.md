
# Mappings Response

## Structure

`MappingsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `login` | `str` | Optional | The Login that owns this resource. |
| `name` | `str` | Optional | Name of Mappings. |
| `description` | `str` | Optional | A description of this Mapping. |
| `input` | `str` | Optional | A JSON document that describes the input fields that should be mapped.<br>This field is stored as a text string and must be between 1 and 5000 characters long. |
| `output` | `str` | Optional | A JSON document that describes the fields that should appear in the output, after the input fields have been mapped.<br>This field is stored as a text string and must be between 1 and 5000 characters long. |
| `namespace` | `str` | Optional | A valid URL that represents the XML namespace of the input and output documents.<br>This field is stored as a text string and must be between 1 and 100 characters long. |

## Example (as JSON)

```json
{
  "id": "id0",
  "created": "created0",
  "modified": "modified8",
  "creator": "String9",
  "modifier": "modifier4"
}
```

