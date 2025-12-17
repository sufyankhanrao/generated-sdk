
# Priced Response Data

## Structure

`PricedResponseData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | Name of the account<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `36` |
| `account_id` | `int` | Optional | Account Id (i.e. Customer Id of the Sub Account in GFN) of the selected account. |
| `account_number` | `str` | Optional | AccountNumber of the selected account. |
| `account_short_name` | `str` | Optional | Nick name of the account<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `25` |
| `additional_1` | `str` | Optional | Addtional SerialId or endpoint Id<br><br>**Constraints**: *Minimum Length*: `14`, *Maximum Length*: `20` |
| `additional_2` | `str` | Optional | Addtional SerialId or endpoint Id<br><br>**Constraints**: *Minimum Length*: `14`, *Maximum Length*: `20` |
| `additional_3` | `str` | Optional | Addtional SerialId or endpoint Id<br><br>**Constraints**: *Minimum Length*: `14`, *Maximum Length*: `20` |
| `additional_4` | `str` | Optional | Addtional SerialId or endpoint Id<br><br>**Constraints**: *Minimum Length*: `14`, *Maximum Length*: `20` |
| `allow_clearing` | `str` | Optional | Allow clearings<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `25` |
| `authorisation_code` | `int` | Optional | Autorization code<br><br>**Constraints**: `>= 1`, `<= 999999` |
| `transaction_status` | `str` | Optional | Status of the transaction<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `1` |
| `driver_name` | `str` | Optional | Driver Name of Card record<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `25` |
| `card_expiry_period` | `int` | Optional | Expiry period of the card<br><br>**Constraints**: `>= 1`, `<= 9999` |
| `card_expiry` | `date` | Optional | Card Expiry Date |
| `card_group_id` | `int` | Optional | Card Group Code<br><br>**Constraints**: `>= 1`, `<= 99999` |
| `card_group_name` | `str` | Optional | Group nmae of the card |
| `issuer_code` | `int` | Optional | Issuer code<br><br>**Constraints**: `>= 1`, `<= 9999` |
| `card_pan` | `str` | Optional | Full Card PAN<br><br>**Constraints**: *Minimum Length*: `19`, *Maximum Length*: `19` |
| `release_code` | `int` | Optional | Release code<br><br>**Constraints**: `>= 1`, `<= 10` |
| `card_sequence_number` | `int` | Optional | Sequesnce number of the card<br><br>**Constraints**: `>= 1`, `<= 999` |
| `card_type` | `str` | Optional | Type of card<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `50` |
| `col_co_code` | `str` | Optional | Collecting Company Code (Shell Code) of the selected payer.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `unit_discount_invoice_currency` | `float` | Optional | Unit discount Invoice currency |
| `col_co_exchange_rate` | `float` | Optional | Colco exchange rate |
| `invoice_currency_symbol` | `str` | Optional | Currency symbol on which the invoice was raised<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `correction_flag` | `bool` | Optional | Is there any correction |
| `crm_number` | `float` | Optional | CRM number<br><br>**Constraints**: `>= 10`, `<= 10` |
| `customer_country` | `str` | Optional | Customer country<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `30` |
| `customer_currency_code` | `str` | Optional | Curreny which customer uses to transact.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `customer_currency_symbol` | `str` | Optional | Custome currency symbol<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `1` |
| `rebateon_net_amount_in_customer_currency` | `float` | Optional | Rebate on net amount in customer currency |
| `effective_discount_in_customer_currency` | `float` | Optional | Effective discount in customers currency |
| `effective_unit_discount_in_customer_currency` | `float` | Optional | effectiive unit discount in customers currency |
| `unit_price_in_invoice_currency` | `float` | Optional | Unitpricing in invoice currency |
| `invoice_tax` | `float` | Optional | Invoice tax |
| `invoice_gross_amount` | `float` | Optional | Invoice amount befor tax |
| `invoice_net_amount` | `float` | Optional | Invoice amount after tax |
| `va_ton_net_amount_in_customer_currency` | `float` | Optional | Vat on net amount in customer currency |
| `customer_retail_price_unit_gross` | `float` | Optional | Customer retail unit price before tax |
| `customer_retail_value_total_gross` | `float` | Optional | Total Customer retail value before tax |
| `customer_retail_value_total_net` | `float` | Optional | Total customer retail value after tax |
| `transaction_type_description` | `float` | Optional | Trasaction type description |
| `rebateon_net_amount_in_transaction_currency` | `float` | Optional | Rebate give to net amountin transaction currency that is used |
| `effective_discount_in_trx_currency` | `float` | Optional | Currency used to giveEffective discount on transactions |
| `del_co_to_col_co_exchange_rate` | `int` | Optional | Exchange rate between Delco and Colco |
| `cards` | `List[int]` | Optional | **Constraints**: *Minimum Items*: `1`, *Maximum Items*: `500` |
| `unit_discount_transaction_currency` | `float` | Optional | Currency used forto provide unit Transaction discount |
| `transaction_gross_amount` | `float` | Optional | Transactional amount before tax |
| `transaction_net_amount` | `float` | Optional | Transaction net amount after tax |
| `transaction_tax` | `float` | Optional | Transaction tax |
| `va_ton_net_amount` | `float` | Optional | Transactinal tax rates |
| `delco_list_price_unit_net` | `float` | Optional | Priv |
| `delco_retail_price_unit_gross` | `float` | Optional | Delco retail price per unit before tax |
| `unit_price_in_transaction_currency` | `float` | Optional | Delco retail price per unit after tax |
| `delco_retail_price_unit_net` | `float` | Optional | Delco retail price per unit |
| `delco_retail_value_total_gross` | `float` | Optional | Delco retail price before tax |
| `delco_retail_value_total_net` | `float` | Optional | Delco per unit price after tax |
| `transaction_currency_symbol` | `str` | Optional | Currency used for transaction. |
| `discount_type` | `str` | Optional | Type of discount available |
| `dispute_status` | `bool` | Optional | Is there any dispute status?True or False<br><br>**Default**: `False` |
| `is_shell_site` | `bool` | Optional | Is it a shell sites?True or False<br><br>**Default**: `False` |
| `fleet_id_input` | `str` | Optional | Fleet identifier |
| `incoming_product_code` | `int` | Optional | In coming product code |
| `posting_date` | `date` | Optional | Date of Posting |
| `posting_time` | `datetime` | Optional | Time whern posting happened |
| `product_code` | `int` | Optional | Product Code - 21 Unleaded - High octane,22 Unleaded - Medium octane,23 Unleaded - Low octane,24 Unleaded Environmental |
| `product_name` | `str` | Optional | Name of the product<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `30` |
| `product_group_id` | `int` | Optional | Id of the product to which group it belongs |
| `incoming_currency_code` | `str` | Optional | In coming currecncy code<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `incoming_site_description` | `str` | Optional | In coming Site description |
| `location` | `str` | Optional | Location of the Shell site<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `50` |
| `site_name` | `str` | Optional | Shell site name<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `50` |
| `site_code` | `int` | Optional | Shell site code |
| `incoming_site_number` | `int` | Optional | In coming site number |
| `invoice_currency_code` | `str` | Optional | Currency code on which the invoice is raised<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `invoice_date` | `date` | Optional | Date on which the invoice was raised |
| `invoice_number` | `float` | Optional | Invoice number |
| `fuel_product` | `bool` | Optional | Is it a fuel product? True or False |
| `vat_applicable` | `str` | Optional | Is VAT applicable?Y or N<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `1` |
| `payer_name` | `str` | Optional | Name of the payer<br><br>**Constraints**: *Minimum Length*: `20`, *Maximum Length*: `50` |
| `payer_number` | `str` | Optional | Payer account number<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `15` |
| `parent_customer_number` | `str` | Optional | Parent account number of the payer<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `15` |
| `payer_group` | `str` | Optional | The group which the payer belongs to |
| `payer_group_name` | `str` | Optional | Name of the group to which the payer belongs to.<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `50` |
| `check_digit` | `int` | Optional | Check digit |
| `net_invoice_indicator` | `str` | Optional | After tax net invoice number |
| `delco_code` | `int` | Optional | Delco code |
| `network_code` | `int` | Optional | Network  code of the payer<br><br>**Constraints**: `>= 3`, `<= 3` |
| `purchased_in_country` | `str` | Optional | Country of purchase<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `50` |
| `site_country` | `str` | Optional | Country where the site exists<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `50` |
| `vat_country` | `str` | Optional | Country where VAT is applicable<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `50` |
| `delco_name` | `str` | Optional | Name of the delivery company<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `50` |
| `network` | `str` | Optional | Network of the Delivery company<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `25` |
| `odometer_input` | `int` | Optional | Odometet input |
| `original_sales_item_id` | `str` | Optional | Original item identifier for sales<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `25` |
| `fleet_id_description` | `str` | Optional | Fleet identifier description |
| `parent_customer_id` | `int` | Optional | Identifier of parent customer |
| `pin_indicator` | `str` | Optional | PIN indicator |
| `product_group_name` | `str` | Optional | Name og the group the product belongs to |
| `purchased_in_country_code` | `str` | Optional | The countroy code where the purchase was made |
| `quantity` | `float` | Optional | Quantity of the product |
| `rebate_rate` | `float` | Optional | Rebate rate if any |
| `receipt_number` | `int` | Optional | Reciept number |
| `refund_flag` | [`PricedTransactionRespV2RefundFlagEnum`](../../doc/models/priced-transaction-resp-v2-refund-flag-enum.md) | Optional | Flag to check if there is any refund<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `1` |
| `site_group_id` | `int` | Optional | Group identifier for the site |
| `site_group_name` | `str` | Optional | Name of the Site group |
| `latitude` | `float` | Optional | Latitude of the site |
| `longitude` | `float` | Optional | Longitude of the site |
| `del_co_exchange_rate` | `float` | Optional | Delivery company exchange rate |
| `euro_rebate_amount` | `float` | Optional | Rebate amount in Euros |
| `net_euro_amount` | `float` | Optional | Net amount in Euros |
| `euro_vat_amount` | `float` | Optional | Vat amount in Euros |
| `parent_customer_name` | `str` | Optional | Customers parent name<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `50` |
| `is_invoiced` | `bool` | Optional | Is invoice raised<br><br>**Default**: `False` |
| `transaction_currency_code` | `str` | Optional | Transaction currency code |
| `credit_debit_code` | `str` | Optional | Is it Credit or debit C for credit D for Debit |
| `transaction_date` | `date` | Optional | Date of transaction |
| `transaction_time` | `datetime` | Optional | Time of transaction |
| `transaction_item_id` | `str` | Optional | Identifier of the Iem in transaction |
| `trn_identifier` | `str` | Optional | Transaction identifier |
| `mtype` | `str` | Optional | Transaction type for Delco |
| `transaction_line` | `int` | Optional | - |
| `transaction_type` | `str` | Optional | Transaction type Colco |
| `utc_offset` | `str` | Optional | Leaving country |
| `vat_category` | `str` | Optional | To which category and counry does the  VAT come under |
| `vat_rate` | `float` | Optional | VAT rate |
| `vehicle_registration` | `str` | Optional | Vehicle registration number |
| `is_cancelled` | `str` | Optional | Check if the pruchase is cancelled<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `1` |
| `col_co_gross_amount` | `float` | Optional | Gross amount from Colco |
| `col_co_net_amount` | `float` | Optional | Net amount from Colco |
| `col_co_vat_amount` | `float` | Optional | Colco VAT amount |
| `original_currency_symbol` | `str` | Optional | Original currency code<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `1` |
| `original_currency_code` | `str` | Optional | Original currency code<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `1` |
| `original_vat_amount` | `float` | Optional | Original VAT amount |
| `emboss_text` | `str` | Optional | Comapany name embosses in text<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `50` |
| `original_exchange_rate` | `float` | Optional | Orginal exchange rate |
| `original_transaction_item_invoice_date` | `date` | Optional | Original treansaction date |
| `fee_type_id` | `int` | Optional | Fee type identifier<br><br>**Constraints**: `>= 1`, `<= 1` |
| `line_item_description` | `bool` | Optional | Line item identifier of the product<br><br>**Default**: `False` |
| `fee_rule_description` | `str` | Optional | Fee rule description<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `25` |
| `frequency` | `int` | Optional | Frequency of transaction<br><br>**Constraints**: `>= 1`, `<= 1` |
| `fee_rule_id` | `int` | Optional | Fee rule identifier<br><br>**Constraints**: `>= 1`, `<= 1` |
| `system_entry_date` | `date` | Optional | Entry date in the system |
| `system_entry_time` | `datetime` | Optional | Entry time in the system |
| `is_manual` | `str` | Optional | Checking if its manual<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `1` |
| `original_transaction_item_id` | `str` | Optional | Is it manual<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `1` |
| `original_transaction_item_invoice_number` | `int` | Optional | Original invoice transaction number |
| `original_transaction_item_invoice_id` | `int` | Optional | Original Invoice transaction Identifier |
| `payer_short_name` | `str` | Optional | Payers short name<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `50` |
| `reverse_charge` | `str` | Optional | Is reverse charge?<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `1` |
| `original_gross_amount` | `float` | Optional | Original gross amount |
| `original_net_amount` | `float` | Optional | Original Net amount |
| `unit_of_measure` | `str` | Optional | Unit of measure<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `1` |
| `road_type` | `str` | Optional | Type of road<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `50` |
| `customer_country_iso_code` | `str` | Optional | Customer country ISO Code<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `ev_operator` | `str` | Optional | EvOperator Name<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `20` |
| `ev_serial_id` | `str` | Optional | Ev Operator identifier<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `50` |
| `ev_charge_point_serial` | `str` | Optional | EV Charging point iserial identifier<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `50` |
| `ev_charge_point_connector_type` | `int` | Optional | Ev chariging connector type |
| `ev_charge_point_connector_type_description` | `str` | Optional | EV charging point connector type description |
| `ev_charge_duration` | `str` | Optional | Ev charging Duration |
| `ev_charge_start_date` | `date` | Optional | EvCharging start Date |
| `ev_charge_start_time` | `datetime` | Optional | EvCharging start time |
| `ev_charge_end_date` | `date` | Optional | EvCharging End Date |
| `ev_charge_end_time` | `datetime` | Optional | EvCharging End time |
| `hosting_collecting_company_number` | `int` | Optional | - |
| `transaction_id` | `float` | Optional | - |
| `fuel_only` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "AccountName": "Blue Colour Ltd",
  "AccountId": 29484,
  "AccountNumber": "DE26667080",
  "AccountShortName": "Mathew",
  "Additional1": "GBALLEGO0002452",
  "Additional2": "GBALLEGO0002452",
  "Additional3": "GBALLEGO0002452",
  "Additional4": "GBALLEGO0002452",
  "AllowClearing": "Null",
  "AuthorisationCode": 300796,
  "TransactionStatus": "Y",
  "DriverName": "SATTY BHAMRA",
  "CardExpiryPeriod": 2204,
  "CardExpiry": "2022-01-01",
  "CardGroupId": 40000,
  "CardGroupName": "006240 FIRE BRIGHT SOLUTIONS",
  "IssuerCode": 7002,
  "CardPAN": "7002053465789891000",
  "ReleaseCode": 9,
  "CardSequenceNumber": 617,
  "CardType": "GB STD FLT NAT SINGLE R9",
  "ColCoCode": "014",
  "UnitDiscountInvoiceCurrency": -0.0051,
  "ColCoExchangeRate": 0.851858,
  "InvoiceCurrencySymbol": "GBP",
  "CustomerCountry": "United Kingdom",
  "CustomerCurrencyCode": "GBP",
  "CustomerCurrencySymbol": "£",
  "EffectiveDiscountInCustomerCurrency": -0.22,
  "EffectiveUnitDiscountInCustomerCurrency": -0.0051,
  "UnitPriceInInvoiceCurrency": 1.1024,
  "InvoiceTax": 0,
  "InvoiceGrossAmount": 57.25,
  "InvoiceNetAmount": 47.71,
  "VATonNetAmountInCustomerCurrency": 9.54,
  "CustomerRetailPriceUnitGross": 0,
  "CustomerRetailValueTotalGross": 57.52,
  "CustomerRetailValueTotalNet": 47.93,
  "TransactionTypeDescription": 9.59,
  "RebateonNetAmountInTransactionCurrency": -0.22,
  "EffectiveDiscountInTrxCurrency": -0.22,
  "UnitDiscountTransactionCurrency": -0.005,
  "TransactionGrossAmount": 57.25,
  "TransactionNetAmount": 47.71,
  "TransactionTax": 9.54,
  "VATonNetAmount": 9.54,
  "DelcoListPriceUnitNet": 0,
  "DelcoRetailPriceUnitGross": 1.32888,
  "UnitPriceInTransactionCurrency": 1.1074,
  "DelcoRetailPriceUnitNet": 1.1074,
  "DelcoRetailValueTotalGross": 57.52,
  "DelcoRetailValueTotalNet": 47.93,
  "TransactionCurrencySymbol": "$",
  "DiscountType": "Retail",
  "DisputeStatus": false,
  "IsShellSite": false,
  "FleetIdInput": "YG67OUM",
  "IncomingProductCode": 23,
  "PostingDate": "2021-08-02",
  "ProductCode": 30,
  "ProductName": "Unleaded - Medium octane",
  "ProductGroupId": 22,
  "IncomingCurrencyCode": "GBP",
  "IncomingSiteDescription": "Shell Broadway Ring",
  "Location": "Shell Broadway Ring",
  "SiteName": "Shell Broadway Ring",
  "SiteCode": 32,
  "IncomingSiteNumber": 15,
  "InvoiceCurrencyCode": "GBP",
  "InvoiceDate": "2021-08-02",
  "InvoiceNumber": 3201016193,
  "VATApplicable": "Y",
  "PayerName": "Colours Services Ltd",
  "PayerNumber": "GB12121212",
  "ParentCustomerNumber": "GB12121212",
  "PayerGroup": "H312066",
  "PayerGroupName": "12162566 - FUEL CARD SERVICE",
  "CheckDigit": 6,
  "NetInvoiceIndicator": "Y",
  "DelcoCode": 5,
  "NetworkCode": 3,
  "PurchasedInCountry": "United Kingdom",
  "SiteCountry": "United Kingdom",
  "VATCountry": "United Kingdom",
  "DelcoName": "Shell U.K. Oil Products Limited",
  "Network": "Shell",
  "OdometerInput": 0,
  "OriginalSalesItemId": "Null",
  "FleetIDDescription": "YG67OUM",
  "ParentCustomerId": 6494,
  "PINIndicator": "Y, N",
  "ProductGroupName": "Fees",
  "PurchasedInCountryCode": "GB",
  "Quantity": 43.28,
  "RebateRate": 0.0022,
  "ReceiptNumber": 6803,
  "RefundFlag": "Y",
  "SiteGroupId": 202,
  "SiteGroupName": "CZ 9100 ECONOMY NETWORK",
  "Latitude": 53.83606,
  "Longitude": -1.61854,
  "DelCoExchangeRate": 0.851858,
  "EuroRebateAmount": -0.258259,
  "NetEuroAmount": 56.01,
  "EuroVATAmount": 11.2,
  "ParentCustomerName": "FUEL CARD SERVICES LTD",
  "IsInvoiced": false,
  "TransactionCurrencyCode": "GBP",
  "CreditDebitCode": "D or C",
  "TransactionDate": "2021-08-01",
  "TransactionTime": "01/01/0001 12:16:58",
  "TransactionItemId": "H305908971030",
  "TrnIdentifier": "H305908971030",
  "Type": "SALE",
  "TransactionLine": 1,
  "TransactionType": "Purchase",
  "UTCOffset": "Europe/London",
  "VATCategory": "United Kingdom Standard VAT Rate",
  "VATRate": 0.2,
  "VehicleRegistration": "YG67OUM",
  "IsCancelled": "Y",
  "ColCoGrossAmount": 57.25,
  "ColCoNetAmount": 47.71,
  "ColCoVATAmount": 9.54,
  "OriginalCurrencySymbol": "$",
  "OriginalCurrencyCode": "$",
  "OriginalVATAmount": 0,
  "EmbossText": "PARKLANE PROPERTIES LTD",
  "OriginalExchangeRate": 0,
  "OriginalTransactionItemInvoiceDate": "2022-02-02",
  "FeeTypeId": 1,
  "LineItemDescription": true,
  "FeeRuleDescription": "Simple Fee",
  "Frequency": 1,
  "FeeRuleId": 1,
  "SystemEntryDate": "2021-08-28",
  "SystemEntryTime": "01/01/0001 20:21:08",
  "IsManual": "Y",
  "OriginalTransactionItemId": "Y",
  "OriginalTransactionItemInvoiceNumber": 6750802,
  "OriginalTransactionItemInvoiceId": 234,
  "PayerShortName": "FUEL CARD SERVICES LTD",
  "ReverseCharge": "Y",
  "OriginalGrossAmount": 57.25,
  "OriginalNetAmount": 57.25,
  "UnitOfMeasure": "L",
  "RoadType": "National Road",
  "CustomerCountryIsoCode": "DE",
  "EVOperator": "Shell Recharge",
  "EVSerialId": "GBALLEGO0002452",
  "EVChargePointSerial": "GBALLEGO0002452",
  "EVChargePointConnectorType": 5,
  "EVChargePointConnectorTypeDescription": "DC 50 kW",
  "EVChargeDuration": "PT3205S",
  "EVChargeStartDate": "2021-08-01",
  "EVChargeStartTime": "01/01/0001 20:08:01",
  "EVChargeEndDate": "2022-08-01",
  "EVChargeEndTime": "01/01/0001 20:08:01"
}
```

