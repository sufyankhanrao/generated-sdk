
# Payments Since Last SOA

List of payments made by the customer after the latest Statement of Account.
Note: All the payments made by the customer will be returned when there is no Statement of Account available for customer.

## Structure

`PaymentsSinceLastSOA`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `int` | Optional | Account Identifier for which payment is made.<br>Example: 12345 |
| `account_number` | `str` | Optional | Account number for which payment is made.<br>Example: GB000000123 |
| `account_short_name` | `str` | Optional | Account Short Name<br>Example: GB Earth Movers-SN |
| `summary_document_id` | `int` | Optional | Summary billing document reference id.<br>Example: 2 |
| `summary_document_number` | `str` | Optional | Summary billing document reference number. |
| `summary_document_date` | `str` | Optional | Summary billing document date.<br>Format: YYYYMMDD |
| `summary_document_payment_due_date` | `str` | Optional | Payment due date of the Summary billing document.<br>Format: YYYYMMDD |
| `summary_document_total_value` | `float` | Optional | Total value in the Summary billing document. |
| `summary_document_total_vat` | `float` | Optional | Total VAT in the Summary billing document. |
| `summary_document_dd_amount` | `float` | Optional | Total DD amount in the Summary billing document. |
| `payment_date` | `str` | Optional | Date of payment.<br>Format: YYYYMMDD |
| `payment_reference` | `str` | Optional | Reference text of the payment. |
| `payment_currency_code` | `str` | Optional | ISO code of payment currency.<br>Example: EUR |
| `payment_currency_symbol` | `str` | Optional | Symbol of payment currency.<br>Example: € |
| `amount_paid` | `float` | Optional | Amount paid. |
| `balance` | `float` | Optional | Balance amount to be settled for the Summary document. |
| `true_payment` | `str` | Optional | True Payment. |
| `prepaid_balance` | `float` | Optional | Balance in the pre-paid amount. |
| `local_currency_code` | `str` | Optional | Currency ISO code of the local country. It is derived based on CountryCode from microservice configuration. This field is expected to have different value than the previously mentioned field CurrencyCode, only in the case of serviced OUs.<br>Example: EUR |
| `local_currency_symbol` | `str` | Optional | Currency Symbol of the local country. It is derived based on CountryCode from microservice configuration. This field is expected to have different value than the previously mentioned field CurrencySymbol, only in the case of serviced OUs.<br>Example: € |
| `local_currency_exchange_rate` | `str` | Optional | Exchange rate from Payment currency to local currency. |

## Example (as JSON)

```json
{
  "AccountId": 0,
  "AccountNumber": "AccountNumber4",
  "AccountShortName": "AccountShortName6",
  "SummaryDocumentId": 92,
  "SummaryDocumentNumber": "SummaryDocumentNumber8"
}
```

