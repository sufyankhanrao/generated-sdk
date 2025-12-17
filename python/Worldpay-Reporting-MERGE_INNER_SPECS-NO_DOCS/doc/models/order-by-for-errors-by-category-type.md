
# Order by for Errors by Category Type

Details of Order By Errors Category Type

## Structure

`OrderByForErrorsByCategoryType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field_name` | [`FieldName12Enum`](../../doc/models/field-name-12-enum.md) | Optional | This is the field is used to sort on in the request. Default sorting RETURN_DATE<br><br>**Constraints**: *Maximum Length*: `15` |
| `order_by` | [`OrderByEnum`](../../doc/models/order-by-enum.md) | Optional | Order by refers to the ordering being requested in the search that is based on the Field Name.  The response will return the data records in ascending or descending order.<br><br>**Constraints**: *Maximum Length*: `4` |

## Example (as JSON)

```json
{
  "fieldName": "RETURN_DATE",
  "orderBy": "ASC"
}
```

