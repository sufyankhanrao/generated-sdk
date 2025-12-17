
# Data 21

## Structure

`Data21`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_name` | `str` | Optional | Account holder name<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `32` |
| `account_vault_api_id` | `str` | Optional | This field can be used to correlate Tokens in our system to data within an outside software integration<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `64` |
| `token_api_id` | `str` | Optional | This field can be used to correlate Tokens in our system to data within an outside software integration<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `64` |
| `accountvault_c_1` | `str` | Optional | DEPRECATED (Use token_c1 instead)<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `128` |
| `accountvault_c_2` | `str` | Optional | DEPRECATED (Use token_c2 instead)<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `128` |
| `accountvault_c_3` | `str` | Optional | DEPRECATED (Use token_c3 instead)<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `128` |
| `token_c_1` | `str` | Optional | Custom field 1 for API users to store custom data<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `128` |
| `token_c_2` | `str` | Optional | Custom field 2 for API users to store custom data<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `128` |
| `token_c_3` | `str` | Optional | Custom field 3 for API users to store custom data<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `128` |
| `ach_sec_code` | [`AchSecCode3Enum`](../../doc/models/ach-sec-code-3-enum.md) | Optional | SEC code for the account |
| `billing_address` | [`BillingAddress`](../../doc/models/billing-address.md) | Optional | Billing Address Object |
| `contact_id` | `str` | Optional | Used to associate the Token with a Contact.<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `customer_id` | `str` | Optional | Used to store a customer identification number.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `50` |
| `identity_verification` | [`IdentityVerification2`](../../doc/models/identity-verification-2.md) | Optional | Identity verification |
| `location_id` | `str` | Optional | A valid Location Id associated with the Contact for this Token<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `previous_account_vault_api_id` | `str` | Optional | Can be used to pull payment info from a previous token api id.<br><br>**Constraints**: *Maximum Length*: `64` |
| `previous_token_api_id` | `str` | Optional | Can be used to pull payment info from a previous token api id.<br><br>**Constraints**: *Maximum Length*: `64` |
| `previous_account_vault_id` | `str` | Optional | Can be used to pull payment info from a previous token.<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `previous_token_id` | `str` | Optional | Can be used to pull payment info from a previous token.<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `previous_transaction_id` | `str` | Optional | Can be used to pull payment info from a previous transaction.<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `account_number` | `str` | Optional | Account number<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `19`, *Pattern*: `^[\d]+$` |
| `terms_agree` | `bool` | Optional | Terms agreement. |
| `terms_agree_ip` | `str` | Optional | The ip address of the client that agreed to terms. |
| `title` | `str` | Optional | Used to describe the Token for easier identification within our UI.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `16` |
| `joi` | [`Joi4`](../../doc/models/joi-4.md) | Optional | - |
| `id` | `str` | Optional | A unique, system-generated identifier for the Token.<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `account_type` | `str` | Optional | Account type<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `32` |
| `active` | `bool` | Optional | Register is Active |
| `cau_summary_status_id` | [`CauSummaryStatusIdEnum`](../../doc/models/cau-summary-status-id-enum.md) | Optional | CAU Summary Status ID. |
| `created_ts` | `int` | Optional | Created Time Stamp |
| `e_serial_number` | `str` | Optional | E Serial Number<br><br>**Constraints**: *Maximum Length*: `36`, *Pattern*: `^[a-zA-Z0-9]*$` |
| `e_track_data` | `str` | Optional | E Track Data |
| `e_format` | `str` | Optional | E Format |
| `e_keyed_data` | `str` | Optional | E Keyed Data |
| `expiring_in_months` | `int` | Optional | Determined by API based on card exp_date. |
| `exp_date` | `str` | Optional | Required for CC. The Expiration Date for the credit card. (MMYY format).<br><br>**Constraints**: *Maximum Length*: `4` |
| `first_six` | `str` | Optional | The first six numbers of an account number.  System will generate a value for this field automatically.<br><br>**Constraints**: *Maximum Length*: `6` |
| `has_recurring` | `bool` | Optional | True indicates that this token is tied to a Recurring Payment |
| `last_four` | `str` | Optional | The last four numbers of an account number.  System will generate a value for this field automatically.<br><br>**Constraints**: *Maximum Length*: `4` |
| `modified_ts` | `int` | Optional | Modified Time Stamp |
| `payment_method` | [`PaymentMethod13Enum`](../../doc/models/payment-method-13-enum.md) | Optional | Must be provided as either 'cc' or 'ach'. |
| `ticket` | `str` | Optional | A valid ticket that was created to store the token.<br><br>**Constraints**: *Maximum Length*: `36` |
| `track_data` | `str` | Optional | Track Data from a magnetic card swipe.<br><br>**Constraints**: *Maximum Length*: `256` |
| `created_user_id` | `str` | Optional | User ID Created the register<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `cau_last_updated_ts` | `int` | Optional | CAU Last Updated Timestamp |
| `card_bin` | `str` | Optional | Card bin |
| `routing_number` | `str` | Optional | Required for ACH. The Routing Number for the bank account being used. |
| `location` | [`Location`](../../doc/models/location.md) | Optional | Location Information on `expand` |
| `contact` | [`Contact1`](../../doc/models/contact-1.md) | Optional | Contact Information on `expand` |
| `transactions` | [`List[Transaction]`](../../doc/models/transaction.md) | Optional | Transaction Information on `expand` |
| `active_recurrings` | [`List[ActiveRecurring]`](../../doc/models/active-recurring.md) | Optional | ActiveRecurring Information on `expand` |
| `is_deletable` | `bool` | Optional | Is Deletable Information on `expand` |
| `signature` | [`Signature`](../../doc/models/signature.md) | Optional | Signature Information on `expand` |
| `created_user` | [`CreatedUser`](../../doc/models/created-user.md) | Optional | User Information on `expand` |
| `changelogs` | [`List[Changelog]`](../../doc/models/changelog.md) | Optional | Changelog Information on `expand` |
| `account_vault_cau_logs` | [`List[AccountVaultCauLog]`](../../doc/models/account-vault-cau-log.md) | Optional | Token Cau Log Information on `expand` |
| `account_vault_cau_product_transactions` | [`List[AccountVaultCauProductTransaction]`](../../doc/models/account-vault-cau-product-transaction.md) | Optional | Token Cau Product Transaction Information on `expand` |

## Example (as JSON)

```json
{
  "account_holder_name": "John Smith",
  "account_vault_api_id": "accountvaultabcd",
  "token_api_id": "tokenabcd",
  "accountvault_c1": "accountvault custom 1",
  "accountvault_c2": "accountvault custom 2",
  "accountvault_c3": "accountvault custom 3",
  "token_c1": "token custom 1",
  "token_c2": "token custom 2",
  "token_c3": "token custom 3",
  "ach_sec_code": "WEB",
  "contact_id": "11e95f8ec39de8fbdb0a4f1a",
  "customer_id": "123456",
  "location_id": "11e95f8ec39de8fbdb0a4f1a",
  "previous_account_vault_api_id": "previousaccountvault123456",
  "previous_token_api_id": "previousaccountvault123456",
  "previous_account_vault_id": "11e95f8ec39de8fbdb0a4f1a",
  "previous_token_id": "11e95f8ec39de8fbdb0a4f1a",
  "previous_transaction_id": "11e95f8ec39de8fbdb0a4f1a",
  "account_number": "545454545454545",
  "terms_agree": true,
  "terms_agree_ip": "192.168.0.10",
  "title": "Test CC Account",
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "account_type": "checking",
  "active": true,
  "cau_summary_status_id": 1,
  "created_ts": 1422040992,
  "e_serial_number": "1234567890",
  "exp_date": "0722",
  "first_six": "700953",
  "has_recurring": false,
  "last_four": "3657",
  "modified_ts": 1422040992,
  "payment_method": "cc",
  "created_user_id": "11e95f8ec39de8fbdb0a4f1a",
  "cau_last_updated_ts": 1422040992,
  "routing_number": "051904524",
  "is_deletable": true
}
```

