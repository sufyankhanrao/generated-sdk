
# Ach Product Transaction

Ach Product Transaction Information on `expand`

## Structure

`AchProductTransaction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `processor_version` | `str` | Optional | Processor Version |
| `industry_type` | [`IndustryTypeEnum`](../../doc/models/industry-type-enum.md) | Optional | Industry Type<br><br>**Constraints**: *Maximum Length*: `45` |
| `title` | `str` | Optional | Title<br><br>**Constraints**: *Maximum Length*: `64` |
| `payment_method` | [`PaymentMethodEnum`](../../doc/models/payment-method-enum.md) | Optional | Payment method |
| `processor` | [`ProcessorEnum`](../../doc/models/processor-enum.md) | Optional | Processor |
| `mcc` | `str` | Optional | MCC<br><br>**Constraints**: *Maximum Length*: `4`, *Pattern*: `^\d+$` |
| `tax_surcharge_config` | [`TaxSurchargeConfigEnum`](../../doc/models/tax-surcharge-config-enum.md) | Optional | Tax Surcharge Config<br><br>**Default**: `2` |
| `terminal_id` | `str` | Optional | Terminal ID<br><br>**Constraints**: *Maximum Length*: `24` |
| `partner` | [`PartnerEnum`](../../doc/models/partner-enum.md) | Optional | Partner<br><br>**Constraints**: *Maximum Length*: `24` |
| `product_ach_pv_store_id` | `str` | Optional | Product Ach Pv Store ID |
| `invoice_adjustment_title` | `str` | Optional | Invoice Adjustment Title |
| `location_id` | `str` | Optional | Location ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `location_api_id` | `str` | Optional | Location Api ID |
| `billing_location_api_id` | `str` | Optional | Billing Location API ID |
| `portfolio_id` | `str` | Optional | Portfolio ID |
| `portfolio_validation_rule` | `str` | Optional | Product Validation Rule |
| `sub_processor` | `str` | Optional | Sub Processor<br><br>**Constraints**: *Maximum Length*: `48` |
| `surcharge` | `Any` | Optional | Surcharge |
| `processor_data` | `Any` | Optional | - |
| `vt_clerk_number` | `bool` | Optional | Vt Clerk Number |
| `vt_billing_phone` | `bool` | Optional | Card Type JCB |
| `vt_enable_tip` | `bool` | Optional | VT Enable Tip |
| `ach_allow_debit` | `bool` | Optional | Ach Allow Debit |
| `ach_allow_credit` | `bool` | Optional | Ach Allow Credit |
| `ach_allow_refund` | `bool` | Optional | Ach Allow Refund |
| `vt_cvv` | `bool` | Optional | VT CVV |
| `vt_street` | `bool` | Optional | VT Street |
| `vt_zip` | `bool` | Optional | VT Zip |
| `vt_order_num` | `bool` | Optional | VT Order Num |
| `vt_enable` | `bool` | Optional | VT Enable |
| `receipt_show_contact_name` | `bool` | Optional | Receipt Show Contact Name |
| `display_avs` | `bool` | Optional | Display Avs |
| `card_type_visa` | `bool` | Optional | Card Type Visa |
| `card_type_mc` | `bool` | Optional | Card Type Mc |
| `card_type_disc` | `bool` | Optional | Card Type Disc |
| `card_type_amex` | `bool` | Optional | Card Type Amex |
| `card_type_diners` | `bool` | Optional | Card Type Dinners |
| `card_type_jcb` | `bool` | Optional | - |
| `invoice_location` | `bool` | Optional | Invoice Location |
| `allow_partial_authorization` | `bool` | Optional | Allow Partial Authorization |
| `allow_recurring_partial_authorization` | `bool` | Optional | Allow Recurring Partial Authorization |
| `auto_decline_cvv` | `bool` | Optional | Auto Decline Cvv |
| `auto_decline_street` | `bool` | Optional | Auto Decline Street |
| `auto_decline_zip` | `bool` | Optional | Auto Decline ZIP |
| `split_payments_allow` | `bool` | Optional | Split Payments Allow |
| `vt_show_custom_fields` | `bool` | Optional | Vt Show Custom Fields |
| `receipt_show_custom_fields` | `bool` | Optional | Receipt Show Custom Fields |
| `vt_override_sales_tax_allowed` | `bool` | Optional | Vt Override Sales Tax Allowed |
| `vt_enable_sales_tax` | `bool` | Optional | Vt Enable Sales Tax |
| `vt_require_zip` | `bool` | Optional | Vt Require ZIP |
| `vt_require_street` | `bool` | Optional | Vt Require Street |
| `auto_decline_cavv` | `bool` | Optional | Auto Decline Cavv |
| `merchant_id` | `str` | Optional | Merchant ID<br><br>**Constraints**: *Maximum Length*: `24` |
| `receipt_header` | `str` | Optional | Receipt Header<br><br>**Constraints**: *Maximum Length*: `255` |
| `receipt_footer` | `str` | Optional | Receipt Footer<br><br>**Constraints**: *Maximum Length*: `255` |
| `receipt_add_account_above_signature` | `str` | Optional | Receipt Add Account Above Signature<br><br>**Constraints**: *Maximum Length*: `1032` |
| `receipt_add_recurring_above_signature` | `str` | Optional | Receipt Add Recurring Above Signature<br><br>**Constraints**: *Maximum Length*: `1032` |
| `receipt_vt_above_signature` | `str` | Optional | Receipt VT Above Signature<br><br>**Constraints**: *Maximum Length*: `1032` |
| `default_transaction_type` | [`DefaultTransactionTypeEnum`](../../doc/models/default-transaction-type-enum.md) | Optional | Default Transaction Type |
| `username` | `str` | Optional | Username<br><br>**Constraints**: *Maximum Length*: `512` |
| `password` | `str` | Optional | Passowrd<br><br>**Constraints**: *Maximum Length*: `512` |
| `current_batch` | `float` | Optional | Current Batch<br><br>**Default**: `1`<br><br>**Constraints**: `>= 1`, `<= 9999` |
| `dup_check_per_batch` | `str` | Optional | Dup Check Per Batch<br><br>**Constraints**: *Maximum Length*: `500` |
| `agent_code` | `str` | Optional | Agent Code<br><br>**Constraints**: *Maximum Length*: `16`, *Pattern*: `^[\w\-]+$` |
| `paylink_allow` | `bool` | Optional | Paylink Allow |
| `quick_invoice_allow` | `bool` | Optional | Quick Invoice Allow |
| `level_3_allow` | `bool` | Optional | Level3 Allow |
| `payfac_enable` | `bool` | Optional | Payfac Enable |
| `sales_office_id` | `str` | Optional | Sales Office ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `hosted_payment_page_max_allowed` | `float` | Optional | Hosted Payment Page Max Allowed<br><br>**Default**: `5`<br><br>**Constraints**: `>= 1`, `<= 999` |
| `hosted_payment_page_allow` | `bool` | Optional | Hosted Payment Page Allow |
| `surcharge_id` | `str` | Optional | Surcharge ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `level_3_default` | `Any` | Optional | Level3 Default |
| `cau_subscribe_type_id` | [`CauSubscribeTypeIdEnum`](../../doc/models/cau-subscribe-type-id-enum.md) | Optional | Cau Subscribe Type ID |
| `cau_account_number` | `str` | Optional | Cau Account Number<br><br>**Constraints**: *Minimum Length*: `32`, *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-]+$` |
| `location_billing_account_id` | `str` | Optional | Location Billing Account ID |
| `product_billing_group_id` | `str` | Optional | Product Billing Group ID |
| `account_number` | `str` | Optional | Account number<br><br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `run_avs_on_accountvault_create` | `bool` | Optional | Run Avs On Accountvault Create |
| `accountvault_expire_notification_email_enable` | `bool` | Optional | Accountvault Expire Notification Email Enable |
| `debit_allow_void` | `bool` | Optional | Debit Allow Void |
| `quick_invoice_text_to_pay` | `bool` | Optional | Quick Invoice Text To Pay |
| `authentication_code` | `str` | Optional | Authentication Code |
| `sms_enable` | `bool` | Optional | SMS Enable |
| `vt_show_currency` | `bool` | Optional | Vt Show Currency |
| `receipt_show_currency` | `bool` | Optional | Receipt Show Currency |
| `allow_blind_refund` | `bool` | Optional | Allow Blind Refund |
| `vt_show_company_name` | `bool` | Optional | Vt Show Company Name |
| `receipt_show_company_name` | `bool` | Optional | Receipt Show Company Name |
| `bank_funded_only` | `bool` | Optional | Bank Funded Only |
| `require_cvv_on_keyed_cnp` | `bool` | Optional | Require CVV on keyed CNP |
| `require_cvv_on_tokenized_cnp` | `bool` | Optional | Require CVV on tokenized CNP |
| `show_secondary_amount` | `bool` | Optional | Show Retained Amount |
| `allow_secondary_amount` | `bool` | Optional | Allow Retained Amount |
| `show_google_pay` | `bool` | Optional | Vt Require Street |
| `show_apple_pay` | `bool` | Optional | Vt Require Street |
| `id` | `str` | Optional | User Reports ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `receipt_logo` | `str` | Optional | Receipt Logo |
| `active` | `bool` | Optional | Active |
| `tz` | `str` | Optional | TZ |
| `currency_code` | `float` | Optional | Currency Code<br><br>**Default**: `840` |
| `current_stan` | `float` | Optional | Current Stan<br><br>**Default**: `1` |
| `created_ts` | `int` | Optional | Created Time Stamp |
| `modified_ts` | `int` | Optional | Modified Time Stamp |
| `created_user_id` | `str` | Optional | User ID Created the register<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `modified_user_id` | `str` | Optional | Last User ID that updated the register<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `product_transaction_api_id` | `str` | Optional | Product Transaction API ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `transaction_amount_notification_threshold` | `int` | Optional | Transaction Amount Notification Treshold |
| `is_secondary_amount_allowed` | `bool` | Optional | Allow Retained Amount |
| `batch_risk_config` | `Any` | Optional | Batch Risk Config |
| `fortis_id` | `str` | Optional | - |
| `product_billing_group_code` | `str` | Optional | Product Billing Group Code |
| `cau_subscribe_type_code` | [`CauSubscribeTypeCodeEnum`](../../doc/models/cau-subscribe-type-code-enum.md) | Optional | Cau Subscribe Type Code |
| `merchant_code` | `str` | Optional | Merchant Code<br><br>**Constraints**: *Maximum Length*: `24` |

