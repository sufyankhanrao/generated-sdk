
# Pricing Element

Array of pricing items from template to be changed.

## Structure

`PricingElement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `int` | Required | Item ID.<br><br>**Constraints**: `>= 0` |
| `item_value` | `float` | Required | Item value.<br><br>**Constraints**: `>= 0` |
| `item_term` | `int` | Required | Item term.<br><br>**Constraints**: `>= 0` |
| `item_description` | `str` | Optional | Item desciption.<br><br>**Constraints**: *Maximum Length*: `100` |

## Example (as JSON)

```json
{
  "item_id": 5,
  "item_value": 1.5,
  "item_term": 2,
  "item_description": "AVS fee."
}
```

