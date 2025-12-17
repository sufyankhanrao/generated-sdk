
# Sort Leads Count Disqualified

Sorting order for the search results of disqualified leads.

## Structure

`SortLeadsCountDisqualified`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field_name` | [`FieldName81Enum`](../../doc/models/field-name-81-enum.md) | Optional | List of fields for sorting the result set. The result set is sorted in the given order <br> By default sorting will be done by DISQUALIFICATION_REASON.<br><br>**Constraints**: *Maximum Length*: `23` |
| `order_by` | [`OrderByEnum`](../../doc/models/order-by-enum.md) | Optional | Type of ordering. <BR> ASC stands for ascending order. <BR> DESC stands for descending order.<br><br>**Constraints**: *Maximum Length*: `4` |

## Example (as JSON)

```json
{
  "fieldName": "DISQUALIFICATION_REASON",
  "orderBy": "ASC"
}
```

