
# Line of Credit Balances

Data elements included with balances specific to line of credit accounts

*This model accepts additional fields of type Any.*

## Structure

`LineOfCreditBalances`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `str` | Optional | Long-term persistent identity of the account. Not an account number. This identity must be unique to the owning institution. |
| `account_type` | `str` | Optional | The type of an account. For instance, CHECKING, SAVINGS, 401K, etc. |
| `account_number_display` | `str` | Optional | Account display number for the end user’s handle at owning institution. This is to be displayed by the Interface Provider. |
| `currency` | [`CurrencyEntity`](../../doc/models/currency-entity.md) | Optional | Indicates the currency code used by the account. May also include currency rate. |
| `description` | `str` | Optional | - |
| `fi_attributes` | [`List[FiAttributeEntity]`](../../doc/models/fi-attribute-entity.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `nickname` | `str` | Optional | Name given by the user. Used in UIs to assist in account selection |
| `product_name` | `str` | Optional | Marketed product name for this account.  Used in UIs to assist in account selection |
| `status` | [`AccountInfoStatus`](../../doc/models/account-info-status.md) | Optional | The status of an account. |
| `line_of_business` | `str` | Optional | The line of business, such as consumer, consumer joint, small business, corporate, etc. |
| `balance_type` | [`BalanceType`](../../doc/models/balance-type.md) | Optional | ASSET (positive transaction amount increases balance), LIABILITY (positive transaction amount decreases balance) |
| `interest_rate` | `float` | Optional | Interest Rate of Account |
| `interest_rate_type` | [`InterestRateType`](../../doc/models/interest-rate-type.md) | Optional | The type of interest rate. FIXED or VARIABLE. |
| `interest_rate_as_of` | `datetime` | Optional | Date of account’s interest rate |
| `last_activity_date` | `datetime` | Optional | Date that last transaction occurred on account |
| `micr_number` | `str` | Optional | MICR Number |
| `parent_account_id` | `str` | Optional | Long-term persistent identity of the parent account. This is used to group accounts. |
| `prior_interest_rate` | `float` | Optional | Previous Interest Rate of Account |
| `transfer_in` | `bool` | Optional | Account is eligible for incoming transfers |
| `transfer_out` | `bool` | Optional | Account is eligible for outgoing transfers |
| `balance_as_of` | `datetime` | Optional | As-of date of balances |
| `advances_apr` | `float` | Optional | Advances APR |
| `available_cash` | `float` | Optional | Available cash |
| `available_credit` | `float` | Optional | Available credit |
| `cash_advance_limit` | `float` | Optional | Cash advance limit |
| `credit_line` | `float` | Optional | Credit limit |
| `current_balance` | `float` | Optional | Current balance LOC |
| `current_rewards_balance` | `float` | Optional | Current rewards balance |
| `finance_charges` | `float` | Optional | Finance charges |
| `last_payment_amount` | `float` | Optional | Last payment amount |
| `last_payment_date` | `datetime` | Optional | Last payment date |
| `last_stmt_balance` | `float` | Optional | Last Statement Balance |
| `last_stmt_date` | `datetime` | Optional | Last Statement Date |
| `minimum_payment_amount` | `float` | Optional | Minimum payment amount |
| `next_payment_amount` | `float` | Optional | Amount of next payment |
| `next_payment_date` | `datetime` | Optional | Due date of next payment |
| `past_due_amount` | `float` | Optional | Past Due Amount |
| `points_accrued` | `float` | Optional | Points accrued |
| `principal_balance` | `float` | Optional | Principal balance |
| `points_redeemed` | `float` | Optional | Points redeemed |
| `purchases_apr` | `float` | Optional | Purchases APR |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "accountId": "accountId6",
  "accountType": "accountType6",
  "accountNumberDisplay": "accountNumberDisplay2",
  "currency": {
    "currencyCode": "currencyCode0",
    "currencyRate": 27.48,
    "originalCurrencyCode": "originalCurrencyCode4",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "description": "description6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

