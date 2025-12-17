
# Quick Invoice

Quick Invoice Information on `expand`

## Structure

`QuickInvoice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Optional | Location ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `title` | `str` | Optional | Title<br><br>**Constraints**: *Maximum Length*: `64` |
| `cc_product_transaction_id` | `str` | Optional | Transaction ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `ach_product_transaction_id` | `str` | Optional | ACH Product Transaction Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `due_date` | `str` | Optional | Due Date, Format: Y-m-d<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[\d]{4}-[\d]{2}-[\d]{2}$` |
| `item_list` | [`List[ItemList]`](../../doc/models/item-list.md) | Optional | Item List<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `99`, *Unique Items Required* |
| `allow_overpayment` | `bool` | Optional | Allow Overpayment. |
| `bank_funded_only_override` | `bool` | Optional | Bank Funded Only override |
| `email` | `str` | Optional | Email<br><br>**Constraints**: *Maximum Length*: `128` |
| `contact_id` | `str` | Optional | Contact ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `contact_api_id` | `str` | Optional | Contact API Id<br><br>**Constraints**: *Maximum Length*: `64` |
| `quick_invoice_api_id` | `str` | Optional | Quick Invoice API Id<br><br>**Constraints**: *Maximum Length*: `64` |
| `customer_id` | `str` | Optional | Customer Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `expire_date` | `str` | Optional | Expire Date.<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[\d]{4}-[\d]{2}-[\d]{2}$` |
| `allow_partial_pay` | `bool` | Optional | Allow partial pay |
| `attach_files_to_email` | `bool` | Optional | Attach Files to Email |
| `send_email` | `bool` | Optional | Send Email |
| `invoice_number` | `str` | Optional | Invoice number<br><br>**Constraints**: *Maximum Length*: `64` |
| `item_header` | `str` | Optional | Item Header<br><br>**Constraints**: *Maximum Length*: `250` |
| `item_footer` | `str` | Optional | Item footer<br><br>**Constraints**: *Maximum Length*: `250` |
| `amount_due` | `float` | Optional | Amount Due |
| `notification_email` | `str` | Optional | Notification email<br><br>**Constraints**: *Maximum Length*: `640` |
| `status_id` | [`StatusIdEnum`](../../doc/models/status-id-enum.md) | Optional | (DEPRECATED) Status Id |
| `status_code` | [`StatusCode12Enum`](../../doc/models/status-code-12-enum.md) | Optional | Status Code |
| `note` | `str` | Optional | Note<br><br>**Constraints**: *Maximum Length*: `200` |
| `notification_days_before_due_date` | `int` | Optional | Notification days before due date<br><br>**Constraints**: `>= 0`, `<= 99` |
| `notification_days_after_due_date` | `int` | Optional | Notification days after due date<br><br>**Constraints**: `>= 0`, `<= 99` |
| `notification_on_due_date` | `bool` | Optional | Notification on due date |
| `send_text_to_pay` | `bool` | Optional | Send Text To Pay |
| `files` | `List[Any]` | Optional | Files |
| `remaining_balance` | `float` | Optional | Remaining Balance |
| `single_payment_min_amount` | `int` | Optional | Single Payment Min Amount |
| `single_payment_max_amount` | `int` | Optional | Single Payment Max Amount<br><br>**Default**: `999999999` |
| `cell_phone` | `str` | Optional | Cell Phone<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^\d{10}$` |
| `tags` | `List[str]` | Optional | Tags |
| `id` | `str` | Optional | Quick Invoice ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `created_ts` | `int` | Optional | Created Time Stamp |
| `modified_ts` | `int` | Optional | Modified Time Stamp |
| `created_user_id` | `str` | Optional | Created User Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `modified_user_id` | `str` | Optional | Modified User Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `active` | `bool` | Optional | Active status |
| `payment_status_id` | `int` | Optional | Payment Status Id<br><br>**Constraints**: `>= 1`, `<= 3` |
| `is_active` | `bool` | Optional | Register is active |

## Example (as JSON)

```json
{
  "location_id": "11e95f8ec39de8fbdb0a4f1a",
  "title": "My terminal",
  "cc_product_transaction_id": "11e95f8ec39de8fbdb0a4f1a",
  "ach_product_transaction_id": "11e95f8ec39de8fbdb0a4f1a",
  "due_date": "2021-12-01",
  "allow_overpayment": true,
  "bank_funded_only_override": true,
  "email": "email@domain.com",
  "contact_id": "11e95f8ec39de8fbdb0a4f1a",
  "contact_api_id": "contact12345",
  "quick_invoice_api_id": "quickinvoice12345",
  "customer_id": "11e95f8ec39de8fbdb0a4f1a",
  "expire_date": "2021-12-01",
  "allow_partial_pay": true,
  "attach_files_to_email": true,
  "send_email": true,
  "invoice_number": "invoice12345",
  "item_header": "Quick invoice header sample",
  "item_footer": "Thank you",
  "amount_due": 245.36,
  "notification_email": "email@domain.com",
  "status_id": 1,
  "status_code": 1,
  "note": "some note",
  "notification_days_before_due_date": 3,
  "notification_days_after_due_date": 7,
  "notification_on_due_date": true,
  "send_text_to_pay": true,
  "remaining_balance": 245.36,
  "single_payment_min_amount": 500,
  "single_payment_max_amount": 500000,
  "cell_phone": "3339998822",
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "created_ts": 1422040992,
  "modified_ts": 1422040992,
  "created_user_id": "11e95f8ec39de8fbdb0a4f1a",
  "modified_user_id": "11e95f8ec39de8fbdb0a4f1a",
  "active": true,
  "payment_status_id": 1,
  "is_active": true
}
```

