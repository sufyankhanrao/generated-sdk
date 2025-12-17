
# Parent 3

Parent Information on `expand`

## Structure

`Parent3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Location ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `created_ts` | `int` | Optional | Created Time Stamp |
| `modified_ts` | `int` | Optional | Modified Time Stamp |
| `account_number` | `str` | Optional | Account number<br><br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `address` | [`Address1`](../../doc/models/address-1.md) | Optional | Address |
| `branding_domain_id` | `str` | Optional | GUID for Branding Domain<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `contact_email_trx_receipt_default` | `bool` | Optional | If true, will email contact receipt for any transaction |
| `default_ach` | `str` | Optional | GUID for Location's default ACH Product Transaction<br><br>**Constraints**: *Minimum Length*: `24`, *Maximum Length*: `36` |
| `default_cc` | `str` | Optional | GUID for Location's default CC Product Transaction<br><br>**Constraints**: *Minimum Length*: `24`, *Maximum Length*: `36` |
| `email_reply_to` | `str` | Optional | Used as from email address when sending various notifications<br><br>**Constraints**: *Maximum Length*: `64` |
| `fax` | `str` | Optional | Fax number<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^\d{10}$` |
| `location_api_id` | `str` | Optional | Location api ID<br><br>**Constraints**: *Maximum Length*: `36` |
| `location_api_key` | `str` | Optional | Location api key<br><br>**Constraints**: *Maximum Length*: `36` |
| `location_c_1` | `str` | Optional | Can be used to store custom information for location.<br><br>**Constraints**: *Maximum Length*: `128` |
| `location_c_2` | `str` | Optional | Can be used to store custom information for location.<br><br>**Constraints**: *Maximum Length*: `128` |
| `location_c_3` | `str` | Optional | Can be used to store custom information for location.<br><br>**Constraints**: *Maximum Length*: `128` |
| `name` | `str` | Optional | Name of the company<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `64` |
| `office_phone` | `str` | Optional | Office phone number<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10` |
| `office_ext_phone` | `str` | Optional | Office phone extension number<br><br>**Constraints**: *Maximum Length*: `10` |
| `tz` | `str` | Optional | Time zone<br><br>**Constraints**: *Maximum Length*: `30` |
| `parent_id` | `str` | Optional | Location GUID of the parent location<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `show_contact_notes` | `bool` | Optional | If set to true will show 'Notes' tab on Contact |
| `show_contact_files` | `bool` | Optional | If set to true will show 'Files' tab on Contact |
| `created_user_id` | `str` | Optional | User ID Created the register<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `location_type` | [`LocationTypeEnum`](../../doc/models/location-type-enum.md) | Optional | Location Type |
| `ticket_hash_key` | `str` | Optional | Ticket Hash Key<br><br>**Constraints**: *Maximum Length*: `36` |

## Example (as JSON)

```json
{
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "created_ts": 1422040992,
  "modified_ts": 1422040992,
  "account_number": "5454545454545454",
  "branding_domain_id": "11e95f8ec39de8fbdb0a4f1a",
  "contact_email_trx_receipt_default": true,
  "default_ach": "11e608a7d515f1e093242bb2",
  "default_cc": "11e608a442a5f1e092242dda",
  "email_reply_to": "email@domain.com",
  "fax": "3339998822",
  "location_api_id": "location-111111",
  "location_api_key": "AE34BBCAADF4AE34BBCAADF4",
  "location_c1": "custom 1",
  "location_c2": "custom 2",
  "location_c3": "custom data 3",
  "name": "Sample Company Headquarters",
  "office_phone": "2481234567",
  "office_ext_phone": "1021021209",
  "tz": "America/New_York",
  "parent_id": "11e95f8ec39de8fbdb0a4f1a",
  "show_contact_notes": true,
  "show_contact_files": true,
  "created_user_id": "11e95f8ec39de8fbdb0a4f1a",
  "location_type": "merchant",
  "ticket_hash_key": "A5F443CADF4AE34BBCAADF4",
  "address": {
    "city": "city6",
    "state": "state2",
    "postal_code": "postal_code8",
    "country": "US",
    "street": "street6"
  }
}
```

