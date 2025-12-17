
# Update Sale Date Request

Update Sales Date Request Model

## Structure

`UpdateSaleDateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sale_id` | `int` | Optional | The Sale ID for which saleDate needs to be updated. This is the `Sale[].Id` returned from GET Sales. |
| `sale_date` | `datetime` | Optional | The sale date which needs to be modified. |

## Example (as JSON)

```json
{
  "SaleID": 100,
  "SaleDate": "2016-03-13T12:52:32.123Z"
}
```

