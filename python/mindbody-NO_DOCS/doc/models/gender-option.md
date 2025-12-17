
# Gender Option

A gender option available at a site

## Structure

`GenderOption`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The id of the gender option. |
| `name` | `str` | Optional | The value that describes this gender option. |
| `is_active` | `bool` | Optional | When `true`, this indicates that the gender option is active and may be assigned to a client. |
| `is_default` | `bool` | Optional | When true, this indicates that this is the default gender option at the site. |

## Example (as JSON)

```json
{
  "Id": 134,
  "Name": "Name4",
  "IsActive": false,
  "IsDefault": false
}
```

