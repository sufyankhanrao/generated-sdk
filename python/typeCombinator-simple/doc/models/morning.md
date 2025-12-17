
# Morning

Course morning session

## Structure

`Morning`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `starts_at` | `str` | Required | Session start time |
| `ends_at` | `str` | Required | Session end time |
| `offer_tea_break` | `bool` | Required | Offer tea break during session |
| `session_type` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "sessionType": "Morning",
  "startsAt": "startsAt6",
  "endsAt": "endsAt2",
  "offerTeaBreak": false
}
```

