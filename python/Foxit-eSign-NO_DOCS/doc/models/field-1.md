
# Field 1

## Structure

`Field1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Required | - |
| `x` | `int` | Required | - |
| `y` | `int` | Required | - |
| `width` | `int` | Required | - |
| `height` | `int` | Required | - |
| `page_number` | `int` | Required | - |
| `tab_order` | `int` | Optional | - |
| `party` | `int` | Required | - |
| `name` | `str` | Optional | - |
| `tooltip` | `str` | Optional | - |
| `value` | `str` | Optional | - |
| `required` | `bool` | Optional | - |
| `character_limit` | `int` | Optional | - |
| `font_size` | `int` | Optional | - |
| `font_color` | `str` | Optional | - |
| `validation` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "type": "text",
  "x": 100,
  "y": 50,
  "width": 60,
  "height": 20,
  "pageNumber": 1,
  "tabOrder": 1,
  "party": 1,
  "name": "optional name",
  "value": "Name",
  "required": true,
  "characterLimit": 100,
  "fontSize": 12,
  "fontColor": "#000000",
  "validation": "Letters",
  "tooltip": "tooltip6"
}
```

