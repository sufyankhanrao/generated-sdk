
# Sort Partner Vertical

Sorting order for the search results of signed deals summary.

## Structure

`SortPartnerVertical`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field_name` | [`FieldName5Enum`](../../doc/models/field-name-5-enum.md) | Optional | List of fields for sorting the result set. The result set is sorted in the given order. <br> By default sorting will be done by VERTICAL. |
| `order_by` | [`OrderByEnum`](../../doc/models/order-by-enum.md) | Optional | Way of ordering the result. Default - ASC. |

## Example (as JSON)

```json
{
  "fieldName": "VERTICAL",
  "orderBy": "ASC"
}
```

