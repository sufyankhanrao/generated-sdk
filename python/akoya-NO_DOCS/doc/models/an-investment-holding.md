
# An Investment Holding

*This model accepts additional fields of type Any.*

## Structure

`AnInvestmentHolding`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `asset_classes` | [`List[AssetClassItem]`](../../doc/models/asset-class-item.md) | Optional | Percent breakdown by asset class.<br><br>**Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `average_cost` | `bool` | Optional | Cost is average of all purchases for holding. |
| `cash_account` | `bool` | Optional | If true, indicates that this holding is used to maintain proceeds from sales, dividends, and other cash postings to the investment account. |
| `change_in_price` | `float` | Optional | Change in current price compared to previous day's close |
| `currency` | [`CurrencyEntity`](../../doc/models/currency-entity.md) | Optional | Indicates the currency code used by the account. May also include currency rate. |
| `current_unit_price` | `float` | Optional | - |
| `current_unit_price_date` | `datetime` | Optional | Current unit price as of date |
| `description` | `str` | Optional | Description of the holding |
| `expiration_date` | `datetime` | Optional | For CDs, bonds, and other time-based holdings. |
| `face_value` | `float` | Optional | Face value at the time of data retrieved. |
| `fi_asset_classes` | [`List[FiAssetClassItem]`](../../doc/models/fi-asset-class-item.md) | Optional | Percent breakdown by FI-specific asset class percentage breakdown |
| `fi_attributes` | [`List[FiAttributeEntity]`](../../doc/models/fi-attribute-entity.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `held_in_account` | [`HeldInAccount`](../../doc/models/held-in-account.md) | Optional | Sub-account |
| `holding_id` | `str` | Optional | Long term persistent identity of the holding |
| `holding_name` | `str` | Optional | Holding name or security name |
| `holding_sub_type` | [`HoldingSubType`](../../doc/models/holding-sub-type.md) | Optional | - |
| `holding_type` | [`HoldingType`](../../doc/models/holding-type.md) | Optional | - |
| `inv_401_k_surce` | [`Inv401KSurce`](../../doc/models/inv-401-k-surce.md) | Optional | Source for money for this security. |
| `market_value` | `float` | Optional | Market value at the time of data retrieved |
| `original_purchase_date` | `datetime` | Optional | Date of original purchase |
| `position_type` | [`PositionType`](../../doc/models/position-type.md) | Optional | LONG, SHORT. |
| `purchased_price` | `float` | Optional | Price of holding at the time of purchase |
| `rate` | `float` | Optional | For CDs, bonds, and other rate based holdings. |
| `security_id` | `str` | Optional | Unique identifier of security |
| `security_id_type` | [`SecurityIdType`](../../doc/models/security-id-type.md) | Optional | Security identifier type |
| `symbol` | `str` | Optional | Ticker / Market symbol |
| `tax_lots` | [`List[Items]`](../../doc/models/items.md) | Optional | Breakdown by tax lot.<br><br>**Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `units` | `float` | Optional | Number of shares (with decimals). |
| `mutual_fund_security` | [`MutualFundSecurityEntity`](../../doc/models/mutual-fund-security-entity.md) | Optional | Information about the mutual fund security specific to the type of security |
| `option_security` | [`OptionSecurityEntity`](../../doc/models/option-security-entity.md) | Optional | Information about the option security specific to the type of security |
| `other_security` | [`OtherSecurityEntity`](../../doc/models/other-security-entity.md) | Optional | Information about the security specific to the type of security |
| `stock_security` | [`StockSecurityEntity`](../../doc/models/stock-security-entity.md) | Optional | Information about the stock security specific to the type of security |
| `sweep_security` | [`SweepSecurityEntity`](../../doc/models/sweep-security-entity.md) | Optional | Information about the sweep security specific to the type of security |
| `debt_security` | [`DebtSecurityEntity`](../../doc/models/debt-security-entity.md) | Optional | Information about the debt security specific to the type of security |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "assetClasses": [
    {
      "assetClass": "DOMESTICBOND",
      "percent": 174.1,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    {
      "assetClass": "DOMESTICBOND",
      "percent": 174.1,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "averageCost": false,
  "cashAccount": false,
  "changeInPrice": 26.72,
  "currency": {
    "currencyCode": "currencyCode0",
    "currencyRate": 27.48,
    "originalCurrencyCode": "originalCurrencyCode4",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

