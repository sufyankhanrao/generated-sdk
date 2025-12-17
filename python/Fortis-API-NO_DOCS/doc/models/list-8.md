
# List 8

## Structure

`List8`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Optional | Location ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `cc_product_transaction_id` | `str` | Optional | cc_product_transaction_id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `email` | `str` | Optional | Email<br><br>**Constraints**: *Maximum Length*: `128` |
| `amount_due` | `int` | Optional | Amount Due<br><br>**Constraints**: `>= 1`, `<= 999999999` |
| `location_api_id` | `str` | Optional | Location Api Id |
| `contact_id` | `str` | Optional | Contact Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `contact_api_id` | `str` | Optional | Contact Api Id |
| `paylink_api_id` | `str` | Optional | Paylinke Api Id<br><br>**Constraints**: *Maximum Length*: `64` |
| `ach_product_transaction_id` | `str` | Optional | Ach Product Transaction Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `expire_date` | `str` | Optional | Expire Date<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[\d]{4}-[\d]{2}-[\d]{2}$` |
| `display_product_transaction_receipt_details` | `bool` | Optional | Display Product Transaction Receipt Details |
| `display_billing_fields` | `bool` | Optional | Display Billing Fields |
| `delivery_method` | [`DeliveryMethodEnum`](../../doc/models/delivery-method-enum.md) | Optional | Delivery Method<br><br>> 0 - Do not send<br>> <br>> 1 - Email<br>> <br>> 2 - SMS<br>> <br>> 3 - Both |
| `cell_phone` | `str` | Optional | Cell Phone<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^\d{10}$` |
| `description` | `str` | Optional | Description<br><br>**Constraints**: *Maximum Length*: `64` |
| `store_token` | `bool` | Optional | Store Token |
| `store_token_title` | `str` | Optional | Store Token Title<br><br>**Constraints**: *Maximum Length*: `16` |
| `paylink_action` | [`PaylinkActionEnum`](../../doc/models/paylink-action-enum.md) | Optional | Paylink Action |
| `bank_funded_only_override` | `bool` | Optional | Bank Funded Only Override |
| `tags` | `List[str]` | Optional | Used to apply tags to a paylink. |
| `id` | `str` | Optional | Paylink Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `status_id` | `bool` | Optional | (DEPRECATED) Status Id |
| `status_code` | [`StatusCode12Enum`](../../doc/models/status-code-12-enum.md) | Optional | Status Code |
| `active` | `bool` | Optional | Active |
| `created_ts` | `int` | Optional | Created Time Stamp |
| `modified_ts` | `int` | Optional | Modified Time Stamp |
| `created_user_id` | `str` | Optional | User ID Created the register<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `modified_user_id` | `str` | Optional | Last User ID that updated the register<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |

## Example (as JSON)

```json
{
  "location_id": "11e95f8ec39de8fbdb0a4f1a",
  "cc_product_transaction_id": "11e95f8ec39de8fbdb0a4f1a",
  "email": "email@domain.com",
  "amount_due": 1,
  "contact_id": "11e95f8ec39de8fbdb0a4f1a",
  "ach_product_transaction_id": "11e95f8ec39de8fbdb0a4f1a",
  "expire_date": "2021-12-01",
  "display_product_transaction_receipt_details": true,
  "display_billing_fields": true,
  "delivery_method": 0,
  "cell_phone": "3339998822",
  "description": "Description",
  "store_token": false,
  "store_token_title": "John Account",
  "bank_funded_only_override": false,
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "status_id": true,
  "status_code": 1,
  "active": true,
  "created_ts": 1422040992,
  "modified_ts": 1422040992,
  "created_user_id": "11e95f8ec39de8fbdb0a4f1a",
  "modified_user_id": "11e95f8ec39de8fbdb0a4f1a",
  "location_api_id": "location_api_id0"
}
```

