
# Sort Partner

Sorting order for the search results of leads source.

## Structure

`SortPartner`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field_name` | [`FieldName3Enum`](../../doc/models/field-name-3-enum.md) | Optional | List of fields for sorting the result set. The result set is sorted in the given order. <br> By default sorting will be done by PROCESS_MONTH . |
| `order_by` | [`OrderByEnum`](../../doc/models/order-by-enum.md) | Optional | Type of Ordering. Default - ASC |

## Example (as JSON)

```json
{
  "fieldName": "PROCESS_MONTH",
  "orderBy": "ASC"
}
```

