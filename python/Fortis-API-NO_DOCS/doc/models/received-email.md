
# Received Email

## Structure

`ReceivedEmail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subject` | `str` | Optional | Subject<br><br>**Constraints**: *Maximum Length*: `256` |
| `body` | `str` | Optional | Body |
| `source_address` | `str` | Optional | Source Address<br><br>**Constraints**: *Maximum Length*: `64` |
| `return_path` | `str` | Optional | Return Path<br><br>**Constraints**: *Maximum Length*: `64` |
| `provider_id` | `str` | Optional | Provider<br><br>**Constraints**: *Maximum Length*: `60` |
| `domain_id` | `str` | Optional | Domain<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `reason_sent` | `str` | Optional | Reason Sent<br><br>**Constraints**: *Maximum Length*: `36` |
| `reason_model` | [`ReasonModelEnum`](../../doc/models/reason-model-enum.md) | Optional | Reason Model<br><br>**Constraints**: *Maximum Length*: `64` |
| `reason_model_id` | `str` | Optional | Reason Model<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `reply_to` | `str` | Optional | Reply To<br><br>**Constraints**: *Maximum Length*: `520` |
| `id` | `str` | Optional | Log Email Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `created_ts` | `int` | Optional | Created Time Stamp |

## Example (as JSON)

```json
{
  "subject": "Payment Receipt - 12skiestech",
  "body": "This email is being sent from a server.",
  "source_address": "\"12skiestech A7t3qi\" <noreply@zeamster.email>",
  "return_path": "\"12skiestech A7t3qi\" <noreply@zeamster.email>",
  "provider_id": "0100017e67bcc530-e1dd23b4-8a39-4a5b-8d5d-68d51c4c942f-000000",
  "domain_id": "11e95f8ec39de8fbdb0a4f1a",
  "reason_sent": "Contact Email",
  "reason_model": "Transaction",
  "reason_model_id": "11e95f8ec39de8fbdb0a4f1a",
  "reply_to": "\"Zeamster\" <emma.p@zeamster.com>",
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "created_ts": 1422040992
}
```

