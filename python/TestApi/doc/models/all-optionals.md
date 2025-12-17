
# All Optionals

## Structure

`AllOptionals`

## Inherits From

[`StringAsOptional`](../../doc/models/string-as-optional.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `optional_numbers` | [`List[NumberAsOptional]`](../../doc/models/number-as-optional.md) | Optional | - |
| `optional_long` | [`LongAsOptional`](../../doc/models/long-as-optional.md) | Optional | - |
| `optional_precision` | [`PrecisionAsOptional`](../../doc/models/precision-as-optional.md) | Optional | - |

## Example (as JSON)

```json
{
  "string": "test",
  "id": 234,
  "optionalNumbers": [
    null
  ],
  "optionalLong": null,
  "optionalPrecision": null
}
```

