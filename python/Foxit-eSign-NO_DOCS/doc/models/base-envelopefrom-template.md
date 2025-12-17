
# Base Envelopefrom Template

## Structure

`BaseEnvelopefromTemplate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `folder_name` | `str` | Optional | Name of the document(s) folder. If this value is not provided, then the document(s) folder name is kept same as the template(s) name(s). |
| `template_ids` | `List[int]` | Required | An array of template IDs you want to use to create the documents for this folder. |
| `fields` | `Any` | Optional | You may pass of the field values used in the templates to prefill them in the documents created from the template. FIELD_NAME is the name of the field used in the template. FIELD_VALUE is the document field value. |
| `allow_advanced_email_validation` | `bool` | Optional | Validate the email addresses of the parties when set as true. |
| `parties` | [`List[Party]`](../../doc/models/party.md) | Required | List of recipients with first name, last name and email address. |
| `folder_password` | `str` | Optional | This password will be required by the signer/author in order to open the digitally signed document. If the parameter is kept blank then no password will be required to open the digitally signed document. |
| `sign_in_sequence` | `bool` | Optional | This field is used to determine whether recipients will sign the envelope documents in a sequence. If false, then all the recipients receive invitation email simultaneously. When true, then each recipient receives invitation email successively after previous recipient completes the required task, like signing the documents or filling fields, etc. |
| `in_person_enable` | `bool` | Optional | This field is used to initiate the in-person signing process which can be easily completed on any device in a matter of minutes and avoids email based signatures where required. If false, then all the recipients receive the invitation email simultaneously. When true, then in-person administrator receives an invitation email to initiate the signing process for the signer. |
| `send_now` | `bool` | Optional | Use this field to send the folder to the recipient parties. Each party will then receive a unique link in their email to sign the document. The invitation mail and subject in this case will be the same as the default invitation mail setup in your account. |
| `sign_success_url_all_parties` | `bool` | Optional | If set as true, signer will be redirected to URL provided in the signSuccessUrl after successfully signing. This is only applicable when the sendNow is true. |
| `create_embedded_sending_session` | `bool` | Optional | If set to true, it will generate an embedded URL to open the document preparing view of Foxit eSign. |
| `fix_recipient_parties` | `bool` | Optional | If true, then in the embedded sending view cannot change the parties for the envelope which are already added as a part of this API request. |
| `fix_documents` | `bool` | Optional | If true, then in the embedded sending cannot change the documents for the envelope which are already added as a part of this API request. |
| `send_success_url` | `str` | Optional | Enter the absolute URL for the landing page, which the signer will be redirected to after successfully sending the folder in the embedded sending view. |
| `send_error_url` | `str` | Optional | Enter the absolute URL for the landing page, which the signer will be redirected to if error comes during sending the folder in the embedded sending view. |
| `hide_signer_select_option` | `bool` | Optional | If true, it will hide the "Existing Signer Name/Email" input box on Recipient Parties in an embedded sending session. |
| `hide_signer_actions` | `bool` | Optional | If true, it will hide the signer "edit", "change" and "remove" actions on Recipient Parties in an embedded sending session. |
| `hide_sender_name` | `bool` | Optional | If true, it will hide the sender name on Recipient Parties in an embedded sending session. |
| `hide_send_button` | `bool` | Optional | If true, it will hide the Send button in the embedded sending session. |
| `hide_folder_name` | `bool` | Optional | If true, it will hide the folder name on navigation in both embedded sessions. |
| `hide_documents_name` | `bool` | Optional | If true, it will hide the document name in both embedded sessions. |
| `hide_add_me_button` | `bool` | Optional | If true, it will hide the "Add Me" button on Recipient Parties in an embedded sending session. |
| `hide_add_new_button` | `bool` | Optional | If true, it will hide the "Add New" button on Recipient Parties in an embedded sending session. |
| `hide_add_group_button` | `bool` | Optional | If true, it will hide the "Add Group" button on Recipient Parties in an embedded sending session. |
| `create_embedded_signing_session` | `bool` | Optional | Signing session token will be generated without sending out emails to the recipients. |
| `create_embedded_signing_session_for_all_parties` | `bool` | Optional | - |
| `embedded_signers_email_ids` | `List[str]` | Optional | An array of email ids of recipients for whom an embedded signing session needs to be created. The email ids from the recipient parties added in the parties list. |
| `sign_success_url` | `str` | Optional | Enter the absolute URL for the signers who will be redirected to after successfully signing in embedded signing view. |
| `sign_decline_url` | `str` | Optional | Enter the absolute URL for the signers who will be redirected to if declines to sign in embedded signing view. |
| `sign_later_url` | `str` | Optional | Enter the absolute URL for the signers who will be redirected to if chooses to sign later in embedded signing view. |
| `sign_error_url` | `str` | Optional | Enter the absolute URL for the signers who will be redirected to if error comes during signing the document in embedded signing view. |
| `hide_next_required_field_btn` | `bool` | Optional | - |
| `theme_color` | `str` | Optional | Enter the CSS value to set the theme color. |
| `hide_decline_to_sign` | `bool` | Optional | - |
| `hide_more_action` | `bool` | Optional | - |
| `hide_add_parties_option` | `bool` | Optional | - |
| `session_expire` | `bool` | Optional | Set as true to initiate the expire of the embedded signing session. |
| `expiry` | `int` | Optional | Required if sessionExpire is true. Enter duration in milliseconds of the expiry on the embedded signing session. |
| `sender_email` | `str` | Optional | enter email of another user in your account which will be used for sending this document(s) folder to the recipient parties. |
| `allow_send_now_and_embedded_signing_session` | `bool` | Optional | - |
| `enable_step_by_step` | `bool` | Optional | To enable step by step action in the embedded sending session.<br><br>**Default**: `False` |
| `custom_field` | [`CustomField`](../../doc/models/custom-field.md) | Optional | - |

## Example (as JSON)

```json
{
  "folderName": "Testing Flow1",
  "templateIds": [
    271591
  ],
  "allowAdvancedEmailValidation": false,
  "parties": [
    {
      "firstName": "FIRST_NAME_OF_RECIPIENT_PARTY",
      "lastName": "LAST_NAME_OF_RECIPIENT_PARTY",
      "emailId": "peter.parker@spiderman.com",
      "permission": "FILL_FIELDS_AND_SIGN",
      "workflowSequence": 1,
      "sequence": 1,
      "hostEmailId": "EMAIL_ID_OF_INPERSON_ADMINISTRATOR",
      "allowNameChange": "true",
      "signerAuthLevel": "NO",
      "isPlaceholder": false,
      "partyRole": "partyRole4",
      "partyIsEmailGroup": "partyIsEmailGroup8"
    },
    {
      "firstName": "FIRST_NAME_OF_RECIPIENT_PARTY",
      "lastName": "LAST_NAME_OF_RECIPIENT_PARTY",
      "emailId": "bruce@batman.com",
      "permission": "FILL_FIELDS_AND_SIGN",
      "workflowSequence": 2,
      "sequence": 2,
      "hostEmailId": "EMAIL_ID_OF_INPERSON_ADMINISTRATOR",
      "allowNameChange": "true",
      "signerAuthLevel": "NO",
      "isPlaceholder": false,
      "partyRole": "partyRole4",
      "partyIsEmailGroup": "partyIsEmailGroup8"
    }
  ],
  "signInSequence": false,
  "inPersonEnable": false,
  "sendNow": true,
  "signSuccessUrlAllParties": false,
  "createEmbeddedSendingSession": true,
  "fixRecipientParties": true,
  "fixDocuments": true,
  "sendSuccessUrl": "YOUR_PAGE_TO_REDIRECT_USER_FROM_EMBEDDED_SESSION",
  "sendErrorUrl": "YOUR_PAGE_TO_REDIRECT_USER_FROM_EMBEDDED_SESSION",
  "hideSignerSelectOption": false,
  "hideSignerActions": false,
  "hideSenderName": true,
  "hideSendButton": true,
  "hideFolderName": false,
  "hideDocumentsName": true,
  "hideAddMeButton": false,
  "hideAddNewButton": true,
  "hideAddGroupButton": false,
  "createEmbeddedSigningSession": true,
  "createEmbeddedSigningSessionForAllParties": false,
  "embeddedSignersEmailIds": [
    "peter.parker@spiderman.com",
    "bruce@batman.com"
  ],
  "signSuccessUrl": "YOUR_PAGE_TO_REDIRECT_USER_FROM_EMBEDDED_SESSION",
  "signDeclineUrl": "YOUR_PAGE_TO_REDIRECT_USER_FROM_EMBEDDED_SESSION",
  "signLaterUrl": "YOUR_PAGE_TO_REDIRECT_USER_FROM_EMBEDDED_SESSION",
  "signErrorUrl": "YOUR_PAGE_TO_REDIRECT_USER_FROM_EMBEDDED_SESSION",
  "hideNextRequiredFieldBtn": false,
  "themeColor": "ANY_CSS_COLOR_TO_MATCH_YOUR_APPLICATION",
  "hideDeclineToSign": false,
  "hideMoreAction": false,
  "hideAddPartiesOption": false,
  "sessionExpire": false,
  "expiry": 300000,
  "senderEmail": "jon.dpe@ggmail.com",
  "allowSendNowAndEmbeddedSigningSession": false,
  "enableStepByStep": false,
  "fields": {
    "key1": "val1",
    "key2": "val2"
  },
  "folderPassword": "folderPassword8"
}
```

