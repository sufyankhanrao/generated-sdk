
# Auto Renew Card Response

## Structure

`AutoRenewCardResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `main_reference` | `int` | Optional | Main reference number for tracking.<br>Example: 123455 |
| `request_id` | `str` | Optional | API |
| `status` | `str` | Optional | Indicates overall status of the request. Allowed values: SUCCES, FAILED, PARTIAL_SUCCESS |
| `data` | [`List[AutoRenewCardResponseDataItems]`](../../doc/models/auto-renew-card-response-data-items.md) | Optional | List of Auto Renew reference entity. The fields of this entity are described below. |

## Example (as JSON)

```json
{
  "MainReference": 14,
  "RequestId": "RequestId6",
  "Status": "Status2",
  "Data": [
    {
      "AutoRenewReferenceId": 102,
      "CardIdAndPAN": "CardIdAndPAN4"
    }
  ]
}
```

