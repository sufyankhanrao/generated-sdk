
# Get Sales Reps Request

This is the request class for the get sales reps API

## Structure

`GetSalesRepsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sales_rep_numbers` | `List[int]` | Optional | This is the list of the sales rep numbers for which the salesrep data will be fetched. |
| `active_only` | `bool` | Optional | When `true`, will return only active reps data.<br>Default : **false** |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "SalesRepNumbers": [
    62,
    63,
    64
  ],
  "ActiveOnly": false,
  "Limit": 8,
  "Offset": 74
}
```

