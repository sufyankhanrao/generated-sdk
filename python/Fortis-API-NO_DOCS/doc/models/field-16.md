
# Field 16

## Structure

`Field16`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | id |
| `label` | `str` | Optional | Label |
| `field_type` | `str` | Optional | Field Type |
| `position` | `List[str]` | Optional | Position<br><br>**Constraints**: *Minimum Items*: `1` |
| `required` | `bool` | Optional | Required |
| `readonly` | `bool` | Optional | Read Only |
| `visible` | `bool` | Optional | Visible |
| `value` | `str` | Optional | Value |

## Example (as JSON)

```json
{
  "id": "transaction_amount",
  "label": "Header",
  "field_type": "heading",
  "position": [
    "1",
    "0",
    "1",
    "1"
  ],
  "required": true,
  "readonly": true,
  "visible": true
}
```

