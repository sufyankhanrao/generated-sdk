
# Annuity Account

Annuity Account

*This model accepts additional fields of type Any.*

## Structure

`AnnuityAccount`

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
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "accountId": "accountId8",
  "accountType": "accountType8",
  "accountNumberDisplay": "accountNumberDisplay4",
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

