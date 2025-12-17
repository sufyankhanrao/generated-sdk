
# Divisions for Update Response

## Structure

`DivisionsForUpdateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `division_name` | `str` | Optional | Division name for the division<br><br>**Constraints**: *Maximum Length*: `30` |

## Example (as JSON)

```json
{
  "divisionName": "Division 001",
  "correlationId": "correlationId6",
  "httpStatusCode": "httpStatusCode2",
  "httpStatusMessage": "httpStatusMessage6"
}
```

