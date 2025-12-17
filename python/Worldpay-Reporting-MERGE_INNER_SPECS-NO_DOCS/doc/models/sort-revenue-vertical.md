
# Sort Revenue Vertical

## Structure

`SortRevenueVertical`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field_name` | [`FieldName11Enum`](../../doc/models/field-name-11-enum.md) | Optional | List of fields for sorting the result set. The result set is sorted in the given order. <br> By default sorting will be done by PROCESS_MONTH. |
| `order_by` | [`OrderByEnum`](../../doc/models/order-by-enum.md) | Optional | Way of ordering the result. Default - ASC. |

## Example (as JSON)

```json
{
  "fieldName": "PROCESS_MONTH",
  "orderBy": "ASC"
}
```

