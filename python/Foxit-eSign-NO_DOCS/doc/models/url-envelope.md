
# URL Envelope

An Envelope meant to be used when sending documents via URLs

## Structure

`URLEnvelope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `folder_name` | `str` | Required | Name of the document(s) folder |
| `input_type` | `str` | Optional | Value can be either url or base64 |
| `file_urls` | `List[str]` | Required | - |
| `file_names` | `List[str]` | Required | - |
| `parties` | [`List[Party]`](../../doc/models/party.md) | Required | - |
| `fields` | `List[Any]` | Optional | - |
| `send_now` | `bool` | Optional | Use this field to send the folder to the recipient parties. Each party will then receive a unique link in their email to sign the document. The invitation mail and subject in this case will be the same as the default invitation mail setup in your account.<br><br>**Default**: `True` |
| `create_embedded_signing_session` | `bool` | Required | Signing session token will be generated without sending out emails to the recipients.<br><br>**Default**: `True` |
| `create_embedded_signing_session_for_all_parties` | `bool` | Optional | **Default**: `True` |
| `process_text_tags` | `bool` | Required | Value can be either true or false. This field is used to determine whether Foxit eSign should parse the documents for Text Tags to convert them into Foxit eSign fields.<br><br>**Default**: `False` |
| `process_acro_fields` | `bool` | Required | This field is used to determine whether Foxit eSign should parse the documents for AcroFields to convert them into Foxit eSign fields.<br><br>**Default**: `False` |
| `sign_in_sequence` | `bool` | Optional | This field is used to determine whether recipients will sign the envelope documents in a sequence. If false, then all the recipients receive invitation email simultaneously. When true, then each recipient receives invitation email successively after previous recipient completes the required task, like signing the documents or filling fields, etc.<br><br>**Default**: `False` |
| `in_person_enable` | `bool` | Optional | This field is used to initiate the in-person signing process which can be easily completed on any device in a matter of minutes and avoids email based signatures where required. If false, then all the recipients receive the invitation email simultaneously. When true, then in-person administrator receives an invitation email to initiate the signing process for the signer.<br><br>**Default**: `False` |
| `custom_field_1` | [`CustomField`](../../doc/models/custom-field.md) | Optional | Maximum of two custom fields can be passed to Foxit eSign via API that are stored at the folder level. Webhook response includes these custom field. |
| `fix_recipient_parties` | `bool` | Optional | If true, then in the embedded sending view cannot change the parties for the envelope which are already added as a part of this API request.<br><br>**Default**: `False` |
| `fix_documents` | `bool` | Optional | If true, then in the embedded sending cannot change the documents for the envelope which are already added as a part of this API request.<br><br>**Default**: `False` |
| `send_success_url` | `str` | Optional | Enter the absolute URL for the landing page, which the signer will be redirected to after successfully sending the folder in the embedded sending view. |
| `send_error_url` | `str` | Optional | Enter the absolute URL for the landing page, which the signer will be redirected to if error comes during sending the folder in the embedded sending view. |
| `create_embedded_sending_session` | `bool` | Optional | If set to true, it will generate an embedded token to open the document preparing view of Foxit eSign.<br><br>**Default**: `False` |
| `embedded_signers_email_ids` | `List[str]` | Optional | An array of email ids of recipients for whom an embedded signing session needs to be created. The email ids from the recipient parties added in the parties list. |
| `sign_success_url` | `str` | Optional | Enter the absolute URL for the signers who will be redirected to after successfully signing in embedded signing view. |
| `sign_decline_url` | `str` | Optional | Enter the absolute URL for the signers who will be redirected to if declines to sign in embedded signing view. |
| `sign_later_url` | `str` | Optional | Enter the absolute URL for the signers who will be redirected to if chooses to sign later in embedded signing view. |
| `sign_error_url` | `str` | Optional | Enter the absolute URL for the signers who will be redirected to if error comes during signing the document in embedded signing view. |
| `allow_send_now_and_embedded_signing_session` | `bool` | Optional | If set as true, Foxit eSign will send unique signing link to each recipient. This is ONLY applicable when parameters sendNow and createEmbeddedSigningSession is true.<br><br>**Default**: `False` |
| `allow_advanced_email_validation` | `bool` | Optional | Validate the email address of the parties when set as true.<br><br>**Default**: `False` |
| `sign_success_url_all_parties` | `bool` | Optional | If set as true, signer will be redirected to URL provided in the signSuccessUrl after successfully signing. This is only applicable when the sendNow is true.<br><br>**Default**: `False` |
| `email_template_id` | `int` | Optional | Pass the email template Id to send the email templates other than default email templates. |
| `signer_instruction_id` | `int` | Optional | Pass the instruction Id to send signer instructions other than the default signer instructions |
| `confirmation_instruction_id` | `str` | Optional | Pass the confirmation instruction id to send confirmation instructions other than the default confirmation instructions. |
| `theme_color` | `str` | Optional | Enter the CSS value to set the theme color. |
| `session_expire` | `bool` | Optional | Set as true to initiate the expire of the embedded signing session.<br><br>**Default**: `False` |
| `expiry` | `int` | Optional | Required if sessionExpire is true. Enter duration in milliseconds of the expiry on the embedded signing session. |
| `dependent_fields` | [`DependentField`](../../doc/models/dependent-field.md) | Optional | - |
| `metadata` | `Any` | Optional | This should be in key value pair. Maximum 1000 key value pairs are allowed. |
| `sender_email` | `str` | Optional | enter email of another user in your account which will be used for sending this document(s) folder to the recipient parties. |
| `hide_add_me_button` | `bool` | Optional | If true, it will hide the "Add Me" button on Recipient Parties in an embedded sending session.<br><br>**Default**: `False` |
| `hide_add_new_button` | `bool` | Optional | If true, it will hide the "Add New" button on Recipient Parties in an embedded sending session.<br><br>**Default**: `False` |
| `hide_add_group_button` | `bool` | Optional | If true, it will hide the "Add Group" button on Recipient Parties in an embedded sending session.<br><br>**Default**: `False` |
| `hide_field_name_for_recipients` | `bool` | Optional | Hide field names for Recipients for Data Entry Fields and Advanced Fields. (Except Radio button, Checkbox, Image and Hyperlink).<br><br>**Default**: `False` |
| `hide_checkbox_border` | `bool` | Optional | Borders of Checkbox will be hidden in the executed documents.<br><br>**Default**: `False` |
| `hide_signer_select_option` | `bool` | Optional | If true, it will hide the "Existing Signer Name/Email" input box on Recipient Parties in an embedded sending session.<br><br>**Default**: `False` |
| `hide_signer_actions` | `bool` | Optional | If true, it will hide the signer "edit", "change" and "remove" actions on Recipient Parties in an embedded sending session.<br><br>**Default**: `False` |
| `hide_sender_name` | `bool` | Optional | If true, it will hide the sender name on Recipient Parties in an embedded sending session.<br><br>**Default**: `False` |
| `hide_folder_name` | `bool` | Optional | If true, it will hide the folder name on navigation in both embedded sessions.<br><br>**Default**: `False` |
| `hide_documents_name` | `bool` | Optional | If true, it will hide the document name in both embedded sessions.<br><br>**Default**: `False` |
| `hide_decline_to_sign` | `bool` | Optional | If true, it will hide the option of "Decline to Sign" for the signer.<br><br>**Default**: `False` |
| `hide_more_action` | `bool` | Optional | If true, it will hide "More Actions" button in sending/signing session. In case of "Send Now": true, it will not hide anything.<br><br>**Default**: `False` |
| `hide_send_button` | `bool` | Optional | If true, it will hide the Send button in the embedded sending session.<br><br>**Default**: `False` |
| `hide_next_required_fieldbtn` | `bool` | Optional | **Default**: `False` |
| `required_both_embedded_session` | `bool` | Optional | If true, it will generate the embedded sending and signing URLs together.<br><br>**Default**: `False` |
| `folder_password` | `str` | Optional | This password will be required by the signer/author in order to open the digitally signed document. If the parameter is kept blank then no password will be required to open the digitally signed document. |
| `enable_step_by_step` | `bool` | Optional | To enable step by step action in the embedded sending session.<br><br>**Default**: `False` |
| `hide_add_parties_option` | `bool` | Optional | If true, it will hide the option to add parties option in Draft and Template Creation mode.<br><br>**Default**: `False` |
| `self_sign` | `bool` | Optional | It enables embedded Self Sign via APIs. This parameter is only applicable when the createEmbeddedSendingSession parameter is true.<br><br>**Default**: `False` |
| `self_signer_success_url` | `str` | Optional | Enter the absolute URL for the landing page on your website/application, which the user will be redirected to after successfully Self Sign sending the folder in the embedded sending view. |

## Example (as JSON)

```json
{
  "folderName": "Foxit eSign Contract.pdf",
  "inputType": "url",
  "fileUrls": [
    "https://www.esigngenie.com/wp-content/uploads/2022/04/Orange.pdf"
  ],
  "fileNames": [
    "Foxit eSign Contract.pdf"
  ],
  "processTextTags": false,
  "processAcroFields": false,
  "parties": [
    {
      "firstName": "Peter",
      "lastName": "Parker",
      "emailId": "spiderman@demo.com",
      "permission": "FILL_FIELDS_AND_SIGN",
      "sequence": 1,
      "allowNameChange": "false",
      "signerAuthLevel": "Voice Access Code",
      "isPlaceholder": false,
      "partyRole": "partyRole4",
      "partyIsEmailGroup": "partyIsEmailGroup8"
    }
  ],
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
  "createEmbeddedSigningSessionForAllParties": true,
  "signInSequence": false
}
```

