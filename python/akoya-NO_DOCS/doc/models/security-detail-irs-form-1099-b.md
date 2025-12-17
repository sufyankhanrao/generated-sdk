
# Security Detail Irs Form 1099 B

Tax information for a single security transaction

*This model accepts additional fields of type Any.*

## Structure

`SecurityDetailIrsForm1099B`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkbox_on_form_8949` | `str` | Optional | Applicable checkbox on Form 8949 |
| `security_name` | `str` | Optional | Security name |
| `number_of_shares` | `float` | Optional | Number of shares |
| `sale_description` | `str` | Optional | Box 1a, Description of property |
| `date_acquired` | `date` | Optional | Box 1b, Date acquired |
| `various_dates_acquired` | `bool` | Optional | Box 1b, Date acquired Various |
| `date_of_sale` | `date` | Optional | Box 1c, Date sold or disposed |
| `sales_price` | `float` | Optional | Box 1d, Proceeds (not price per share) |
| `accrued_market_discount` | `float` | Optional | Box 1f, Accrued market discount |
| `adjustment_codes` | [`List[CodeAndAmount]`](../../doc/models/code-and-amount.md) | Optional | Other adjustments (code and amount) |
| `cost_basis` | `float` | Optional | Box 1e, Cost or other basis |
| `corrected_cost_basis` | `float` | Optional | Corrected cost basis. May be supplied in lieu of adjustmentCode code B. If both adjustmentCodes and correctedCostBasis are supplied, costBasis plus adjustmentCode B should equal correctedCostBasis |
| `wash_sale_loss_disallowed` | `float` | Optional | Box 1g, Wash sale loss disallowed |
| `long_or_short` | [`SaleTermType`](../../doc/models/sale-term-type.md) | Optional | LONG or SHORT (1099-B box 2) |
| `ordinary` | `bool` | Optional | Box 2, Ordinary |
| `collectible` | `bool` | Optional | Box 3, Collectibles |
| `qof` | `bool` | Optional | Box 3, Qualified Opportunity Fund (QOF) |
| `federal_tax_withheld` | `float` | Optional | Box 4, Federal income tax withheld |
| `noncovered_security` | `bool` | Optional | Box 5, Noncovered security |
| `gross_or_net` | [`SaleProceedsType`](../../doc/models/sale-proceeds-type.md) | Optional | Box 6, Reported to IRS: GROSS or NET |
| `loss_not_allowed` | `bool` | Optional | Box 7, Loss not allowed based on proceeds |
| `basis_reported` | `bool` | Optional | Box 12, Basis reported to IRS |
| `state_and_local` | [`List[StateAndLocalTaxWithholding]`](../../doc/models/state-and-local-tax-withholding.md) | Optional | Boxes 14-16, State and Local tax withholding |
| `cusip` | `str` | Optional | CUSIP number |
| `foreign_account_tax_compliance` | `bool` | Optional | Foreign account tax compliance |
| `expired_option` | [`ExpiredOptionType`](../../doc/models/expired-option-type.md) | Optional | To indicate gain or loss resulted from option expiration. If salesPrice (1d, proceeds) is zero, use PURCHASED. If costBasis (1e) is zero, use GRANTED |
| `investment_sale_type` | [`InvestmentSaleType`](../../doc/models/investment-sale-type.md) | Optional | Type of investment sale |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "dateAcquired": "2021-07-15",
  "dateOfSale": "2021-07-15",
  "checkboxOnForm8949": "checkboxOnForm89498",
  "securityName": "securityName6",
  "numberOfShares": 126.44,
  "saleDescription": "saleDescription4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

