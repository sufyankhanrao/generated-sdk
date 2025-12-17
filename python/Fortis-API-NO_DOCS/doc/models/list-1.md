
# List 1

## Structure

`List1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Optional | Location ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `account_number` | `str` | Optional | Contact Account Number<br><br>**Constraints**: *Maximum Length*: `32` |
| `contact_api_id` | `str` | Optional | Contact API Id<br><br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9]*$` |
| `first_name` | `str` | Optional | First Name<br><br>**Constraints**: *Maximum Length*: `64` |
| `last_name` | `str` | Optional | Last Name<br><br>**Constraints**: *Maximum Length*: `64` |
| `cell_phone` | `str` | Optional | Cell phone of contact<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^\d{10}$` |
| `balance` | `float` | Optional | Balance<br><br>**Constraints**: `>= -99999999.99`, `<= 99999999.99` |
| `address` | [`Address`](../../doc/models/address.md) | Optional | Address of contact |
| `company_name` | `str` | Optional | Company Name<br><br>**Constraints**: *Maximum Length*: `64` |
| `header_message` | `str` | Optional | Header Message<br><br>**Constraints**: *Maximum Length*: `250` |
| `date_of_birth` | `str` | Optional | Contacts DOB, Format: yyyy-MM-dd<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[\d]{4}-[\d]{2}-[\d]{2}$` |
| `email_trx_receipt` | `bool` | Optional | Whether or not to email all transactions receipts to contact (1 or 0) |
| `home_phone` | `str` | Optional | Contacts home phone<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^\d{10}$` |
| `office_phone` | `str` | Optional | Contacts office phone<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^\d{10}$` |
| `office_phone_ext` | `str` | Optional | Contacts office phone extension for office phone<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^\d{1,10}$` |
| `header_message_type` | `int` | Optional | Header Message Type<br><br>**Constraints**: `>= 0`, `<= 4` |
| `update_if_exists` | [`UpdateIfExistsEnum`](../../doc/models/update-if-exists-enum.md) | Optional | Update If Exists |
| `contact_c_1` | `str` | Optional | Custom field 1 for api users to store custom data<br><br>**Constraints**: *Maximum Length*: `128` |
| `contact_c_2` | `str` | Optional | Custom field 2 for api users to store custom data<br><br>**Constraints**: *Maximum Length*: `128` |
| `contact_c_3` | `str` | Optional | Custom field 3 for api users to store custom data<br><br>**Constraints**: *Maximum Length*: `128` |
| `parent_id` | `str` | Optional | Parent Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `email` | `str` | Optional | Email of contact<br><br>**Constraints**: *Maximum Length*: `64` |
| `id` | `str` | Optional | Contact ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `created_ts` | `int` | Optional | Created Time Stamp |
| `modified_ts` | `int` | Optional | Modified Time Stamp |
| `active` | `bool` | Optional | Active |
| `created_user_id` | `str` | Optional | User ID Created the register<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `received_emails` | [`List[ReceivedEmail]`](../../doc/models/received-email.md) | Optional | Received Email Information on `expand` |
| `is_deletable` | `bool` | Optional | Is Deletable Information on `expand` |
| `location` | [`Location`](../../doc/models/location.md) | Optional | Location Information on `expand` |
| `user` | [`User1`](../../doc/models/user-1.md) | Optional | User Information on `expand` |
| `recurrings` | [`List[Recurring]`](../../doc/models/recurring.md) | Optional | Recurring Information on `expand` |
| `email_blacklist` | [`EmailBlacklist`](../../doc/models/email-blacklist.md) | Optional | Email Blacklist Information on `expand` |
| `sms_blacklist` | [`SmsBlacklist`](../../doc/models/sms-blacklist.md) | Optional | Sms Blacklist Information on `expand` |
| `changelogs` | [`List[Changelog]`](../../doc/models/changelog.md) | Optional | Changelog Information on `expand` |
| `postback_logs` | [`List[PostbackLog]`](../../doc/models/postback-log.md) | Optional | Postback Log Information on `expand` |
| `created_user` | [`CreatedUser`](../../doc/models/created-user.md) | Optional | User Information on `expand` |
| `parent` | [`Parent`](../../doc/models/parent.md) | Optional | Parent Information on `expand` |
| `children` | [`Children`](../../doc/models/children.md) | Optional | Children Information on `expand` |

## Example (as JSON)

```json
{
  "location_id": "11e95f8ec39de8fbdb0a4f1a",
  "account_number": "54545433332",
  "contact_api_id": "137",
  "first_name": "John",
  "last_name": "Smith",
  "cell_phone": "3339998822",
  "balance": 245.36,
  "company_name": "Fortis Payment Systems, LLC",
  "header_message": "This is a sample message for you",
  "date_of_birth": "2021-12-01",
  "email_trx_receipt": true,
  "home_phone": "3339998822",
  "office_phone": "3339998822",
  "office_phone_ext": "5",
  "header_message_type": 0,
  "update_if_exists": 1,
  "contact_c1": "any",
  "contact_c2": "anything",
  "contact_c3": "something",
  "parent_id": "11e95f8ec39de8fbdb0a4f1a",
  "email": "email@domain.com",
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "created_ts": 1422040992,
  "modified_ts": 1422040992,
  "active": true,
  "created_user_id": "11e95f8ec39de8fbdb0a4f1a",
  "is_deletable": true
}
```

