
# Field

## Structure

`Field`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | - |
| `x` | `int` | Optional | - |
| `y` | `int` | Optional | - |
| `width` | `int` | Optional | - |
| `height` | `int` | Optional | - |
| `page_number` | `int` | Optional | - |
| `document_number` | `int` | Optional | - |
| `hide_field_name_for_recipients` | `bool` | Optional | - |
| `name` | `str` | Optional | - |
| `tooltip` | `str` | Optional | - |
| `value` | `str` | Optional | - |
| `required` | `bool` | Optional | - |
| `character_limit` | `int` | Optional | - |
| `party` | `int` | Optional | - |
| `font_size` | `int` | Optional | - |
| `font_color` | `str` | Optional | - |
| `options` | `List[str]` | Optional | - |
| `tab_order` | `int` | Optional | - |
| `group` | `str` | Optional | - |
| `multicheck` | `bool` | Optional | - |
| `checked` | `bool` | Optional | - |
| `hide_checkbox_border` | `bool` | Optional | - |
| `date_format` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "type": "text",
  "x": 348,
  "y": 157,
  "width": 171,
  "height": 28,
  "pageNumber": 1,
  "documentNumber": 1,
  "hideFieldNameForRecipients": true,
  "name": "Number(fillable) d0107804-ce35-45e8-8d06-a26d67f0d9bd",
  "tooltip": "First Name",
  "required": false,
  "characterLimit": 100,
  "party": 1,
  "fontSize": 12,
  "fontColor": "#000000",
  "options": [
    "None"
  ],
  "tabOrder": 1,
  "multicheck": true,
  "checked": true,
  "hideCheckboxBorder": true,
  "dateFormat": "MM-DD-YYYY"
}
```

