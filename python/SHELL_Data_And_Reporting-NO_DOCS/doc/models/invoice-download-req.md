
# Invoice Download Req

## Structure

`InvoiceDownloadReq`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `col_co_code` | `int` | Required | Collecting Company Code of the selected payer.<br>Mandatory |
| `payer_number` | `str` | Required | Payer Number of the selected payer.<br>Mandatory<br>Example: GB000000123 |
| `account_number` | `List[str]` | Optional | List of Account Numbers of the invoices.<br>Mandatory for customer users else optional. |
| `document_reference` | `List[int]` | Optional | Unique reference ids of invoice document (of zip file).<br>Optional if InvoiceOrSOANumber is passed else Mandatory. |
| `invoice_or_soa_number` | `str` | Optional | Invoice or the SOA document reference number issued by Card s Platform. |

## Example (as JSON)

```json
{
  "ColCoCode": 126,
  "PayerNumber": "PayerNumber0",
  "AccountNumber": [
    "AccountNumber4",
    "AccountNumber5",
    "AccountNumber6"
  ],
  "DocumentReference": [
    117,
    116,
    115
  ],
  "InvoiceOrSOANumber": "InvoiceOrSOANumber0"
}
```

