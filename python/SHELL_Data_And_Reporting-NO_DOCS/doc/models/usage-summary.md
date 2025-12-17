
# Usage Summary

## Structure

`UsageSummary`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date` | `str` | Optional | Transaction date.<br>The records will be sorted by this field in ascending order.<br><br>Format: yyyyMMdd |
| `product_id` | `int` | Optional | Product Id |
| `product_code` | `str` | Optional | Client Product code |
| `product_name` | `str` | Optional | Product name in English |
| `is_fuel_product` | `bool` | Optional | Whether the product is fuel or non-fuel |
| `site_group_id` | `int` | Optional | Site Group Id |
| `site_group_name` | `str` | Optional | Site Group Name |
| `total_volume` | `float` | Optional | Total Volume |
| `total_gross` | `float` | Optional | Total Gross in Customer Currency |
| `total_net` | `float` | Optional | Total Net in Customer Currency |
| `currency_code` | `str` | Optional | Customer Currency Code |
| `currency_symbol` | `str` | Optional | Customer Currency Symbol |
| `product_group_id` | `int` | Optional | Product group ID |
| `product_group_name` | `str` | Optional | Product group Name |

## Example (as JSON)

```json
{
  "Date": "Date0",
  "ProductId": 198,
  "ProductCode": "ProductCode6",
  "ProductName": "ProductName6",
  "IsFuelProduct": false
}
```

