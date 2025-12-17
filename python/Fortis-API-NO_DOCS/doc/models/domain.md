
# Domain

Domain Information on `expand`

## Structure

`Domain`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Optional | URL<br><br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9]+([\-\.]{1}[a-zA-Z0-9]+)*\.[a-zA-Z]{2,5}$` |
| `title` | `str` | Optional | Domain Name<br><br>**Constraints**: *Maximum Length*: `64` |
| `logo` | `str` | Optional | Logo<br><br>**Constraints**: *Maximum Length*: `64` |
| `support_email` | `str` | Optional | Support Email<br><br>**Constraints**: *Maximum Length*: `64` |
| `allow_contact_signup` | `bool` | Optional | Allow Contact Signup. |
| `allow_contact_registration` | `bool` | Optional | Allow Contact Registration. |
| `allow_contact_login` | `bool` | Optional | Allow Contact Login. |
| `registration_fields` | [`List[RegistrationFieldEnum]`](../../doc/models/registration-field-enum.md) | Optional | Registration Fields |
| `company_name` | `str` | Optional | Company Name.<br><br>**Constraints**: *Maximum Length*: `32` |
| `nav_color` | `str` | Optional | Nav Color.<br><br>**Constraints**: *Maximum Length*: `7` |
| `button_primary_color` | `str` | Optional | Button Primary Color.<br><br>**Constraints**: *Maximum Length*: `7` |
| `logo_background_color` | `str` | Optional | Logo Background Color.<br><br>**Constraints**: *Maximum Length*: `7` |
| `icon_background_color` | `str` | Optional | Icon Background Color.<br><br>**Constraints**: *Maximum Length*: `7` |
| `menu_text_background_color` | `str` | Optional | Menu Text Background Color<br><br>**Constraints**: *Maximum Length*: `7` |
| `menu_text_color` | `str` | Optional | Menu Text Color.<br><br>**Constraints**: *Maximum Length*: `7` |
| `right_menu_background_color` | `str` | Optional | Right Menu Background Color.<br><br>**Constraints**: *Maximum Length*: `7` |
| `right_menu_text_color` | `str` | Optional | Right Menu Text Color.<br><br>**Constraints**: *Maximum Length*: `7` |
| `button_primary_text_color` | `str` | Optional | Button Primary Text Color.<br><br>**Constraints**: *Maximum Length*: `7` |
| `nav_logo` | `str` | Optional | Nav Logo.<br><br>**Constraints**: *Maximum Length*: `256` |
| `fav_icon` | `str` | Optional | Fav Icon.<br><br>**Constraints**: *Maximum Length*: `256` |
| `aes_key` | `str` | Optional | Aes Key.<br><br>**Constraints**: *Maximum Length*: `255` |
| `help_text` | `str` | Optional | Help Text. |
| `email_reply_to` | `str` | Optional | Email Reply To. |
| `email` | `str` | Optional | Email. |
| `custom_javascript` | `str` | Optional | Custom Javascript.<br><br>**Constraints**: *Maximum Length*: `2048`, *Pattern*: `^<script\b[^>]*>([\s\S]*?)<\/script>$` |
| `custom_theme` | `str` | Optional | Custom Theme<br><br>**Constraints**: *Maximum Length*: `48` |
| `custom_css` | `str` | Optional | Custom CSS<br><br>**Constraints**: *Maximum Length*: `2048` |
| `contact_user_default_entry_page` | [`ContactUserDefaultEntryPageEnum`](../../doc/models/contact-user-default-entry-page-enum.md) | Optional | Contact User Default Entry Page |
| `contact_user_default_auth_roles` | `List[Any]` | Optional | Contact User Default Auth Role |
| `custom_stylesheet_url` | `str` | Optional | Custom Stylesheet URL<br><br>**Constraints**: *Maximum Length*: `256` |
| `id` | `str` | Optional | Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `created_ts` | `int` | Optional | Created Time Stamp |
| `modified_ts` | `int` | Optional | Modified Time Stamp |

## Example (as JSON)

```json
{
  "url": "fortispayrbyn9y.sandbox.zeamster.com",
  "title": "Test Brand Domain Title 2",
  "support_email": "email@domain.com",
  "allow_contact_signup": true,
  "allow_contact_registration": true,
  "allow_contact_login": true,
  "registration_fields": [
    "id",
    "email"
  ],
  "email_reply_to": "email@domain.com",
  "email": "email@domain.com",
  "contact_user_default_entry_page": "dashboard",
  "custom_stylesheet_url": "https://127.0.0.1/receiver",
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "created_ts": 1422040992,
  "modified_ts": 1422040992,
  "logo": "logo0"
}
```

