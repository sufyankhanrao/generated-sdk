
# Sort Results By

The sort results by fields are used in request to establish the sort order for the data to be returned in ascending or descending order.

## Structure

`SortResultsBy`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field_name` | [`FieldNameEnum`](../../doc/models/field-name-enum.md) | Optional | Fields to sort the search results. <br> Default:OPEN_DATE |
| `order_by` | [`OrderByEnum`](../../doc/models/order-by-enum.md) | Optional | Decide the sorting order by ASC or DESC. <br> Default:ASC |

## Example (as JSON)

```json
{
  "fieldName": "BATCH_STATUS",
  "orderBy": "DESC"
}
```

