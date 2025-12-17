
# Get Add Ons Response

Get AddOns Response Model

## Structure

`GetAddOnsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `add_ons` | [`List[AppointmentAddOn]`](../../doc/models/appointment-add-on.md) | Optional | A list of available add-ons. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "AddOns": [
    {
      "Id": 138,
      "Name": "Name2",
      "NumDeducted": 22,
      "CategoryId": 52,
      "Category": "Category4"
    }
  ]
}
```

