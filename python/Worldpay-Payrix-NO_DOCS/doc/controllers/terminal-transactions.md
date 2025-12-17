# Terminal Transactions

```python
terminal_transactions_controller = client.terminal_transactions
```

## Class Name

`TerminalTransactionsController`

## Methods

* [Get Terminal Txns by Id](../../doc/controllers/terminal-transactions.md#get-terminal-txns-by-id)
* [Update Terminal Txns by Id](../../doc/controllers/terminal-transactions.md#update-terminal-txns-by-id)
* [Delete Terminal Txns by Id](../../doc/controllers/terminal-transactions.md#delete-terminal-txns-by-id)
* [Get Terminal Txns](../../doc/controllers/terminal-transactions.md#get-terminal-txns)
* [Post Terminal Txns](../../doc/controllers/terminal-transactions.md#post-terminal-txns)


# Get Terminal Txns by Id

Query a TerminalTxn holds all of the information to a related final transaction, which they are used to be reconciled with that actual, final transaction.

```python
def get_terminal_txns_by_id(self,
                           id,
                           request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Terminal Transaction ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalTxnsResponseResult`](../../doc/models/terminal-txns-response-result.md).

## Example Usage

```python
id = 't1_ttx_67c76e07ebc6fbbbd476ee0'

request_token = '20250423-yourmerchant-refunds-001'

result = terminal_transactions_controller.get_terminal_txns_by_id(
    id,
    request_token=request_token
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "response": {
    "data": [
      {
        "id": "t1_ttx_67c76e07ebc6fbbbd476ee0",
        "created": "2025-03-04 14:40:26.0000",
        "modified": "2025-03-04 16:17:59.9960",
        "creator": "t1_log_62fd0aa37c3d8ec3a9dcea0",
        "modifier": "t1_log_62fd0aa37c3d8ec3a9dcea0",
        "ipCreated": "3.90.49.108",
        "ipModified": "3.90.49.108",
        "merchant": "t1_mer_64415e89a919c1566a2b49b",
        "mid": "4445061378323",
        "txn": "",
        "type": 4,
        "expiration": "0623",
        "currency": "CAD",
        "fundingCurrency": "CAD",
        "fee": 0,
        "platform": "VCORE",
        "authDate": 20160120,
        "authCode": "",
        "order": "",
        "description": "",
        "traceNumber": 853202,
        "discount": 0,
        "shipping": 0,
        "duty": 0,
        "terminal": "",
        "terminalCapability": 1,
        "entryMode": 1,
        "origin": 1,
        "tax": 0,
        "total": 8000,
        "cashback": 0,
        "authorization": "422301",
        "approved": 8000,
        "cvv": 0,
        "cvvStatus": "notPresent",
        "swiped": 0,
        "emv": 0,
        "signature": 0,
        "pin": 0,
        "unattended": 0,
        "pos": 0,
        "receipt": "noReceipt",
        "clientIp": "",
        "first": "",
        "middle": "",
        "last": "",
        "company": "",
        "email": "",
        "address1": "",
        "address2": "",
        "city": "",
        "state": "AB",
        "zip": "",
        "country": "CAN",
        "phone": "",
        "status": 1,
        "reserved": 0,
        "checkStage": "",
        "inactive": 0,
        "frozen": 0,
        "tid": "",
        "forterminalTxn": "",
        "token": "124f2d0efab0bcda46f2118d688bbf97",
        "binType": "CREDIT",
        "tip": 0,
        "paymentNumber": 7,
        "paymentMethod": 2,
        "originatingApp": "",
        "OEMTTxnRefNumber": "",
        "posApplicationId": "15668",
        "posApplicationName": "XML Test Example",
        "posApplicationVersion": "1.00",
        "customerReferenceNumber": "123456",
        "gatewayTransactionId": "486689252",
        "customerTicketNumber": "123456",
        "cardNetworkTransactionId": "250630144026744",
        "omnitoken": "4445223322990007",
        "convenienceFee": 0,
        "surcharge": 0,
        "softPosDeviceTypeIndicator": "",
        "terminalClassificationCode": "",
        "softPosId": "",
        "hsaFsaCardIndicator": 0,
        "gatewayTerminalId": "11",
        "descriptor": "",
        "cardNetworkBankNetReferenceNumber": "",
        "cardNetworkBankNetSettlementDate": "1123"
      }
    ],
    "details": {
      "requestId": "1",
      "totals": [],
      "page": {
        "current": 1,
        "last": 1,
        "hasMore": false
      }
    },
    "errors": []
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ErrorFourHundredException`](../../doc/models/error-four-hundred-exception.md) |


# Update Terminal Txns by Id

Update a TerminalTxn holds all of the information to a related final transaction and is used to be reconciled with that actual, final transaction.

```python
def update_terminal_txns_by_id(self,
                              id,
                              body,
                              request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Terminal Transaction ID. |
| `body` | [`TerminalTxnsPutRequest`](../../doc/models/terminal-txns-put-request.md) | Body, Required | Update Terminal Transaction Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalTxnsResponseResult`](../../doc/models/terminal-txns-response-result.md).

## Example Usage

```python
id = 't1_ttx_67c76e07ebc6fbbbd476ee0'

body = TerminalTxnsPutRequest(
    bin_type=BinTypeEnum.DEBIT,
    expiration='1123',
    payment=TerminalTxnsPayment(
        method=TerminalTxnPaymentMethodEnum.AMEX,
        number='2222',
        routing='1',
        expiration='0623',
        cvv=123,
        track='Track 1'
    ),
    trace_number=853202,
    txn='related txn',
    token='124f2d0efab0bcda46f2118d688bbf97',
    payment_number=7,
    payment_method=TerminalTxnPaymentMethodEnum.VISA,
    tip=0,
    originating_app='originatingApp',
    oemt_txn_ref_number='TxnRefNumber',
    pos_application_id='15668',
    unattended=UnattendedEnum.ATTENDEDTERMINAL,
    pos_application_name='XML Test Example',
    pos_application_version='1.00',
    customer_reference_number='123456',
    gateway_transaction_id='486689252',
    customer_ticket_number='123456',
    client_ip='Client IP address',
    description='Transaction1',
    swiped=SwipedEnum.SWIPED,
    emv=EmvEnum.DIPPED,
    entry_mode=EntryModeEnum.KEYED,
    first='John',
    last='Doe',
    middle='M',
    order='orderId',
    reserved=Reserved1Enum.ENUM_NONE,
    signature=SignatureEnum.CAPTURED,
    total=8000,
    status=TerminalTxnStatusEnum.CAPTURED,
    card_network_transaction_id='250630144026744',
    omnitoken='4445223322990007',
    convenience_fee=0,
    surcharge=0,
    soft_pos_device_type_indicator='device type indicator',
    soft_pos_id='software POS ID',
    hsa_fsa_card_indicator=HsaFsaCardIndicatorEnum.NOTHSAFSA,
    gateway_terminal_id='12',
    descriptor='billing Descriptor',
    card_network_bank_net_reference_number='cardNetworkBankNetReferenceNumber',
    card_network_bank_net_settlement_date='1123',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = terminal_transactions_controller.update_terminal_txns_by_id(
    id,
    body,
    request_token=request_token
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "response": {
    "data": [
      {
        "id": "t1_ttx_67c76e07ebc6fbbbd476ee0",
        "created": "2025-03-04 14:40:26.0000",
        "modified": "2025-03-04 16:17:59.9960",
        "creator": "t1_log_62fd0aa37c3d8ec3a9dcea0",
        "modifier": "t1_log_62fd0aa37c3d8ec3a9dcea0",
        "ipCreated": "3.90.49.108",
        "ipModified": "3.90.49.108",
        "merchant": "t1_mer_64415e89a919c1566a2b49b",
        "mid": "4445061378323",
        "txn": "",
        "type": 4,
        "expiration": "0623",
        "currency": "CAD",
        "fundingCurrency": "CAD",
        "fee": 0,
        "platform": "VCORE",
        "authDate": 20160120,
        "authCode": "",
        "order": "",
        "description": "",
        "traceNumber": 853202,
        "discount": 0,
        "shipping": 0,
        "duty": 0,
        "terminal": "",
        "terminalCapability": 1,
        "entryMode": 1,
        "origin": 1,
        "tax": 0,
        "total": 8000,
        "cashback": 0,
        "authorization": "422301",
        "approved": 8000,
        "cvv": 0,
        "cvvStatus": "notPresent",
        "swiped": 0,
        "emv": 0,
        "signature": 0,
        "pin": 0,
        "unattended": 0,
        "pos": 0,
        "receipt": "noReceipt",
        "clientIp": "",
        "first": "",
        "middle": "",
        "last": "",
        "company": "",
        "email": "",
        "address1": "",
        "address2": "",
        "city": "",
        "state": "AB",
        "zip": "",
        "country": "CAN",
        "phone": "",
        "status": 1,
        "reserved": 0,
        "checkStage": "",
        "inactive": 0,
        "frozen": 0,
        "tid": "",
        "forterminalTxn": "",
        "token": "124f2d0efab0bcda46f2118d688bbf97",
        "binType": "CREDIT",
        "tip": 0,
        "paymentNumber": 7,
        "paymentMethod": 2,
        "originatingApp": "",
        "OEMTTxnRefNumber": "",
        "posApplicationId": "15668",
        "posApplicationName": "XML Test Example",
        "posApplicationVersion": "1.00",
        "customerReferenceNumber": "123456",
        "gatewayTransactionId": "486689252",
        "customerTicketNumber": "123456",
        "cardNetworkTransactionId": "250630144026744",
        "omnitoken": "4445223322990007",
        "convenienceFee": 0,
        "surcharge": 0,
        "softPosDeviceTypeIndicator": "",
        "terminalClassificationCode": "",
        "softPosId": "",
        "hsaFsaCardIndicator": 0,
        "gatewayTerminalId": "11",
        "descriptor": "",
        "cardNetworkBankNetReferenceNumber": "",
        "cardNetworkBankNetSettlementDate": "1123"
      }
    ],
    "details": {
      "requestId": "1",
      "totals": [],
      "page": {
        "current": 1,
        "last": 1,
        "hasMore": false
      }
    },
    "errors": []
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ErrorFourHundredException`](../../doc/models/error-four-hundred-exception.md) |


# Delete Terminal Txns by Id

Delete a TerminalTxn that holds all of the information to a related final transaction and is used to be reconciled with that actual, final transaction.

```python
def delete_terminal_txns_by_id(self,
                              id,
                              request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Terminal Transaction ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalTxnsResponseResult`](../../doc/models/terminal-txns-response-result.md).

