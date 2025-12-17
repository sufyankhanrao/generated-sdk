
# Invoice Search Request Filters

## Structure

`InvoiceSearchRequestFilters`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `col_co_id` | `int` | Optional | Collecting Company Id of the selected payer.<br>Optional.<br>Example:<br>1-Philippines<br>5-UK |
| `payer_id` | `int` | Optional | Payer Id of the selected payer.<br>Optional if PayerNumber is passed else Mandatory<br>Example: 123456 |
| `payer_number` | `str` | Optional | Payer Number of the selected payer.<br>Optional if PayerId is passed else Mandatory<br>Example: GB000000123 |
| `invoice_id` | `int` | Optional | Invoice id.<br>Optional.<br>This input is a search criterion, if given.<br>Example: 1 |
| `invoice_number` | `str` | Optional | Invoice number.<br>Optional.<br>This input is a search criterion, if given.<br>Example: 0123456789 |
| `from_date` | `str` | Optional | Invoice date searched from this date.<br>Optional.<br>This input is a search criterion, if given.<br>Date format: yyyyMMdd<br>Example: 20170830<br>Note: This criterion is ignored if ‘Period’ is given.<br>Also, this criterion is ignored if ‘ToDate’ is not provided. |
| `to_date` | `str` | Optional | Invoice date searched until this date.<br>Optional.<br>This input is a search criterion, if given.<br>Date format: yyyyMMdd<br>Example: 20170830<br>Note: This criterion is ignored if ‘Period’ is given.<br>Also, this criterion is ignored if ‘FromDate’ is not provided. |
| `invoice_date` | `str` | Optional | Date of invoicing.<br>Optional.<br>This input is a search criterion, if given.<br>Date format: yyyyMMdd<br>Example: 20170830 |
| `summary_document_id` | `int` | Optional | Summary document id<br>Optional.<br>This input is a search criterion, if given.<br>Example: 1 |
| `summary_document_number` | `str` | Optional | Summary document number<br>Optional.<br>This input is a search criterion, if given.<br>Example: ‘0/CZ0000000123456/2017’ |
| `statement_of_account_id` | `str` | Optional | Statement of Account Id of the payment customer.<br>Optional.<br>This input is a search criterion, if given.<br>Example: 1 |
| `so_a_reference_number` | `str` | Optional | Statement of Account reference number of the payment customer.<br>Optional.<br>This input is a search criterion, if given.<br>Example: 123 |
| `period` | `int` | Optional | Invoice date search period. Valid values –<br><br>1. Last 7 days – Issued in last 7 days.<br>2. Last 30 days – Issued in last 30 days.<br>3. Last 90 days – Issued in last 90 days.<br>   Optional.<br>   This input is a search criterion, if given.<br>   Example: 1 |
| `invoice_status` | `str` | Optional | Status of the invoice. Valid values –<br>•	Due – Invoices due for payment and is within the due date.<br>•	Paid – Fully paid Invoices.<br>•	Overdue – Invoices due of payment and has crossed the due date.<br>•	CreditNote – Credit notes<br>•	CreditStatement<br>Optional.<br>This input is a search criterion, if given. |
| `invoiced_on_behalf_of` | `str` | Optional | ISO code of the country i.e., UK, DE, MY, etc.<br>Optional |
| `include_e_invoice_details` | `bool` | Optional | Whether to include the additional invoice details in the API response.<br>Optional. Default value “False”.<br>The parameters that are populated<br>•	DocumentReference<br>•	AdditionalDocuments<br>The above fields will not be present in the response when the respective data is not available in the source system. |
| `col_co_code` | `int` | Optional | Collecting Company Code of the selected payer.<br>Mandatory - It is mandatory field to external source ATOS for E-invoicing.<br>Example:<br>86-Philippines<br>5-UK |
| `accounts` | [`List[Accounts]`](../../doc/models/accounts.md) | Optional | - |
| `mtype` | `str` | Optional | Invoice type. Allowed values –<br>•	Original – Original document.<br>•	Reversal – Reversed document.<br>•	Replacement – Replaced document.<br>Optional. (When not passed all invoice, types are considered for search)<br>This input is a search criterion, if given.<br>Example: Original |

## Example (as JSON)

```json
{
  "ColCoId": 170,
  "PayerId": 218,
  "PayerNumber": "PayerNumber0",
  "InvoiceId": 102,
  "InvoiceNumber": "InvoiceNumber0"
}
```

