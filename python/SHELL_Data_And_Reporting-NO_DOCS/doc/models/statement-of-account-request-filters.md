
# Statement of Account Request Filters

## Structure

`StatementOfAccountRequestFilters`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `col_co_code` | `int` | Optional | Collecting Company Code (Shell Code) of the selected payer.<br>Optional If ColCo Id is passed else Mandatory. |
| `payer_id` | `int` | Optional | Payer Id of the selected payer.<br>Optional if PayerNumber is passed else Mandatory. |
| `payer_number` | `str` | Optional | Payer Number of the selected payer.<br>Optional if PayerId is passed else Mandatory. |
| `include_monthly_invoice_trend` | `bool` | Optional | True/False.<br>Optional. Default is False.<br>True if the past 13 monthly invoice trend to be included as part of the response. Else false. |
| `include_past_statement_of_accounts` | `bool` | Optional | True/False.<br>Optional. Default is False.<br>True if the past X SOA documents are to be included as part of the response. Else false. |
| `due_or_over_due_soa_documents_only` | `bool` | Optional | True/False<br>Optional Default is False.<br>If true PastStatementOfAccounts entity on this API output should contain the SOA documents that are due or overdue only. |
| `number_of_soa_documents` | `int` | Optional | This parameter is only applicable when “IncludePastStatementOfAccounts” parameter is set to True. |
| `include_account_invoices_summary` | `bool` | Optional | True/False<br>Optional.<br>Default value is false.<br>When true InvoicesSummaries list will be returned in the API output. |
| `col_co_id` | `int` | Optional | Collecting Company Id of the selected payer.<br>Optional If ColCo Code is passed else Mandatory. |
| `accounts` | [`List[Accounts]`](../../doc/models/accounts.md) | Optional | - |

## Example (as JSON)

```json
{
  "ColCoCode": 14,
  "PayerId": 48,
  "PayerNumber": "PayerNumber8",
  "IncludeMonthlyInvoiceTrend": false,
  "IncludePastStatementOfAccounts": false
}
```

