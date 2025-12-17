
# Month and Amount

Month and amount pair used on IRS Form 1099-K, etc.

*This model accepts additional fields of type Any.*

## Structure

`MonthAndAmount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `month` | [`MonthAbbreviation`](../../doc/models/month-abbreviation.md) | Optional | Month |
| `amount` | `float` | Optional | Amount |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "month": "SEP",
  "amount": 97.94,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

