
# Divisions Get Response

## Structure

`DivisionsGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `divisions` | [`List[Division]`](../../doc/models/division.md) | Optional | - |

## Example (as JSON)

```json
{
  "correlationId": "0acfc8fe1816421ab7376337d5729b94",
  "httpStatusCode": "200",
  "httpStatusMessage": "OK",
  "divisions": [
    {
      "chainCode": "chainCode2",
      "divisionCode": "divisionCode2",
      "divisionName": "divisionName6"
    },
    {
      "chainCode": "chainCode2",
      "divisionCode": "divisionCode2",
      "divisionName": "divisionName6"
    },
    {
      "chainCode": "chainCode2",
      "divisionCode": "divisionCode2",
      "divisionName": "divisionName6"
    }
  ]
}
```

