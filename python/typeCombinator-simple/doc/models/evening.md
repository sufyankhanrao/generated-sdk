
# Evening

Course evening session

## Structure

`Evening`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `starts_at` | `str` | Required | Session start time |
| `ends_at` | `str` | Required | Session end time |
| `offer_dinner` | `bool` | Required | Offer dinner during session |
| `session_type` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "sessionType": "Evening",
  "startsAt": "startsAt4",
  "endsAt": "endsAt2",
  "offerDinner": false
}
```

