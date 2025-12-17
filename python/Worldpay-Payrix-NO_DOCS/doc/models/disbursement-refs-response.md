
# Disbursement Refs Response

## Structure

`DisbursementRefsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `disbursement` | `str` | Optional | The identifier of the Disbursement that this disbursementRef resource refers to. |
| `disbursement_ref` | `str` | Optional | The identifier of the DisbursementRef that this disbursementRef resource refers to. |
| `platform` | [`DisbursementPlatformEnum`](../../doc/models/disbursement-platform-enum.md) | Optional | The platform used to process this Transaction.<br><br><details><br><summary>Valid Values</summary><br>- `ELAVON`  - The Elavon processor.<br>- `VANTIV`  - The WorldPay (aka Vantiv or Litle) eComm (aka VAP) processor.<br><br>- `VCORE` - The WorldPay (aka Vantiv) Core processor.<br><br>- `TDBANK` - External funding with TD Bank via the Operating Account.<br><br>- `TDBANKCA` - External funding with TD Bank Canada via the Operating Account.<br><br>- `WELLSACH` - The Wells Fargo ACH processor.<br><br>- `WELLSFARGO` - The Wells Fargo Merchant Services processor.<br><br>- `WFSINGLE` - The WFSINGLE processor.<br><br>- `WORLDPAY` - The WORLDPAY processor.<br><br></details><br> |
| `company_id` | `str` | Optional | An identification document for a company. |
| `ref` | `str` | Optional | The Disbursement reference code itself. This field is stored as a text string and must be between 1 and 50 characters long. |
| `file_ref` | `str` | Optional | A file reference code that is stored as a text string and must be between 1 and 50 characters long. |
| `stage` | [`DisbursementRefStageEnum`](../../doc/models/disbursement-ref-stage-enum.md) | Optional | The stage of the Disbursement reference.<br><br><details><br><summary>Valid Values</summary><br>- `create`  - Funding is sent to the processor (based on prior split setup).<br>- `approve`  - Funding approved by the processor.<br><br>- `split` - Disbursement amount is split for processing.<br><br>- `failed` - Funding failed.<br><br></details><br> |
| `amount` | `int` | Optional | The amount of the disbursement related to this disbursementRef. |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "frozen": 0,
  "inactive": 0,
  "id": "id4",
  "created": "created4",
  "modified": "modified2",
  "creator": "String3",
  "modifier": "modifier2"
}
```

