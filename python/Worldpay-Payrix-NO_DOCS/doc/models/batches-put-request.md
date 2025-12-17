
# Batches Put Request

## Structure

`BatchesPutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`BatchStatusEnum`](../../doc/models/batch-status-enum.md) | Optional | The current status of this Batch.<br><br><details><br><summary>Valid Values</summary><br>- `open`  - **This Batch can accept more Transactions.**<br>- `closed` - **This Batch is closed to new Transactions and is ready to be sent to the processor.**<br></details><br>**Default**: `"open"`<br> |
| `ref` | `str` | Optional | The reference code of the batch.<br>This field is automatically generated and stored as a text string and must be between 0 and 50 characters long. |
| `client_ref` | `str` | Optional | The merchant's reference code of the batch.<br>This field is stored as a text string and must be between 0 and 50 characters long. |
| `processing_id` | `str` | Optional | Internal ID set for processing. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "status": "open",
  "ref": "reference code of batch",
  "clientRef": "merchant's reference code",
  "processingId": "Internal ID",
  "inactive": 0,
  "frozen": 0
}
```

