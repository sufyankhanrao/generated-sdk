
# Sort Partner Card Network

Sorting order for the search results of pending leads summary.

## Structure

`SortPartnerCardNetwork`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field_name` | [`FieldName4Enum`](../../doc/models/field-name-4-enum.md) | Optional | List of fields for sorting the result set. The result set is sorted in the given order. <br> By default sorting will be done by CARD_NETWORK. |
| `order_by` | [`OrderByEnum`](../../doc/models/order-by-enum.md) | Optional | Type of Ordering. Default - ASC |

## Example (as JSON)

```json
{
  "fieldName": "CARD_NETWORK",
  "orderBy": "ASC"
}
```

