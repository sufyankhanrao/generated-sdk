
# Invoice Download Request

## Structure

`InvoiceDownloadRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filters` | [`InvoiceDownloadReq`](../../doc/models/invoice-download-req.md) | Optional | - |

## Example (as JSON)

```json
{
  "Filters": {
    "ColCoCode": 14,
    "PayerNumber": "PayerNumber0",
    "AccountNumber": [
      "AccountNumber4",
      "AccountNumber5"
    ],
    "DocumentReference": [
      59,
      60,
      61
    ],
    "InvoiceOrSOANumber": "InvoiceOrSOANumber0"
  }
}
```

