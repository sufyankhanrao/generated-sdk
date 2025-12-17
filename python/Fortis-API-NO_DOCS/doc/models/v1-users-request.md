
# V1 Users Request

## Structure

`V1UsersRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Optional | Account Number |
| `branding_domain_url` | `str` | Optional | Branding Domain Url<br><br>**Constraints**: *Maximum Length*: `64` |
| `cell_phone` | `str` | Optional | Cell Phone<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^\d{10}$` |
| `company_name` | `str` | Optional | Company Name<br><br>**Constraints**: *Maximum Length*: `64` |
| `contact_id` | `str` | Optional | Contact<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `date_of_birth` | `str` | Optional | Date Of Birth<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[\d]{4}-[\d]{2}-[\d]{2}$` |
| `domain_id` | `str` | Optional | Domain<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `email` | `str` | Required | Email<br><br>**Constraints**: *Maximum Length*: `128` |
| `email_trx_receipt` | `bool` | Optional | Email Trx Receipt |
| `home_phone` | `str` | Optional | Home Phone<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^\d{10}$` |
| `first_name` | `str` | Optional | First Name<br><br>**Constraints**: *Maximum Length*: `64` |
| `last_name` | `str` | Required | Last Name<br><br>**Constraints**: *Maximum Length*: `64` |
| `locale` | `str` | Optional | Locale<br><br>**Constraints**: *Maximum Length*: `8` |
| `office_phone` | `str` | Optional | Office Phone<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^\d{10}$` |
| `office_ext_phone` | `str` | Optional | Office Ext Phone<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^\d{1,10}$` |
| `primary_location_id` | `str` | Required | Primary Location ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `requires_new_password` | `str` | Optional | Requires New Password<br><br>**Constraints**: *Maximum Length*: `1` |
| `terms_condition_code` | `str` | Optional | Terms Condition (This field is required when updating your own password). |
| `tz` | `str` | Optional | Time zone<br><br>**Constraints**: *Maximum Length*: `30` |
| `ui_prefs` | [`UiPrefs`](../../doc/models/ui-prefs.md) | Optional | Ui Prefs |
| `username` | `str` | Required | Username<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `64` |
| `user_api_key` | `str` | Optional | User Api Key<br><br>**Constraints**: *Minimum Length*: `16`, *Maximum Length*: `64` |
| `user_hash_key` | `str` | Optional | User Hash Key<br><br>**Constraints**: *Minimum Length*: `24`, *Maximum Length*: `36` |
| `user_type_code` | [`UserTypeCodeEnum`](../../doc/models/user-type-code-enum.md) | Required | User Type |
| `password` | `str` | Optional | Password<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `128`, *Pattern*: ``^(?=.*[`!@#$%^&*()_+\-=\[\]{};':"\\\|,.<>\/?~])(?=.*[0-9])(?=.*[a-zA-Z]).*$`` |
| `zip` | `str` | Optional | Zip<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `10`, *Pattern*: `^[a-zA-Z0-9\-\s]+$` |
| `location_id` | `str` | Optional | Location ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `contact_api_id` | `str` | Optional | ContactApi Id |
| `primary_location_api_id` | `str` | Optional | Primary LocationApi ID |
| `status_code` | [`StatusCodeEnum`](../../doc/models/status-code-enum.md) | Optional | Status Code |
| `api_only` | `bool` | Optional | API Only |
| `is_invitation` | `bool` | Optional | Is Invitation |
| `address` | [`Address2`](../../doc/models/address-2.md) | Optional | Address |

## Example (as JSON)

```json
{
  "account_number": "5454545454545454",
  "branding_domain_url": "{branding_domain_url}",
  "cell_phone": "3339998822",
  "company_name": "Fortis Payment Systems, LLC",
  "contact_id": "11e95f8ec39de8fbdb0a4f1a",
  "date_of_birth": "2021-12-01",
  "domain_id": "11e95f8ec39de8fbdb0a4f1a",
  "email": "email@domain.com",
  "email_trx_receipt": true,
  "home_phone": "3339998822",
  "first_name": "John",
  "last_name": "Smith",
  "locale": "en-US",
  "office_phone": "3339998822",
  "office_ext_phone": "5",
  "primary_location_id": "11e95f8ec39de8fbdb0a4f1a",
  "terms_condition_code": "20220308",
  "tz": "America/New_York",
  "username": "{user_name}",
  "user_api_key": "234bas8dfn8238f923w2",
  "user_type_code": 100,
  "zip": "48375",
  "location_id": "11e95f8ec39de8fbdb0a4f1a",
  "status_code": 1,
  "api_only": false,
  "is_invitation": false
}
```

