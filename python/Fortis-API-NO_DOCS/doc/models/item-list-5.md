
# Item List 5

## Structure

`ItemList5`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Item's Name, must be unique on the list<br><br>**Constraints**: *Maximum Length*: `100` |
| `amount` | `int` | Optional | Item's Amount<br><br>**Constraints**: `>= -999999999`, `<= 999999999` |

## Example (as JSON)

```json
{
  "name": "Bread",
  "amount": 2015
}
```

