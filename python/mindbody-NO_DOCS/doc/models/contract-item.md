
# Contract Item

## Structure

`ContractItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of the item. |
| `name` | `str` | Optional | The name of the item. |
| `description` | `str` | Optional | A description of the item. |
| `mtype` | `str` | Optional | The type of the item. |
| `price` | `float` | Optional | The price of the item. |
| `quantity` | `int` | Optional | The quantity of the item. |
| `one_time_item` | `bool` | Optional | When `true`, indicates that the item is charged only once.<br /><br>When `false`, indicates that the item is charged multiple times. |

## Example (as JSON)

```json
{
  "Id": "Id6",
  "Name": "Name0",
  "Description": "Description6",
  "Type": "Type0",
  "Price": 54.6
}
```

