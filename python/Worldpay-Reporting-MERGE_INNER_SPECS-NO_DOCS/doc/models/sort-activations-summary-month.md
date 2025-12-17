
# Sort Activations Summary Month

Sorting order for the search results of activated accounts summary.

## Structure

`SortActivationsSummaryMonth`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field_name` | [`FieldName71Enum`](../../doc/models/field-name-71-enum.md) | Optional | List of fields for sorting the result set. The result set is sorted in the given order <br> By default sorting will be done by PROCESS_MONTH.<br><br>**Constraints**: *Maximum Length*: `24` |
| `order_by` | [`OrderByEnum`](../../doc/models/order-by-enum.md) | Optional | Type of ordering. <BR> ASC stands for ascending order. <BR> DESC stands for descending order.<br><br>**Constraints**: *Maximum Length*: `4` |

## Example (as JSON)

```json
{
  "fieldName": "PROCESS_MONTH",
  "orderBy": "ASC"
}
```

