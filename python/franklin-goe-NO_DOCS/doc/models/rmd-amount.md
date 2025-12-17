
# Rmd Amount

*This model accepts additional fields of type Any.*

## Structure

`RmdAmount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `float` | Required | - |
| `member_id` | `str` | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "amount": 176.32,
  "memberId": "memberId0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

