
# Enums Allow Additional Response

## Structure

`EnumsAllowAdditionalResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `numeric_enum` | [`NumericEnum`](../../doc/models/numeric-enum.md) | Optional | - |
| `string_enum` | [`StringEnum`](../../doc/models/string-enum.md) | Optional | - |
| `const_value` | `str` | Required, Constant | **Value**: `"five"` |

## Example (as JSON)

```json
{
  "const_value": "five",
  "numeric_enum": 3,
  "string_enum": "one"
}
```

