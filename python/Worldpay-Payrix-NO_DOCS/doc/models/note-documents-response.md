
# Note Documents Response

## Structure

`NoteDocumentsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `note` | `str` | Optional | The identifier of the Note that owns this note documents resource. |
| `custom` | `str` | Optional | The identifier of the Custom that relates to this notes resource. |
| `mtype` | [`NoteDocumentTypeEnum`](../../doc/models/note-document-type-enum.md) | Optional | The desired type to take on the referenced Note.<br><br><details><br><summary>Valid Values</summary><br>- `jpg` - **JPG Image File Type**<br>- `jpeg` - **JPEG Image File Type**<br>- `gif` - **GIF Image File Type**<br>- `png` - **PNG Image File Type**<br>- `pdf` - **PDF Document File Type**<br>- `tif` - **TIF Tag Image File Type**<br>- `tiff` - **TIFF Tag Image File Type**<br>- `txt` - **TXT Document File Type**<br>- `xml` - **XML Document File Type**<br>- `asc` - **American Standard Code II File Type**<br>- `rtf` - **Rich Text Document File Type**<br>- `csv` - **Comma Separated Values Table File Type**<br>- `xls` - **Microsoft Excel File Type**<br>- `doc` - **Microsoft Word File Type**<br>- `odt` - **OpenDocument Text File Type**<br>- `ods` - **OpenDocument Spreadsheet File Type**<br>- `json` - **JSON Document File Type**<br>- `soap` - **SOAP Document File Type**<br></details><br> |
| `document_type` | [`NoteDocumentsDocumentTypeEnum`](../../doc/models/note-documents-document-type-enum.md) | Optional | The purpose of the document upload.<br><br><details><br><summary>Valid Values</summary><br>- `general` - **General use for unspecified type.**<br>- `personalId` - **An identification document for a person.**<br>- `companyId` - **An identification document for a company.**<br>- `voidCheck` - **A voided check for bank account verification.**<br>- `bankStatement` - **A bank statement.**<br>- `bankLetter` - **A bank letter for verification.**<br>- `contract` - **A contract for goods or services.**<br>- `taxDocument` - **A tax document for verification.**<br></details><br>**Default**: `'general'`<br> |
| `name` | `str` | Optional | The name of the document on the referenced NoteDocument. |
| `description` | `str` | Optional | A brief description of the document. |
| `status` | [`NoteStatusEnum`](../../doc/models/note-status-enum.md) | Optional | The current status of the document upload.<br><br><details><br><summary>Valid Values</summary><br>- `created` - **The database record has been created.**<br>- `processed` - **The document upload for this record was processed successfully.**<br><br>- `failed` - **The document upload for this record could not be processed**<br><br></details><br> |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "documentType": "general",
  "inactive": 0,
  "frozen": 0,
  "id": "id6",
  "created": "created6",
  "modified": "modified4",
  "creator": "String5",
  "modifier": "modifier0"
}
```

