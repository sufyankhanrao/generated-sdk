
# Invoice Summary Response

## Structure

`InvoiceSummaryResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | API Request Id |
| `status` | `str` | Optional | Indicates overall status of the request. Allowed values: SUCCES, FAILED |
| `data` | [`List[InvoiceSummaryDetails]`](../../doc/models/invoice-summary-details.md) | Optional | - |

## Example (as JSON)

```json
{
  "RequestId": "RequestId6",
  "Status": "Status2",
  "Data": [
    {
      "TotalInvoices": 230,
      "TotalGrossAmountCustomerCurrency": 149.02,
      "TotalNetAmountCustomerCurrency": 18.22,
      "TotalVATAmountCustomerCurrency": 21.48,
      "CustomerCurrencyCode": "CustomerCurrencyCode4"
    },
    {
      "TotalInvoices": 230,
      "TotalGrossAmountCustomerCurrency": 149.02,
      "TotalNetAmountCustomerCurrency": 18.22,
      "TotalVATAmountCustomerCurrency": 21.48,
      "CustomerCurrencyCode": "CustomerCurrencyCode4"
    }
  ]
}
```

