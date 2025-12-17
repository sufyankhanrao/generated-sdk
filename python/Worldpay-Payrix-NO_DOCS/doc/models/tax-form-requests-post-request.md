
# Tax Form Requests Post Request

## Structure

`TaxFormRequestsPostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant` | `str` | Optional | The identifies of the Merchant requesting the tax document. |
| `mtype` | [`TypeEnum`](../../doc/models/type-enum.md) | Optional | The tax document type.<br>Valid Value - `1099k` - **1099k Tax Document.** |
| `tax_year` | `int` | Optional | The tax year for which the document is requested. |
| `response_code` | `int` | Optional | The API call response code. |

## Example (as JSON)

```json
{
  "merchant": "t1_mer_6705400c6dbd095b4cb0000",
  "type": "1099k",
  "taxYear": 2024,
  "responseCode": 500
}
```

