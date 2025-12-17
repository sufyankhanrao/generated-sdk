
# Investment Loan Entity

Information about an investment loan.

*This model accepts additional fields of type Any.*

## Structure

`InvestmentLoanEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `loan_id` | `str` | Optional | Unique identifier for this loan |
| `loan_description` | `str` | Optional | Description |
| `initial_loan_balance` | `float` | Optional | Initial loan balance amount |
| `loan_start_date` | `datetime` | Optional | Start date of the loan |
| `current_loan_balance` | `float` | Optional | Current loan principal balance amount |
| `date_as_of` | `datetime` | Optional | Date and time of current loan balance |
| `loan_rate` | `float` | Optional | Loan annual interest rate for the loan |
| `loan_payment_amount` | `float` | Optional | Loan payment amount |
| `loan_payment_frequency` | [`LoanPaymentFrequency`](../../doc/models/loan-payment-frequency.md) | Optional | - |
| `loan_payment_initial` | `float` | Optional | Initial number of loan payments |
| `loan_payments_remaining` | `int` | Optional | Remaining number of loan payments |
| `loan_maturity_date` | `datetime` | Optional | Expected loan end date |
| `loan_interest_to_date` | `float` | Optional | Total interest paid to date on this loan |
| `loan_total_projected_interest` | `float` | Optional | Total projected interest to be paid on this loan |
| `loan_next_payment_date` | `datetime` | Optional | The next payment date for the loan |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "loanId": "loanId2",
  "loanDescription": "loanDescription4",
  "initialLoanBalance": 205.08,
  "loanStartDate": "2016-03-13T12:52:32.123Z",
  "currentLoanBalance": 206.82,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

