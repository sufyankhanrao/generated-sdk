
# Log Sms

Log Sms Information on `expand`

## Structure

`LogSms`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Log Sms Id<br><br>**Constraints**: *Maximum Length*: `24`, *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `body` | `str` | Optional | Body |
| `reason_model` | `str` | Optional | Reason Model<br><br>**Constraints**: *Maximum Length*: `24` |
| `reason_model_id` | `str` | Optional | Reason Model ID<br><br>**Constraints**: *Maximum Length*: `36` |
| `provider_id` | `str` | Optional | Provider ID<br><br>**Constraints**: *Maximum Length*: `60` |
| `status` | `str` | Optional | Status<br><br>**Constraints**: *Maximum Length*: `10` |
| `sender` | `str` | Optional | Sender<br><br>**Constraints**: *Maximum Length*: `10` |
| `recipient` | `str` | Optional | Recipient<br><br>**Constraints**: *Maximum Length*: `10` |
| `created_ts` | `int` | Optional | Created Time Stamp |
| `created_user_id` | `str` | Optional | User ID Created the register<br><br>**Constraints**: *Maximum Length*: `36`, *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |

## Example (as JSON)

```json
{
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "created_ts": 1422040992,
  "created_user_id": "11e95f8ec39de8fbdb0a4f1a",
  "body": "body2",
  "reason_model": "reason_model2",
  "reason_model_id": "reason_model_id8",
  "provider_id": "provider_id8"
}
```

