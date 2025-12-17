
# V1 Transactions Cc Balance Inquiry Prev Trxn Request

## Structure

`V1TransactionsCcBalanceInquiryPrevTrxnRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_amounts` | [`List[AdditionalAmount]`](../../doc/models/additional-amount.md) | Optional | Additional amounts |
| `billing_address` | [`BillingAddress`](../../doc/models/billing-address.md) | Optional | Billing Address Object |
| `checkin_date` | `str` | Optional | Checkin Date - The time difference between checkin_date and checkout_date must be less than or equal to 99 days.<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[\d]{4}-[\d]{2}-[\d]{2}$` |
| `checkout_date` | `str` | Optional | Checkout Date - The time difference between checkin_date and checkout_date must be less than or equal to 99 days.<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[\d]{4}-[\d]{2}-[\d]{2}$` |
| `clerk_number` | `str` | Optional | Clerk or Employee Identifier<br><br>**Constraints**: *Maximum Length*: `16` |
| `contact_api_id` | `str` | Optional | This can be supplied in place of contact_id if you would like to use a contact for the transaction and are using your own custom api_id's to track contacts in the system.<br><br>**Constraints**: *Maximum Length*: `36` |
| `contact_id` | `str` | Optional | If contact_id is provided, ensure it belongs to the same location as the transaction. You cannot move transaction across locations.<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `custom_data` | `Any` | Optional | A field that allows custom JSON to be entered to store extra data. |
| `customer_id` | `str` | Optional | Can be used by Merchants to identify Contacts in our system by an ID from another system.<br><br>**Constraints**: *Maximum Length*: `64` |
| `description` | `str` | Optional | Description<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `64` |
| `identity_verification` | [`IdentityVerification`](../../doc/models/identity-verification.md) | Optional | Identity Verification |
| `iias_ind` | [`IiasIndEnum`](../../doc/models/iias-ind-enum.md) | Optional | Possible values are '0', '1','2' |
| `image_front` | `str` | Optional | A base64 encoded string for the image.  Used with Check21 ACH transactions. |
| `image_back` | `str` | Optional | A base64 encoded string for the image.  Used with Check21 ACH transactions. |
| `installment` | `bool` | Optional | Flag that is allowed to be passed on card not present industries to signify the transaction is a fixed installment plan transaction. |
| `installment_number` | `int` | Optional | If this is a fixed installment plan and installment field is being passed as 1, then this field must have a vlue of 1-999 specifying the current installment number that is running.<br><br>**Constraints**: `>= 1`, `<= 999` |
| `installment_count` | `int` | Optional | If this is a fixed installment plan and installment field is being passed as 1, then this field must have a vlue of 1-999 specifying the total number of installments on the plan. This number must be grater than or equal to installment_number.<br><br>**Constraints**: `>= 1`, `<= 999` |
| `location_api_id` | `str` | Optional | This can be supplied in place of location_id for the transaction if you are using your own custom api_id's for your locations.<br><br>**Constraints**: *Maximum Length*: `36` |
| `location_id` | `str` | Optional | A valid Location Id to associate the transaction with.<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `product_transaction_id` | `str` | Optional | The Product's method (cc/ach) has to match the action. If not provided, the API will use the default configured for the Location.<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `advance_deposit` | `bool` | Optional | Advance Deposit |
| `no_show` | `bool` | Optional | Used in Lodging |
| `notification_email_address` | `str` | Optional | If email is supplied then receipt will be emailed |
| `order_number` | `str` | Optional | Required for CC transactions , if merchant's deposit account's duplicate check per batch has 'order_number' field<br><br>**Constraints**: *Maximum Length*: `32` |
| `po_number` | `str` | Optional | Purchase Order number<br><br>**Constraints**: *Maximum Length*: `36` |
| `quick_invoice_id` | `str` | Optional | Can be used to associate a transaction to a Quick Invoice.  Quick Invoice transactions will have a value for this field automatically.<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `recurring` | `bool` | Optional | Flag that is allowed to be passed on card not present industries to signify the transaction is an ongoing recurring transaction. Possible values to send are 0 or 1. This field must be 0 or not present if installment is sent as 1. |
| `recurring_number` | `int` | Optional | If this is an ongoing recurring and recurring field is being passed as 1, then this field must have a vlue of 1-999 specifying the current recurring number that is running.<br><br>**Constraints**: `>= 1`, `<= 999` |
| `room_num` | `str` | Optional | Used in Lodging<br><br>**Constraints**: *Maximum Length*: `12` |
| `room_rate` | `int` | Optional | Required if merchant industry type is lodging. |
| `save_account` | `bool` | Optional | Specifies to save account to contacts profile if account_number/track_data is present with either contact_id or contact_api_id in params. |
| `save_account_title` | `str` | Optional | If saving token while running a transaction, this will be the title of the token.<br><br>**Constraints**: *Maximum Length*: `16` |
| `subtotal_amount` | `int` | Optional | This field is allowed and required for transactions that have a product where surcharge is configured. Use only integer numbers, so $10.99 will be 1099.<br><br>**Constraints**: `>= 0`, `<= 999999999` |
| `surcharge_amount` | `int` | Optional | This field is allowed and required for transactions that have a product where surcharge is configured. Use only integer numbers, so $10.99 will be 1099.<br><br>**Constraints**: `>= 0`, `<= 999999999` |
| `tags` | `List[str]` | Optional | Tags |
| `tax` | `int` | Optional | Amount of Sales tax - If supplied, this amount should be included in the total transaction_amount field. Use only integer numbers, so $10.99 will be 1099.<br><br>**Constraints**: `>= 0`, `<= 999999999` |
| `tip_amount` | `int` | Optional | Optional tip amount. Tip is not supported for lodging and ecommerce merchants. Use only integer numbers, so $10.99 will be 1099.<br><br>**Constraints**: `>= 0`, `<= 999999999` |
| `transaction_amount` | `int` | Optional | Amount of the transaction. This should always be the desired settle amount of the transaction. Use only integer numbers, so $10.99 will be 1099.<br><br>**Constraints**: `>= 0`, `<= 999999999` |
| `secondary_amount` | `int` | Optional | Retained Amount of the transaction. This should always be less than transaction amount. Use only integer numbers, so $10.99 will be 1099<br><br>**Constraints**: `>= 0`, `<= 999999999` |
| `transaction_api_id` | `str` | Optional | See api_id page for more details<br><br>**Constraints**: *Maximum Length*: `64` |
| `transaction_c_1` | `str` | Optional | Custom field 1 for api users to store custom data<br><br>**Constraints**: *Maximum Length*: `128` |
| `transaction_c_2` | `str` | Optional | Custom field 2 for api users to store custom data<br><br>**Constraints**: *Maximum Length*: `128` |
| `transaction_c_3` | `str` | Optional | Custom field 3 for api users to store custom data<br><br>**Constraints**: *Maximum Length*: `128` |
| `bank_funded_only_override` | `bool` | Optional | Bank Funded Only Override |
| `allow_partial_authorization_override` | `bool` | Optional | Allow Partial Authorization Override |
| `auto_decline_cvv_override` | `bool` | Optional | Auto Decline CVV Override |
| `auto_decline_street_override` | `bool` | Optional | Auto Decline Street Override |
| `auto_decline_zip_override` | `bool` | Optional | Auto Decline Zip Override |
| `cardholder_present` | `bool` | Optional | If the cardholder is present at the point of service |
| `card_present` | `bool` | Optional | A POST only field to specify whether or not the card is present. |
| `secure_auth_data` | `str` | Optional | (ECOMM) The token authentication value associated with 3D secure transactions (Such as CAVV, UCAF auth data) |
| `secure_protocol_version` | `int` | Optional | (ECOMM)  Secure Program Protocol Version |
| `secure_collection_indicator` | `int` | Optional | (ECOMM) Used for UCAF collection indicator or Discover Autentication type |
| `secure_crytogram` | `str` | Optional | (ECOMM) Used to supply the Digital Payment Cryptogram obtained from a Digital Secure Remote Payment (DSRP) transaction |
| `secure_directory_server_transaction_id` | `str` | Optional | (ECOMM) Directory Server Transaction ID (Such as XID, TAVV) |
| `secure_ecomm_url` | `str` | Optional | (ECOMM) This field is used to enter a merchant identifier such as the Merchant URL or reverse domain name as presented to the consumer during the checkout process for a Digital Secure Remote payment transaction |
| `terminal_serial_number` | `str` | Optional | If transaction was processed using a terminal, this field would contain the terminal's serial number<br><br>**Constraints**: *Maximum Length*: `36`, *Pattern*: `^[a-zA-Z0-9]*$` |
| `threedsecure` | `bool` | Optional | Specifies to save account to contacts profile if account_number/track_data is present with either contact_id or contact_api_id in params. |
| `wallet_type` | [`WalletTypeEnum`](../../doc/models/wallet-type-enum.md) | Optional | This value provides information from where the transaction was initialized (Such as In-App provider)<br><br>> 000 - Unknown wallet type (i.e., Discover PayButton)<br>> <br>> 101 - MasterPass by MasterCard<br>> <br>> 103 - Apple Pay<br>> <br>> 216 - Google Pay<br>> <br>> 217 - Samsung Pay<br>> <br>> 327 - Merchant tokenization program |
| `previous_transaction_id` | `str` | Optional | previous_transaction_id is used as token to run transaction. Account details OR previous_transaction_id should be passed to run transaction.<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `previous_transaction_api_id` | `str` | Optional | previous_transaction_api_id is used as token to run transaction. Account details OR previous_transaction_api_id should be passed to run transaction.<br><br>**Constraints**: *Maximum Length*: `36` |
| `joi` | [`Joi24`](../../doc/models/joi-24.md) | Optional | - |
| `cvv` | `str` | Optional | Required for CC transactions if vt_require_cvv is true on producttransaction(Merchant Deposit Account).<br><br>**Constraints**: *Maximum Length*: `4` |
| `account_holder_name` | `str` | Optional | For CC, this is the 'Name (as it appears) on Card'. For ACH, this is the 'Name on Account'.<br><br>**Constraints**: *Maximum Length*: `32` |

