
# Envelope Fields Update

## Structure

`EnvelopeFieldsUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `folder_id` | `int` | Required | - |
| `custom_field_1` | [`CustomField`](../../doc/models/custom-field.md) | Optional | - |
| `custom_field_2` | [`CustomField`](../../doc/models/custom-field.md) | Optional | - |
| `fields` | `Any` | Required | - |

## Example (as JSON)

```json
{
  "folderId": 198,
  "fields": {
    "FIELD1_NAME": "VALUE",
    "FIELD2_NAME": "VALUE"
  },
  "custom_field1": {
    "name": "name2",
    "value": "value4"
  },
  "custom_field2": {
    "name": "name2",
    "value": "value4"
  }
}
```

