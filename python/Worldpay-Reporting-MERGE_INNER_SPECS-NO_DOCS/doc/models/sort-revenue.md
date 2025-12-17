
# Sort Revenue

## Structure

`SortRevenue`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field_name` | [`FieldName21Enum`](../../doc/models/field-name-21-enum.md) | Optional | List of fields for ordering the result set. <br> By default sorting will be done by GROSS_REVENUE. |
| `order_by` | [`OrderByEnum`](../../doc/models/order-by-enum.md) | Optional | Type of Ordering. Default - ASC |

## Example (as JSON)

```json
{
  "fieldName": "GROSS_REVENUE",
  "orderBy": "ASC"
}
```

