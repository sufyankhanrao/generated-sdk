
# URL Template

Create a template by uploading a PDF document using URL or Base64. To create a template from a PDF file, either provide publicly accessible URLs to PDF documents or pass PDF documents as multipart form data with the number of recipient parties, etc.

## Structure

`URLTemplate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `template_name` | `str` | Required | Name of the template |
| `template_url` | `str` | Required | URL to PDF document for template creation. It should be publicly accessible while creating the template. |
| `input_type` | `str` | Optional | Value can be either url or base64.<br><br>**Default**: `'url'` |
| `process_text_tags` | `bool` | Required | This field is used to determine whether Foxit eSign should parse the documents for Text Tags to convert them into Foxit eSign fields.<br><br>**Default**: `True` |
| `process_acro_fields` | `bool` | Required | This field is used to determine whether Foxit eSign should parse the documents for AcroFields to convert them into Foxit eSign fields. |
| `share_all` | `bool` | Required | Share this template with all users in your account.<br><br>**Default**: `False` |
| `number_of_parties` | `int` | Required | Add number of parties in the template. The values of this parameter should be less than 20. |
| `theme_color` | `str` | Optional | Enter a css value for a color to change the theme of createEmbeddedTemplateSession . |
| `author_email` | `str` | Optional | Enter email of another user in an account which will be used as the author for this template. |
| `create_embedded_template_session` | `bool` | Optional | If set as true, an embedded template session to directly open the Foxit eSign template preparing view. Dragging and dropping various fields on the template will be available.<br><br>**Default**: `False` |
| `redirect_url` | `str` | Optional | If createEmbeddedTemplateSession is true, the absolute URL can be entered for the landing page on any website/application, which the user will be redirected to after clicking "save and close" in the embedded template view. |
| `hide_send_template` | `bool` | Optional | If true, it will hide the Send button in an embedded template view.<br><br>**Default**: `False` |
| `fix_recipient_parties` | `bool` | Optional | If true, then in the embedded template view cannot change the parties for the envelope which are already added.<br><br>**Default**: `False` |
| `fields` | `List[Any]` | Optional | A list of different fields to be added to the template. |
| `parties` | [`List[TemplateParty]`](../../doc/models/template-party.md) | Required | A list of parties to be adding in the template. Every entry must contain sequence field. |
| `hide_more_action` | `bool` | Optional | If true, it will hide "More Actions" button in template session.<br><br>**Default**: `False` |
| `hide_share_with_all` | `bool` | Optional | If true, it will hide "Share with All" option in template session.<br><br>**Default**: `False` |
| `hide_add_party` | `bool` | Optional | If true, it will hide all add party's options in an embedded template session.<br><br>**Default**: `False` |
| `hide_me_button` | `bool` | Optional | If true, it will hide the "Me" button on Recipient Parties in an embedded template session.<br><br>**Default**: `False` |
| `hide_others_button` | `bool` | Optional | If true, it will hide the "Others" button on Recipient Parties in an embedded template session.<br><br>**Default**: `False` |
| `hide_existing_contact_select_option` | `bool` | Optional | If true, it will hide the "Find and Add Existing Contact" input box on Recipient Parties in an embedded template session. |
| `hide_field_name_for_recipients` | `bool` | Optional | Hide field names for Recipients for Data Entry Fields and Advanced Fields.(Except Radio button, Checkbox, Image and Hyperlink).<br><br>**Default**: `False` |
| `hide_checkbox_border` | `bool` | Optional | Borders of Checkbox will be hidden in the executed documents.<br><br>**Default**: `False` |

## Example (as JSON)

```json
{
  "templateName": "onboardingmulti_2.pdf",
  "inputType": "url",
  "templateUrl": "https://developers.esigngenie.com/uploads/eSignGenieAPISampleDoc.pdf",
  "processTextTags": true,
  "processAcroFields": true,
  "numberOfParties": 2,
  "themeColor": "#42caf4",
  "shareAll": false,
  "authorEmail": "jon.doe@ggmail.com",
  "createEmbeddedTemplateSession": true,
  "fields": [
    {
      "type": "text",
      "x": 348,
      "y": 157,
      "width": 171,
      "height": 28,
      "pageNumber": 1,
      "documentNumber": 1,
      "hideFieldNameForRecipients": true,
      "name": "Number(fillable) d0107804-ce35-45e8-8d06-a26d67f0d9bd",
      "tooltip": "First Name",
      "value": "",
      "required": false,
      "characterLimit": 100,
      "party": 1,
      "fontSize": 12,
      "fontColor": "#000000",
      "options": [
        "None"
      ],
      "tabOrder": 1
    },
    {
      "type": "text",
      "x": 348,
      "y": 257,
      "width": 171,
      "height": 28,
      "pageNumber": 1,
      "documentNumber": 1,
      "hideFieldNameForRecipients": true,
      "name": "Number(fillable) d0107804-ce35-45e8-8d06-a26d67a1e9ee",
      "tooltip": "Last Name",
      "value": "",
      "required": false,
      "characterLimit": 100,
      "party": 1,
      "fontSize": 12,
      "fontColor": "#000000",
      "options": [
        "None"
      ],
      "tabOrder": 2
    },
    {
      "type": "checkbox",
      "x": 348,
      "y": 357,
      "width": 13,
      "height": 13,
      "pageNumber": 1,
      "documentNumber": 1,
      "name": "isBorn",
      "tooltip": "First child?",
      "required": false,
      "party": 1,
      "group": null,
      "multicheck": true,
      "checked": true,
      "tabOrder": 3,
      "hideCheckboxBorder": true
    },
    {
      "type": "date",
      "x": 348,
      "y": 457,
      "width": 60,
      "height": 13,
      "pageNumber": 1,
      "documentNumber": 1,
      "tooltip": "Date this is signed",
      "required": true,
      "party": 1,
      "name": "exampleDateField",
      "hideFieldNameForRecipients": true,
      "value": "",
      "dateFormat": "MM-DD-YYYY"
    }
  ],
  "parties": [
    {
      "permission": "FILL_FIELDS_AND_SIGN",
      "sequence": 1,
      "partyRole": "Manager"
    },
    {
      "permission": "FILL_FIELDS_AND_SIGN",
      "sequence": 2,
      "partyRole": "Manager 2"
    }
  ],
  "redirectURL": "redirectURL4"
}
```

