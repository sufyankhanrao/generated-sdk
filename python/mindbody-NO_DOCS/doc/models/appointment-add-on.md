
# Appointment Add On

## Structure

`AppointmentAddOn`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The ID of this add-on. |
| `name` | `str` | Optional | The name of this add-on. |
| `num_deducted` | `int` | Optional | The number of sessions that this add-on deducts from the pricing option used to pay for this add-on. |
| `category_id` | `int` | Optional | This ID of this add-on’s category. |
| `category` | `str` | Optional | The name of this add-on’s category. |

## Example (as JSON)

```json
{
  "Id": 18,
  "Name": "Name0",
  "NumDeducted": 98,
  "CategoryId": 68,
  "Category": "Category8"
}
```

