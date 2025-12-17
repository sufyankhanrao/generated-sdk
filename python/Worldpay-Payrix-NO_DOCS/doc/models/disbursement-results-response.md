
# Disbursement Results Response

## Structure

`DisbursementResultsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `disbursement` | `str` | Optional | The identifier of the Disbursement that this disbursementResult resource refers to. |
| `disbursement_ref` | `str` | Optional | The ID of the disbursementRef for which this result is recorded. |
| `code` | [`DisbursementResultCodeEnum`](../../doc/models/disbursement-result-code-enum.md) | Optional | The code identifying the disbursement result.<br><br><details><br><summary>Valid Values</summary> <br>- `pending` - **Disbursement processing is pending account verification.**<br>- `internal` - **Failed. Internal note and/or failure.**<br><br>- `nsf` - **Failed. Disbursement return due to insufficient funds.**<br><br>- `badAccount` - **Failed. Disbursement return due to incorrect payment account information.**<br><br>- `unauthorized` - **Failed. Disbursement return due to customer dispute of authorization.**<br><br>- `general` - **General note and/or failure.**<br><br>- `noc` - **Notice of change.**<br><br>- `parameter` - **Disbursement processing withheld due to parameter configuration.**<br><br>- `sameDay` - **Failed. Same-day processing note and/or failure.**<br><br>- `transferDetails` - **Trace number note and/or data.**<br><br>- `platform` - **Failed. Processor note and/or failure.**<br><br></details><br> |
| `original_code` | `str` | Optional | The original, unmapped code as received from the processor for this result. |
| `platform` | [`DisbursementPlatformEnum`](../../doc/models/disbursement-platform-enum.md) | Optional | The platform used to process this Disbursement.<br><br><details><br><summary>Valid Values</summary><br>- `ELAVON`  - **The Elavon processor.**<br>- `VANTIV`  - **The Worldpay (aka Vantiv or Litle) eComm (aka VAP) processor.**<br><br>- `VCORE` - **The Worldpay (aka Vantiv) Core processor.**<br><br>- `TDBANK` - **External funding with TD Bank via the Operating Account.**<br><br>- `TDBANKCA` - **External funding with TD Bank Canada via the Operating Account.**<br><br>- `WELLSACH` - **The Wells Fargo ACH processor.**<br><br>- `WELLSFARGO` - **The Wells Fargo Merchant Services processor.**<br><br>- `WFSINGLE` - **The WFSINGLE processor.**<br><br>- `WORLDPAY` - **The WORLDPAY processor.**<br><br></details><br> |
| `message` | `str` | Optional | The message string for this result. |
| `amount` | `int` | Optional | The amount of the disbursement relevant for this result. |
| `data` | `str` | Optional | Data (the trace number, if applicable). |

## Example (as JSON)

```json
{
  "id": "id0",
  "created": "created0",
  "modified": "modified8",
  "creator": "String9",
  "modifier": "modifier4"
}
```

