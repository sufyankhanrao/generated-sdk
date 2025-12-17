
# Invoices Summaries

## Structure

`InvoicesSummaries`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount_due` | `float` | Optional | Amount due from last summary document date. |
| `amount_not_overdue` | `float` | Optional | Amount that are due from past summary documents. |
| `amount_overdue` | `float` | Optional | Amount that are overdue from past summary documents. |
| `amount_paid` | `float` | Optional | Total amount paid in billing currency. |
| `billing_currency_code` | `str` | Optional | Billing currency ISO code. |
| `billing_currency_symbol` | `str` | Optional | Billing currency symbol.<br>Example: € |
| `outstanding_balance` | `float` | Optional | Current outstanding balance amount |
| `payment_due_date` | `str` | Optional | Payment due date.<br>Format: YYYYMMDD |
| `summary_document_date` | `str` | Optional | Summary document date.<br>Format: YYYYMMDD |
| `total_billing_documents` | `int` | Optional | Total number of invoices generated on this date. |
| `total_gross_amount_billing_currency` | `float` | Optional | Total gross amount in billing currency. |
| `total_net_amount_billing_currency` | `float` | Optional | Total net amount in billing currency. |
| `total_summary_documents` | `int` | Optional | Total number of summary documents generated on this date. |
| `total_vat_amount_billing_currency` | `float` | Optional | Total VAT amount in billing currency. |

## Example (as JSON)

```json
{
  "AmountDue": 132.62,
  "AmountNotOverdue": 125.36,
  "AmountOverdue": 110.28,
  "AmountPaid": 62.46,
  "BillingCurrencyCode": "BillingCurrencyCode0"
}
```

