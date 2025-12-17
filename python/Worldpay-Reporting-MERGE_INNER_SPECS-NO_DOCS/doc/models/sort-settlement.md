
# Sort Settlement

## Structure

`SortSettlement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field_name` | [`FieldName6Enum`](../../doc/models/field-name-6-enum.md) | Optional | List of fields for sorting the result set. The result set is sorted in the given order <br> By default sorting will be done by PROCESS_MONTH.<br><br>**Constraints**: *Maximum Length*: `18` |
| `order_by` | [`OrderByEnum`](../../doc/models/order-by-enum.md) | Optional | Type of Ordering. Default - ASC<br><br>**Constraints**: *Maximum Length*: `4` |

## Example (as JSON)

```json
{
  "fieldName": "PROCESS_MONTH",
  "orderBy": "ASC"
}
```

