
# Location Billing Account

## Structure

`LocationBillingAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `title` | `str` | Optional | Title<br><br>**Constraints**: *Maximum Length*: `64` |
| `location_id` | `str` | Optional | Location ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `location_api_id` | `str` | Optional | Location Api Id |
| `ach_sec_code` | `str` | Optional | Ach Sec Code |
| `account_number` | `str` | Optional | Account number |
| `routing` | `str` | Optional | Routing |
| `exp_date` | `str` | Optional | Exp Date |
| `billing_zip` | `str` | Optional | Billing Zip<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `10`, *Pattern*: `^[a-zA-Z0-9\-\s]+$` |
| `account_type` | `str` | Optional | Account Type |
| `account_holder_name` | `str` | Optional | Account Holder Name |
| `id` | `str` | Optional | Location Billing Account Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `created_ts` | `int` | Optional | Created Time Stamp |
| `modified_ts` | `int` | Optional | Modified Time Stamp |
| `created_user_id` | `str` | Optional | Created User Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `modified_user_id` | `str` | Optional | Modified User Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `billing_descriptor` | `str` | Optional | Billing Descriptor |
| `payment_method` | `str` | Optional | Billing Descriptor |
| `portfolio_id` | `str` | Optional | Portfolio Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |

## Example (as JSON)

```json
{
  "title": "Billing Acccount Title",
  "location_id": "11e95f8ec39de8fbdb0a4f1a",
  "exp_date": "0722",
  "billing_zip": "48375",
  "account_holder_name": "John Smith",
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "created_ts": 1422040992,
  "modified_ts": 1422040992,
  "created_user_id": "11e95f8ec39de8fbdb0a4f1a",
  "modified_user_id": "11e95f8ec39de8fbdb0a4f1a",
  "portfolio_id": "11e95f8ec39de8fbdb0a4f1a",
  "location_api_id": "location_api_id4",
  "ach_sec_code": "ach_sec_code6",
  "account_number": "account_number4"
}
```

