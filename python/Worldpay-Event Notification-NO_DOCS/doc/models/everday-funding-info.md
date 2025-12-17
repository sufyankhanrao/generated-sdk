
# Everday Funding Info

EverdayFunding product enrollment status

## Structure

`EverdayFundingInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status_code` | [`StatusCodeEnum`](../../doc/models/status-code-enum.md) | Optional | Direct Funds Transfer Status code<br><br>**Constraints**: *Maximum Length*: `1` |
| `status_description` | [`StatusDescriptionEnum`](../../doc/models/status-description-enum.md) | Optional | Status description F-Pending, N-Not Enrolled, R-Active, K-Disabled by settlement<br><br>**Constraints**: *Maximum Length*: `12` |
| `last_updated_date_time` | `str` | Optional | Status change date and time<br><br>**Constraints**: *Maximum Length*: `26`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}:[0-9]{6}` |

## Example (as JSON)

```json
{
  "statusCode": "R",
  "statusDescription": "ACTIVE",
  "lastUpdatedDateTime": "lastUpdatedDateTime2"
}
```

