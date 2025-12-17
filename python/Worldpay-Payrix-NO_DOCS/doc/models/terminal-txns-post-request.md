
# Terminal Txns Post Request

## Structure

`TerminalTxnsPostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bin_type` | [`BinTypeEnum`](../../doc/models/bin-type-enum.md) | Required | The type of bank issuer number (BIN) that allows for resulting transactions.<br><br><details><br><summary>Valid Values</summary><br>- `CREDIT` - **Credit BIN Type.**<br>- `DEBIT` - **Debit BIN Type.**<br>- `PREPAID` - **Prepaid BIN Type.**<br></details><br> |
| `expiration` | `str` | Optional | The expiration date of this Transaction. This field is stored as a text string in 'MMYY' format, where 'MM' is the number of a month and 'YY' is the last two digits of a year. For example, '0623' for June 2023. The value must reflect a future date. |
| `forterminal_txn` | `str` | Optional | If this Terminal Transaction is related to another Terminal Transaction, then this field is set to the identifier of the other Terminal Transaction. For example, if this Terminal Transaction is a Refund, this field could be set to the identifier of the original Sale Terminal Transaction. |
| `origin` | [`TerminalTxnOriginEnum`](../../doc/models/terminal-txn-origin-enum.md) | Required | The origin of this Transaction.<br><br><details><br><summary>Valid Values</summary><br>- `1` - **Credit Card Terminal.**<br>- `2` - **eCommerce System.**<br>- `3` - **Mail or Telephone Order Transaction.**<br>- `4` - **Apple Pay (deprecated).**<br>- `5` - **Successful 3D Secure Transaction.**<br>- `6` - **Attempted 3D Secure Transaction.**<br>- `7` - **Recurring Card Transaction (deprecated).**<br>- `8` - **Payframe.**<br>- `9` - **Writing.**<br></details><br>**Default**: `1`<br> |
| `payment` | [`TerminalTxnsPayment`](../../doc/models/terminal-txns-payment.md) | Optional | The payment method associated with this Transaction, including the card details. |
| `platform` | [`Platform1Enum`](../../doc/models/platform-1-enum.md) | Optional | The platform used to process this resource.<br><br><details><br><summary>Valid Values</summary><br>- `APPLE` - **The Apple Payment Processor.**<br>- `ELAVON` - **The Elavon processor.**<br>- `FIRSTDATA` - **The FirstData processor.**<br>- `GOOGLE` - **The Google Payment Processor.**<br>- `VANTIV` - **The WorldPay (aka Vantiv or Litle) eComm (aka VAP) processor.**<br>- `VCORE` - **The WorldPay (aka Vantiv) Core processor.**<br>- `TDBANKCA` - **External funding with TD Bank Canada via the Operating Account.**<br>- `WELLSACH` - **The Wells Fargo ACH processor.**<br>- `WELLSFARGO` - **The Wells Fargo Merchant Services processor.**<br>- `WFSINGLE` - **The WFSINGLE processor.**<br>- `WORLDPAY` - **The WORLDPAY processor.**<br></details><br> |
| `pos` | [`PosEnum`](../../doc/models/pos-enum.md) | Required | Whether the terminalTxn is coming from a POS system that needs terminal activation.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **POS Terminal Activation.** (Internal)<br>- `1` - **External Terminal Activation.**<br></details><br> |
| `receipt` | [`ReceiptEnum`](../../doc/models/receipt-enum.md) | Optional | Whether the terminal should print a receipt or not.<br><br><details><br><summary>Valid Values</summary><br>- `noReceipt` - **No Receipt.**<br>- `merchant` - **Merchant copy only.**<br>- `customer` - **Customer copy only.**<br>- `both` - **Merchant and Customer copy.**<br></details><br> |
| `tid` | `str` | Optional | The Terminal ID as set by the platform activating the terminal. This field is stored as a text string and must be between 0 and 50 characters long. |
| `trace_number` | `int` | Optional | Sequencial number that uniquely identifies the terminalTxn. |
| `txn` | `str` | Optional | The related txn this terminalTxn belongs to. |
| `token` | `str` | Optional | The ID of the token record to associate with this terminal transaction request. |
| `payment_number` | `int` | Optional | The last four numbers of the credit card associated with this Transaction. |
| `payment_method` | [`TerminalTxnPaymentMethodEnum`](../../doc/models/terminal-txn-payment-method-enum.md) | Optional | The payment method for this Transaction. |
| `mtype` | [`TerminalTxnTypeEnum`](../../doc/models/terminal-txn-type-enum.md) | Required | The type of Transaction.<br><br><details><br><summary>Valid Values</summary><br>- `1` - **Credit Card Only: Sale Transaction.** This is the most common type of Transaction, it processes a sale and charges the customer.<br>- `2` - **Credit Card Only: Auth Transaction.** Authorizes and holds the requested total on the credit card.<br>- `4` - **Credit Card Only: Reverse Authorization.** Reverses a prior Auth or Sale Transaction and releases the credit hold.<br>- `5` - **Credit Card Only: Refund Transaction.** Refunds a prior Capture or Sale Transaction (total may be specified for a partial refund).<br>- `13` - **Batch out terminal.**<br></details><br> |
| `tip` | `int` | Optional | This field indicates the tip amount associated with a transaction. This value is for reporting purposes only, because transaction amount includes this amount in the total. |
| `originating_app` | `str` | Optional | Field identifying Payrix PAX terminal originating app. |
| `oemt_txn_ref_number` | `str` | Optional | Field identifying original Payrix Verifone transaction reference number, used for refunds and cancellation request. |
| `pos_application_id` | `str` | Optional | Express assigned identifier i.e. Software Id being used in express terminal. |
| `pos_application_name` | `str` | Optional | Software Name being used in express terminal. |
| `pos_application_version` | `str` | Optional | Software version being used in express terminal. |
| `customer_reference_number` | `str` | Optional | Express Reference Number. |
| `gateway_transaction_id` | `str` | Optional | The gateway transaction ID relates to Express Transaction ID. |
| `customer_ticket_number` | `str` | Optional | Express ticket Number. |
| `auth_code` | `str` | Optional | The authorization code for this Transaction. This field is stored as a text string and must be between 0 and 20 characters long. |
| `auth_date` | `int` | Optional | The date on which the Transaction was authorized. The date is specified as an eight digit string in YYYYMMDD format, for example, '20160120' for January 20, 2016. The value of this field must represent a date in the past. |
| `cashback` | `int` | Optional | The amount of the total sum of this Transaction that is given as cash back. This field is specified as an integer in cents. |
| `client_ip` | `str` | Optional | The client IP address from which the Transaction was created. Valid values are any Ipv4 or Ipv6 address. |
| `company` | `str` | Optional | The name of the company associated with this Transaction. nSetting this field is especially important when processing an eCheck from a company. |
| `currency` | [`CurrencyEnum`](../../doc/models/currency-enum.md) | Required | The currency for this transaction. See <a href="https://www.iban.com/currency-codes" target="_blank">Currency codes</a>  for all valid values. |
| `funding_currency` | [`FundingCurrencyEnum`](../../doc/models/funding-currency-enum.md) | Required | The currency for which this transaction was funded on. See <a href="https://www.iban.com/currency-codes" target="_blank">Currency codes</a>  for all valid values. |
| `cvv_status` | [`CvvStatusEnum`](../../doc/models/cvv-status-enum.md) | Optional | The status of the CVV on the card.<br><br><details><br><summary>Valid Values</summary><br>- `notPresent` - **CVV is not present.**<br>- `illegible` - **CVV is illegible.**<br>- `notProvided` - **CVV was not provided.**<br></details><br> |
| `description` | `str` | Optional | A description of this Transaction. This field is stored as a text string and must be between 0 and 1000 characters long. |
| `discount` | `int` | Optional | The discount applied to the transaction. |
| `duty` | `int` | Optional | The duty fee applicable to this transaction. |
| `email` | `str` | Optional | The email associated with this Transaction. |
| `swiped` | [`SwipedEnum`](../../doc/models/swiped-enum.md) | Required | Whether the card was swiped during this Transaction.<br>This field is set to '1' automatically if 'track' data was received.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Swiped.**<br>- `1` - **Swiped.**<br></details><br> |
| `entry_mode` | [`EntryModeEnum`](../../doc/models/entry-mode-enum.md) | Optional | How payment information has been entered, including manually keyed entries, card swipes with track 1 or 2 data received, card dips with EMV chip data received, contactless card reads with track or EMV data received, and ApplePay read with cryptogram data received.<br><br><details><br><summary>Valid Values</summary><br>- `1` - **Manually keyed entry.**<br>- `2` - **Card swiped. Track 1 received.**<br>- `3` - **Card swiped. Track 2 received.**<br>- `4` - **Card swiped. Track 1 & 2 received.**<br>- `5` - **Card dipped. EMV chip received.**<br>- `6` - **Contactless card read. Track or EMV data received.**<br>- `7` - **Track Data from Card Swipe after EMV chip failure.**<br>- `8` - **Track Data from Manually keyed entry after EMV chip failure.**<br>- `9` - **ApplePay**<br>- `10` - **Google Pay.**<br>- `11` - **Merchant created transaction.**<br>- `12` - **Invoice payment.**<br>- `13` - **Merchant created transaction in payrix portal.**<br>- `14` - **Invoice payment from payrix portal.**<br></details><br> |
| `fee` | `float` | Optional | Optional calculated fee amount indicator. This should be used in conjunction with txnFee setting on Fees resource. This field is specified in cents(up to three decimal points). |
| `first` | `str` | Optional | The first name associated with this Transaction. For eCheck transactions, either first or last is required. |
| `last` | `str` | Optional | The last name associated with this Transaction. For eCheck transactions, either first or last is required. |
| `merchant` | `str` | Required | The identifier of the Merchant associated with this Transaction. |
| `mid` | `str` | Required | The Merchant ID as set by the processor. This field is stored as a text string and must be between 0 and 50 characters long. |
| `middle` | `str` | Optional | The middle name associated with this Transaction. |
| `order` | `str` | Optional | The identifier of the Order associated with this Transaction. This field is stored as a text string and must be between 0 and 1000 characters long. |
| `pin` | [`PinEnum`](../../doc/models/pin-enum.md) | Required | Whether this Transaction was verified with a PIN.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **No PIN verification.**<br>- `1` - **PIN verification.**<br><br></details><br>**Default**: `0`<br> |
| `reserved` | `int` | Required, Constant | Indicates whether the Transaction is reserved and the action that will be taken as a result.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **No reserve.**<br></details><br>**Value**: `0`<br> |
| `shipping` | `int` | Optional | The shipping fee pertaining to this transaction. |
| `signature` | [`SignatureEnum`](../../doc/models/signature-enum.md) | Required | Whether a signature should be captured during this Transaction.<br><br>* You can set this field if you want the terminal to take a signature for the Transaction.<br>* The API also sets this field automatically if you associate a signature to the Transaction by creating a 'terminalTxnDatas' resource.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not captured.**<br>- `1` - **Captured.**<br></details><br> |
| `tax` | `int` | Optional | The amount of the total sum of this Transaction that is made up of tax. This field is specified as an integer in cents. |
| `terminal` | `str` | Optional | The identifier of the terminal that processed this Transaction. The identifier is taken from the terminal system and varies in format according to the type of terminal. This field is stored as a text string and must be between 0 and 50 characters long. |
| `terminal_capability` | [`TerminalCapabilityEnum`](../../doc/models/terminal-capability-enum.md) | Optional | Capabilities of the terminal device.<br><br><details><br><summary>Valid Values</summary><br>- `1` - **Key entry only terminal.**<br>- `2` - **Can read magnetic stripe.**<br>- `3` - **Integrated circuit reader.**<br>- `4` - **Can detect contactless payment.**<br></details><br> |
| `total` | `int` | Required | The total amount of this Transaction. This field is specified as an integer in cents. |
| `unattended` | [`UnattendedEnum`](../../doc/models/unattended-enum.md) | Optional | Whether the card was swiped at an unattended terminal during this Transaction.<br>This field is set to '0' by default.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Attended terminal.**<br>- `1` - **Unattended terminal.**<br></details><br> |
| `status` | [`TerminalTxnStatusEnum`](../../doc/models/terminal-txn-status-enum.md) | Required | The status of the Transaction.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Pending.**<br>- `1` - **Approved.** Payments can be voided or cancelled.<br>- `2` - **Failed.**<br>- `3` - **Captured.** Payments can be refunded.<br>- `4` - **Settled.** Payments can be refunded.<br>- `5` - **Returned.** Payments have been successfully refunded.<br></details><br>**Default**: `0`<br> |
| `address_1` | `str` | Optional | The first line of the address associated with this Transaction. This field is stored as a text string and must be between 1 and 500 characters long. |
| `address_2` | `str` | Optional | The second line of the address associated with this Transaction. This field is stored as a text string and must be between 1 and 500 characters long. |
| `city` | `str` | Optional | The name of the city in the address associated with this Transaction. This field is stored as a text string and must be between 1 and 500 characters long. |
| `state` | `str` | Optional | The U.S. state or Canadian province relevant to the address provided here. If the location is within the U.S. and Canada, specify the 2-character postal abbreviation for the state. If the location is outside of the U.S. and Canada, provide the full state name. This field is stored as a text string and must be between 2 and 100 characters long.<br><br><details><br><summary>U.S. States</summary><br> <br> - `AK` - **Alaska (US)**<br> <br> - `AR` - **Arkansas (US)**<br> <br> - `AL` - **Alabama (US)**<br> <br> - `AZ` - **Arizona (US)**<br> <br> - `CA` - **California (US)**<br> <br> - `CO` - **Colorado (US)**<br> <br> - `CT` - **Connecticut (US)**<br> <br> - `DE` - **Delaware (US)**<br> <br> - `FL` - **Florida (US)**<br> <br> - `GA` - **Georgia (US)**<br> <br> - `HI` - **Hawaii (US)**<br> <br> - `IA` - **Iowa (US)**<br> <br> - `ID` - **Idaho (US)**<br> <br> - `IL` - **Illinois (US)**<br> <br> - `IN` - **Indiana (US)**<br> <br> - `KY` - **Kentucky (US)**<br> <br> - `KS` - **Kansas (US)**<br> <br> - `LA` - **Louisiana (US)**<br> <br> - `MA` - **Massachusetts (US)**<br> <br> - `MD` - **Maryland (US)**<br> <br> - `ME` - **Maine (US)**<br> <br> - `MI` - **Michigan (US)**<br> <br> - `MN` - **Minnesota (US)**<br> <br> - `MO` - **Missouri (US)**<br> <br> - `MS` - **Mississippi (US)**<br> <br> - `MT` - **Montana (US)**<br> <br> - `NC` - **North Carolina (US)**<br> <br> - `ND` - **North Dakota (US)**<br> <br> - `NE` - **Nebraska (US)**<br> <br> - `NH` - **New Hampshire (US)**<br> <br> - `NJ` - **New Jersey (US)**<br> <br> - `NM` - **New Mexico (US)**<br> <br> - `NV` - **Nevada (US)**<br> <br> - `NY` - **New York (US)**<br> <br> - `OH` - **Ohio (US)**<br> <br> - `OK`- **Oklahoma (US)**<br> <br> - `OR` - **Oregon (US)**<br> <br> - `PA` - **Pennsylvania (US)**<br> <br> - `RI` - **Rhode Island (US)**<br> <br> - `SC`- **South Carolina (US)**<br> <br> - `SD` - **South Dakota (US)**<br> <br> - `TN` - **Tennessee (US)**<br> <br> - `TX` - **Texas (US)**<br> <br> - `UT` - **Utah (US)**<br> <br> - `VA` - **Virginia (US)**<br> <br> - `VT` - **Vermont (US)**<br> <br> - `WA` - **Washington (US)**<br> <br> - `WI` - **Wisconsin (US)**<br> <br> - `WV` - **West Virginia (US)**<br> <br> - `WY` - **Wyoming (US)**<br> </details><br> <details><br><summary>Canada Provinces and Territories</summary><br> <br> - `AB` - **Alberta (CAN)**<br> <br> - `BC` - **British Columbia (CAN)**<br> <br> - `MB` - **Manitoba (CAN)**<br> <br> - `ON` - **Ontario (CAN)**<br> <br> - `NS` - **Nova Scotia (CAN)**<br> <br> - `NB` - **New Brunswick (CAN)**<br> <br> - `NL` - **Newfoundland and Labrador (CAN)**<br> <br> - `NT` - **Northwest Territories (CAN)**<br> <br> - `NU` - **Nunavut (CAN)**<br> <br> - `PE` - **Prince Edward Island (CAN)**<br> <br> - `QC` - **Quebec (CAN)**<br> <br> - `SK` - **Saskatchewan (CAN)**<br> <br> - `YT` - **Yukon (CAN)**<br> </details><br> |
| `zip` | `str` | Optional | The ZIP code in the address associated with this Transaction. This field is stored as a text string and must be between 1 and 20 characters long. |
| `country` | [`CountryEnum`](../../doc/models/country-enum.md) | Optional | The country associated with this transaction, valid values for this field are the 3-letter ISO code for the country. |
| `phone` | `str` | Optional | The phone number associated with this Transaction. This field is stored as a text string and must be between 10 and 15 characters long. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Required | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Required | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "binType": "DEBIT",
  "expiration": "1023",
  "forterminalTxn": "forterminalTxn",
  "origin": 1,
  "payment": {
    "method": 1,
    "number": "1234",
    "routing": "123456789",
    "expiration": "1023",
    "cvv": 123,
    "track": "Track1"
  },
  "platform": "VCORE",
  "pos": 0,
  "receipt": "noReceipt",
  "tid": "Terminal ID",
  "traceNumber": 853202,
  "txn": "related txn",
  "token": "124f2d0efab0bcda46f2118d688bbf97",
  "paymentNumber": 7,
  "paymentMethod": 2,
  "type": 1,
  "tip": 0,
  "originatingApp": "originatingApp",
  "OEMTTxnRefNumber": "TxnRefNumber",
  "posApplicationId": "15668",
  "posApplicationName": "XML Test Example",
  "posApplicationVersion": "1.00",
  "customerReferenceNumber": "123456",
  "gatewayTransactionId": "486689252",
  "customerTicketNumber": "123456",
  "authCode": "authorization code",
  "authDate": 20160120,
  "cashback": 0,
  "clientIp": "Client IP address",
  "company": "company1",
  "currency": "USD",
  "fundingCurrency": "USD",
  "cvvStatus": "notPresent",
  "description": "description1",
  "discount": 0,
  "duty": 0,
  "email": "john.johnson@example.com",
  "swiped": 1,
  "entryMode": 1,
  "fee": 0,
  "first": "John",
  "last": "Doe",
  "merchant": "t1_mer_64415e89a919c1566a2b49b",
  "mid": "4445061378323",
  "middle": "M",
  "order": "orderId",
  "pin": 0,
  "reserved": 0,
  "shipping": 0,
  "signature": 0,
  "tax": 0,
  "terminal": "identifier of terminal",
  "terminalCapability": 1,
  "total": 8000,
  "unattended": 0,
  "status": 1,
  "address1": "address1",
  "address2": "address2",
  "city": "city1",
  "state": "AB",
  "zip": "ZIP code",
  "country": "CAN",
  "phone": "9999888888",
  "inactive": 0,
  "frozen": 0
}
```

