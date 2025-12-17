
# Changelog

## Structure

`Changelog`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Change Log ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `created_ts` | `int` | Optional | Created Time Stamp |
| `action` | `str` | Optional | Action<br><br>**Constraints**: *Maximum Length*: `255` |
| `model` | `str` | Optional | Model<br><br>**Constraints**: *Maximum Length*: `255` |
| `model_id` | `str` | Optional | Model ID<br><br>**Constraints**: *Maximum Length*: `255` |
| `user_id` | `str` | Optional | User ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `changelog_details` | [`List[ChangelogDetail]`](../../doc/models/changelog-detail.md) | Optional | Change Log Details |
| `user` | [`User`](../../doc/models/user.md) | Optional | User |

## Example (as JSON)

```json
{
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "created_ts": 1422040992,
  "action": "CREATE",
  "model": "TransactionRequest",
  "model_id": "11ec829598f0d4008be9aba4",
  "user_id": "11e95f8ec39de8fbdb0a4f1a"
}
```

