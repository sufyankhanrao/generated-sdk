
# Sort Leads Count Category

Sorting order for the search results of leads category.

## Structure

`SortLeadsCountCategory`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field_name` | [`FieldName22Enum`](../../doc/models/field-name-22-enum.md) | Optional | List of fields for sorting the result set. The result set is sorted in the given order <br> By default sorting will be done by CATEGORY.<br><br>**Constraints**: *Maximum Length*: `8` |
| `order_by` | [`OrderByEnum`](../../doc/models/order-by-enum.md) | Optional | Type of ordering. <BR> ASC stands for ascending order. <BR> DESC stands for descending order.<br><br>**Constraints**: *Maximum Length*: `4` |

## Example (as JSON)

```json
{
  "fieldName": "CATEGORY",
  "orderBy": "ASC"
}
```

