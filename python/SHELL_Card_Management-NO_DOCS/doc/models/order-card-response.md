
# Order Card Response

## Structure

`OrderCardResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | Unique request identifier passed from end user. This identifier helps in tracing a transaction |
| `status` | `str` | Optional | Indicates overall status of the request. Allowed values: SUCCESS, FAILED |
| `data` | [`List[CreateCardResponse]`](../../doc/models/create-card-response.md) | Optional | - |
| `main_reference` | `int` | Optional | Main order reference number for tracking. |

## Example (as JSON)

```json
{
  "RequestId": "RequestId2",
  "Status": "Status8",
  "Data": [
    {
      "DriverAndVRN": "DriverAndVRN6",
      "OrderCardReference": 86
    }
  ],
  "MainReference": 110
}
```

