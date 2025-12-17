
# Response Onboarding

## Structure

`ResponseOnboarding`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type45Enum`](../../doc/models/type-45-enum.md) | Optional | Resource Type<br><br>**Default**: `"Onboarding"` |
| `data` | [`Data12`](../../doc/models/data-12.md) | Optional | - |

## Example (as JSON)

```json
{
  "type": "Onboarding",
  "data": {
    "parent_id": "parent_id6",
    "primary_principal": {
      "first_name": "first_name6",
      "last_name": "last_name4",
      "middle_name": "middle_name6",
      "title": "title2",
      "date_of_birth": "date_of_birth2"
    },
    "template_code": "template_code0",
    "email": "email6",
    "dba_name": "dba_name8"
  }
}
```

