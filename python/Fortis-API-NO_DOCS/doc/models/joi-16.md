
# Joi 16

## Structure

`Joi16`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `conditions` | [Conditions16](../../doc/models/conditions-16.md) \| [Conditions161](../../doc/models/conditions-161.md) \| [Conditions4](../../doc/models/conditions-4.md) \| [Conditions41](../../doc/models/conditions-41.md) \| [Conditions42](../../doc/models/conditions-42.md) \| [Conditions43](../../doc/models/conditions-43.md) \| None | Optional | This is a container for any-of cases. |

## Example (as JSON)

```json
{
  "conditions": {
    "method": "xor",
    "values": "account_number"
  }
}
```

