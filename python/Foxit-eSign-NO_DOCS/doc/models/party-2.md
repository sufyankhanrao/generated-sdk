
# Party 2

## Structure

`Party2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Required | - |
| `last_name` | `str` | Required | - |
| `email_id` | `str` | Required | - |
| `permission` | `str` | Required | - |
| `workflow_sequence` | `int` | Required | - |
| `sequence` | `int` | Required | - |
| `host_email_id` | `str` | Required | - |
| `allow_name_change` | `bool` | Required | - |
| `dialing_code` | `str` | Optional | - |
| `signer_auth_level` | `str` | Required | - |
| `user_defined_access_code` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "firstName": "FIRST_NAME_OF_RECIPIENT_PARTY",
  "lastName": "LAST_NAME_OF_RECIPIENT_PARTY",
  "emailId": "mhashmi@esigngenie.com",
  "permission": "FILL_FIELDS_AND_SIGN",
  "workflowSequence": 1,
  "sequence": 1,
  "hostEmailId": "EMAIL_ID_OF_INPERSON_ADMINISTRATOR",
  "allowNameChange": true,
  "dialingCode": "+1",
  "signerAuthLevel": "Email Access Code",
  "userDefinedAccessCode": "123@Test"
}
```

