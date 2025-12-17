
# Date and Amount

Date, description, and amount. When used in 1098-Q, description is optional

*This model accepts additional fields of type Any.*

## Structure

`DateAndAmount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date` | `date` | Optional | Date of amount. When used in 1098-Q, date of last payment in month |
| `description` | `str` | Optional | Description of amount. When used in 1098-Q, may use MonthAbbreviation |
| `amount` | `float` | Optional | Amount of payment or receipt. When used in 1098-Q, monthly total |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "date": "2021-07-15",
  "description": "description4",
  "amount": 231.46,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

