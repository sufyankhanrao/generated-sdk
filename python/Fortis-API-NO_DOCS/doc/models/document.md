
# Document

Array of document objects.

## Structure

`Document`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document_name` | `str` | Required | Array of bank account objects.<br><br>**Constraints**: *Maximum Length*: `32` |
| `document_data` | `str` | Required | Base64 encoded document content. |
| `mime_type` | `str` | Required | Mime type of document.<br><br>**Constraints**: *Maximum Length*: `20` |

## Example (as JSON)

```json
{
  "document_name": "ImportantDoc.txt",
  "document_data": "alskj;asijia;eiom;weirj;iomj",
  "mime_type": "application/json"
}
```

