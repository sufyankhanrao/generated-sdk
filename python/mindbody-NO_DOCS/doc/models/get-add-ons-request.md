
# Get Add Ons Request

## Structure

`GetAddOnsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `staff_id` | `int` | Optional | Filter to add-ons only performed by this staff member. |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "StaffId": 98,
  "Limit": 58,
  "Offset": 124
}
```

