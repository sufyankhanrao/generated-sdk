
# Recurring

## Structure

`Recurring`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_vault_id` | `str` | Optional | Token ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `token_id` | `str` | Optional | Token ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `contact_id` | `str` | Optional | Contact ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `account_vault_api_id` | `str` | Optional | Token API ID<br><br>**Constraints**: *Maximum Length*: `64` |
| `token_api_id` | `str` | Optional | Token API ID<br><br>**Constraints**: *Maximum Length*: `64` |
| `joi` | [`Joi`](../../doc/models/joi.md) | Optional | - |
| `active` | `bool` | Optional | Active |
| `description` | `str` | Optional | Description<br><br>**Constraints**: *Maximum Length*: `36` |
| `end_date` | `str` | Optional | End date<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[\d]{4}-[\d]{2}-[\d]{2}$` |
| `installment_total_count` | `int` | Optional | Installment Total Count<br><br>**Constraints**: `>= 1`, `<= 999` |
| `interval` | `int` | Optional | Interval<br><br>**Constraints**: `>= 0`, `<= 365` |
| `interval_type` | [`IntervalTypeEnum`](../../doc/models/interval-type-enum.md) | Optional | Interval Type |
| `location_id` | `str` | Optional | Location ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `notification_days` | `int` | Optional | Notification Days<br><br>**Constraints**: `>= 0`, `<= 365` |
| `payment_method` | [`PaymentMethod1Enum`](../../doc/models/payment-method-1-enum.md) | Optional | Payment Method |
| `product_transaction_id` | `str` | Optional | Product Transaction ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `recurring_id` | `str` | Optional | Recurring ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `recurring_api_id` | `str` | Optional | Recurring Api ID<br><br>**Constraints**: *Maximum Length*: `64` |
| `start_date` | `str` | Optional | Start date<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[\d]{4}-[\d]{2}-[\d]{2}$` |
| `status` | [`StatusEnum`](../../doc/models/status-enum.md) | Optional | Status |
| `transaction_amount` | `int` | Optional | Transaction amount |
| `terms_agree` | `bool` | Optional | Terms Agree |
| `terms_agree_ip` | `str` | Optional | Terms Agree Ip |
| `recurring_c_1` | `str` | Optional | Custom field used for integrations<br><br>**Constraints**: *Maximum Length*: `128` |
| `recurring_c_2` | `str` | Optional | Custom field used for integrations<br><br>**Constraints**: *Maximum Length*: `128` |
| `recurring_c_3` | `str` | Optional | Custom field used for integrations<br><br>**Constraints**: *Maximum Length*: `128` |
| `send_to_proc_as_recur` | `bool` | Optional | Send To Proc As Recur |
| `tags` | `List[str]` | Optional | Tags |
| `secondary_amount` | `int` | Optional | Retained Amount |
| `currency` | `str` | Optional | - |
| `id` | `str` | Optional | Recurring ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `next_run_date` | `str` | Optional | Next Run Date<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[\d]{4}-[\d]{2}-[\d]{2}$` |
| `created_ts` | `int` | Optional | Created Time Stamp |
| `modified_ts` | `int` | Optional | Modified Time Stamp |
| `recurring_type_id` | [`RecurringTypeIdEnum`](../../doc/models/recurring-type-id-enum.md) | Optional | Recurring Type |
| `installment_amount_total` | `int` | Optional | Installment Amount Total |
| `created_user_id` | `str` | Optional | User ID Created the register<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |

## Example (as JSON)

```json
{
  "account_vault_id": "11e95f8ec39de8fbdb0a4f1a",
  "token_id": "11e95f8ec39de8fbdb0a4f1a",
  "contact_id": "11e95f8ec39de8fbdb0a4f1a",
  "account_vault_api_id": "token1234abcd",
  "token_api_id": "token1234abcd",
  "active": true,
  "description": "Description",
  "end_date": "2021-12-01",
  "installment_total_count": 20,
  "interval": 1,
  "interval_type": "d",
  "location_id": "11e95f8ec39de8fbdb0a4f1a",
  "notification_days": 2,
  "payment_method": "cc",
  "product_transaction_id": "11e95f8ec39de8fbdb0a4f1a",
  "recurring_id": "11e95f8ec39de8fbdb0a4f1a",
  "recurring_api_id": "recurring1234abcd",
  "start_date": "2021-12-01",
  "status": "active",
  "transaction_amount": 300,
  "terms_agree": true,
  "terms_agree_ip": "192.168.0.10",
  "recurring_c1": "recurring custom data 1",
  "recurring_c2": "recurring custom data 2",
  "recurring_c3": "recurring custom data 3",
  "send_to_proc_as_recur": true,
  "secondary_amount": 100,
  "currency": "USD",
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "next_run_date": "2021-12-01",
  "created_ts": 1422040992,
  "modified_ts": 1422040992,
  "recurring_type_id": "i",
  "installment_amount_total": 99999999,
  "created_user_id": "11e95f8ec39de8fbdb0a4f1a"
}
```

