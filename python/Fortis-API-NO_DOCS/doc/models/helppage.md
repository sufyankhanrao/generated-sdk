
# Helppage

## Structure

`Helppage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_type_code` | [`UserTypeCodeEnum`](../../doc/models/user-type-code-enum.md) | Optional | User Type |
| `body` | `str` | Optional | Body<br><br>**Constraints**: *Maximum Length*: `65000` |
| `title` | `str` | Optional | Title<br><br>**Constraints**: *Maximum Length*: `255` |
| `id` | `str` | Optional | Help Page ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `created_ts` | `int` | Optional | Created Time Stamp |
| `modified_ts` | `int` | Optional | Modified Time Stamp |
| `created_user_id` | `str` | Optional | User ID Created the register<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `modified_user_id` | `str` | Optional | Last User ID that updated the register<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |

## Example (as JSON)

```json
{
  "user_type_code": 100,
  "body": "Sample Body",
  "title": "Sample Title",
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "created_ts": 1422040992,
  "modified_ts": 1422040992,
  "created_user_id": "11e95f8ec39de8fbdb0a4f1a",
  "modified_user_id": "11e95f8ec39de8fbdb0a4f1a"
}
```

