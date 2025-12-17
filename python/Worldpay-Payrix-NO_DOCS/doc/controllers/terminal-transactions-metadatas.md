# Terminal Transactions Metadatas

```python
terminal_transactions_metadatas_controller = client.terminal_transactions_metadatas
```

## Class Name

`TerminalTransactionsMetadatasController`

## Methods

* [Get Terminal Txns Metadatas Id](../../doc/controllers/terminal-transactions-metadatas.md#get-terminal-txns-metadatas-id)
* [Get Terminal Txns Metadatas](../../doc/controllers/terminal-transactions-metadatas.md#get-terminal-txns-metadatas)
* [Post Terminal Txns Metadatas](../../doc/controllers/terminal-transactions-metadatas.md#post-terminal-txns-metadatas)


# Get Terminal Txns Metadatas Id

Query a terminalTxnMetadatas resource.
A terminalTxnMetadatas resource represents data from an EMV Transaction and/or returned by the credit card network associated with a Transaction.

```python
def get_terminal_txns_metadatas_id(self,
                                  id,
                                  request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalTxnMetadatasResponseResult`](../../doc/models/terminal-txn-metadatas-response-result.md).

## Example Usage

```python
id = 't1_ttm_6806cde43c3480e154d7a0z'

request_token = '20250423-yourmerchant-refunds-001'

result = terminal_transactions_metadatas_controller.get_terminal_txns_metadatas_id(
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
        "id": "t1_ttm_6806cde43c3480e154d7a0z",
        "created": "2025-04-21 18:59:48.2547",
        "modified": "2025-04-21 18:59:48.2547",
        "creator": "t1_log_62fd0aa37c3d8ec3a9dcea8",
        "modifier": "t1_log_62fd0aa37c3d8ec3a9dcea8",
        "terminalTxn": "t1_ttx_6806cde42b47ee61cdf6ab9",
        "type": "discretionary",
        "field": "discretionary1",
        "value": "0421"
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


# Get Terminal Txns Metadatas

Query a terminalTxnMetadatas resource.
A terminalTxnMetadatas resource represents data from an EMV Transaction and/or returned by the credit card network associated with a Transaction.

```python
def get_terminal_txns_metadatas(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalTxnMetadatasResponseResult`](../../doc/models/terminal-txn-metadatas-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = terminal_transactions_metadatas_controller.get_terminal_txns_metadatas(
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
        "id": "t1_ttm_6806cde43c3480e154d7a0z",
        "created": "2025-04-21 18:59:48.2547",
        "modified": "2025-04-21 18:59:48.2547",
        "creator": "t1_log_62fd0aa37c3d8ec3a9dcea8",
        "modifier": "t1_log_62fd0aa37c3d8ec3a9dcea8",
        "terminalTxn": "t1_ttx_6806cde42b47ee61cdf6ab9",
        "type": "discretionary",
        "field": "discretionary1",
        "value": "0421"
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


# Post Terminal Txns Metadatas

Create a terminalTxnMetadatas resource. A terminalTxnMetadatas resource represents data from an EMV Transaction and/or returned by the credit card network associated with a Transaction.

```python
def post_terminal_txns_metadatas(self,
                                body,
                                request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TerminalTxnsMetadatasPostRequest`](../../doc/models/terminal-txns-metadatas-post-request.md) | Body, Required | Create Terminal Transaction Metadata Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalTxnMetadatasResponseResult`](../../doc/models/terminal-txn-metadatas-response-result.md).

## Example Usage

```python
body = TerminalTxnsMetadatasPostRequest(
    terminal_txn='t1_ttx_6806cde42b47ee61cdf6ab9',
    mtype=TerminalTxnMetadataTypeEnum.DISCRETIONARY,
    field=FieldEnum.DISCRETIONARY1,
    value='0421'
)

request_token = '20250423-yourmerchant-refunds-001'

result = terminal_transactions_metadatas_controller.post_terminal_txns_metadatas(
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
        "id": "t1_ttm_6806cde43c3480e154d7a0z",
        "created": "2025-04-21 18:59:48.2547",
        "modified": "2025-04-21 18:59:48.2547",
        "creator": "t1_log_62fd0aa37c3d8ec3a9dcea8",
        "modifier": "t1_log_62fd0aa37c3d8ec3a9dcea8",
        "terminalTxn": "t1_ttx_6806cde42b47ee61cdf6ab9",
        "type": "discretionary",
        "field": "discretionary1",
        "value": "0421"
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

