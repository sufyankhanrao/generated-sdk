
# Upload Client Photo Request

## Structure

`UploadClientPhotoRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bytes` | `str` | Required | A Base64-encoded string representation of the image’s byte array. |
| `client_id` | `str` | Required | The RSSID of the client for whom the photo is to be uploaded. |

## Example (as JSON)

```json
{
  "Bytes": "Bytes4",
  "ClientId": "ClientId8"
}
```

