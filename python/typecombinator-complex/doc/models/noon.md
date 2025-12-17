
# Noon

Course noon session

## Structure

`Noon`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `starts_at` | `str` | Required | Session start time |
| `ends_at` | `str` | Required | Session end time |
| `offer_lunch` | `bool` | Required | Offer lunch during session |
| `session_type` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "sessionType": "Noon",
  "startsAt": "startsAt6",
  "endsAt": "endsAt4",
  "offerLunch": false
}
```

