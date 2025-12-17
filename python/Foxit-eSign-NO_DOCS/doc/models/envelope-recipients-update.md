
# Envelope Recipients Update

## Structure

`EnvelopeRecipientsUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `folder_id` | `int` | Required | - |
| `allow_advanced_email_validation` | `bool` | Optional | Choose whether to validate the email address of the recipients.<br><br>**Default**: `False` |
| `parties` | [`List[Party]`](../../doc/models/party.md) | Required | - |

## Example (as JSON)

```json
{
  "folderId": 222,
  "allowAdvancedEmailValidation": false,
  "parties": [
    {
      "firstName": "John",
      "lastName": "Doe",
      "emailId": "john.doe@example.com",
      "permission": "FILL_FIELDS_AND_SIGN",
      "sequence": 1,
      "signerAuthLevel": "Voice Access Code",
      "isPlaceholder": false,
      "partyRole": "partyRole4",
      "allowNameChange": "allowNameChange8",
      "partyIsEmailGroup": "partyIsEmailGroup8"
    }
  ]
}
```

