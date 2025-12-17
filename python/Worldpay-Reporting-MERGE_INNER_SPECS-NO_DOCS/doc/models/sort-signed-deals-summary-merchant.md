
# Sort Signed Deals Summary Merchant

Sorting order for the search results of signed deals summary by merchant.

## Structure

`SortSignedDealsSummaryMerchant`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field_name` | [`FieldName61Enum`](../../doc/models/field-name-61-enum.md) | Optional | List of fields for sorting the result set. The result set is sorted in the given order <br> By default sorting will be done by MERCHANT_NAME.<br><br>**Constraints**: *Maximum Length*: `31` |
| `order_by` | [`OrderByEnum`](../../doc/models/order-by-enum.md) | Optional | Type of ordering. <BR> ASC stands for ascending order. <BR> DESC stands for descending order.<br><br>**Constraints**: *Maximum Length*: `4` |

## Example (as JSON)

```json
{
  "fieldName": "MERCHANT_NAME",
  "orderBy": "ASC"
}
```

