
# Sorts Leads Count Closed Lost Reasons

Sorting order for search results of closed lost reasons.

## Structure

`SortsLeadsCountClosedLostReasons`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field_name` | [`FieldName91Enum`](../../doc/models/field-name-91-enum.md) | Optional | List of fields for sorting the result set. The result set is sorted in the given order <br> By default sorting will be done by CLOSED_LOST_REASON.<br><br>**Constraints**: *Maximum Length*: `18` |
| `order_by` | [`OrderByEnum`](../../doc/models/order-by-enum.md) | Optional | Type of ordering. <BR> ASC stands for ascending order. <BR> DESC stands for descending order.<br><br>**Constraints**: *Maximum Length*: `4` |

## Example (as JSON)

```json
{
  "fieldName": "CLOSED_LOST_REASON",
  "orderBy": "ASC"
}
```

