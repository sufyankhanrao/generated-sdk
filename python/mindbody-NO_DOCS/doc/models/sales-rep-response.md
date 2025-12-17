
# Sales Rep Response

This is the sales rep DTO

## Structure

`SalesRepResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The unique Id of the sales rep |
| `first_name` | `str` | Optional | The firstname of the sales rep |
| `last_name` | `str` | Optional | The lastname of the sales rep |
| `sales_rep_numbers` | `List[int]` | Optional | The sales rep Ids that are assigned to the rep |

## Example (as JSON)

```json
{
  "Id": 160,
  "FirstName": "FirstName8",
  "LastName": "LastName8",
  "SalesRepNumbers": [
    84,
    85
  ]
}
```

