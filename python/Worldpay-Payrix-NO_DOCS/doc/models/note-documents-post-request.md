
# Note Documents Post Request

## Structure

`NoteDocumentsPostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `note` | `str` | Required | The identifier of the Note that owns this note documents resource. |
| `mtype` | [`NoteDocumentTypeEnum`](../../doc/models/note-document-type-enum.md) | Optional | The desired type to take on the referenced Note.<br><br><details><br><summary>Valid Values</summary><br>- `jpg` - **JPG Image File Type**<br>- `jpeg` - **JPEG Image File Type**<br>- `gif` - **GIF Image File Type**<br>- `png` - **PNG Image File Type**<br>- `pdf` - **PDF Document File Type**<br>- `tif` - **TIF Tag Image File Type**<br>- `tiff` - **TIFF Tag Image File Type**<br>- `txt` - **TXT Document File Type**<br>- `xml` - **XML Document File Type**<br>- `asc` - **American Standard Code II File Type**<br>- `rtf` - **Rich Text Document File Type**<br>- `csv` - **Comma Separated Values Table File Type**<br>- `xls` - **Microsoft Excel File Type**<br>- `doc` - **Microsoft Word File Type**<br>- `odt` - **OpenDocument Text File Type**<br>- `ods` - **OpenDocument Spreadsheet File Type**<br>- `json` - **JSON Document File Type**<br>- `soap` - **SOAP Document File Type**<br></details><br> |
| `name` | `str` | Optional | The name of the document on the referenced NoteDocument. |
| `custom` | `str` | Optional | The identifier of the Custom that relates to this notes resource. |
| `description` | `str` | Optional | A brief description of the document. |
| `status` | [`NoteDocumentStatusEnum`](../../doc/models/note-document-status-enum.md) | Required | The current status of the document upload.<br><br><details><br><summary>Valid Values</summary><br>- `created` - **The database record has been created.**<br>- `processed` - **The document upload for this record was processed successfully.**<br>- `failed` - **The document upload for this record could not be processed.**<br></details><br>**Default**: `'created'`<br> |
| `document_type` | [`NoteDocumentsDocumentTypeEnum`](../../doc/models/note-documents-document-type-enum.md) | Optional | The purpose of the document upload.<br><br><details><br><summary>Valid Values</summary><br>- `general` - **General use for unspecified type.**<br>- `personalId` - **An identification document for a person.**<br>- `companyId` - **An identification document for a company.**<br>- `voidCheck` - **A voided check for bank account verification.**<br>- `bankStatement` - **A bank statement.**<br>- `bankLetter` - **A bank letter for verification.**<br>- `contract` - **A contract for goods or services.**<br>- `taxDocument` - **A tax document for verification.**<br></details><br>**Default**: `'general'`<br> |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Required | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Required | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "note": "t1_not_67eef7a7a830eb17b0aefd5",
  "type": "png",
  "name": "Boy1.png",
  "custom": "identifier",
  "description": "doc description1",
  "status": "processed",
  "documentType": "voidCheck",
  "inactive": 0,
  "frozen": 0
}
```

