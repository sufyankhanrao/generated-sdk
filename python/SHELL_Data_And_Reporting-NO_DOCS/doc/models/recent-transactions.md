
# Recent Transactions

## Structure

`RecentTransactions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `col_co_code` | `int` | Optional | ColCoCode |
| `payer_number` | `str` | Optional | PayerNumber |
| `account_number` | `str` | Optional | Account Number |
| `card_issue_number` | `str` | Optional | Card Issue Number |
| `collecting_company_currency_code` | `str` | Optional | Collecting Company Currency IsoCode |
| `cust_data_customer_entered` | `str` | Optional | Customer entered data for reference. |
| `cust_data_driver_id` | `str` | Optional | Customer Data DriverId |
| `cust_data_fleet_description` | `str` | Optional | Cust Data Fleet Description |
| `fleet_id_input` | `str` | Optional | Fleet Id Input |
| `amount` | `float` | Optional | Amount |
| `euroshell_site_number` | `str` | Optional | EuroshellSiteNumber |
| `incoming_product_code` | `str` | Optional | IncomingProductCode |
| `product_code` | `str` | Optional | ProductCode |
| `product_name` | `str` | Optional | ProductName |
| `site_code` | `int` | Optional | SiteCode |
| `hosting_collecting_company_name` | `str` | Optional | HostingCollectingCompanyName |
| `hosting_collecting_company_number` | `str` | Optional | HostingCollectingCompanyNumber |
| `iccdata_tran_type_code` | `str` | Optional | Transaction type code |
| `transaction_type` | `str` | Optional | Transaction type description. |
| `latitude` | `str` | Optional | Latitude of the Coordinate 3.11573 |
| `longitude` | `str` | Optional | Longitude of the Coordinate |
| `merchant_category` | `str` | Optional | Merchant category |
| `merchant_category_description` | `str` | Optional | Merchant category description |
| `purchased_in_country` | `str` | Optional | Purchased in country |
| `merchant_id` | `str` | Optional | Merchant Id |
| `site_name` | `str` | Optional | Site name |
| `network` | `str` | Optional | Network |
| `delco_code` | `str` | Optional | Three character DelcoCode |
| `odometer_input` | `str` | Optional | Odometer input |
| `odometer_reading_km` | `str` | Optional | Odometer reading in Kms |
| `odometer_reading_miles` | `str` | Optional | Odometer reading in miles |
| `card_pan` | `str` | Optional | Masked Card PAN |
| `pin_indicator` | `str` | Optional | PIN indicator |
| `poi_receipt_number` | `str` | Optional | POIReceiptNumber |
| `products_code_additional` | `str` | Optional | Additinal Products Code |
| `products_tax_code` | `str` | Optional | Products tax code |
| `fuel_volume` | `float` | Optional | Fuel volume |
| `sfgw_card_date_of_expiry` | `str` | Optional | SfgwCard expiry date |
| `site_currency_iso_code` | `str` | Optional | Three character Site currency ISO code |
| `card_id` | `str` | Optional | Card ID |
| `transaction_date` | `date` | Optional | ISO8601-compliant UTC datetime of the last update of the EVSE |
| `transaction_date_time` | `str` | Optional | ISO8601-compliant UTC datetime of the last update of the EVSE |
| `transaction_id` | `str` | Optional | TransactionId |
| `transaction_status` | `str` | Optional | Type of the connector in the EVSE unit. |
| `unit_of_measure` | `str` | Optional | Unit of measure |
| `vehicle_registration_number` | `str` | Optional | VehicleRegistrationNumber |
| `network_delco_name` | `str` | Optional | Network Delco name |
| `product_group_name` | `str` | Optional | ProductGroupName |
| `fuel_product` | `str` | Optional | FuelProduct |
| `account_customer_name` | `str` | Optional | AccountCustomerName |
| `payer_name` | `str` | Optional | PayerName |
| `transaction_time` | `str` | Optional | ISO8601-compliant UTC datetime of the last update of the EVSE |
| `transaction_currency` | `str` | Optional | TransactionCurrencySymbol |
| `unit_price` | `float` | Optional | UnitPrice |
| `authorised_flag` | `str` | Optional | AuthorisedFlag |
| `transaction_time_gmt` | `str` | Optional | TransactionTimeGMT update of the EVSE |
| `reason_code` | `str` | Optional | ReasonCode |
| `issuer_action_code` | `str` | Optional | IssuerActionCode |
| `issuer_action_code_description` | `str` | Optional | IssuerActionCodeDescription. |
| `declined_reason` | `str` | Optional | DeclinedReason. |
| `card_status_reason_description` | `str` | Optional | CardStatusReasonDescription. |
| `transaction_country` | `str` | Optional | TransactionCountry |
| `issuing_collecting_company_name` | `str` | Optional | IssuingCollectingCompanyName. |
| `card_issuer_name` | `str` | Optional | CardIssuerName. |
| `driver_name` | `str` | Optional | DriverName. |
| `bearer_description` | `str` | Optional | BearerDescription. |
| `card_category_description` | `str` | Optional | CardCategoryDescription. |
| `card_type_description` | `str` | Optional | CardTypeDescription. |
| `card_token_type_description` | `str` | Optional | CardTokenTypeDescription. |
| `emboss_type` | `str` | Optional | EmbossType. |
| `ev_printed_number` | `str` | Optional | The EVPrintedNumber which can be found on the Shell EV Card |
| `is_rfid` | `bool` | Optional | Whether the card type is enabled for RFID (Radio Frequency Identification) |

## Example (as JSON)

```json
{
  "ColCoCode": 84,
  "PayerNumber": "MY00200653",
  "AccountNumber": "MY00200653",
  "CardIssueNumber": "1",
  "CollectingCompanyCurrencyCode": "MYR",
  "CustDataCustomerEntered": "PartnerId",
  "CustDataDriverId": "D123",
  "CustDataFleetDescription": "Fleet-Truck",
  "FleetIdInput": "AS2344",
  "Amount": 62.47,
  "EuroshellSiteNumber": "1231",
  "IncomingProductCode": "10",
  "ProductCode": "23",
  "ProductName": "Unleaded - Low octane",
  "SiteCode": 3350,
  "HostingCollectingCompanyName": "Shell Malaysia Trading Sdn Bhd",
  "HostingCollectingCompanyNumber": "84",
  "IccdataTranTypeCode": "1",
  "TransactionType": "Transaction Type description",
  "Latitude": "52.143814",
  "Longitude": "101.72869",
  "MerchantCategory": "5542",
  "MerchantCategoryDescription": "Description",
  "PurchasedInCountry": "MY",
  "MerchantId": "MY1737000000000",
  "SiteName": "ShellPT3895 BATU 4    KUALA LUMPUR MY",
  "Network": "458",
  "DelcoCode": "084",
  "OdometerInput": "201620",
  "OdometerReadingKm": "201620",
  "OdometerReadingMiles": "201620",
  "CardPAN": "700214*******780061",
  "PINIndicator": "Y",
  "POIReceiptNumber": "417662",
  "ProductsCodeAdditional": "Additional Code",
  "ProductsTaxCode": "0",
  "FuelVolume": 34.15,
  "SfgwCardDateOfExpiry": "2024-12",
  "SiteCurrencyISOCode": "MYR",
  "CardId": "330743",
  "TransactionDate": "2021-11-11",
  "TransactionDateTime": "2021-11-11 16:32:09.000",
  "TransactionId": "864220307",
  "TransactionStatus": "Approved",
  "UnitOfMeasure": "L",
  "VehicleRegistrationNumber": "WD33637",
  "NetworkDelcoName": "Shell Malaysia Trading Sdn Bhd",
  "ProductGroupName": "Motor gasoline",
  "FuelProduct": "All Fuels",
  "AccountCustomerName": "WCT BERHAD",
  "PayerName": "WCT BERHAD",
  "TransactionTime": "2021-11-11",
  "TransactionCurrency": "RM",
  "UnitPrice": 0.02050073206442167,
  "AuthorisedFlag": "Y",
  "TransactionTimeGMT": "08:41:02",
  "ReasonCode": "10",
  "IssuerActionCode": "2",
  "IssuerActionCodeDescription": "Approved, partial",
  "DeclinedReason": "partial",
  "CardStatusReasonDescription": "Approved, partial",
  "TransactionCountry": "458",
  "IssuingCollectingCompanyName": "Partner Name",
  "CardIssuerName": "John",
  "DriverName": "PAK PAK",
  "BearerDescription": "Description",
  "CardCategoryDescription": "Driver Card",
  "CardTypeDescription": "SHELL FLEET- HONG KONG 7002821",
  "CardTokenTypeDescription": "HK FLE NAT SIN R1 - CHIP",
  "EmbossType": "Driver",
  "EVPrintedNumber": "NL-TNM-C00122045-K",
  "IsRFID": false
}
```

