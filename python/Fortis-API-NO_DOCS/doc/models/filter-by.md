
# Filter By

## Structure

`FilterBy`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Required | Resource key to filter by |
| `operator` | [Operator1](../../doc/models/operator-1-enum.md) | Required | This is a container for one-of cases. |
| `value` | float \| str \| bool | Required | This is a container for one-of cases. |

## Example (as JSON)

```json
{
  "key": "first_name",
  "operator": "<=",
  "value": "Fred"
}
```

