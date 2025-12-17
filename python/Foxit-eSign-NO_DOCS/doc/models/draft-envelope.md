
# Draft Envelope

An Envelope meant to be used when sending documents via URLs

## Structure

`DraftEnvelope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `folder_id` | `int` | Required | Envelope Id that has been saved in the draft with documents. |
| `folder_name` | `str` | Required | Name of the document(s) folder |
| `parties` | [`List[Party]`](../../doc/models/party.md) | Required | List of recipient parties can be added in the draft. Every entry must contain firstName, lastName, emailId, permission and sequence fields. |
| `sign_in_sequence` | `bool` | Optional | This field is used to determine whether recipients will sign the envelope documents in a sequence. If false, then all the recipients receive invitation email simultaneously. When true, then each recipient receives invitation email successively after previous recipient completes the required task, like signing the documents or filling fields, etc.<br><br>**Default**: `False` |
| `in_person_enable` | `bool` | Optional | This field is used to initiate the in-person signing process which can be easily completed on any device in a matter of minutes and avoids email based signatures where required. If false, then all the recipients receive the invitation email simultaneously. When true, then in-person administrator receives an invitation email to initiate the signing process for the signer.<br><br>**Default**: `False` |
| `fields` | `List[Any]` | Optional | - |
| `send_now` | `bool` | Optional | Use this field to send the folder to the recipient parties. Each party will then receive a unique link in their email to sign the document. The invitation mail and subject in this case will be the same as the default invitation mail setup in your account.<br><br>**Default**: `True` |
| `create_embedded_signing_session` | `bool` | Optional | Signing session token will be generated without sending out emails to the recipients.<br><br>**Default**: `False` |
| `embedded_signers_email_ids` | `List[str]` | Optional | An array of email ids of recipients for whom an embedded signing session needs to be created. The email ids from the recipient parties added in the parties list. |
| `custom_field_1` | [`CustomField`](../../doc/models/custom-field.md) | Optional | Maximum of two custom fields can be passed to Foxit eSign via API that are stored at the folder level. Webhook response includes these custom field. |
| `sign_success_url` | `str` | Optional | Enter the absolute URL for the signers who will be redirected to after successfully signing in embedded signing view. |
| `sign_decline_url` | `str` | Optional | Enter the absolute URL for the signers who will be redirected to if declines to sign in embedded signing view. |
| `sign_later_url` | `str` | Optional | Enter the absolute URL for the signers who will be redirected to if chooses to sign later in embedded signing view. |
| `sign_error_url` | `str` | Optional | Enter the absolute URL for the signers who will be redirected to if error comes during signing the document in embedded signing view. |
| `allow_send_now_and_embedded_signing_session` | `bool` | Optional | If set as true, Foxit eSign will send unique signing link to each recipient. This is ONLY applicable when parameters sendNow and createEmbeddedSigningSession is true.<br><br>**Default**: `False` |
| `allow_advanced_email_validation` | `bool` | Optional | Validate the email address of the parties when set as true.<br><br>**Default**: `False` |
| `sign_success_url_all_parties` | `bool` | Optional | If set as true, signer will be redirected to URL provided in the signSuccessUrl after successfully signing. This is only applicable when the sendNow is true.<br><br>**Default**: `False` |
| `email_template_id` | `int` | Optional | Pass the email template Id to send the email templates other than default email templates. |
| `signer_instruction_id` | `int` | Optional | Pass the instruction Id to send signer instructions other than the default signer instructions |
| `confirmation_instruction_id` | `int` | Optional | Pass the confirmation instruction id to send confirmation instructions other than the default confirmation instructions. |
| `theme_color` | `str` | Optional | Enter the CSS value to set the theme color. |
| `session_expire` | `bool` | Optional | Set as true to initiate the expire of the embedded signing session.<br><br>**Default**: `False` |
| `expiry` | `int` | Optional | Required if sessionExpire is true. Enter duration in milliseconds of the expiry on the embedded signing session. |
| `sender_email` | `str` | Optional | enter email of another user in your account which will be used for sending this document(s) folder to the recipient parties. |
| `create_executed_folder` | `bool` | Optional | If true, Envelope automatically executed with existing party.<br><br>**Default**: `False` |
| `hide_field_name_for_recipients` | `bool` | Optional | Hide field names for Recipients for Data Entry Fields and Advanced Fields. (Except Radio button, Checkbox, Image and Hyperlink).<br><br>**Default**: `False` |
| `hide_checkbox_border` | `bool` | Optional | Borders of Checkbox will be hidden in the executed documents.<br><br>**Default**: `False` |
| `hide_decline_to_sign` | `bool` | Optional | If true, it will hide the option of "Decline to Sign" for the signer.<br><br>**Default**: `False` |
| `hide_more_action` | `bool` | Optional | If true, it will hide "More Actions" button in sending/signing session. In case of "Send Now": true, it will not hide anything.<br><br>**Default**: `False` |
| `hide_next_required_fieldbtn` | `bool` | Optional | **Default**: `False` |
| `folder_password` | `str` | Optional | This password will be required by the signer/author in order to open the digitally signed document. If the parameter is kept blank then no password will be required to open the digitally signed document. |

## Example (as JSON)

```json
{
  "folderId": 2520579,
  "folderName": "Example Documents",
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
  ],
  "signInSequence": false,
  "inPersonEnable": false,
  "fields": [
    {
      "type": "text",
      "name": "Signer Name",
      "x": 108,
      "y": 500,
      "width": 60,
      "height": 20,
      "documentNumber": 1,
      "pageNumber": 1,
      "tabOrder": 1,
      "party": 1,
      "tooltip": "",
      "required": true,
      "characterLimit": 100,
      "fontSize": 12,
      "fontColor": "#000000",
      "hideFieldNameForRecipients": false
    },
    {
      "type": "date",
      "x": 336,
      "y": 500,
      "width": 60,
      "height": 20,
      "documentNumber": 1,
      "pageNumber": 1,
      "tabOrder": 1,
      "party": 1,
      "name": "Date",
      "required": true,
      "fontSize": 12,
      "dateFormat": "MM-DD-YYYY"
    },
    {
      "type": "signature",
      "x": 108,
      "y": 565,
      "width": 60,
      "height": 20,
      "documentNumber": 1,
      "pageNumber": 1,
      "party": 1,
      "required": true
    },
    {
      "type": "date",
      "x": 336,
      "y": 565,
      "width": 60,
      "height": 20,
      "documentNumber": 1,
      "pageNumber": 1,
      "tabOrder": 1,
      "party": 1,
      "name": "Date Signed",
      "required": true,
      "fontSize": 12,
      "dateFormat": "MM-DD-YYYY",
      "readOnly": true,
      "systemField": true
    }
  ],
  "sendNow": true,
  "createEmbeddedSigningSession": true,
  "embeddedSignersEmailIds": [
    "peter@ggmail.com",
    "spidey@ggmail.com"
  ],
  "allowSendNowAndEmbeddedSigningSession": false,
  "allowAdvancedEmailValidation": false,
  "signSuccessUrlAllParties": false,
  "emailTemplateId": 2,
  "signerInstructionId": 1,
  "confirmationInstructionId": 3,
  "sessionExpire": false,
  "senderEmail": "\"user2@example.com\"",
  "createExecutedFolder": false,
  "hideFieldNameForRecipients": false,
  "hideCheckboxBorder": false,
  "hideDeclineToSign": false,
  "hideMoreAction": false,
  "hideNextRequiredFieldbtn": false
}
```

