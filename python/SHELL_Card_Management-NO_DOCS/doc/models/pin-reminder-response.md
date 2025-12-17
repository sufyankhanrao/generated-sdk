
# PIN Reminder Response

## Structure

`PINReminderResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | Unique request identifier passed from end user. This identifier helps in tracing a transaction |
| `main_reference` | `int` | Optional | Service reference number for tracking. |
| `status` | `str` | Optional | Indicates overall status of the request. Allowed values: SUCCESS, FAILED |
| `data` | [`List[PINReminderReference]`](../../doc/models/pin-reminder-reference.md) | Optional | - |

## Example (as JSON)

```json
{
  "RequestId": "RequestId8",
  "MainReference": 42,
  "Status": "Status4",
  "Data": [
    {
      "CardId": 224,
      "PANID": 0,
      "PAN": 154,
      "CardExpiryDate": "CardExpiryDate6",
      "ReferenceId": 108
    },
    {
      "CardId": 224,
      "PANID": 0,
      "PAN": 154,
      "CardExpiryDate": "CardExpiryDate6",
      "ReferenceId": 108
    }
  ]
}
```

