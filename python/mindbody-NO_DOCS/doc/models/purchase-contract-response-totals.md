
# Purchase Contract Response Totals

Totals for the purchase

## Structure

`PurchaseContractResponseTotals`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total` | `float` | Optional | Total payment amount |
| `sub_total` | `float` | Optional | Sub total. For VAT, sum of asking prices (include taxes, excludes discounts). For non vat, excludes taxes and discounts. |
| `discount` | `float` | Optional | Discount |
| `tax` | `float` | Optional | Tax |

## Example (as JSON)

```json
{
  "Total": 58.52,
  "SubTotal": 16.62,
  "Discount": 230.64,
  "Tax": 195.98
}
```

