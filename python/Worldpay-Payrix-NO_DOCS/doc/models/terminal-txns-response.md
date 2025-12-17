
# Terminal Txns Response

## Structure

`TerminalTxnsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `ip_created` | `str` | Optional | The incoming ip address from which this Transaction was created. |
| `ip_modified` | `str` | Optional | The incoming ip address from which this Transaction was last modified. |
| `merchant` | `str` | Optional | The identifier of the Merchant associated with this Transaction. |
| `mid` | `str` | Optional | The Merchant ID, as set by the processor, is stored as a text string and must be between 0 and 50 characters long. |
| `txn` | `str` | Optional | The related txn this terminalTxn belongs to. |
| `token` | `str` | Optional | The ID of the token record to associate with this terminal transaction request. |
| `payment_number` | `int` | Optional | The last four numbers of the credit card associated with this Transaction. |
| `payment_method` | [`TerminalTxnPaymentMethodEnum`](../../doc/models/terminal-txn-payment-method-enum.md) | Optional | The payment method for this Transaction. |
| `forterminal_txn` | `str` | Optional | TIf this Terminal Transaction is related to another Terminal Transaction, then this field is set to the identifier of the other Terminal Transaction. For example, if this Terminal Transaction is a Refund, this field could be set to the identifier of the original Sale Terminal Transaction. |
| `mtype` | [`TerminalTxnTypeEnum`](../../doc/models/terminal-txn-type-enum.md) | Optional | The type of Transaction.<br><br><details><br><summary>Valid Values</summary><br>- `1` - **Credit Card Only: Sale Transaction.** This is the most common type of Transaction, it processes a sale and charges the customer.<br>- `2` - **Credit Card Only: Auth Transaction.** Authorizes and holds the requested total on the credit card.<br>- `4` - **Credit Card Only: Reverse Authorization.** Reverses a prior Auth or Sale Transaction and releases the credit hold.<br>- `5` - **Credit Card Only: Refund Transaction.** Refunds a prior Capture or Sale Transaction (total may be specified for a partial refund).<br>- `13` - **Batch out terminal.**<br></details><br> |
| `expiration` | `str` | Optional | The expiration date of this Transaction. This field is stored as a text string in 'MMYY' format, where 'MM' is the number of a month and 'YY' is the last two digits of a year. For example, '0623' for June 2023. The value must reflect a future date. |
| `currency` | [`CurrencyEnum`](../../doc/models/currency-enum.md) | Optional | The currency for this transaction. See <a href="https://www.iban.com/currency-codes" target="_blank">Currency codes</a>  for all valid values. |
| `funding_currency` | [`FundingCurrencyEnum`](../../doc/models/funding-currency-enum.md) | Optional | The currency for which transaction was funded on. See <a href="https://www.iban.com/currency-codes" target="_blank">Currency codes</a>  for all valid values. |
| `fee` | `float` | Optional | Optional calculated fee amount indicator, which should be used in conjunction with txnFee setting on Fees resource, This field is specified in cents(up to three decimal points). |
| `platform` | [`Platform1Enum`](../../doc/models/platform-1-enum.md) | Optional | The platform used to process this resource.<br><br><details><br><summary>Valid Values</summary><br>- `APPLE` - **The Apple Payment Processor.**<br>- `ELAVON` - **The Elavon processor.**<br>- `FIRSTDATA` - **The FirstData processor.**<br>- `GOOGLE` - **The Google Payment Processor.**<br>- `VANTIV` - **The WorldPay (aka Vantiv or Litle) eComm (aka VAP) processor.**<br>- `VCORE` - **The WorldPay (aka Vantiv) Core processor.**<br>- `TDBANKCA` - **External funding with TD Bank Canada via the Operating Account.**<br>- `WELLSACH` - **The Wells Fargo ACH processor.**<br>- `WELLSFARGO` - **The Wells Fargo Merchant Services processor.**<br>- `WFSINGLE` - **The WFSINGLE processor.**<br>- `WORLDPAY` - **The WORLDPAY processor.**<br></details><br> |
| `auth_date` | `int` | Optional | The date on which the Transaction was authorized, specified as an eight digit string in YYYYMMDD format, for example, '20160120' for January 20, 2016, and the value of this field must represent a date in the past. |
| `auth_code` | `str` | Optional | The authorization code for this Transaction. This field is stored as a text string and must be between 0 and 20 characters long. |
| `order` | `str` | Optional | The identifier of the Order associated with this Transaction, This field is stored as a text string and must be between 0 and 1000 characters long. |
| `description` | `str` | Optional | A description of this Transaction. This field is stored as a text string and must be between 0 and 1000 characters long. |
| `trace_number` | `int` | Optional | Sequencial number that uniquely identifies the terminalTxn. |
| `discount` | `int` | Optional | The discount applied to the transaction. |
| `shipping` | `int` | Optional | The shipping fee pertaining to this transaction. |
| `duty` | `int` | Optional | The duty fee applicable to this transaction. |
| `terminal` | `str` | Optional | The identifier of the terminal that processed this Transaction, which is taken from the terminal system and varies in format according to the type of terminal, is stored as a text string and must be between 0 and 50 characters long. |
| `tid` | `str` | Optional | The Terminal ID as set by the platform activating the terminal, stored as a text string and must be between 0 and 50 characters long. |
| `terminal_capability` | [`TerminalCapabilityEnum`](../../doc/models/terminal-capability-enum.md) | Optional | Capabilities of the terminal device.<br><br><details><br><summary>Valid Values</summary><br>- `1` - **Key entry only terminal.**<br>- `2` - **Can read magnetic stripe.**<br>- `3` - **Integrated circuit reader.**<br>- `4` - **Can detect contactless payment.**<br></details><br> |
| `entry_mode` | [`EntryModeEnum`](../../doc/models/entry-mode-enum.md) | Optional | How payment information has been entered, including manually keyed entries, card swipes with track 1 or 2 data received, card dips with EMV chip data received, contactless card reads with track or EMV data received, and ApplePay read with cryptogram data received.<br><br><details><br><summary>Valid Values</summary><br>- `1` - **Manually keyed entry.**<br>- `2` - **Card swiped. Track 1 received.**<br>- `3` - **Card swiped. Track 2 received.**<br>- `4` - **Card swiped. Track 1 & 2 received.**<br>- `5` - **Card dipped. EMV chip received.**<br>- `6` - **Contactless card read. Track or EMV data received.**<br>- `7` - **Track Data from Card Swipe after EMV chip failure.**<br>- `8` - **Track Data from Manually keyed entry after EMV chip failure.**<br>- `9` - **ApplePay**<br>- `10` - **Google Pay.**<br>- `11` - **Merchant created transaction.**<br>- `12` - **Invoice payment.**<br>- `13` - **Merchant created transaction in payrix portal.**<br>- `14` - **Invoice payment from payrix portal.**<br></details><br> |
| `origin` | [`TerminalTxnOriginEnum`](../../doc/models/terminal-txn-origin-enum.md) | Optional | The origin of this Transaction.<br><br><details><br><summary>Valid Values</summary><br>- `1` - **Credit Card Terminal.**<br>- `2` - **eCommerce System.**<br>- `3` - **Mail or Telephone Order Transaction.**<br>- `4` - **Apple Pay (deprecated).**<br>- `5` - **Successful 3D Secure Transaction.**<br>- `6` - **Attempted 3D Secure Transaction.**<br>- `7` - **Recurring Card Transaction (deprecated).**<br>- `8` - **Payframe.**<br>- `9` - **Writing.**<br></details><br> |
| `tax` | `int` | Optional | The amount of the total sum of this Transaction that is made up of tax, This field is specified as an integer in cents. |
| `total` | `int` | Optional | The total amount of this Transaction, This field is specified as an integer in cents. |
| `tip` | `int` | Optional | This field indicates the tip amount associated with a transaction. This value is for reporting purposes only, because transaction amount includes this amount in the total. |
| `cashback` | `int` | Optional | The amount of the total sum of this Transaction that is given as cash back, specified as an integer in cents. |
| `authorization` | `str` | Optional | The authorization code for this Transaction, as returned by the network. |
| `approved` | `int` | Optional | The total amount that was approved for this Transaction by the processor, which is specified as an integer in cents. |
| `cvv` | `int` | Optional | Whether correct cvv was sent during this Transaction. |
| `cvv_status` | [`CvvStatusEnum`](../../doc/models/cvv-status-enum.md) | Optional | The status of the CVV on the card.<br><br><details><br><summary>Valid Values</summary><br>- `notPresent` - **CVV is not present.**<br>- `illegible` - **CVV is illegible.**<br>- `notProvided` - **CVV was not provided.**<br></details><br> |
| `swiped` | [`SwipedEnum`](../../doc/models/swiped-enum.md) | Optional | Whether the card was swiped during this Transaction.<br>This field is set to '1' automatically if 'track' data was received.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Swiped.**<br>- `1` - **Swiped.**<br></details><br> |
| `emv` | [`EmvEnum`](../../doc/models/emv-enum.md) | Optional | Whether the card was dipped (using the EMV chip) during this Transaction.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not dipped.**<br>- `1` - **Dipped.**<br></details><br> |
| `signature` | [`SignatureEnum`](../../doc/models/signature-enum.md) | Optional | Whether a signature should be captured during this Transaction.<br><br>* You can set this field if you want the terminal to take a signature for the Transaction.<br>* The API also sets this field automatically if you associate a signature to the Transaction by creating a 'terminalTxnDatas' resource.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not captured.**<br>- `1` - **Captured.**<br></details><br> |
| `pin` | [`PinEnum`](../../doc/models/pin-enum.md) | Optional | Whether this Transaction was verified with a PIN.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **No PIN verification.**<br>- `1` - **PIN verification.**<br><br></details><br> |
| `unattended` | [`UnattendedEnum`](../../doc/models/unattended-enum.md) | Optional | Whether the card was swiped at an unattended terminal during this Transaction.<br>This field is set to '0' by default.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Attended terminal.**<br>- `1` - **Unattended terminal.**<br></details><br> |
| `pos` | [`PosEnum`](../../doc/models/pos-enum.md) | Optional | Whether the terminalTxn is coming from a POS system that needs terminal activation.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **POS Terminal Activation.** (Internal)<br>- `1` - **External Terminal Activation.**<br></details><br> |
| `bin_type` | [`BinTypeEnum`](../../doc/models/bin-type-enum.md) | Optional | The type of bank issuer number (BIN) that allows for resulting transactions.<br><br><details><br><summary>Valid Values</summary><br>- `CREDIT` - **Credit BIN Type.**<br>- `DEBIT` - **Debit BIN Type.**<br>- `PREPAID` - **Prepaid BIN Type.**<br></details><br> |
| `receipt` | [`ReceiptEnum`](../../doc/models/receipt-enum.md) | Optional | Whether the terminal should print a receipt or not.<br><br><details><br><summary>Valid Values</summary><br>- `noReceipt` - **No Receipt.**<br>- `merchant` - **Merchant copy only.**<br>- `customer` - **Customer copy only.**<br>- `both` - **Merchant and Customer copy.**<br></details><br> |
| `client_ip` | `str` | Optional | The client IP address from which the transaction was created, valid values are any IPv4 or IPv6 address. |
| `first` | `str` | Optional | The first name associated with this Transaction. For eCheck transactions, either first or last is required. |
| `middle` | `str` | Optional | The middle name associated with this Transaction. |
| `last` | `str` | Optional | The last name associated with this Transaction. For eCheck transactions, either first or last is required. |
| `company` | `str` | Optional | The name of the company associated with this Transaction, setting this field is especially important when processing an eCheck from a company. |
| `email` | `str` | Optional | The email associated with this Transaction. |
| `address_1` | `str` | Optional | The first line of the address associated with this Transaction. This field is stored as a text string and must be between 1 and 500 characters long. |
| `address_2` | `str` | Optional | The second line of the address associated with this Transaction. This field is stored as a text string and must be between 1 and 500 characters long. |
| `city` | `str` | Optional | The city in the address associated with this Transaction, which is stored as a text string and must be between 1 and 500 characters long. |
| `state` | `str` | Optional | The U.S. state or Canadian province relevant to the address provided here. If the location is within the U.S. and Canada, specify the 2-character postal abbreviation for the state. If the location is outside of the U.S. and Canada, provide the full state name. This field is stored as a text string and must be between 2 and 100 characters long.<br><br><details><br><summary>U.S. States</summary><br> <br> - `AK` - **Alaska (US)**<br> <br> - `AR` - **Arkansas (US)**<br> <br> - `AL` - **Alabama (US)**<br> <br> - `AZ` - **Arizona (US)**<br> <br> - `CA` - **California (US)**<br> <br> - `CO` - **Colorado (US)**<br> <br> - `CT` - **Connecticut (US)**<br> <br> - `DE` - **Delaware (US)**<br> <br> - `FL` - **Florida (US)**<br> <br> - `GA` - **Georgia (US)**<br> <br> - `HI` - **Hawaii (US)**<br> <br> - `IA` - **Iowa (US)**<br> <br> - `ID` - **Idaho (US)**<br> <br> - `IL` - **Illinois (US)**<br> <br> - `IN` - **Indiana (US)**<br> <br> - `KY` - **Kentucky (US)**<br> <br> - `KS` - **Kansas (US)**<br> <br> - `LA` - **Louisiana (US)**<br> <br> - `MA` - **Massachusetts (US)**<br> <br> - `MD` - **Maryland (US)**<br> <br> - `ME` - **Maine (US)**<br> <br> - `MI` - **Michigan (US)**<br> <br> - `MN` - **Minnesota (US)**<br> <br> - `MO` - **Missouri (US)**<br> <br> - `MS` - **Mississippi (US)**<br> <br> - `MT` - **Montana (US)**<br> <br> - `NC` - **North Carolina (US)**<br> <br> - `ND` - **North Dakota (US)**<br> <br> - `NE` - **Nebraska (US)**<br> <br> - `NH` - **New Hampshire (US)**<br> <br> - `NJ` - **New Jersey (US)**<br> <br> - `NM` - **New Mexico (US)**<br> <br> - `NV` - **Nevada (US)**<br> <br> - `NY` - **New York (US)**<br> <br> - `OH` - **Ohio (US)**<br> <br> - `OK`- **Oklahoma (US)**<br> <br> - `OR` - **Oregon (US)**<br> <br> - `PA` - **Pennsylvania (US)**<br> <br> - `RI` - **Rhode Island (US)**<br> <br> - `SC`- **South Carolina (US)**<br> <br> - `SD` - **South Dakota (US)**<br> <br> - `TN` - **Tennessee (US)**<br> <br> - `TX` - **Texas (US)**<br> <br> - `UT` - **Utah (US)**<br> <br> - `VA` - **Virginia (US)**<br> <br> - `VT` - **Vermont (US)**<br> <br> - `WA` - **Washington (US)**<br> <br> - `WI` - **Wisconsin (US)**<br> <br> - `WV` - **West Virginia (US)**<br> <br> - `WY` - **Wyoming (US)**<br> </details><br> <details><br><summary>Canada Provinces and Territories</summary><br> <br> - `AB` - **Alberta (CAN)**<br> <br> - `BC` - **British Columbia (CAN)**<br> <br> - `MB` - **Manitoba (CAN)**<br> <br> - `ON` - **Ontario (CAN)**<br> <br> - `NS` - **Nova Scotia (CAN)**<br> <br> - `NB` - **New Brunswick (CAN)**<br> <br> - `NL` - **Newfoundland and Labrador (CAN)**<br> <br> - `NT` - **Northwest Territories (CAN)**<br> <br> - `NU` - **Nunavut (CAN)**<br> <br> - `PE` - **Prince Edward Island (CAN)**<br> <br> - `QC` - **Quebec (CAN)**<br> <br> - `SK` - **Saskatchewan (CAN)**<br> <br> - `YT` - **Yukon (CAN)**<br> </details><br> |
| `zip` | `str` | Optional | The ZIP code in the address associated with this Transaction, This field is stored as a text string and must be between 1 and 20 characters long. |
| `country` | [`CountryEnum`](../../doc/models/country-enum.md) | Optional | The country associated with this transaction, valid values for this field are the 3-letter ISO code for the country. |
| `phone` | `str` | Optional | The phone number associated with this transaction, stored as a text string and must be between 10 and 15 characters long. |
| `status` | [`TerminalTxnStatusEnum`](../../doc/models/terminal-txn-status-enum.md) | Optional | The status of the Transaction.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Pending.**<br>- `1` - **Approved.** Payments can be voided or cancelled.<br>- `2` - **Failed.**<br>- `3` - **Captured.** Payments can be refunded.<br>- `4` - **Settled.** Payments can be refunded.<br>- `5` - **Returned.** Payments have been successfully refunded.<br></details><br>**Default**: `0`<br> |
| `reserved` | [`Reserved1Enum`](../../doc/models/reserved-1-enum.md) | Optional | Indicates whether the Transaction is reserved and the action that will be taken as a result.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **No reserve.**<br></details><br> |
| `check_stage` | `str` | Optional | The last transaction stage check for risk. |
| `originating_app` | `str` | Optional | Field identifying Payrix PAX terminal originating app. |
| `oemt_txn_ref_number` | `str` | Optional | Field identifying original Payrix Verifone transaction reference number, used for refunds and cancellation request. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `pos_application_id` | `str` | Optional | Express assigned identifier i.e. Software Id being used in express terminal. |
| `pos_application_name` | `str` | Optional | Software Name being used in express terminal. |
| `pos_application_version` | `str` | Optional | Software version being used in express terminal. |
| `customer_reference_number` | `str` | Optional | Express Reference Number. |
| `gateway_transaction_id` | `str` | Optional | The gateway transaction ID relates to Express Transaction ID. |
| `customer_ticket_number` | `str` | Optional | Express ticket Number. |
| `card_network_transaction_id` | `str` | Optional | Card network transaction ID associated with this transaction. |
| `omnitoken` | `str` | Optional | The OmniToken associated with this Transaction. |
| `convenience_fee` | `int` | Optional | The amount of the total sum of this Transaction that is made up of convenience fee. Fee charged when card payment is an alternative form of payment not ordinarily accepted by a merchant or service provider. This field is specified as an integer in cents. [currently not active] |
| `surcharge` | `int` | Optional | Surcharge amount included in the total amount of the transaction. A surcharge fee is an additional charge added to the price of a purchase when a customer pays with a credit card. This field is specified as an integer in cents. |
| `soft_pos_device_type_indicator` | `str` | Optional | The device type indicator for the terminal.<br><br><details><br><summary>Valid Values</summary><br>- `1` - **Apple (Worldpay as PSP)**<br>- `2` - **Android (Worldpay as PSP)**<br>- `3` - **Apple (Worldpay not PSP)**<br>- `4` - **Android (Worldpay not PSP)**<br></details><br> |
| `terminal_classification_code` | `str` | Optional | The terminal classification code.<br><br><details><br><summary>Valid Values</summary><br>- `AC` - **ATap with Accessory/dongle.**<br>- `AS` - **Tap with PIN on Glass option on Accessory/dongle.**<br>- `CC` - **Tap on Mobile device.**<br>- `CS` - **Tap with PIN on Glass option on Mobile device.**<br></details><br> |
| `soft_pos_id` | `str` | Optional | The software POS ID. |
| `hsa_fsa_card_indicator` | [`HsaFsaCardIndicatorEnum`](../../doc/models/hsa-fsa-card-indicator-enum.md) | Optional | Indicates if the card is a Flexible Spending Account (FSA) or Health Savings Account (HSA) card.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not an HSA/FSA card.**<br>- `1` - **HSA/FSA card.**<br></details><br> |
| `gateway_terminal_id` | `str` | Optional | The gateway terminal ID. |
| `descriptor` | `str` | Optional | The billing Descriptor that is used when the transaction is part of a subscription. |
| `card_network_bank_net_reference_number` | `str` | Optional | The reference number associated with the card network. |
| `card_network_bank_net_settlement_date` | `str` | Optional | The settlement date associated with the card network. |

## Example (as JSON)

```json
{
  "currency": "USD",
  "fundingCurrency": "USD",
  "status": 0,
  "inactive": 0,
  "frozen": 0,
  "id": "id4",
  "created": "created4",
  "modified": "modified2",
  "creator": "String3",
  "modifier": "modifier8"
}
```

