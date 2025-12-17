
# Multiple Enums

This class contains enum types in oneOf/anyOf cases.

## Structure

`MultipleEnums`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `daysvs_string` | [Days](../../doc/models/days-enum.md) \| str | Required | This is a container for any-of cases. |
| `all_one_of` | [Days](../../doc/models/days-enum.md) \| [MonthName](../../doc/models/month-name-enum.md) \| [MonthNumber](../../doc/models/month-number-enum.md) | Required | This is a container for one-of cases. |
| `all_outer_array` | List[[Days](../../doc/models/days-enum.md) \| [MonthName](../../doc/models/month-name-enum.md) \| [MonthNumber](../../doc/models/month-number-enum.md)] | Required | This is List of a container for one-of cases. |
| `enumvs_array` | [Days](../../doc/models/days-enum.md) \| List[[Days](../../doc/models/days-enum.md)] | Required | This is a container for any-of cases. |
| `mapvs_array` | Dict[str, [Days](../../doc/models/days-enum.md)] \| List[[Days](../../doc/models/days-enum.md)] | Required | This is a container for any-of cases. |

## Example (as JSON)

```json
{
  "daysvsString": "Wednesday",
  "allOneOf": "Thursday",
  "allOuterArray": [
    "Friday",
    "Saturday",
    "Sunday"
  ],
  "enumvsArray": "Friday",
  "mapvsArray": {
    "key0": "Tuesday",
    "key1": "Wednesday",
    "key2": "Thursday"
  }
}
```

