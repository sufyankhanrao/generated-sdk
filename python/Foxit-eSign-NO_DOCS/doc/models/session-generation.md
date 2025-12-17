
# Session Generation

## Structure

`SessionGeneration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `folder_id` | `int` | Required | Folder id you want to use to regenerate the expired folder embedded signing token for this folder. You can determine the folder id from the folder URL. |
| `email_id` | `str` | Required | Recipient email id you want to use to regenerate the expired folder embedded signing token for this folder. |
| `party_id` | `str` | Optional | Recipient party id you want to use to regenerate the expired folder embedded signing token for this folder. |
| `session_expire` | `str` | Optional | Use this field to initiate the expiration of the embedded signing session.<br><br>**Default**: `"false"` |
| `expiry` | `str` | Optional | Use this field to enter the time duration in milliseconds of the expiry on the embedded signing session. *Note*: required if `sessionExpire` is `true` |

## Example (as JSON)

```json
{
  "folderId": 70,
  "emailId": "emailId4",
  "sessionExpire": "false",
  "partyId": "partyId4",
  "expiry": "expiry4"
}
```

