
# Terminals for Update

## Structure

`TerminalsForUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `batch_close_time` | `str` | Required | Required field |
| `batch_close_type` | `str` | Optional | Optional field. Allowed values are H, T, N. H- Host auto close, T- Terminal auto close, N- None. Default value is H |
| `batch_turn_off` | `str` | Optional | Optional field. Allowed values are Yes, No. Default value is No. If this value is No then batchCloseType must be sent as H. If this value is Yes then batchCloseType can be sent as either T or N |

## Example (as JSON)

```json
{
  "batchCloseTime": "0430",
  "batchCloseType": "H",
  "batchTurnOff": "No"
}
```

