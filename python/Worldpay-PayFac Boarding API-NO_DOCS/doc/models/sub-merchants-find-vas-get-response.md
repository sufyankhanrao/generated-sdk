
# Sub Merchants Find Vas Get Response

## Structure

`SubMerchantsFindVasGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `sub_merchants` | [`List[SubMerchantsFindVas]`](../../doc/models/sub-merchants-find-vas.md) | Optional | - |

## Example (as JSON)

```json
{
  "correlationId": "correlationId8",
  "httpStatusCode": "httpStatusCode6",
  "httpStatusMessage": "httpStatusMessage8",
  "subMerchants": [
    {
      "id": 162,
      "mid": 118,
      "uuid": "00000d80-0000-0000-0000-000000000000",
      "chainCode": "chainCode4",
      "divisionCode": "divisionCode0"
    },
    {
      "id": 162,
      "mid": 118,
      "uuid": "00000d80-0000-0000-0000-000000000000",
      "chainCode": "chainCode4",
      "divisionCode": "divisionCode0"
    }
  ]
}
```