## Example Usage

```python
id = 't1_ttx_67c76e07ebc6fbbbd476ee0'

request_token = '20250423-yourmerchant-refunds-001'

result = terminal_transactions_controller.delete_terminal_txns_by_id(
    id,
    request_token=request_token
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "response": {
    "data": [
      {
        "id": "t1_ttx_67c76e07ebc6fbbbd476ee0",
        "created": "2025-03-04 14:40:26.0000",
        "modified": "2025-03-04 16:17:59.9960",
        "creator": "t1_log_62fd0aa37c3d8ec3a9dcea0",
        "modifier": "t1_log_62fd0aa37c3d8ec3a9dcea0",
        "ipCreated": "3.90.49.108",
        "ipModified": "3.90.49.108",
        "merchant": "t1_mer_64415e89a919c1566a2b49b",
        "mid": "4445061378323",
        "txn": "",
        "type": 4,
        "expiration": "0623",
        "currency": "CAD",
        "fundingCurrency": "CAD",
        "fee": 0,
        "platform": "VCORE",
        "authDate": 20160120,
        "authCode": "",
        "order": "",
        "description": "",
        "traceNumber": 853202,
        "discount": 0,
        "shipping": 0,
        "duty": 0,
        "terminal": "",
        "terminalCapability": 1,
        "entryMode": 1,
        "origin": 1,
        "tax": 0,
        "total": 8000,
        "cashback": 0,
        "authorization": "422301",
        "approved": 8000,
        "cvv": 0,
        "cvvStatus": "notPresent",
        "swiped": 0,
        "emv": 0,
        "signature": 0,
        "pin": 0,
        "unattended": 0,
        "pos": 0,
        "receipt": "noReceipt",
        "clientIp": "",
        "first": "",
        "middle": "",
        "last": "",
        "company": "",
        "email": "",
        "address1": "",
        "address2": "",
        "city": "",
        "state": "AB",
        "zip": "",
        "country": "CAN",
        "phone": "",
        "status": 1,
        "reserved": 0,
        "checkStage": "",
        "inactive": 0,
        "frozen": 0,
        "tid": "",
        "forterminalTxn": "",
        "token": "124f2d0efab0bcda46f2118d688bbf97",
        "binType": "CREDIT",
        "tip": 0,
        "paymentNumber": 7,
        "paymentMethod": 2,
        "originatingApp": "",
        "OEMTTxnRefNumber": "",
        "posApplicationId": "15668",
        "posApplicationName": "XML Test Example",
        "posApplicationVersion": "1.00",
        "customerReferenceNumber": "123456",
        "gatewayTransactionId": "486689252",
        "customerTicketNumber": "123456",
        "cardNetworkTransactionId": "250630144026744",
        "omnitoken": "4445223322990007",
        "convenienceFee": 0,
        "surcharge": 0,
        "softPosDeviceTypeIndicator": "",
        "terminalClassificationCode": "",
        "softPosId": "",
        "hsaFsaCardIndicator": 0,
        "gatewayTerminalId": "11",
        "descriptor": "",
        "cardNetworkBankNetReferenceNumber": "",
        "cardNetworkBankNetSettlementDate": "1123"
      }
    ],
    "details": {
      "requestId": "1",
      "totals": [],
      "page": {
        "current": 1,
        "last": 1,
        "hasMore": false
      }
    },
    "errors": []
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ErrorFourHundredException`](../../doc/models/error-four-hundred-exception.md) |


