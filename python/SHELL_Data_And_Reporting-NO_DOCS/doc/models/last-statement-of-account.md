
# Last Statement of Account

Latest statement of the account generated for the given Payer.

## Structure

`LastStatementOfAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount_due` | `float` | Optional | Invoiced amount and due for payment. |
| `amount_not_overdue` | `float` | Optional | Invoiced amount and not overdue for payment. |
| `amount_overdue` | `float` | Optional | Invoiced amount and overdue for payment. |
| `credit_limit` | `int` | Optional | Credit limit. |
| `credit_limit_currency_code` | `str` | Optional | ISO code of the credit limit’s currency.<br>Example: EUR |
| `credit_limit_currency_symbol` | `str` | Optional | Symbol of the credit limit’s currency.<br>Example: € |
| `credit_limit_in_customer_currency` | `float` | Optional | Credit limit in Customer currency.<br>**Note**: For currency details refer the parameters CurrencyCode & CurrencySymbol in the StatementOfAccount response. |
| `currency_code` | `str` | Optional | ISO code of SOA currency.<br>Example: EUR |
| `currency_symbol` | `str` | Optional | Symbol of SOA currency.<br>Example: € |
| `last_payment_currency_code` | `str` | Optional | ISO code of Last Payment currency.<br>Example: EUR |
| `last_payment_currency_symbol` | `str` | Optional | Symbol of Last Payment currency.<br>Example: € |
| `last_payment_date` | `str` | Optional | Last payment date. Format: yyyyMMdd |
| `last_payment_value` | `float` | Optional | Last payment value. |
| `outstanding_balance` | `float` | Optional | Current outstanding balance amount. |
| `payer_id` | `int` | Optional | Payment customer id of the customer. |
| `payer_number` | `str` | Optional | Payment customer number. |
| `payment_due_date` | `str` | Optional | Due date for payment. Format: yyyyMMdd |
| `payment_method` | `str` | Optional | Payment method description of the Payer.<br>Example: Id & Description<br>•	Incoming - Direct Debit<br>•	Incoming - Cheque<br>•	Incoming - Direct Debit A<br>•	Incoming - Bank Transfer<br>•	Incoming - Cash |
| `payment_method_id` | `int` | Optional | Payment method Id of the Payer.<br>Example: Id & Description<br>•	Incoming - Direct Debit<br>•	Incoming - Cheque<br>•	Incoming - Direct Debit A<br>•	Incoming - Bank Transfer<br>•	Incoming - Cash |
| `payment_terms` | `str` | Optional | Payment terms description of the Payer.<br>Example: Id & Description<br>•	14 days after Invoice<br>•	15 days after Invoice<br>•	21 days after Invoice<br>•	30 days after Invoice<br>•	45 days after Invoice<br>•	0 days after invoice<br>•	days after invoice<br>•	days after invoice<br>•	7 days after invoice<br>•	10th of the following month |
| `payment_terms_id` | `int` | Optional | Payment terms Id of the Payer.<br>Example: Id & Description<br>•	14 days after Invoice<br>•	15 days after Invoice<br>•	21 days after Invoice<br>•	30 days after Invoice<br>•	45 days after Invoice<br>•	0 days after invoice<br>•	days after invoice<br>•	days after invoice<br>•	7 days after invoice<br>•	10th of the following month |
| `so_a_reference_number` | `str` | Optional | Statement of account reference number |
| `statement_date` | `str` | Optional | Date on which the SOA was generated.<br>Format: yyyyMMdd |
| `statement_of_account_id` | `int` | Optional | Statement of account identifier,<br>Example: 1 |
| `total_billing_documents` | `int` | Optional | Total number of billing documents for this Statement of Account |
| `total_summary_billing_documents` | `int` | Optional | Total number of summary billing documents for this Statement of Account |
| `unallocated_payment` | `int` | Optional | Unallocated payment.<br>When negative, indicates overdue amount. |

## Example (as JSON)

```json
{
  "AmountDue": 220.3,
  "AmountNotOverdue": 42.96,
  "AmountOverdue": 58.04,
  "CreditLimit": 162,
  "CreditLimitCurrencyCode": "CreditLimitCurrencyCode4"
}
```

