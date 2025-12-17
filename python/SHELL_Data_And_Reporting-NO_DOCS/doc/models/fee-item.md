
# Fee Item

## Structure

`FeeItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fee_item_id` | `int` | Optional | Fee Item unique identifier in the H3 Cards Platform |
| `account_id` | `int` | Optional | Account Id |
| `account_number` | `str` | Optional | Account Number |
| `account_short_name` | `str` | Optional | Account short Number |
| `invoice_account_id` | `int` | Optional | Invoice Account Id |
| `invoice_account_number` | `str` | Optional | Invoice Account Number |
| `invoice_account_short_name` | `str` | Optional | Invoice Account short Name |
| `payer_id` | `int` | Optional | Payer Id |
| `payer_number` | `str` | Optional | Payer Number |
| `payer_short_name` | `str` | Optional | Payer short Name |
| `card_id` | `int` | Optional | Unique Card Id |
| `pan` | `str` | Optional | Card PAN |
| `card_group_id` | `int` | Optional | Card Group Id |
| `card_group_name` | `str` | Optional | Card Group Name |
| `fee_type_id` | `int` | Optional | Fee type identifier. |
| `fee_type` | `str` | Optional | Fee type description |
| `fee_type_group` | `str` | Optional | Fee type group in under which the Fee item is generated.<br>Example:<br>Account<br>Card<br>Others |
| `fee_rule_id` | `int` | Optional | Fee rule identifier |
| `fee_rule_description` | `str` | Optional | Fee rule description |
| `fee_rule_tiers` | [`List[FeesFeeRuleTiers]`](../../doc/models/fees-fee-rule-tiers.md) | Optional | - |
| `fee_item_date` | `str` | Optional | Local Fee Item Date of when the transaction took place<br>Format: yyyyMMdd |
| `fee_item_time` | `str` | Optional | Local Fee Item Time of where the transaction took place<br>Format: HH:mm:ss (24 hours format) |
| `is_manual` | `bool` | Optional | True/False.<br>Is manual |
| `is_cancelled` | `bool` | Optional | True/False.<br>Is cancelled |
| `customer_currency_code` | `str` | Optional | ISO currency code<br>Example: GBP |
| `customer_currency_symbol` | `str` | Optional | Currency symbol of the Currency Code<br>Example: £, $ |
| `product_id` | `int` | Optional | Product Id<br>Example: Sample list of product ids and description.<br>100 Service fee<br>102 Invoice production fee<br>103 Account fee<br>104 Transaction fee<br>105 Card membership fee |
| `product_code` | `str` | Optional | Product Code – Global as per GFN configuration<br>Example:<br>2 Service fee<br>4 Invoice production fee<br>5 Account fee<br>6 Transaction fee<br>7 Card membership fee |
| `product_name` | `str` | Optional | Product Name<br>Example: Sample list of product ids and description.<br>Service fee<br>Invoice production fee |
| `product_group_id` | `int` | Optional | Product Group Id<br>Example: Sample list<br>22	Card related fees<br>23	Monetary Adjustment |
| `product_group_name` | `str` | Optional | Product Group Name<br>Example: Sample list<br>22	Card related fees<br>23	Monetary Adjustment |
| `line_item_description` | `str` | Optional | Line Item Description generally the quantity as printed on Invoice or the manually keyed in description for manual fees |
| `quantity` | `int` | Optional | Quantity |
| `is_invoiced` | `bool` | Optional | True/False.<br>Is fee item invoiced |
| `vat_country_code` | `str` | Optional | VAT country ISO code |
| `vat_country_name` | `str` | Optional | VAT country name |
| `vat_percentage` | `float` | Optional | VAT percentage |
| `vat_category_id` | `int` | Optional | VAT Category identifier |
| `vat_category_description` | `str` | Optional | VAT Category description |
| `legislative_region_id` | `int` | Optional | Legislative region id |
| `legislative_region_name` | `str` | Optional | Legislative region name |
| `system_entry_date` | `str` | Optional | System entry date |
| `system_entry_time` | `str` | Optional | System entry time |
| `col_co_net_amount` | `float` | Optional | ColCo net amount |
| `col_co_vat_amount` | `float` | Optional | ColCoVAT amount |
| `col_co_gross_amount` | `float` | Optional | ColCo gross amount |
| `interim_invoice_id` | `int` | Optional | Interim invoice id |
| `interim_invoice_number` | `str` | Optional | Interim invoice number |
| `invoice_id` | `int` | Optional | Invoice id |
| `invoice_number` | `str` | Optional | Invoice number |
| `invoice_date` | `str` | Optional | Invoice date<br>Format: yyyyMMdd |
| `customer_exchange_rate` | `float` | Optional | Customer exchange rate |
| `invoice_net_amount` | `float` | Optional | Invoice net amount |
| `invoice_gross_amount` | `float` | Optional | Invoice gross amount |
| `invoice_vat_amount` | `float` | Optional | Invoice VAT amount |
| `reverse_charge` | `bool` | Optional | True/False.<br>Reverse charge. |
| `original_fee_item_id` | `int` | Optional | Original Fee Item id. |
| `original_currency_code` | `str` | Optional | Original FeeItem Currency ISO code. |
| `original_currency_symbol` | `str` | Optional | Original FeeItem currency symbol |
| `original_unit_price` | `float` | Optional | Original FeeItem unit price |
| `original_net_amount` | `float` | Optional | Original FeeItem net amount |
| `original_vat_amount` | `float` | Optional | Original FeeItem VAT amount |
| `original_gross_amount` | `float` | Optional | Original FeeItem gross amount |
| `original_exchange_rate` | `float` | Optional | Original FeeItem exchange rate |
| `original_legislative_region_id` | `int` | Optional | Original legislative region id |
| `original_legislative_region_name` | `str` | Optional | Original legislative region name |
| `frequency` | `str` | Optional | Fee frequency derived from Fee rules if applicable<br>Returns ID-Description in one field<br>Example:<br>1- Daily (all days)<br>2-Daily (only working days)<br>3-Weekly – Monday<br>4-Weekly - Tuesday |
| `fee_item_card_level_breakup` | `str` | Optional | Fee breakup at card level for Fee Items where applicable. |
| `original_fee_item_invoice_id` | `int` | Optional | Invoice Id/ Billing Document Id of the original fee item (when not null).<br>Applicable only for fee items that are refund to an original fee item that is already invoiced. |
| `original_fee_item_invoice_number` | `str` | Optional | Invoice Number of the original fee item (when not null).<br>Applicable only for fee items that are refund to an original fee item that is already invoiced. |
| `original_fee_item_invoice_date` | `str` | Optional | Invoice Date of the original fee item (when not null).<br>Applicable only for fee items that are refund to an original fee item that is already invoiced.<br>Format: yyyyMMdd |
| `driver_name` | `str` | Optional | Driver name embossed on the Card |
| `emboss_text` | `str` | Optional | Text embossed on the Card |
| `vrn` | `str` | Optional | Reg. Number embossed on the Card |

## Example (as JSON)

```json
{
  "FeeItemId": 156,
  "AccountId": 244,
  "AccountNumber": "AccountNumber6",
  "AccountShortName": "AccountShortName8",
  "InvoiceAccountId": 204
}
```

