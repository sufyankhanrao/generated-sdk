
# Price List

## Structure

`PriceList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date` | `str` | Optional | Date on which the price is applicable.<br>Format: yyyyMMdd<br>E.g.: 20180131 |
| `day` | `str` | Optional | Day on which the price is applicable.<br>E.g.: Sunday, Monday etc. |
| `mtype` | `str` | Optional | Price list type.<br>E.g., List, Shell Standard International List |
| `price_list_id` | `int` | Optional | Price list ID |
| `price_list_description` | `str` | Optional | Price list description<br>E.g., UK Fuels CRT Reseller List Price |
| `price_rule_id` | `int` | Optional | Price Rule Id |
| `price_rule_name` | `str` | Optional | Price Rule Name |
| `del_co_id` | `int` | Optional | DelCo Id |
| `country_code` | `str` | Optional | Country ISO Code<br>E.g., UK, NL, etc., |
| `country` | `str` | Optional | Country<br>E.g., United Kingdom, Netherlands etc |
| `product_group_id` | `int` | Optional | Product Group Id |
| `product_group_name` | `str` | Optional | Product Group name |
| `product_code` | `str` | Optional | Client Product Code |
| `product_id` | `int` | Optional | Product Id |
| `product_name` | `str` | Optional | Product name in English |
| `price_per_unit` | `float` | Optional | Price per unit |
| `currency_code` | `str` | Optional | Currency Code.<br>Format : 3 digit ISO code |
| `currency_symbol` | `str` | Optional | Currency Symbol<br>Example: £ |
| `price_type` | `str` | Optional | Price Type<br>Possible Values are:<br>•	Country– Price rule defined at country whereas Price Rule DelcoId same as ColcoId.<br>•	TPNDelcoPrice – Price rule defined in the TPN whereas Price Rule DelcoId is different from ColcoId.<br>•	NetworkPrice – Price rule defined at Fuel Network level.<br>•	Other – Price rule defined at either Site or SiteGroup level. |
| `site_group_id` | `int` | Optional | Site-Group ID<br>E.g.: 100007 |
| `site_group_name` | `str` | Optional | Site-Group name |
| `site_code` | `int` | Optional | Site Code |
| `site_id` | `int` | Optional | Site ID |
| `site_name` | `str` | Optional | Site Name |
| `fuel_network_id` | `int` | Optional | Fuel Network ID |
| `network_name` | `str` | Optional | Network Name |
| `price_rule_delco_id` | `int` | Optional | PriceRuleDelcoId |
| `price_rule_delco_name` | `str` | Optional | Company Name of the price rule DelCo.<br><br>E.g.:<br>•	Pilipinas Shell Petroleum Corp<br>•	Shell U.K. Oil Products Limited<br>•	G & V SERVICE STATIONS NV |
| `price_rule_country` | `str` | Optional | PriceRuleCountry<br>E.g.: United Kingdom |
| `price_rule_country_code` | `str` | Optional | ISO Code of PriceRuleCountry<br>E.g.: UK, NL, etc., |
| `price_rule_basis_id` | `int` | Optional | PriceRuleBasisId |
| `discount_value` | `float` | Optional | Discount value |
| `price_per_unit_after_discount` | `float` | Optional | Price per unit after discount |
| `vat_percentage` | `float` | Optional | VAT Percentage |
| `price_rule_category_id` | `int` | Optional | PriceRuleCategoryId |
| `tiers` | [`List[Tier]`](../../doc/models/tier.md) | Optional | - |

## Example (as JSON)

```json
{
  "Date": "Date8",
  "Day": "Day4",
  "Type": "Type0",
  "PriceListId": 210,
  "PriceListDescription": "PriceListDescription0"
}
```

