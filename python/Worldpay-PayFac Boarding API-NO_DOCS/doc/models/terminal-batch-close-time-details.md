
# Terminal Batch Close Time Details

## Structure

`TerminalBatchCloseTimeDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | Unique identifier for a Terminal of a Merchant. |
| `tid` | `int` | Optional | Unique identification number for every terminal under a particular merchant |
| `batch_close_time` | `str` | Optional | Terminal batch auto-close time of the given Terminal. HHMM format |

## Example (as JSON)

```json
{
  "id": 12345,
  "tid": 11,
  "batchCloseTime": "0430"
}
```

