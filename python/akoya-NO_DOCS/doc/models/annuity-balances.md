
# Annuity Balances

Data elements included with balances specific to annuity accounts

*This model accepts additional fields of type Any.*

## Structure

`AnnuityBalances`

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
| `annuity_product_type` | [`AnnunityProductType`](../../doc/models/annunity-product-type.md) | Optional | - |
| `annuity_value_basis` | [`AnnunityValueBasis`](../../doc/models/annunity-value-basis.md) | Optional | - |
| `payment_frequency` | [`AnnuityAccountPaymentFrequency`](../../doc/models/annuity-account-payment-frequency.md) | Optional | - |
| `annual_increase` | `float` | Optional | Percent or dollar amount of annual payment increase |
| `annual_increase_type` | [`AnnualIncreaseType`](../../doc/models/annual-increase-type.md) | Optional | - |
| `net_present_value` | `float` | Optional | Surrender or cash balance value |
| `payment_amount` | `float` | Optional | Amount of the recurring payment |
| `payment_end_date` | `datetime` | Optional | Date last payment will be made |
| `payment_start_date` | `datetime` | Optional | Date of first payment; could be a future date |
| `period_certain_guarantee` | [`PeriodCertainGuarantee`](../../doc/models/period-certain-guarantee.md) | Optional | - |
| `total_payment_count` | `float` | Optional | Total number of payments that will be produced by the annuity |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "accountId": "accountId4",
  "accountType": "accountType4",
  "accountNumberDisplay": "accountNumberDisplay0",
  "currency": {
    "currencyCode": "currencyCode0",
    "currencyRate": 27.48,
    "originalCurrencyCode": "originalCurrencyCode4",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "description": "description4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

