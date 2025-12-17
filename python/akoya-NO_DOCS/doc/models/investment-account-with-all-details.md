
# Investment Account With All Details

Data elements included with the investment product

*This model accepts additional fields of type Any.*

## Structure

`InvestmentAccountWithAllDetails`

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
| `allowed_check_writing` | `bool` | Optional | Check writing privileges |
| `allowed_option_trade` | `bool` | Optional | Allowed to trade options |
| `broker_id` | `str` | Optional | Unique identifier FI |
| `calendar_year_for_401_k` | `str` | Optional | Date for this calendar year for 401K account |
| `employer_name` | `str` | Optional | Name of the employer in investment 401k Plan |
| `margin` | `bool` | Optional | Margin trading is allowed |
| `plan_id` | `str` | Optional | Plan number for Investment 401k plan |
| `available_cash_balance` | `float` | Optional | Cash balance across all sub-accounts. Should include sweep funds. |
| `balance_as_of` | `datetime` | Optional | As-of date of balances |
| `balance_list` | [`List[InvestmentBalanceList]`](../../doc/models/investment-balance-list.md) | Optional | Balance List. Name value pair aggregate. |
| `current_value` | `float` | Optional | Total current value of all investments |
| `daily_change` | `float` | Optional | Daily change |
| `margin_balance` | `float` | Optional | Margin balance |
| `percentage_change` | `float` | Optional | Percentage change |
| `rollover_amount` | `float` | Optional | Rollover amount |
| `short_balance` | `float` | Optional | Short balance |
| `holdings` | [`List[AnInvestmentHolding]`](../../doc/models/an-investment-holding.md) | Optional | Array of holdings |
| `open_orders` | [`List[OpenOrderEntity]`](../../doc/models/open-order-entity.md) | Optional | Array of open orders |
| `contribution` | [`List[ContributionEntity]`](../../doc/models/contribution-entity.md) | Optional | Array of contribution objects. Describes how new contributions are distributed among the available securities |
| `vesting` | [`List[VestingEntity]`](../../doc/models/vesting-entity.md) | Optional | Array of vesting objects. Provides the past, present, and future vesting schedule and percentages |
| `investment_loans` | [`List[InvestmentLoanEntity]`](../../doc/models/investment-loan-entity.md) | Optional | Array of investment loans |
| `pension_source` | [`List[PensionSourceEntity]`](../../doc/models/pension-source-entity.md) | Optional | Array of Pension Source |
| `equity_grants` | [`List[EquityGrant]`](../../doc/models/equity-grant.md) | Optional | Provides equity grant information on Restricted Stock Units, Restricted Stock Awards, Stock Appreciation Right, Stock Options, Performance Awards, and Total Share Return Units |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "accountId": "accountId2",
  "accountType": "accountType2",
  "accountNumberDisplay": "accountNumberDisplay8",
  "currency": {
    "currencyCode": "currencyCode0",
    "currencyRate": 27.48,
    "originalCurrencyCode": "originalCurrencyCode4",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "description": "description2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

