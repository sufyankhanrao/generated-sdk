
# Sortbankcarddetails

This object used for sorting

## Structure

`Sortbankcarddetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field_name` | [`FieldName23Enum`](../../doc/models/field-name-23-enum.md) | Optional | A field in a record that is used in determining the final sorted sequence of the records <br> By default sorting is based on PROCESS_DATE. |
| `order_by` | [`OrderByEnum`](../../doc/models/order-by-enum.md) | Optional | Type of Ordering. |

## Example (as JSON)

```json
{
  "fieldName": "PROCESS_DATE",
  "orderBy": "ASC"
}
```

