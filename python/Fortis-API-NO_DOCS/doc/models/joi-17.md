
# Joi 17

## Structure

`Joi17`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `conditions` | [Conditions16](../../doc/models/conditions-16.md) \| [Conditions171](../../doc/models/conditions-171.md) \| [Conditions4](../../doc/models/conditions-4.md) \| [Conditions41](../../doc/models/conditions-41.md) \| [Conditions42](../../doc/models/conditions-42.md) \| [Conditions43](../../doc/models/conditions-43.md) \| None | Optional | This is a container for any-of cases. |

## Example (as JSON)

```json
{
  "conditions": {
    "method": "xor",
    "values": "account_number"
  }
}
```

