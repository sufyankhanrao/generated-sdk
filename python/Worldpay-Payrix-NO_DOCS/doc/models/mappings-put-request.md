
# Mappings Put Request

## Structure

`MappingsPutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `login` | `str` | Optional | The Login that owns this resource. |
| `name` | `str` | Optional | Name of Mappings. |
| `description` | `str` | Optional | A description of this Mapping. |
| `input` | `str` | Optional | A JSON document that describes the input fields that should be mapped.<br>This field is stored as a text string and must be between 1 and 5000 characters long. |
| `output` | `str` | Optional | A JSON document that describes the fields that should appear in the output, after the input fields have been mapped.<br>This field is stored as a text string and must be between 1 and 5000 characters long. |
| `namespace` | `str` | Optional | A valid URL that represents the XML namespace of the input and output documents.<br>This field is stored as a text string and must be between 1 and 100 characters long. |

## Example (as JSON)

```json
{
  "login": "t1_log_63d25f51ea7ddb271d78304",
  "name": "Test1",
  "description": "Test1",
  "input": "{\\\"mappingsCreate\\\":{\\\"requests\\\":[{\\\"name\\\":{\\\"__path__\\\":\\\"mappings2Create;mappings2Request;name\\\"}}]}}",
  "output": "{\\\"mappings2CreateResponse\\\":{\\\"mappings2Responses\\\":[{\\\"name\\\":{\\\"__path__\\\":\\\"mappingsCreateResponse;requests;[];name\\\"}}]}}",
  "namespace": "XML namespace of input and output"
}
```

