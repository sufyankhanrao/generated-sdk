
# Client Reward Transaction

Contains information about the transaction details.

## Structure

`ClientRewardTransaction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action_date_time` | `datetime` | Optional | The date and time when the points were earned or redeemed in the site local time zone. |
| `action` | [`Action9Enum`](../../doc/models/action-9-enum.md) | Optional | Indicates if rewards were earned or redeemed. |
| `source` | `str` | Optional | The source of the reward transaction. |
| `source_id` | `int` | Optional | The unique identifier in the MINDBODY system for the **Source**. |
| `expiration_date_time` | `datetime` | Optional | The date and time when earned points expire. This is calculated based on site and client rewards settings. This date will be in the site local time zone and may be **null**. |
| `points` | `int` | Optional | The amount of points the client earned or redeemed. |

## Example (as JSON)

```json
{
  "ActionDateTime": "2016-03-13T12:52:32.123Z",
  "Action": "Removed",
  "Source": "Source8",
  "SourceID": 80,
  "ExpirationDateTime": "2016-03-13T12:52:32.123Z"
}
```

