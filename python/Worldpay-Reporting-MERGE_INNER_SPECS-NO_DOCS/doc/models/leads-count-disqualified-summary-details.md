
# Leads Count Disqualified Summary Details

Leads count grouped by disqualification reason.

## Structure

`LeadsCountDisqualifiedSummaryDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `disqualification_reason` | `str` | Optional | Reason for disqualification of leads.<br><br>**Constraints**: *Maximum Length*: `10000` |
| `count` | `float` | Optional | Number of leads disqualified for a specific reason.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |

## Example (as JSON)

```json
{
  "disqualificationReason": "Restricted Business Type",
  "count": 84.0
}
```

