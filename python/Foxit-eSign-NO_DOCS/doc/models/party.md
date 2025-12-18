
# Party

A list of recipient parties you're sending the folder to. Every entry must contain firstName, lastName, emailId, permission and sequence fields.

## Structure

`Party`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Required | The first name of the recipient |
| `last_name` | `str` | Required | The last name of the recipient |
| `email_id` | `str` | Required | The email name of the recipient |
| `permission` | [`PermissionsEnum`](../../doc/models/permissions-enum.md) | Required | - |
| `sequence` | `int` | Required | Use this field to assign a sequence number to a recipient in the list of recipient parties. Use unique sequence numbers for each party starting with 1 like 1,2,3,4.... If a single person appears multiple times in the signing workflow, please assign a different sequence each time the recipient is repeated. |
| `signer_auth_level` | [`SignerAuthLevelsEnum`](../../doc/models/signer-auth-levels-enum.md) | Optional | The level of authentication that a signer will leverage for verification purposes |
| `is_placeholder` | `bool` | Optional | Use this field to initiate the party is a placeholder. Note: 1. firstName, lastName, emailId parameter's value must be blank of this party. 2. To add the placeholder, one recipient must be requred with 'PARTY_ASSIGNER' permission.<br><br>**Default**: `False` |
| `party_role` | `str` | Optional | Use this field to assign a role of placeholder. |
| `allow_name_change` | `str` | Optional | Value can be either true or false Use this parameter for allowing signer to update first and last name before completing the signing process.<br><br>**Default**: `'false'` |
| `party_is_email_group` | `str` | Optional | Use this parameter when creating a party as bulk. **Note:** Please make sure the "Update Name Change"option is enabled from company settings.<br><br>**Default**: `'false'` |
| `workflow_sequence` | `int` | Optional | **Default**: `1` |
| `host_email_id` | `str` | Optional | Email address of In-Person Administrator |

## Example (as JSON)

```json
{
  "firstName": "John",
  "lastName": "Doe",
  "emailId": "john.doe@example.com",
  "permission": "FILL_FIELDS_AND_SIGN",
  "sequence": 1,
  "signerAuthLevel": "Voice Access Code",
  "isPlaceholder": false,
  "partyRole": "partyRole8",
  "allowNameChange": "allowNameChange4",
  "partyIsEmailGroup": "partyIsEmailGroup2"
}
```

