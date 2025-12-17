
# Order by for Date Summary Type

Default sorting by field PROCESS_DATE.

## Structure

`OrderByForDateSummaryType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field_name` | [`FieldName16Enum`](../../doc/models/field-name-16-enum.md) | Optional | This is the field used to sort on in the request. |
| `order_by` | [`OrderByEnum`](../../doc/models/order-by-enum.md) | Optional | Order by refers to the ordering being requested in the search that is based on the Field Name.  The response will return the data records in ascending or descending order. |

## Example (as JSON)

```json
{
  "fieldName": "PROCESS_DATE",
  "orderBy": "ASC"
}
```

