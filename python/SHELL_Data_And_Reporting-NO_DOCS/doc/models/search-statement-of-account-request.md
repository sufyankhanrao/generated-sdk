
# Search Statement of Account Request

## Structure

`SearchStatementOfAccountRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filters` | [`SearchSOAReq`](../../doc/models/search-soa-req.md) | Optional | - |
| `page` | `int` | Optional | Page number |
| `page_size` | `int` | Optional | Number of records in page |

## Example (as JSON)

```json
{
  "Filters": {
    "ColCoCode": 14,
    "PayerNumber": "PayerNumber0",
    "InvoiceNumber": "InvoiceNumber0",
    "FromDate": "FromDate6",
    "ToDate": "ToDate4"
  },
  "Page": 114,
  "PageSize": 94
}
```