## Example (as JSON)

```json
{
  "checkin_date": "2021-12-01",
  "checkout_date": "2021-12-01",
  "clerk_number": "AE1234",
  "contact_id": "11e95f8ec39de8fbdb0a4f1a",
  "custom_data": {
    "data1": "custom1",
    "data2": "custom2"
  },
  "customer_id": "customerid",
  "description": "some description",
  "iias_ind": 1,
  "image_front": "U29tZVN0cmluZ09idmlvdXNseU5vdEJhc2U2NEVuY29kZWQ=",
  "image_back": "U29tZVN0cmluZ09idmlvdXNseU5vdEJhc2U2NEVuY29kZWQ=",
  "installment": true,
  "installment_number": 1,
  "installment_count": 1,
  "location_api_id": "location-api-id-florida-2",
  "location_id": "11e95f8ec39de8fbdb0a4f1a",
  "product_transaction_id": "11e95f8ec39de8fbdb0a4f1a",
  "advance_deposit": false,
  "no_show": false,
  "notification_email_address": "johnsmith@smiths.com",
  "order_number": "433659378839",
  "po_number": "555555553123",
  "quick_invoice_id": "11e95f8ec39de8fbdb0a4f1a",
  "recurring": false,
  "recurring_number": 1,
  "room_num": "303",
  "room_rate": 95,
  "save_account": false,
  "save_account_title": "John Account",
  "subtotal_amount": 599,
  "surcharge_amount": 100,
  "tax": 0,
  "tip_amount": 0,
  "transaction_amount": 0,
  "secondary_amount": 0,
  "transaction_api_id": "transaction-payment-abcd123",
  "transaction_c1": "custom-data-1",
  "transaction_c2": "custom-data-2",
  "transaction_c3": "custom-data-3",
  "bank_funded_only_override": false,
  "allow_partial_authorization_override": false,
  "auto_decline_cvv_override": false,
  "auto_decline_street_override": false,
  "auto_decline_zip_override": false,
  "secure_auth_data": "vVwL7UNHCf8W8M2LAfvRChNHN7c%3D",
  "secure_protocol_version": 2,
  "secure_crytogram": "ZVVEVDJITHpTNE9yNlNHMUh0R0E=",
  "secure_directory_server_transaction_id": "d65e93c3-35ab-41ba-b307-767bfc19eae",
  "terminal_serial_number": "1234567890",
  "threedsecure": true,
  "previous_transaction_id": "11e95f8ec39de8fbdb0a4f1a",
  "account_holder_name": "smith",
  "additional_amounts": [
    {
      "type": "cashback",
      "amount": 6,
      "account_type": "cash_benefit",
      "currency": 154.64
    },
    {
      "type": "cashback",
      "amount": 6,
      "account_type": "cash_benefit",
      "currency": 154.64
    }
  ],
  "billing_address": {
    "postal_code": "postal_code0",
    "street": "street8",
    "city": "city2",
    "state": "state6",
    "phone": "phone2"
  }
}
```

