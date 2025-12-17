
# Client Document

## Structure

`ClientDocument`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `file_name` | `str` | Required | The name of the file to be used on the client’s documents page when it is uploaded. |
| `media_type` | `str` | Required | The type of file or file extension. Possible values are:<br><br>* pdf<br>* jpg<br>* jpeg<br>* tif<br>* tiff<br>* png<br>* doc<br>* docx<br>* bmp<br>* txt<br>* rtf<br>* xlsx<br>* xls<br>* gif<br>* zip<br>* ppt<br>* pptx<br>* mov |
| `buffer` | `str` | Required | A Base64-encoded string representation of the file’s byte array. |

## Example (as JSON)

```json
{
  "FileName": "FileName6",
  "MediaType": "MediaType6",
  "Buffer": "Buffer8"
}
```

