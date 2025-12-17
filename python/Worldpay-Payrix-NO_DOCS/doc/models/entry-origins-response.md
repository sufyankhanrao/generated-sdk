
# Entry Origins Response

## Structure

`EntryOriginsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `entry` | `str` | Optional | The entry on which the funding source was recorded. |
| `disbursement` | `str` | Optional | ID of the disbursement related to this entry origin. |
| `adjustment` | `str` | Optional | The adjustment ID from which the funding activity was triggered. |
| `cancellation` | `Any` | Optional | The ID of the entry used to cancel out corresponding debt. |
| `amount` | `float` | Optional | The amount for this funding activity in cents (up to three decimal points for sub-cents). |
| `funding` | `str` | Optional | The processor’s funding ID (related to a merchant, for some processors it is the merchant ID) from which the funds were sourced. |
| `platform` | [`EntryOriginPlatformEnum`](../../doc/models/entry-origin-platform-enum.md) | Optional | The processor through which the funds are available.<br><br><details><br><summary>Valid Values</summary><br>- `ELAVON` - **The Elavon processor.**<br>- `VANTIV` - **The WorldPay (aka Vantiv or Litle) eComm (aka VAP) processor.**<br>- `VCORE` - **The WorldPay (aka Vantiv) Core processor.**<br>- `TDBANK` - **External funding with TD Bank via the Operating Account.**<br>- `TDBANKCA` - **External funding with TD Bank Canada via the Operating Account.**<br>- `WELLSACH` - **The Wells Fargo ACH processor.**<br>- `WELLSFARGO` - **The Wells Fargo Merchant Services processor.**<br>- `WFSINGLE` - **The WFSINGLE processor.**<br>- `WORLDPAY` - **The WORLDPAY processor.**<br></details><br> |
| `fbo` | `str` | Optional | FBO in which each entry origin belongs to. |

## Example (as JSON)

```json
{
  "id": "id6",
  "created": "created6",
  "modified": "modified4",
  "creator": "String5",
  "modifier": "modifier0"
}
```

