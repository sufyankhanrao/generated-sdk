
# Batches Post Request

## Structure

`BatchesPostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant` | `str` | Required | The identifier of the Merchant that is associated with this Batch. |
| `platform` | [`BatchPlatformEnum`](../../doc/models/batch-platform-enum.md) | Required | The platform used to process this Batch.<br><br><details><br><summary>Valid Values</summary><br>- `APPLE` - **Apple Payment Processor**<br>- `ELAVON` - **ELAVON Payment Processor**<br>- `FIRSTDATA` - **FirstData Payment Processor**<br>- `GOOGLE` - **Google Payment Processor**<br>- `VANTIV` - **Worldpay / Vantiv eComm Payment Processor (VAP)**<br>- `VCORE` - **Worldpay / Vantiv Core Payment Processor**<br>- `WELLSACH` - **Wells Fargo Merchant Services Payment Processor (ACH)**<br>- `WELLSFARGO` - **Wells Fargo Merchant Services Payment Processor**<br>- `WFSINGLE` - **Wells Fargo Single Payment Processor**<br>- `WORLDPAY` - **Worldpay Payment Processor**<br>- `TDBANKCA` - **TD Bank Canada Payment Processor**<br></details><br> |
| `status` | [`BatchStatusEnum`](../../doc/models/batch-status-enum.md) | Required | The current status of this Batch.<br><br><details><br><summary>Valid Values</summary><br>- `open`  - **This Batch can accept more Transactions.**<br>- `closed` - **This Batch is closed to new Transactions and is ready to be sent to the processor.**<br></details><br>**Default**: `'open'`<br> |
| `ref` | `str` | Optional | The reference code of the batch.<br>This field is automatically generated and stored as a text string and must be between 0 and 50 characters long. |
| `client_ref` | `str` | Optional | The merchant's reference code of the batch.<br>This field is stored as a text string and must be between 0 and 50 characters long. |
| `processing_id` | `str` | Optional | Internal ID set for processing. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Required | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Required | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "merchant": "t1_mer_63341144b40742676bea201",
  "platform": "VANTIV",
  "status": "open",
  "ref": "reference code of batch",
  "clientRef": "merchant's reference code",
  "processingId": "Internal ID",
  "inactive": 0,
  "frozen": 0
}
```

