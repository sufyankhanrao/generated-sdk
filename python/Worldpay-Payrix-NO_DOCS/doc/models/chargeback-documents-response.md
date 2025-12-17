
# Chargeback Documents Response

## Structure

`ChargebackDocumentsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `chargeback` | `str` | Optional | The identifier of the Chargeback resource that this chargebackDocument relates to. |
| `ref` | `str` | Optional | The reference for this chargebackDocument.<br>This field is stored as a text string and must be between 1 and 100 characters long.<br>The value is set when the file is properly integrated, otherwise will be null. |
| `mtype` | [`ChargebackDocumentTypeEnum`](../../doc/models/chargeback-document-type-enum.md) | Optional | The type of the file that holds this chargebackDocument.<br>The value is set when the file is properly integrated, otherwise will be null.<br><br><details><br><summary>Valid Values</summary><br>- `jpg` - **JPG file**<br>- `jpeg` - **JPEG file**<br>- `gif` - **GIF file**<br>- `png` - **PNG file**<br>- `pdf` - **PDF file**<br>- `tiff` - **TIFF file**<br>- `tif` - **TIF file**<br></details><br> |
| `name` | `str` | Optional | The name of this chargebackDocument.<br>This field is stored as a text string and must be between 1 and 100 characters long.<br>The value is set when the file is created and properly integrated. It holds the real file name used by the user. |
| `description` | `str` | Optional | The description of this chargebackDocument.<br>This field is stored as a text string and must be between 1 and 100 characters long. |
| `status` | [`ChargebackDocumentStatusEnum`](../../doc/models/chargeback-document-status-enum.md) | Optional | The current status of the chargebackDocument.<br><br><details> <br><summary>Valid Values</summary><br>- `created` - **The ChargebackDocument has been created.**<br>- `processed` - **The ChargebackDocument integration has been successful.**<br><br>- `failed` - **The ChargebackDocument integration has failed.**<br><br></details><br>**Default**: `"created"`<br> |
| `document_source` | [`DocumentSourceEnum`](../../doc/models/document-source-enum.md) | Optional | The source of the document.<br><br><details><br><summary>Valid Values</summary><br>- `merchant` - **Merchant.** <br>- `issuer` - **Issuer.** <br></details><br> |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "status": "created",
  "inactive": 0,
  "frozen": 0,
  "id": "id0",
  "created": "created0",
  "modified": "modified8",
  "creator": "String9",
  "modifier": "modifier6"
}
```

