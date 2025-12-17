
# Search Documents Request

## Structure

`SearchDocumentsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filters` | [`SearchDocReq`](../../doc/models/search-doc-req.md) | Optional | - |
| `page` | `str` | Optional | Specify the page of results to be returned. |
| `page_size` | `str` | Optional | Specify the number of records to returned; Max 1000 |

## Example (as JSON)

```json
{
  "Filters": {
    "PayerNumber": "PayerNumber0",
    "AccountNumber": "AccountNumber2",
    "AccountNumberList": [
      "AccountNumberList0"
    ],
    "InvoiceNumber": "InvoiceNumber0",
    "InvoiceNumberList": [
      "InvoiceNumberList5"
    ],
    "InvoiceStatus": "InvoiceStatus4",
    "ColCoCode": 14
  },
  "Page": "Page4",
  "PageSize": "PageSize2"
}
```