# Get Terminal Txns

Query a TerminalTxn, which holds all of the information to a related final transaction and is used to reconcile with the actual, final transaction.

```python
def get_terminal_txns(self,
                     request_token=None,
                     search=None,
                     totals=None,
                     page_number=None,
                     page_limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |
| `search` | `str` | Header, Optional | Set this header to filter or sort the list of resources that the method returns.<br>See [Searches](page:welcome#searches) for detailed information and examples on how to use search header. |
| `totals` | `str` | Header, Optional | To configure a request to return a total for all instances of a field in a result set,  use the totals header in the format `totals={operator}[]={key}`.  This will calculate the desired total and return it in the `details > totals` object of the response.  For instance, if you want to sum the `total` field of all transactions,  you would use the `sum` operator. The response will include the result set,  along with the calculated total in the `details` section. See [Collection Operators](page:welcome#collection-operators) for detailed information and examples on how to use totals header. |
| `page_number` | `int` | Query, Optional | Set this path parameter to request a specific page of records.<br>For example, set `?page[number]=2` to retrieve the second page of records for this request. |
| `page_limit` | `int` | Query, Optional | Set this path parameter to request up to a specific amount of records. By default 30 records are retrieved per page. The maximum limit that can be set is 100.<br>For example, set `?page[limit]=50` to retrieve up to 50 records for this request. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalTxnsResponseResult`](../../doc/models/terminal-txns-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = terminal_transactions_controller.get_terminal_txns(
    request_token=request_token,
    search=search,
    totals=totals,
    page_number=page_number,
    page_limit=page_limit
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "response": {
    "data": [
      {
        "id": "t1_ttx_67c76e07ebc6fbbbd476ee0",
        "created": "2025-03-04 14:40:26.0000",
        "modified": "2025-03-04 16:17:59.9960",
        "creator": "t1_log_62fd0aa37c3d8ec3a9dcea0",
        "modifier": "t1_log_62fd0aa37c3d8ec3a9dcea0",
        "ipCreated": "3.90.49.108",
        "ipModified": "3.90.49.108",
        "merchant": "t1_mer_64415e89a919c1566a2b49b",
        "mid": "4445061378323",
        "txn": "",
        "type": 4,
        "expiration": "0623",
        "currency": "CAD",
        "fundingCurrency": "CAD",
        "fee": 0,
        "platform": "VCORE",
        "authDate": 20160120,
        "authCode": "",
        "order": "",
        "description": "",
        "traceNumber": 853202,
        "discount": 0,
        "shipping": 0,
        "duty": 0,
        "terminal": "",
        "terminalCapability": 1,
        "entryMode": 1,
        "origin": 1,
        "tax": 0,
        "total": 8000,
        "cashback": 0,
        "authorization": "422301",
        "approved": 8000,
        "cvv": 0,
        "cvvStatus": "notPresent",
        "swiped": 0,
        "emv": 0,
        "signature": 0,
        "pin": 0,
        "unattended": 0,
        "pos": 0,
        "receipt": "noReceipt",
        "clientIp": "",
        "first": "",
        "middle": "",
        "last": "",
        "company": "",
        "email": "",
        "address1": "",
        "address2": "",
        "city": "",
        "state": "AB",
        "zip": "",
        "country": "CAN",
        "phone": "",
        "status": 1,
        "reserved": 0,
        "checkStage": "",
        "inactive": 0,
        "frozen": 0,
        "tid": "",
        "forterminalTxn": "",
        "token": "124f2d0efab0bcda46f2118d688bbf97",
        "binType": "CREDIT",
        "tip": 0,
        "paymentNumber": 7,
        "paymentMethod": 2,
        "originatingApp": "",
        "OEMTTxnRefNumber": "",
        "posApplicationId": "15668",
        "posApplicationName": "XML Test Example",
        "posApplicationVersion": "1.00",
        "customerReferenceNumber": "123456",
        "gatewayTransactionId": "486689252",
        "customerTicketNumber": "123456",
        "cardNetworkTransactionId": "250630144026744",
        "omnitoken": "4445223322990007",
        "convenienceFee": 0,
        "surcharge": 0,
        "softPosDeviceTypeIndicator": "",
        "terminalClassificationCode": "",
        "softPosId": "",
        "hsaFsaCardIndicator": 0,
        "gatewayTerminalId": "11",
        "descriptor": "",
        "cardNetworkBankNetReferenceNumber": "",
        "cardNetworkBankNetSettlementDate": "1123"
      }
    ],
    "details": {
      "requestId": "1",
      "totals": [],
      "page": {
        "current": 1,
        "last": 1,
        "hasMore": false
      }
    },
    "errors": []
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ErrorFourHundredException`](../../doc/models/error-four-hundred-exception.md) |


# Post Terminal Txns

Create a TerminalTxn.
TerminalTxns hold all of the information to a related final transaction. They are used to be reconcilliated with that actual, final transaction.

```python
def post_terminal_txns(self,
                      body,
                      request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TerminalTxnsPostRequest`](../../doc/models/terminal-txns-post-request.md) | Body, Required | Create Terminal Transaction Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalTxnsResponseResult`](../../doc/models/terminal-txns-response-result.md).

## Example Usage

```python
body = TerminalTxnsPostRequest(
    bin_type=BinTypeEnum.DEBIT,
    origin=TerminalTxnOriginEnum.TERMINAL,
    pos=PosEnum.POSACTIVATION,
    mtype=TerminalTxnTypeEnum.SALE,
    currency=CurrencyEnum.USD,
    funding_currency=FundingCurrencyEnum.USD,
    swiped=SwipedEnum.SWIPED,
    merchant='t1_mer_64415e89a919c1566a2b49b',
    mid='4445061378323',
    pin=PinEnum.NOPIN,
    reserved=0,
    signature=SignatureEnum.NOTCAPTURED,
    total=8000,
    status=TerminalTxnStatusEnum.APPROVED,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    expiration='1023',
    forterminal_txn='forterminalTxn',
    payment=TerminalTxnsPayment(
        method=TerminalTxnPaymentMethodEnum.AMEX,
        number='1234',
        routing='123456789',
        expiration='1023',
        cvv=123,
        track='Track1'
    ),
    platform=Platform1Enum.VCORE,
    receipt=ReceiptEnum.NORECEIPT,
    tid='Terminal ID',
    trace_number=853202,
    txn='related txn',
    token='124f2d0efab0bcda46f2118d688bbf97',
    payment_number=7,
    payment_method=TerminalTxnPaymentMethodEnum.VISA,
    tip=0,
    originating_app='originatingApp',
    oemt_txn_ref_number='TxnRefNumber',
    pos_application_id='15668',
    pos_application_name='XML Test Example',
    pos_application_version='1.00',
    customer_reference_number='123456',
    gateway_transaction_id='486689252',
    customer_ticket_number='123456',
    auth_code='authorization code',
    auth_date=20160120,
    cashback=0,
    client_ip='Client IP address',
    company='company1',
    cvv_status=CvvStatusEnum.NOTPRESENT,
    description='description1',
    discount=0,
    duty=0,
    email='john.johnson@example.com',
    entry_mode=EntryModeEnum.KEYED,
    fee=0,
    first='John',
    last='Doe',
    middle='M',
    order='orderId',
    shipping=0,
    tax=0,
    terminal='identifier of terminal',
    terminal_capability=TerminalCapabilityEnum.KEYED,
    unattended=UnattendedEnum.ATTENDEDTERMINAL,
    address_1='address1',
    address_2='address2',
    city='city1',
    state='AB',
    zip='ZIP code',
    country=CountryEnum.CAN,
    phone='9999888888'
)

request_token = '20250423-yourmerchant-refunds-001'

result = terminal_transactions_controller.post_terminal_txns(
    body,
    request_token=request_token
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "response": {
    "data": [
      {
        "id": "t1_ttx_67c76e07ebc6fbbbd476ee0",
        "created": "2025-03-04 14:40:26.0000",
        "modified": "2025-03-04 16:17:59.9960",
        "creator": "t1_log_62fd0aa37c3d8ec3a9dcea0",
        "modifier": "t1_log_62fd0aa37c3d8ec3a9dcea0",
        "ipCreated": "3.90.49.108",
        "ipModified": "3.90.49.108",
        "merchant": "t1_mer_64415e89a919c1566a2b49b",
        "mid": "4445061378323",
        "txn": "",
        "type": 4,
        "expiration": "0623",
        "currency": "CAD",
        "fundingCurrency": "CAD",
        "fee": 0,
        "platform": "VCORE",
        "authDate": 20160120,
        "authCode": "",
        "order": "",
        "description": "",
        "traceNumber": 853202,
        "discount": 0,
        "shipping": 0,
        "duty": 0,
        "terminal": "",
        "terminalCapability": 1,
        "entryMode": 1,
        "origin": 1,
        "tax": 0,
        "total": 8000,
        "cashback": 0,
        "authorization": "422301",
        "approved": 8000,
        "cvv": 0,
        "cvvStatus": "notPresent",
        "swiped": 0,
        "emv": 0,
        "signature": 0,
        "pin": 0,
        "unattended": 0,
        "pos": 0,
        "receipt": "noReceipt",
        "clientIp": "",
        "first": "",
        "middle": "",
        "last": "",
        "company": "",
        "email": "",
        "address1": "",
        "address2": "",
        "city": "",
        "state": "AB",
        "zip": "",
        "country": "CAN",
        "phone": "",
        "status": 1,
        "reserved": 0,
        "checkStage": "",
        "inactive": 0,
        "frozen": 0,
        "tid": "",
        "forterminalTxn": "",
        "token": "124f2d0efab0bcda46f2118d688bbf97",
        "binType": "CREDIT",
        "tip": 0,
        "paymentNumber": 7,
        "paymentMethod": 2,
        "originatingApp": "",
        "OEMTTxnRefNumber": "",
        "posApplicationId": "15668",
        "posApplicationName": "XML Test Example",
        "posApplicationVersion": "1.00",
        "customerReferenceNumber": "123456",
        "gatewayTransactionId": "486689252",
        "customerTicketNumber": "123456",
        "cardNetworkTransactionId": "250630144026744",
        "omnitoken": "4445223322990007",
        "convenienceFee": 0,
        "surcharge": 0,
        "softPosDeviceTypeIndicator": "",
        "terminalClassificationCode": "",
        "softPosId": "",
        "hsaFsaCardIndicator": 0,
        "gatewayTerminalId": "11",
        "descriptor": "",
        "cardNetworkBankNetReferenceNumber": "",
        "cardNetworkBankNetSettlementDate": "1123"
      }
    ],
    "details": {
      "requestId": "1",
      "totals": [],
      "page": {
        "current": 1,
        "last": 1,
        "hasMore": false
      }
    },
    "errors": []
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ErrorFourHundredException`](../../doc/models/error-four-hundred-exception.md) |

