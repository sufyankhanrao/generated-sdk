
# Txns Post Request

## Structure

`TxnsPostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allow_partial` | [`AllowPartialEnum`](../../doc/models/allow-partial-enum.md) | Required | Whether to allow partial amount authorizations of this Transaction. For example, if the transaction amount is $1000 and the processor only authorizes a smaller amount, then enabling this field lets the Transaction proceed anyway.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Partial amount authorizations are not allowed.**<br>- `1` - **Partial amount authorizations are allowed.**<br><br></details><br>**Default**: `0`<br> |
| `batch` | `str` | Optional | If the Transaction is linked to a Batch, this field specifies the identifier of the Batch. |
| `authentication` | `str` | Required | Authentication token returned by the network in a 3DSecure txn. |
| `authentication_id` | `str` | Optional | Optional transaction ID returned by the network in a 3DSecure txn. |
| `cof_type` | [`CofTypeEnum`](../../doc/models/cof-type-enum.md) | Optional | The type of Card On File transaction when using a token is single, scheduled, or unscheduled.<br><br><details><br><summary>Valid Values</summary><br>- `single`  - **Individual Transaction.**<br>- `scheduled`  - **Scheduled Transaction.**<br>- `unscheduled`  - **Unscheduled sequential Transaction.**<br>- `installment`  - **Installment Transaction.**<br></details><br> |
| `currency_conversion` | [`CurrencyConversionEnum`](../../doc/models/currency-conversion-enum.md) | Optional | The status of the currency conversion.<br><br><details><br><summary>Valid Values</summary><br>- `customerAccepted` - **The customer accepted the currency conversion rate.**<br>- `customerRejected` - **The customer rejected the currency conversion rate.**<br>- `notEligible` - **This transaction is not eligible for currency conversion.**<br></details><br> |
| `debt_repayment` | [`DebtRepaymentEnum`](../../doc/models/debt-repayment-enum.md) | Required | If this transaction is for debt repayment or not for debt repayment.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Transaction not for debt repayment.**<br>- `1` - **Transaction for debt repayment.**<br><br></details><br>**Default**: `0`<br> |
| `expiration` | `str` | Optional | The expiration date of this Transaction.<br>This field is stored as a text string in 'MMYY' format, where 'MM' is the number of a month and 'YY' is the last two digits of a year. For example, '0623' for June 2023.<br>The value must reflect a future date. |
| `fortxn` | `str` | Required | If this Transaction is related to another Transaction, then this field is set to the identifier of the other Transaction.<br>For example, if this Transaction is a refund, this field could be set to the identifier of the original sale Transaction. |
| `fromtxn` | `str` | Optional | Reauthorize this referenced Transaction. For example, to process a resubmission of a declined Transaction or to reauthorize an expired Transaction. |
| `copy_reason` | [`CopyReasonEnum`](../../doc/models/copy-reason-enum.md) | Optional | Reason for copying Transaction referenced in fromtxn field, which can be either resubmission or reauthorization. <details> <summary>Valid Values</summary><br><br>- `resubmission` - **Resubmission.**<br>- `reauthorization` - **Reauthorization.**<br><br></details><br> |
| `mobile` | [`MobileEnum`](../../doc/models/mobile-enum.md) | Optional | Indicates if a transaction is being processed through a Mobile POS.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Non-mobile POS.**<br>- `1` - **Mobile POS.**<br><br></details><br> |
| `origin` | [`TxnOrigin1Enum`](../../doc/models/txn-origin-1-enum.md) | Required | The origin of the transaction.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Unknown.**<br>- `1` - **Originated at a credit card terminal.**<br><br>- `2` - **Originated through an eCommerce system.**<br><br>- `3` - **Originated as a mail order or telephone order transaction.**<br><br>- `4` - **Originated with Apple Pay.**<br><br>- `5` - **Originated as a Successful 3D Secure transaction.**<br><br>- `6` - **Originated as an Attempted 3D Secure transaction.**<br><br>- `7` - **Originated as a recurring transaction on the card.**<br><br>- `8` - **Originated in a PayFrame.**<br><br>- `9` - **Originated in writing.**<br><br></details><br> |
| `pin_entry_capability` | [`PinEntryCapabilityEnum`](../../doc/models/pin-entry-capability-enum.md) | Optional | Indicates the PIN entry capability of the device, which can be unknown, capable, notCapable, or pinPadDown.<br><br><details><br><summary>Valid Values</summary><br>- `unknown` - **Unknown PIN Entry Capability.**<br>- `capable` - **Terminal can accept PINs.**<br>- `notCapable` - **Terminal cannot accept entry of PINs.**<br>- `pinPadDown` - **Terminal PIN Pad is down.**<br></details><br> |
| `pinless_debit_conversion` | [`PinlessDebitConversionEnum`](../../doc/models/pinless-debit-conversion-enum.md) | Optional | Whether the transaction was converted to PINless Debit or not. If null the conversion was not requested.<br><br><details><br><summary>Valid Values</summary><br>- `0 - **The transaction was not converted to pinless debit.**<br>- `1` - **The transaction was converted to to pinless debit.**<br></details><br> |
| `platform` | [`TxnsPlatformEnum`](../../doc/models/txns-platform-enum.md) | Required | The platform used to process transactions.<br><br><details><br><summary>Valid Values</summary><br>- `APPLE` - **The Apple Payment Processor (Deprecated).**<br>- `ELAVON` - **The Elavon processor (Deprecated).**<br>- `FIRSTDATA` - **The FirstData processor (Deprecated).**<br>- `GOOGLE` - **The Google Payment Processor (Deprecated).**<br>- `VANTIV` - **The WorldPay (aka Vantiv or Litle) eComm (aka VAP) processor.**<br>- `VCORE` - **The WorldPay (aka Vantiv) Core processor.**<br>- `WELLSACH` - **The Wells Fargo ACH processor.**<br>- `WELLSFARGO` - **The Wells Fargo Merchant Services processor (Deprecated).**<br>- `WFSINGLE` - **The WFSINGLE processor (Deprecated).**<br></details><br> |
| `processed_sequence` | `int` | Optional | For entry creation and deletion job sequencing: the current processed sequence number for this transaction.<br><br>**Default**: `0` |
| `funded` | `int` | Optional | A date indicating when this Transaction was funded.<br>This field is set automatically. |
| `returned` | `str` | Optional | The transaction has been returned by the receiver. |
| `funding_enabled` | [`TxnsFundingEnabledEnum`](../../doc/models/txns-funding-enabled-enum.md) | Optional | Whether or not funding is enabled for this Transaction.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Disabled.**<br>- `1` - **Enabled.**<br><br></details><br> |
| `fbo` | `str` | Optional | FBO (for benefit of) in which each entry origin belongs to. |
| `request_sequence` | `int` | Optional | For entry creation and deletion job sequencing: the current processed sequence number for this transaction.<br><br>**Default**: `0` |
| `statement` | `str` | Optional | The statement ID for which this transaction is being processed as payment. |
| `token` | `str` | Optional | The token of the Tokens resource this Transaction is associated with. |
| `mtype` | [`TxnTypeEnum`](../../doc/models/txn-type-enum.md) | Required | The type of Transaction.<br><br><details><br><summary>Valid Values</summary><br>- `1` - **Credit Card Only: Sale Transaction.** Processes a sale and charges the customer.<br>- `2` - **Credit Card Only: Auth Transaction.** Authorizes and holds the requested total on the credit card.<br>- `3` - **Credit Card Only: Capture Transaction.** Finalizes a prior Auth Transaction and charges the customer.<br>- `4` - **Credit Card Only: Reverse Authorization.** Reverses a prior Auth or Sale Transaction and releases the credit hold.<br>- `5` - **Credit Card Only: Refund Transaction.** Refunds a prior Capture or Sale Transaction (total may be specified for a partial refund).<br>- `7` - **Echeck Only: Echeck Sale Transaction.** Sale Transaction for ECheck payment.<br>- `8` - **Echeck Only: Echeck Refund Transaction.** Refund Transaction for prior ECheck Sale Transaction.<br>- `11` - **Echeck Only: Echeck Redeposit Transaction.** Attempt to redeposit a prior failed eCheck Sale Transaction.<br>- `12` - **Echeck Only: Echeck Account Verification Transaction.** Attempt to verify eCheck payment details.<br>- `14` - **Incremental Authorization.**<br></details><br> |
| `unauth_reason` | [`UnauthReasonEnum`](../../doc/models/unauth-reason-enum.md) | Required | The reason for the auth reversal.<br>This field is set to 'customerCancelled' by default.<br><br><details><br><summary>Valid Values</summary><br>- `incomplete` - **Transaction Incomplete.**<br>- `timeout` - **Transaction Timeout.**<br><br>- `clerkCancelled` - **Transaction Cancelled by Clerk.**<br><br>- `customerCancelled` - **Transaction Cancelled by Customer.**<br><br>- `misdispense` - **Misdispense.**<br><br>- `hardwareFailure` - **Hardware Failure.**<br><br>- `suspectedFraud` - **Suspected Fraud.**<br><br></details><br> |
| `auth_token_customer` | `str` | Optional | The customer identifier from the AuthToken used during authentication. |
| `channel` | `str` | Optional | This field is stored as a text string and must be between 0 and 1000 characters long. |
| `cashback` | `int` | Optional | The amount of the total sum of this Transaction that is given as cash back.<br>This field is specified as an integer in cents. |
| `client_ip` | `str` | Optional | The client ip address from which the Transaction was created.<br>Valid values are any Ipv4 or Ipv6 address. |
| `company` | `str` | Optional | The name of the company associated with this Transaction.<br>Setting this field is especially important when processing an eCheck from a company. |
| `currency` | [`CurrencyEnum`](../../doc/models/currency-enum.md) | Required | The currency for this transaction. See <a href="https://www.iban.com/currency-codes" target="_blank">Currency codes</a>  for all valid values. |
| `funding_currency` | [`FundingCurrencyEnum`](../../doc/models/funding-currency-enum.md) | Required | The currency for which transaction was funded on. See <a href="https://www.iban.com/currency-codes" target="_blank">Currency codes</a>  for all valid values. |
| `cvv_status` | [`CvvStatusEnum`](../../doc/models/cvv-status-enum.md) | Optional | The status of the CVV on the card.<br><br><details><br><summary>Valid Values</summary><br>- `notPresent` - **CVV is not present.**<br>- `illegible` - **CVV is illegible.**<br><br>- `notProvided` - **CVV was not provided.**<br><br></details><br> |
| `description` | `str` | Optional | A description of this Transaction.<br>This field is stored as a text string and must be between 0 and 1000 characters long. |
| `discount` | `int` | Optional | The customer discount, in cents, already applied to the total for this transaction. |
| `duty` | `int` | Optional | The amount of the total, in cents, that represents the duties charged to the customer |
| `email` | `str` | Optional | The email associated with this Transaction. |
| `swiped` | [`SwipedEnum`](../../doc/models/swiped-enum.md) | Required | Whether the card was swiped during this Transaction.<br>This field is set to '1' automatically if 'track' data was received.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Swiped.**<br>- `1` - **Swiped.**<br></details><br> |
| `entry_mode` | [`EntryModeEnum`](../../doc/models/entry-mode-enum.md) | Optional | How payment information has been entered, including manually keyed entries, card swipes with track 1 or 2 data received, card dips with EMV chip data received, contactless card reads with track or EMV data received, and ApplePay read with cryptogram data received.<br><br><details><br><summary>Valid Values</summary><br>- `1` - **Manually keyed entry.**<br>- `2` - **Card swiped. Track 1 received.**<br>- `3` - **Card swiped. Track 2 received.**<br>- `4` - **Card swiped. Track 1 & 2 received.**<br>- `5` - **Card dipped. EMV chip received.**<br>- `6` - **Contactless card read. Track or EMV data received.**<br>- `7` - **Track Data from Card Swipe after EMV chip failure.**<br>- `8` - **Track Data from Manually keyed entry after EMV chip failure.**<br>- `9` - **ApplePay**<br>- `10` - **Google Pay.**<br>- `11` - **Merchant created transaction.**<br>- `12` - **Invoice payment.**<br>- `13` - **Merchant created transaction in payrix portal.**<br>- `14` - **Invoice payment from payrix portal.**<br></details><br> |
| `fee` | `float` | Optional | Optional calculated fee amount indicator. This should be used in conjunction with txnFee setting on Fees resource,<br>This field is specified in cents(up to three decimal points) |
| `first` | `str` | Optional | The first name associated with this Transaction. For eCheck transactions, either first or last is required. |
| `last` | `str` | Optional | The last name associated with this Transaction. For eCheck transactions, either first or last is required. |
| `merchant` | `str` | Required | The identifier of the Merchant associated with this Transaction. |
| `mid` | `str` | Required | The Merchant ID as set by the processor.<br>This field is stored as a text string and must be between 0 and 50 characters long. |
| `middle` | `str` | Optional | The middle name associated with this Transaction. |
| `order` | `str` | Optional | The identifier of the Order associated with this Transaction.<br>This field is stored as a text string and must be between 0 and 1000 characters long. |
| `pin` | [`PinEnum`](../../doc/models/pin-enum.md) | Required | Whether this Transaction was verified with a PIN.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **No PIN verification.**<br>- `1` - **PIN verification.**<br><br></details><br>**Default**: `0`<br> |
| `shipping` | `int` | Optional | The amount of the total, in cents, that represents the shipping cost charged to the customer |
| `signature` | [`SignatureEnum`](../../doc/models/signature-enum.md) | Required | Whether a signature was captured during this Transaction. You can set this field if you took a signature for the Transaction. The API also sets this field automatically if you associate a signature to the Transaction by creating a 'txnDatas' resource.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not captured.**<br>- `1` - **Captured.**<br><br></details><br>**Default**: `0`<br> |
| `tax` | `int` | Optional | The amount of the total sum of this Transaction that is made up of tax.<br>This field is specified as an integer in cents. |
| `surcharge` | `int` | Optional | The amount of the total sum of this Transaction that is made up of surcharge.<br>This field is specified as an integer in cents. |
| `terminal` | `str` | Optional | The identifier of the terminal that processed this Transaction.<br>The identifier is taken from the terminal system and varies in format according to the type of terminal.<br>This field is stored as a text string and must be between 0 and 50 characters long. |
| `terminal_capability` | [`TerminalCapabilityEnum`](../../doc/models/terminal-capability-enum.md) | Optional | Capabilities of the terminal device.<br><br><details><br><summary>Valid Values</summary><br>- `1` - **Key entry only terminal.**<br>- `2` - **Can read magnetic stripe.**<br>- `3` - **Integrated circuit reader.**<br>- `4` - **Can detect contactless payment.**<br></details><br> |
| `total` | `int` | Required | The total amount of this Transaction.<br>This field is specified as an integer in cents.For example, $10.15 would be entered as 1015. |
| `unattended` | [`UnattendedEnum`](../../doc/models/unattended-enum.md) | Required | Whether the card was swiped at an unattended terminal during this Transaction.<br>This field is set to '0' by default.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Attended terminal.**<br>- `1` - **Unattended terminal.**<br></details><br> |
| `address_1` | `str` | Optional | The first line of the address associated with this Transaction.<br>This field is stored as a text string and must be between 1 and 500 characters long. |
| `address_2` | `str` | Optional | The second line of the address associated with this Transaction.<br>This field is stored as a text string and must be between 1 and 500 characters long. |
| `city` | `str` | Optional | The name of the city in the address associated with this Transaction.<br>This field is stored as a text string and must be between 1 and 500 characters long. |
| `state` | `str` | Optional | The U.S. state or Canadian province relevant to the address provided here. If the location is within the U.S. and Canada, specify the 2-character postal abbreviation for the state. If the location is outside of the U.S. and Canada, provide the full state name. This field is stored as a text string and must be between 2 and 100 characters long.<br><br><details><br><summary>U.S. States</summary><br> <br> - `AK` - **Alaska (US)**<br> <br> - `AR` - **Arkansas (US)**<br> <br> - `AL` - **Alabama (US)**<br> <br> - `AZ` - **Arizona (US)**<br> <br> - `CA` - **California (US)**<br> <br> - `CO` - **Colorado (US)**<br> <br> - `CT` - **Connecticut (US)**<br> <br> - `DE` - **Delaware (US)**<br> <br> - `FL` - **Florida (US)**<br> <br> - `GA` - **Georgia (US)**<br> <br> - `HI` - **Hawaii (US)**<br> <br> - `IA` - **Iowa (US)**<br> <br> - `ID` - **Idaho (US)**<br> <br> - `IL` - **Illinois (US)**<br> <br> - `IN` - **Indiana (US)**<br> <br> - `KY` - **Kentucky (US)**<br> <br> - `KS` - **Kansas (US)**<br> <br> - `LA` - **Louisiana (US)**<br> <br> - `MA` - **Massachusetts (US)**<br> <br> - `MD` - **Maryland (US)**<br> <br> - `ME` - **Maine (US)**<br> <br> - `MI` - **Michigan (US)**<br> <br> - `MN` - **Minnesota (US)**<br> <br> - `MO` - **Missouri (US)**<br> <br> - `MS` - **Mississippi (US)**<br> <br> - `MT` - **Montana (US)**<br> <br> - `NC` - **North Carolina (US)**<br> <br> - `ND` - **North Dakota (US)**<br> <br> - `NE` - **Nebraska (US)**<br> <br> - `NH` - **New Hampshire (US)**<br> <br> - `NJ` - **New Jersey (US)**<br> <br> - `NM` - **New Mexico (US)**<br> <br> - `NV` - **Nevada (US)**<br> <br> - `NY` - **New York (US)**<br> <br> - `OH` - **Ohio (US)**<br> <br> - `OK`- **Oklahoma (US)**<br> <br> - `OR` - **Oregon (US)**<br> <br> - `PA` - **Pennsylvania (US)**<br> <br> - `RI` - **Rhode Island (US)**<br> <br> - `SC`- **South Carolina (US)**<br> <br> - `SD` - **South Dakota (US)**<br> <br> - `TN` - **Tennessee (US)**<br> <br> - `TX` - **Texas (US)**<br> <br> - `UT` - **Utah (US)**<br> <br> - `VA` - **Virginia (US)**<br> <br> - `VT` - **Vermont (US)**<br> <br> - `WA` - **Washington (US)**<br> <br> - `WI` - **Wisconsin (US)**<br> <br> - `WV` - **West Virginia (US)**<br> <br> - `WY` - **Wyoming (US)**<br> </details><br> <details><br><summary>Canada Provinces and Territories</summary><br> <br> - `AB` - **Alberta (CAN)**<br> <br> - `BC` - **British Columbia (CAN)**<br> <br> - `MB` - **Manitoba (CAN)**<br> <br> - `ON` - **Ontario (CAN)**<br> <br> - `NS` - **Nova Scotia (CAN)**<br> <br> - `NB` - **New Brunswick (CAN)**<br> <br> - `NL` - **Newfoundland and Labrador (CAN)**<br> <br> - `NT` - **Northwest Territories (CAN)**<br> <br> - `NU` - **Nunavut (CAN)**<br> <br> - `PE` - **Prince Edward Island (CAN)**<br> <br> - `QC` - **Quebec (CAN)**<br> <br> - `SK` - **Saskatchewan (CAN)**<br> <br> - `YT` - **Yukon (CAN)**<br> </details><br> |
| `zip` | `str` | Optional | The ZIP code in the address associated with this Transaction.<br>This field is stored as a text string and must be between 1 and 20 characters long. |
| `country` | [`CountryEnum`](../../doc/models/country-enum.md) | Optional | The country associated with this transaction, valid values for this field are the 3-letter ISO code for the country. |
| `phone` | `str` | Optional | The phone number associated with this Transaction.<br>This field is stored as a text string and must be between 10 and 15 characters long. |
| `tmx_session_id` | `str` | Optional | Threatmetrix session ID, used to trace the financial session and prevent possible frauds. |
| `first_txn` | `str` | Optional | For external recurring systems, this is the first transaction ID related to this recurring payment. |
| `payment` | [`TxnsPayment`](../../doc/models/txns-payment.md) | Required | The payment method associated with this Transaction, including the card details. |

## Example (as JSON)

```json
{
  "allowPartial": 1,
  "batch": "t1_bth_67b6129bcca1cbb7cdac000",
  "authentication": "Authentication Token",
  "authenticationId": "Optional transaction ID",
  "cofType": "single",
  "currencyConversion": "customerAccepted",
  "debtRepayment": 1,
  "expiration": "0623",
  "fortxn": "t1_txn_67b5f9801e463c908f453oo",
  "fromtxn": "Reauthorize an expired Transaction",
  "copyReason": "resubmission",
  "mobile": 0,
  "origin": 4,
  "pinEntryCapability": "unknown",
  "platform": "VANTIV",
  "processedSequence": 0,
  "funded": 623,
  "returned": "Returned Transaction",
  "fundingEnabled": 0,
  "fbo": "WORLDPAY_FBO1",
  "requestSequence": 1,
  "statement": "statement ID",
  "token": "31b0ac1d55c898a7b6758ed2209fce00",
  "type": 3,
  "unauthReason": "customerCancelled",
  "authTokenCustomer": "Customer Identifier",
  "channel": "LA",
  "cashback": 0,
  "clientIp": "216.80.4.000",
  "company": "Hotdog Water",
  "currency": "DOP",
  "fundingCurrency": "BRL",
  "cvvStatus": "notPresent",
  "description": "Neon Test",
  "discount": 0,
  "duty": 0,
  "email": "robert.johnson@example.com",
  "swiped": 1,
  "entryMode": 1,
  "fee": 997,
  "first": "Robert",
  "middle": "John",
  "last": "Johnson",
  "merchant": "t1_mer_1344e1a5460f5cfdf21ce11",
  "mid": "11003321",
  "order": "identifier",
  "pin": 1,
  "shipping": 0,
  "signature": 1,
  "tax": 0,
  "surcharge": 0,
  "terminal": "Terminal Identifier",
  "terminalCapability": 1,
  "total": 1010,
  "unattended": 1,
  "address1": "708 Kunde Mission",
  "address2": "Apt 3g",
  "city": "New York",
  "state": "NY",
  "zip": "10001",
  "country": "USA",
  "phone": "1111111111",
  "tmxSessionId": "Threatmetrix session ID",
  "firstTxn": "t1_txn_67b6129bcca1cbb7cdac001",
  "pinlessDebitConversion": 0,
  "payment": {
    "method": 2,
    "number": "1111",
    "routing": "code",
    "cvv": 11,
    "track": {
      "key1": "val1",
      "key2": "val2"
    },
    "expiration": "expiration0"
  }
}
```

