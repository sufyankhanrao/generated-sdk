
# Payer Details

## Structure

`PayerDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `col_co_id` | `int` | Optional | Collecting company id of the customer. |
| `col_co_code` | `int` | Optional | Collecting company code of the customer. |
| `country_code` | `str` | Optional | ISO code of the customer country. |
| `country` | `str` | Optional | Country of the customer |
| `payer_id` | `int` | Optional | Payer id of the customer |
| `payer_number` | `str` | Optional | Payer Number of the customer |
| `payer_full_name` | `str` | Optional | Full Name of the Payer |
| `payer_short_name` | `str` | Optional | Short name of the payer |
| `payer_group_id` | `int` | Optional | Payer Group Id |
| `amount_due` | `float` | Optional | Invoiced amount and due for payment from the last SOA. |
| `amount_overdue` | `float` | Optional | Invoiced amount and overdue for payment from the last SOA. |
| `amount_not_overdue` | `float` | Optional | Invoiced amount and not overdue for payment from the last SOA. |
| `outstanding_balance` | `float` | Optional | Current outstanding balance amount from the last SOA. |
| `unallocated_payment` | `float` | Optional | Unallocated payment.<br>When negative, indicates overdue amount from the last SOA. |
| `soa_currency_code` | `str` | Optional | Currency ISO code |
| `soa_currency_symbol` | `str` | Optional | Currency symbol |
| `soa_credit_limit_currency_code` | `str` | Optional | Currency ISO code |
| `soa_credit_limit_currency_symbol` | `str` | Optional | Currency symbol |
| `last_payment_currency_code` | `str` | Optional | Currency ISO code |
| `last_payment_currency_symbol` | `str` | Optional | currency symbol |
| `last_payment_amount` | `float` | Optional | Latest payment amount for the requested payer. |
| `last_payment_date` | `str` | Optional | Latest payment date for the requested payer. |
| `soa_last_payment_amount` | `float` | Optional | Last payment amount in statement of account for the requested payer. |
| `soa_last_payment_date` | `str` | Optional | Last payment date in statement of account for the requested payer. |
| `currency_code` | `str` | Optional | Currency ISO code |
| `currency_symbol` | `str` | Optional | Currency Symbol |
| `col_co_country_code` | `str` | Optional | The 2-character ISO Code for the customer and card owning country. |
| `local_currency_code` | `str` | Optional | Currency ISO code of the local country. |
| `local_currency_symbol` | `str` | Optional | Currency Symbol of the local country |
| `local_currency_exchange_rate` | `float` | Optional | Exchange rate from OU base currency to local currency. |
| `local_currency_exchange_rate_so_a` | `float` | Optional | Exchange rate from SoA credit limit currency to local currency |
| `billing_frequency_type_id` | `int` | Optional | Billing/Invoice frequency Identifier. Indicates the frequency in which the transactions will be considered for invoicing in a bulling run<br>E.g.: 1, 2, 3, etc. |
| `billing_frequency_type` | `str` | Optional | Billing/Invoice frequency. The frequency in which the transactions will be considered for invoicing in a bulling run<br>E.g.:<br>1	Daily (all days)<br>2	Daily (only working days)<br>3	Weekly - Monday<br>4	Weekly – Tuesday<br>Etc. |
| `billing_run_frequency_type_id` | `int` | Optional | Frequency at which the billing process is triggered.<br>E.g.: 1, 2, 3, etc. |
| `billing_run_frequnecy` | `str` | Optional | Frequency at which the billing process is triggered.E.g.:<br>1	Daily (all days)<br>2	Daily (only working days)<br>3	Weekly - Monday<br>4	Weekly – Tuesday<br>Etc. |
| `day_1_run` | `int` | Optional | The first day in a month when the billing should run in case of multiple billing runs configured with in a single month. |
| `day_2_run` | `int` | Optional | The second day in a month when the billing should run in case of multiple billing runs configured with in a single month. |
| `day_3_run` | `int` | Optional | The third day in a month when the billing should run in case of multiple billing runs configured with in a single month. |
| `day_4_run` | `int` | Optional | The fourth day in a month when the billing should run in case of multiple billing runs configured with in a single month. |
| `invoice_distribution_methods` | [`List[InvoiceDistributionMethod]`](../../doc/models/invoice-distribution-method.md) | Optional | - |
| `output_type` | `str` | Optional | Invoice output type (Id-Description)<br>E.g.:<br>1-PDF<br>6-Print |
| `invoice_account_id` | `int` | Optional | The Account ID of the account on which the invoice is generated. |
| `invoice_account_number` | `str` | Optional | The Account Number of the account on which the invoice is generated. |
| `invoice_account_short_name` | `str` | Optional | The Account Short Name of the account on which the invoice is generated. |
| `best_of_indicator` | `bool` | Optional | Best of Indicator of the Pricing customer/account configured.<br><br>**Default**: `False` |
| `is_international` | `bool` | Optional | Whether the account is international.<br><br>**Default**: `False` |
| `total_accounts` | `int` | Optional | Total number of accounts under the payer. |
| `total_active_accounts` | `int` | Optional | Total number of active accounts under the payer. |
| `total_cards` | `int` | Optional | Total number of cards under the payer. |
| `total_active_cards` | `int` | Optional | Total number of active cards under the payer. |
| `total_blocked_cards` | `int` | Optional | Total number of cards under the payer that are permanently blocked |
| `total_cancelled_cards` | `int` | Optional | Total number of cards under the payer that are cancelled |
| `total_expired_cards` | `int` | Optional | Total number of expired cards under the payer. |
| `total_renewal_pending_cards` | `int` | Optional | Total number of Renewal Pending cards under the payer. |
| `total_replaced_cards` | `int` | Optional | Total number of cards under the payer with status as “Replaced |
| `total_temporary_block_cards_by_customer` | `int` | Optional | Total number of cards under the payer that are temporarily blocked by customer. |
| `total_temporary_block_cards_by_shell` | `int` | Optional | Total number of cards under the payer that are temporarily blocked by Shell. |
| `total_new_cards` | `int` | Optional | Total number of cards in “New” status |
| `total_fraud_cards` | `int` | Optional | Total number of cards in Fraud status |
| `total_blocked_accounts` | `int` | Optional | Total number of accounts in Blocked status |
| `total_cancelled_accounts` | `int` | Optional | Total number of accounts in Cancel status |
| `payer_trading_name` | `str` | Optional | Trading name for the Payer |
| `status` | `str` | Optional | Payer current status id and description<br>e.g. (Id – Description):<br>1-Active<br>2-Requested from UTA<br>3-Awaiting embossing<br>4-Manufactured<br>5-Awaiting despatch |
| `billing_language` | `str` | Optional | Payer Billing Language id and description |
| `legal_entity` | `str` | Optional | Legal entity id and description of the Payer |
| `date_established` | `str` | Optional | Payer/Company Established Date. |
| `customer_classification` | `str` | Optional | Payer/Company Classification id and description |
| `industry_class` | `str` | Optional | Payer/Company Industry class id and description |
| `marketing_segmentation` | `str` | Optional | Marketing Segmentation id and description |
| `line_of_business` | `str` | Optional | Payer/Company Line of Business Id and Description |
| `print_credit_limit` | `bool` | Optional | Is Credit Limit printed on the statement of account: True/False<br>If True Credit Limit is printed on invoice/SOA<br><br>**Default**: `False` |
| `card_group_type` | `str` | Optional | Card Group Type configured for Payer<br>e.g. (Id – Description):<br>1-Horizontal only<br>2-Vertical only<br>3-Both |
| `renew_cards` | `bool` | Optional | If set to True cards will be automatically renewed on expiry<br><br>**Default**: `False` |
| `allow_select_pin` | `bool` | Optional | If set to True then Self Select PIN is allowed for Payer<br><br>**Default**: `False` |
| `use_fleet_pin` | `bool` | Optional | If set to True then Fleet PIN is applied for the cards directly under payer |
| `vat_reg_number` | `str` | Optional | Payer/Company VAT registration number. |
| `vat_reg_number_2` | `str` | Optional | Payer/Company VAT registration number 2. |
| `registration_number` | `str` | Optional | Payer/Company Registration number |
| `registration_number_2` | `str` | Optional | Payer/Company Registration number2 |
| `sales_ledger_balance` | `float` | Optional | Sales Ledger Balance (Billed) |
| `exposure` | `float` | Optional | Exposure after guarantee |
| `outstanding_debt` | `float` | Optional | Total outstanding debt (including billed and unbilled sales and fee items) |
| `available_credit` | `float` | Optional | The available credit for the payer.<br>This is the credit limit minus the outstanding debt. |
| `band` | `str` | Optional | Band Id and Description of the Payer in Card Platform.<br>e.g. (Id – Description):<br>1-Platinum<br>2-Gold<br>3-Silver<br>4-Bronze |
| `global_customer_reference_id` | `str` | Optional | Global Customer reference id configured in card platform for Payer (Same as Payer Group) |
| `credit_limit` | `float` | Optional | Payment Credit limit of Payer. |
| `credit_limit_in_customer_currency` | `float` | Optional | Credit limit in Customer currency.<br>Note: For currency details refer the parameters CurrencyCode & CurrencySymbol in the PayerDetail response. |
| `billing_currency_code` | `str` | Optional | Customer Billing currency ISO code. |
| `billing_currency_symbol` | `str` | Optional | Customer Billing currency Symbol. |
| `payment_method` | `str` | Optional | Payment method Id and Description as configured for Payer in Card Platform |
| `payment_terms` | `str` | Optional | Payment terms Id and Description as configured for Payer in Card Platform |
| `temporary_credit_limit_increase` | `float` | Optional | Temporary Credit limit increase value |
| `temporary_credit_limit_increase_in_customer_currency` | `float` | Optional | Temporary Credit limit increase value |
| `temporary_credit_limit_expiry_date` | `str` | Optional | Temporary Credit limit expiry date |
| `payer_bank_account` | [`List[BankAccount]`](../../doc/models/bank-account.md) | Optional | - |
| `card_delivery_address` | [`Address`](../../doc/models/address.md) | Optional | - |
| `correspondance_address` | [`Address`](../../doc/models/address.md) | Optional | - |
| `billing_address` | [`Address`](../../doc/models/address.md) | Optional | - |
| `has_active_vol_based_pricing` | `bool` | Optional | True, if the payer is setup for volume-based pricing and is active on the current date, else false.<br><br>This field is returned only when IncludeBonusParameters is set to True in the request. Else set to null. |
| `has_active_vol_based_bonus` | `bool` | Optional | True, if the payer is setup for volume-based bonus and is active on the current date, else false.<br>This field is returned only when IncludeBonusParameters is set to True in the request. Else set to null. |
| `has_active_vol_based_association_bonus` | `bool` | Optional | True, if the payer is setup for volume-based association bonus and is active on the current date, else false.<br>This field is returned only when IncludeBonusParameters is set to True in the request. Else set to null. |
| `finance_currency` | [`FinanceCurrency2`](../../doc/models/finance-currency-2.md) | Optional | - |
| `tolls_customer_id` | `str` | Optional | Customer id in e-TM system<br>This field will have value only when ReturnTollsCustomerId is set to true in the request else set to null or empty. |
| `tolls_colco_country_type_id` | `str` | Optional | String	Colco country type id in e-TM system<br>This field will have value only when ReturnTollsCustomerId is set to true in the request else set to null or empty. |
| `contracts` | [`List[CustomerContract]`](../../doc/models/customer-contract.md) | Optional | - |

## Example (as JSON)

```json
{
  "ColCoId": 14,
  "ColCoCode": 14,
  "CountryCode": "DE",
  "Country": "Germany",
  "PayerId": 12345,
  "PayerNumber": "DE000000123",
  "PayerFullName": "ABC Company",
  "PayerShortName": "ABC",
  "PayerGroupId": 456,
  "AmountDue": 1500,
  "AmountOverdue": 450,
  "AmountNotOverdue": 4546.76,
  "OutstandingBalance": 456,
  "UnallocatedPayment": 123,
  "SOACurrencyCode": "EUR",
  "SOACurrencySymbol": "€",
  "SOACreditLimitCurrencyCode": "EUR",
  "SOACreditLimitCurrencySymbol": "€",
  "LastPaymentCurrencyCode": "EUR",
  "LastPaymentCurrencySymbol": "€",
  "LastPaymentAmount": 5465,
  "LastPaymentDate": "20230405",
  "SOALastPaymentAmount": 45443,
  "SOALastPaymentDate": "20230805",
  "CurrencyCode": "EUR",
  "CurrencySymbol": "€",
  "ColCoCountryCode": "DE",
  "LocalCurrencyCode": "EUR",
  "LocalCurrencySymbol": "€",
  "LocalCurrencyExchangeRate": 1.45,
  "LocalCurrencyExchangeRate_SoA": 1.2,
  "BillingFrequencyTypeId": 1,
  "BillingFrequencyType": "weekly",
  "BillingRunFrequencyTypeId": 1,
  "BillingRunFrequnecy": "weekly",
  "Day1Run": 0,
  "Day2Run": 0,
  "Day3Run": 0,
  "Day4Run": 0,
  "OutputType": "PDF",
  "InvoiceAccountID": 12345,
  "InvoiceAccountNumber": "1234567",
  "InvoiceAccountShortName": "Test Account",
  "BestOfIndicator": false,
  "IsInternational": false,
  "TotalAccounts": 5,
  "TotalActiveAccounts": 4,
  "TotalCards": 567,
  "TotalActiveCards": 560,
  "TotalBlockedCards": 6,
  "TotalCancelledCards": 0,
  "TotalExpiredCards": 1,
  "TotalRenewalPendingCards": 0,
  "TotalReplacedCards": 0,
  "TotalTemporaryBlockCardsByCustomer": 0,
  "TotalTemporaryBlockCardsByShell": 0,
  "TotalNewCards": 0,
  "TotalBlockedAccounts": 0,
  "TotalCancelledAccounts": 0,
  "PayerTradingName": "ABC Company",
  "Status": "Active",
  "BillingLanguage": "1-German",
  "LegalEntity": "20-Unlimited Corporation",
  "DateEstablished": "19880504",
  "CustomerClassification": "3-10049 Domestic",
  "IndustryClass": "4-Growing of sugar cane",
  "MarketingSegmentation": "1-National CRT",
  "LineOfBusiness": "1-CRT",
  "PrintCreditLimit": false,
  "CardGroupType": "1-Horizontal only",
  "RenewCards": false,
  "AllowSelectPIN": false,
  "VATRegNumber": "4534545",
  "VATRegNumber2": "45345545",
  "RegistrationNumber": "453543",
  "RegistrationNumber2": "35435",
  "SalesLedgerBalance": 0,
  "Exposure": 0,
  "OutstandingDebt": 0,
  "AvailableCredit": 0,
  "Band": "Gold",
  "GlobalCustomerReferenceId": "1234",
  "CreditLimit": 3434,
  "BillingCurrencyCode": "EUR",
  "BillingCurrencySymbol": "€",
  "PaymentMethod": "Incoming - Bank Transfer",
  "PaymentTerms": "0 days after invoice",
  "TemporaryCreditLimitIncrease": 0,
  "TemporaryCreditLimitIncreaseInCustomerCurrency": 0,
  "TemporaryCreditLimitExpiryDate": "20230504",
  "TollsCustomerId": "2332",
  "TollsColcoCountryTypeId": "33"
}
```

