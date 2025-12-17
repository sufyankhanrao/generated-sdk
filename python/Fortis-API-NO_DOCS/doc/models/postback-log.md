
# Postback Log

## Structure

`PostbackLog`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `postback_status_id` | [`PostbackStatusIdEnum`](../../doc/models/postback-status-id-enum.md) | Optional | Postback Status Id |
| `id` | `str` | Optional | Postback Log Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `postback_config_id` | `str` | Optional | Postback Config Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `changelog_id` | `str` | Optional | Changelog Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `http_verb` | `str` | Optional | Http Verb |
| `next_run_ts` | `int` | Optional | Next Run |
| `created_ts` | `int` | Optional | Created Time Stamp |
| `model` | `str` | Optional | MOdel |
| `model_id` | `str` | Optional | Model Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |

## Example (as JSON)

```json
{
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "postback_config_id": "11e95f8ec39de8fbdb0a4f1a",
  "changelog_id": "11e95f8ec39de8fbdb0a4f1a",
  "next_run_ts": 1422040992,
  "created_ts": 1422040992,
  "model_id": "11e95f8ec39de8fbdb0a4f1a",
  "postback_status_id": 3,
  "http_verb": "http_verb8"
}
```

