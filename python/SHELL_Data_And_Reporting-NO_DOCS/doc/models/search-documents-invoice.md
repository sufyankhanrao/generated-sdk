
# Search Documents Invoice

## Structure

`SearchDocumentsInvoice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document_reference` | `int` | Optional | Unique Invoice Reference id of the invoice for downloading the zip file containing PDF and proofing elements.<br>Example: 123456 |
| `invoice_number` | `str` | Optional | Payment customer number.<br>Example: GB000000123 |
| `payer_name` | `str` | Optional | Customer payer name |
| `account_number` | `str` | Optional | Account Number<br>Example: GB99215176 |
| `account_name` | `str` | Optional | Invoice account name |
| `document_type` | `str` | Optional | Document type<br>String containing one of the following values:<br>•	NAT (National)<br>•	INT (International)<br>•	SOA (Statement of Account) |
| `gross_amount` | `float` | Optional | Included tax amount in the invoice |
| `net_amount` | `float` | Optional | - |
| `tax_amount` | `float` | Optional | - |
| `currency_code` | `str` | Optional | - |
| `invoice_status` | `str` | Optional | - |
| `invoice_date` | `str` | Optional | - |
| `due_date` | `str` | Optional | - |
| `vat_country_iso_code` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "DocumentReference": 10,
  "InvoiceNumber": "InvoiceNumber0",
  "PayerName": "PayerName0",
  "AccountNumber": "AccountNumber2",
  "AccountName": "AccountName8"
}
```

