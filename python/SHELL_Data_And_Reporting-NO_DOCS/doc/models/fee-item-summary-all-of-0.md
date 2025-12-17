
# Fee Item Summary All of 0

## Structure

`FeeItemSummaryAllOf0`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fee_type_group` | `str` | Optional | Fee type group in under which the Fee item is generated. |
| `fee_type_id` | `str` | Optional | Fee Type Id ID  Description |
| `product_id` | `int` | Optional | Product Id |
| `product_code` | `str` | Optional | Product Code |
| `product_name` | `str` | Optional | Product Name |
| `product_group_id` | `int` | Optional | Product Group Id |
| `product_group_name` | `str` | Optional | Product Group Name |
| `total_quantity` | `float` | Optional | Total Quantity |
| `total_invoice_net_amount` | `float` | Optional | Total Net amount in invoice currency |
| `total_invoice_gross_amount` | `float` | Optional | Total Gross amount in invoice currency |
| `total_invoice_vat_amount` | `float` | Optional | Total VAT amount in invoice currency |
| `invoice_currency_code` | `str` | Optional | ISO 4217 currency code of the country |
| `invoice_currency_symbol` | `str` | Optional | Currency symbol of the Invoice Currency Code |

## Example (as JSON)

```json
{
  "FeeTypeGroup": "Account",
  "FeeTypeId": "1",
  "ProductId": 102,
  "ProductCode": "Invoice production fee",
  "ProductName": "Invoice production fee",
  "ProductGroupId": 22,
  "ProductGroupName": "Card related fees",
  "TotalQuantity": 2,
  "TotalInvoiceNetAmount": 22.23,
  "TotalInvoiceGrossAmount": 28.92,
  "TotalInvoiceVATAmount": 10.02,
  "InvoiceCurrencyCode": "GBP",
  "InvoiceCurrencySymbol": "Ã‚Â£"
}
```