## Example (as JSON)

```json
{
  "processor_version": "1_0_0",
  "title": "My terminal",
  "payment_method": "cc",
  "processor": "zgate",
  "mcc": "1111",
  "tax_surcharge_config": 2,
  "partner": "standalone",
  "location_id": "11e95f8ec39de8fbdb0a4f1a",
  "vt_clerk_number": true,
  "vt_billing_phone": true,
  "vt_enable_tip": true,
  "ach_allow_debit": true,
  "ach_allow_credit": true,
  "ach_allow_refund": true,
  "vt_cvv": true,
  "vt_street": true,
  "vt_zip": true,
  "vt_order_num": true,
  "vt_enable": true,
  "receipt_show_contact_name": true,
  "display_avs": true,
  "card_type_visa": true,
  "card_type_mc": true,
  "card_type_disc": true,
  "card_type_amex": true,
  "card_type_diners": true,
  "card_type_jcb": true,
  "invoice_location": true,
  "allow_partial_authorization": true,
  "allow_recurring_partial_authorization": true,
  "auto_decline_cvv": true,
  "auto_decline_street": true,
  "auto_decline_zip": true,
  "split_payments_allow": true,
  "vt_show_custom_fields": true,
  "receipt_show_custom_fields": true,
  "vt_override_sales_tax_allowed": true,
  "vt_enable_sales_tax": true,
  "vt_require_zip": true,
  "vt_require_street": true,
  "auto_decline_cavv": true,
  "current_batch": 34,
  "paylink_allow": false,
  "quick_invoice_allow": false,
  "level3_allow": false,
  "payfac_enable": false,
  "sales_office_id": "11e95f8ec39de8fbdb0a4f1a",
  "hosted_payment_page_max_allowed": 5,
  "hosted_payment_page_allow": false,
  "surcharge_id": "11e95f8ec39de8fbdb0a4f1a",
  "level3_default": {},
  "cau_subscribe_type_id": 0,
  "location_billing_account_id": "11eb88b873980c64a21e5fd2",
  "product_billing_group_id": "nofees",
  "account_number": "12345678",
  "run_avs_on_accountvault_create": false,
  "accountvault_expire_notification_email_enable": false,
  "debit_allow_void": false,
  "quick_invoice_text_to_pay": false,
  "sms_enable": false,
  "vt_show_currency": true,
  "receipt_show_currency": false,
  "allow_blind_refund": false,
  "vt_show_company_name": false,
  "receipt_show_company_name": false,
  "bank_funded_only": false,
  "require_cvv_on_keyed_cnp": true,
  "require_cvv_on_tokenized_cnp": true,
  "show_secondary_amount": false,
  "allow_secondary_amount": false,
  "show_google_pay": true,
  "show_apple_pay": true,
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "active": true,
  "currency_code": 840,
  "current_stan": 1,
  "created_ts": 1422040992,
  "modified_ts": 1422040992,
  "created_user_id": "11e95f8ec39de8fbdb0a4f1a",
  "modified_user_id": "11e95f8ec39de8fbdb0a4f1a",
  "product_transaction_api_id": "11e95f8ec39de8fbdb0a4f1a",
  "is_secondary_amount_allowed": false,
  "fortis_id": "8149742",
  "product_billing_group_code": "nofees",
  "cau_subscribe_type_code": 0,
  "industry_type": "retail"
}
```

