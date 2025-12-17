
# Priced Request Data

This endpoint allows querying the transaction data (i.e. Priced, Billed and Unbilled sales items) from SFSBI. It provides a flexible search criteria and supports paging

## Structure

`PricedRequestData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `col_co_code` | `str` | Required | Collecting Company Code (Shell Code) of the selected payer. |
| `invoice_status` | [`PricedTransactionReqV2InvoiceStatusEnum`](../../doc/models/priced-transaction-req-v2-invoice-status-enum.md) | Required | Invoice status of the transactions. Mandatory Possible options:I - Invoiced, U – Un-Invoiced, A – All<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `1` |
| `payer_number` | `str` | Required | Payer Number of the selected payer.<br><br>**Constraints**: *Minimum Length*: `1` |
| `account_id` | `int` | Optional | Account Id (GFN customer id) |
| `account_number` | `str` | Optional | Account Number of the selected account. |
| `driver_name` | `str` | Optional | Driver Name (of Card record)<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `40` |
| `card_group_id` | `int` | Optional | Card Group Id in GFN |
| `card_pan` | `str` | Optional | Full Card PAN |
| `product_code` | `str` | Optional | Product Code – Global as per GFN configuration<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `8` |
| `product_name` | `str` | Optional | Product Name – Global as per GFN configuration<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `128` |
| `site_code` | `str` | Optional | Site Code in GFN<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `87` |
| `incoming_site_number` | `str` | Optional | Site Code as configured in GFN<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `10` |
| `invoice_date` | `str` | Optional | Returns the billed transaction for the given invoice date |
| `invoice_number` | `str` | Optional | Returns the billed transaction for the given invoice number<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10` |
| `purchased_in_country_code` | `str` | Optional | Purchased InCountryCode<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `purchased_in_country` | `str` | Optional | Network Delco PurchasedCountryName |
| `site_group_id` | `int` | Optional | Site Group Id in GFN |
| `vehicle_registration_number` | `str` | Optional | Vehicle Registration (of Card record)<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `128` |
| `fee_type_id` | `int` | Optional | Card Id (i.e. Unique Card Id in GFN) |
| `line_item_description` | `str` | Optional | Item identifier in the transaction.<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `128` |
| `cards` | `List[int]` | Optional | This entity accepts the list of CardId to filter in the response.<br>Note: The number of cardId allowed to be passed in the request is configurable to a maximum of 500 cards.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `500` |
| `sort_order` | [`PricedTransactionReqV2SortOrderEnum`](../../doc/models/priced-transaction-req-v2-sort-order-enum.md) | Optional | Allowed Sorting Options<br><br>1. TransactionDateAscending<br>2. TransactionDateDescending<br>3. GrossAmountDescending<br>4. GrossAmountAscending<br>5. NetAmountAscending<br>6. NetAmountDescensding<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `1` |
| `from_date` | `str` | Optional | From transaction delivery date<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `19` |
| `to_date` | `str` | Optional | To transaction delivery date<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `19` |
| `period` | [`PricedTransactionReqV2PeriodEnum`](../../doc/models/priced-transaction-req-v2-period-enum.md) | Optional | Pass below one of the value as per the required transaction period<br><br>1. Last 7 Days<br>2. Last 30 Days<br>3. Last 90 Days |
| `posting_date_from` | `str` | Optional | Transaction posting start date and time<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `19` |
| `posting_date_to` | `str` | Optional | Transaction posting end date and time<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `19` |
| `transaction_item_id` | `str` | Optional | Unique id of the transaction that may include one or more salesitems |
| `fuel_only` | `bool` | Optional | Is FuelOnly indicator<br><br>**Default**: `False` |
| `include_fees` | `bool` | Optional | When passed as ‘true’ then all sales items along with fees will be included in the response and the follwoing filteres will be ignored<br><br>* InvoiceNumber<br>* InvoiceDate<br>* PostingDateFrom<br>* PostingDateTo |
| `is_multipayer` | `bool` | Optional | If true then returns all the data linked tothe payer group of the provided PayerNumberin the request |
| `valid_invoice_date_only` | `bool` | Optional | When passed as ‘True’ the transactions records with report date not equal to 9999-12-30 will be returned. When passed as ‘False’ the above condition will not be checked.<br><br>**Default**: `False` |
| `invoice_from_date` | `str` | Optional | Invoice From Date, this is a search criterion to filter invoiced transactions with invoice date from this date.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `19` |
| `invoice_to_date` | `str` | Optional | Invoice To Date, this is a search criterion to filter invoiced transactions with invoice date until this date.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `19` |
| `hosting_collecting_company_number` | `str` | Optional | Hosting Collecting Company Number of the selected payer. |
| `search` | `str` | Optional | Search based on DriverName or VRN |
| `transaction_id` | `str` | Optional | Unique id of the transaction that may include one or more salesitems |

## Example (as JSON)

```json
{
  "ColCoCode": "032",
  "InvoiceStatus": "A",
  "PayerNumber": "DE26685263",
  "AccountId": 29484,
  "AccountNumber": "DE26667080",
  "DriverName": "HH NX 508",
  "CardGroupId": 40000,
  "CardPAN": "7002051006629890645",
  "ProductCode": "10",
  "ProductName": "Diesel AGO",
  "SiteCode": "05000100",
  "IncomingSiteNumber": "100021",
  "InvoiceDate": "2022-01-01 00:00:00",
  "InvoiceNumber": "3201016193",
  "PurchasedInCountryCode": "GB",
  "PurchasedInCountry": "United Kingdom",
  "SiteGroupId": 202,
  "FeeTypeId": 275549,
  "LineItemDescription": "ABC3",
  "SortOrder": "5",
  "FromDate": "2022-01-01 00:00:00",
  "ToDate": "2022-01-01 00:00:00",
  "Period": 3,
  "PostingDateFrom": "2022-01-01 00:00:00",
  "PostingDateTo": "2022-01-01 00:00:00",
  "TransactionItemId": "io9KVXk1UkW57XWKyeaHHg",
  "FuelOnly": false,
  "ValidInvoiceDateOnly": false,
  "InvoiceFromDate": "2022-01-01 00:00:00",
  "InvoiceToDate": "2022-01-01 00:00:00",
  "HostingCollectingCompanyNumber": "032",
  "Search": "2K89909",
  "TransactionId": "io9KVXk1UkW57XWKyeaHHg"
}
```

