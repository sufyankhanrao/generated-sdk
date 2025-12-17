
# Upload Client Document Request

## Structure

`UploadClientDocumentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Required | The RSSID of the client for whom the document is to be uploaded. |
| `file` | [`ClientDocument`](../../doc/models/client-document.md) | Required | - |

## Example (as JSON)

```json
{
  "ClientId": "ClientId6",
  "File": {
    "FileName": "FileName6",
    "MediaType": "MediaType6",
    "Buffer": "Buffer8"
  }
}
```

