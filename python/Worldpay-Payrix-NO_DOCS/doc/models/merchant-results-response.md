
# Merchant Results Response

## Structure

`MerchantResultsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `merchant` | `str` | Optional | The merchant associated with this merchant result. |
| `mtype` | [`MerchantTypeEnum`](../../doc/models/merchant-type-enum.md) | Optional | The type of this merchant result<br><br><details><br><summary>Valid Values</summary><br>- `general` - **General use for unspecified type.**<br>- `internal` - **An internal failure result message.**<br>- `data` - **Missing merchant boarding related data failure message.**<br>- `legal` - **Result message related to legal matters.**<br>- `denial` - **Merchant boarding denial result message.**<br>- `platform` - **Processor boarding failure result message.**<br>- `platformNote` - **Processor note from merchant boarding.**<br></details><br> |
| `platform` | [`Platform1Enum`](../../doc/models/platform-1-enum.md) | Optional | The platform used to process this resource.<br><br><details><br><summary>Valid Values</summary><br>- `APPLE` - **The Apple Payment Processor.**<br>- `ELAVON` - **The Elavon processor.**<br>- `FIRSTDATA` - **The FirstData processor.**<br>- `GOOGLE` - **The Google Payment Processor.**<br>- `VANTIV` - **The WorldPay (aka Vantiv or Litle) eComm (aka VAP) processor.**<br>- `VCORE` - **The WorldPay (aka Vantiv) Core processor.**<br>- `TDBANKCA` - **External funding with TD Bank Canada via the Operating Account.**<br>- `WELLSACH` - **The Wells Fargo ACH processor.**<br>- `WELLSFARGO` - **The Wells Fargo Merchant Services processor.**<br>- `WFSINGLE` - **The WFSINGLE processor.**<br>- `WORLDPAY` - **The WORLDPAY processor.**<br></details><br> |
| `message` | `str` | Optional | The message of this merchant result. |
| `boarding_process_id` | `str` | Optional | Unique identification number that refers merchant. |

## Example (as JSON)

```json
{
  "id": "id8",
  "created": "created8",
  "modified": "modified4",
  "creator": "String7",
  "modifier": "modifier8"
}
```

