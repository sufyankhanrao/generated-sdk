
# Transaction Exceptions

## Structure

`TransactionExceptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sales_item_id` | `float` | Optional | Unique Sales Item Identifier |
| `card_id` | `int` | Optional | Unique Card Identifier |
| `product_id` | `int` | Optional | Product Id |
| `transaction_guid` | `str` | Optional | Transaction Unique Identifier |
| `transaction_date` | `str` | Optional | Local Transaction Date  of where the transaction took place<br>Format: yyyyMMdd |
| `customer_invoice_value_total_gross` | `float` | Optional | Total Gross Amount for the Invoice Customer |
| `card_pan` | `str` | Optional | Card PAN number<br>Returns masked PAN number when masking is enabled at the Microservices configuration (Mask all digits except the last 6 digits of the PAN) |
| `card_expiry` | `str` | Optional | Card Expiry Date<br>Format: yyyyMMdd |
| `transaction_time` | `str` | Optional | Local Transaction Time of where the transaction took place<br>Format: HH:mm:ss (24 hours format) |
| `utc_offset` | `str` | Optional | UTC Offset extracted from GFN Sales Date time. Note: This may not be accurate for all TPN transactions<br>Format: +/-HH:mm:ss (24 hours format) |
| `fleet_id_input` | `str` | Optional | Fleet Id Input as entered by the drivers at the time of transaction |
| `odometer_input` | `int` | Optional | Odometer Input as entered by the drivers at the time of transaction |
| `driver_name` | `str` | Optional | Driver Name embossed on the card |
| `vehicle_registration` | `str` | Optional | Vehicle Registration Number embossed on the card |
| `invoice_currency_code` | `str` | Optional | ISO currency code (Example: GBP) |
| `invoice_currency_symbol` | `str` | Optional | Currency symbol of the Invoice Currency Code (i.e. £, $, etc.,) |
| `transaction_currency_code` | `str` | Optional | ISO currency code |
| `transaction_currency_symbol` | `str` | Optional | Currency symbol of the Transaction Currency Code (i.e. £, $, etc.,) |
| `transaction_net_amount` | `float` | Optional | Net Amount |
| `transaction_tax` | `float` | Optional | Tax Amount |
| `transaction_gross_amount` | `float` | Optional | Gross Amount |
| `invoice_net_amount` | `float` | Optional | Invoiced Net Amount |
| `invoice_tax` | `float` | Optional | Invoiced Tax Amount |
| `invoice_gross_amount` | `float` | Optional | Invoice Gross Amount |
| `purchased_in_country` | `str` | Optional | Country of Purchase (Ex: France, Germany, etc.,) |
| `account_id` | `int` | Optional | Account Id |
| `account_number` | `str` | Optional | Account Number |
| `account_name` | `str` | Optional | Account Name |
| `account_short_name` | `str` | Optional | Account Short Name |
| `quantity` | `float` | Optional | Quantity/Volume |
| `fuel_product` | `bool` | Optional | True if the product on transaction is listed as a fuel product else return false |
| `unit_price_in_transaction_currency` | `float` | Optional | Product Unit Price in transaction currency |
| `unit_price_in_invoice_currency` | `float` | Optional | Product Unit Price in invoice currency |
| `unit_discount_transaction_currency` | `float` | Optional | Unit Discount in transaction currency |
| `unit_discount_invoice_currency` | `float` | Optional | Unit Discount in invoice currency |
| `is_invoiced` | `bool` | Optional | True when the transaction is already invoice, else return False |
| `invoice_number` | `str` | Optional | Invoice Number if invoiced |
| `invoice_date` | `str` | Optional | Invoice Date<br>Format: yyyyMMdd HH:mm:ss |
| `site_code` | `str` | Optional | Site Code |
| `site_name` | `str` | Optional | Site Name |
| `site_country` | `str` | Optional | Site Country |
| `location` | [`ExceptionSiteLocation`](../../doc/models/exception-site-location.md) | Optional | Geography Location entity for Site Location |
| `card_group_name` | `str` | Optional | Card Group Name |
| `receipt_number` | `str` | Optional | Receipt Number |
| `product_code` | `str` | Optional | Product Code |
| `product_name` | `str` | Optional | Product Name |
| `product_group_id` | `int` | Optional | Product Group Id |
| `product_group_name` | `str` | Optional | Product Group Name |
| `del_co_exchange_rate` | `float` | Optional | DelCo Exchange Rate (Site exchange rate) |
| `col_co_exchange_rate` | `float` | Optional | ColCo Exchange Rate (Customer exchange rate) |
| `is_shell_site` | `bool` | Optional | True when transaction occurred at a Shell site else return False |
| `network` | `str` | Optional | Network as configured |
| `site_group_id` | `int` | Optional | Site Group Id |
| `site_group_name` | `str` | Optional | Site GroupName |
| `posting_date` | `str` | Optional | Site GroupName |
| `issuer_code` | `str` | Optional | First digits of the Card PAN<br>7002 = Fleet  <br>7077 = CRT |
| `purchased_in_country_code` | `str` | Optional | ISO code of the country where the transaction took place |
| `customer_country_code` | `str` | Optional | ISO code of the  Customer Country |
| `customer_country` | `str` | Optional | Name of the Customer Country |
| `release_code` | `str` | Optional | Release code, 7th Digit of the Card PAN |
| `card_group_id` | `str` | Optional | Card group ID |
| `card_sequence_number` | `str` | Optional | 3 digits, Card sequence number and Check digit  (Digit 16,17 and 18 on the card pan) |
| `check_digit` | `str` | Optional | Check digit, Last number of the card pan |
| `fleet_id_description` | `str` | Optional | FleetId/CRN description in Card Platform configured at the account level |
| `vat_rate` | `float` | Optional | VAT Percentage |
| `vat_category` | `str` | Optional | VAT Category Id-Description<br>1-Zero Rated<br>2-A1 PH-O 12% Sales Domestic<br>3-VAT exempt |
| `effective_discount_in_trx_currency` | `str` | Optional | Effective Discount (excluding VAT, in transaction currency)  4 digits |
| `transaction_type` | `str` | Optional | Transaction Type |
| `pin_indicator` | `str` | Optional | Pin Indicator (Indicates whether PIN used or not used at the time of transaction) |
| `vat_applicable` | `str` | Optional | Is VAT Applicable for this transaction<br>“Y” or “N” |
| `net_invoice_indicator` | `str` | Optional | Net Invoice Indicator, Will the customer receive an invoice without VAT?<br>Example: “Y” or “N” |
| `customer_currency_code` | `str` | Optional | Customer currency code |
| `customer_currency_symbol` | `str` | Optional | Customer currency Symbol |
| `effective_unit_discount_in_customer_currency` | `float` | Optional | Effective Unit Discount |
| `effective_discount_in_customer_currency` | `float` | Optional | Effective Discount |
| `va_ton_net_amount_in_customer_currency` | `float` | Optional | VAT on Net Amount |
| `discount_type` | `str` | Optional | Discount Type<br>Example: 1-None<br>2-Pence per unit<br>3-Percentage |
| `transaction_status` | `str` | Optional | Transaction status  "U" or "I"<br>“U” stands for Uninvoiced<br>“I” stands for Invoiced |
| `payer_group` | `str` | Optional | Payer Group applicable for the Large Customer NL+8 digit code |
| `refund_flag` | `str` | Optional | Refund Flag “N” for Not Refunded and “Y” for Refunded. |
| `original_sales_item_id` | `float` | Optional | Shows Sales Item Id of the original item that was refunded |
| `delco_name` | `str` | Optional | Delco Name |
| `delco_code` | `str` | Optional | Delco Code |
| `payer_number` | `str` | Optional | Payer number |
| `payer_name` | `str` | Optional | Payer name |
| `card_expiry_period` | `str` | Optional | Year/Month of the Card Expiry captured on the transaction |
| `authorisation_code` | `str` | Optional | Authorisation code of the transaction |
| `transaction_id` | `str` | Optional | Unique id of the transaction that may include one or more salesitems |
| `transaction_line` | `str` | Optional | Transaction line item number |
| `allow_clearing` | `str` | Optional | Is the Sales Item allowed for clearing? i.e. not written off<br>Example: “Y” or “N” |
| `crm_number` | `str` | Optional | CRM Case number if the sales item is in dispute |
| `dispute_status` | `str` | Optional | Sales Item Dispute Status if disputed<br>0	No Dispute<br>1	In Dispute<br>2	Re-Instated<br>3	Adjusted<br>4	Written Off by Colco<br>5	Written Off by Delco<br>6	Charged Back to Site |
| `rebate_rate` | `float` | Optional | Unit discount in customer currency |
| `del_co_to_col_co_exchange_rate` | `float` | Optional | Exchange rate from transaction currency to customer currency. |
| `net_euro_amount` | `float` | Optional | Net euro amount. |
| `euro_rebate_amount` | `float` | Optional | Euro rebate amount. |
| `euro_vat_amount` | `float` | Optional | Euro VAT amount. |
| `parent_customer_number` | `str` | Optional | Parent customer number |
| `va_ton_net_amount` | `float` | Optional | VAT on Net Amount (in transaction currency) 2 decimals |
| `vat_country` | `str` | Optional | VAT Country |

## Example (as JSON)

```json
{
  "SalesItemId": 113.2,
  "CardId": 104,
  "ProductId": 220,
  "TransactionGUID": "TransactionGUID2",
  "TransactionDate": "TransactionDate6"
}
```

