# Txn Sessions

```python
txn_sessions_controller = client.txn_sessions
```

## Class Name

`TxnSessionsController`

## Methods

* [Get Txn Sessions Id](../../doc/controllers/txn-sessions.md#get-txn-sessions-id)
* [Delete Txn Sessions Id](../../doc/controllers/txn-sessions.md#delete-txn-sessions-id)
* [Get Txn Sessions](../../doc/controllers/txn-sessions.md#get-txn-sessions)
* [Post Txn Sessions](../../doc/controllers/txn-sessions.md#post-txn-sessions)


# Get Txn Sessions Id

Query a TxnSession.
A TxnSession represents a temporary method of authentication to the API. Each TxnSession expires automatically after 10 minutes of inactivity or by the customizable configurations field.
They are similar to API Keys (/apikeys) in their capabilities and field structure - but unlike API Keys, TxnSessions are not permanent.

```python
def get_txn_sessions_id(self,
                       id,
                       request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TxnSessionsResponseResult`](../../doc/models/txn-sessions-response-result.md).

## Example Usage

```python
id = 't1_tss_67bc56867a5c6b8f7756d1z'

request_token = '20250423-yourmerchant-refunds-001'

result = txn_sessions_controller.get_txn_sessions_id(
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
        "id": "t1_tss_67bc56867a5c6b8f7756d1z",
        "created": "2025-02-24 06:22:46.5145",
        "modified": "2025-02-24 07:18:10.9777",
        "creator": "t1_log_65a6bb6506be50d9406eb00",
        "modifier": "t1_log_66cddf6fab39005772ca00z",
        "login": "t1_log_65a6bb6506be50d9406eb00",
        "merchant": "t1_mer_66312e43815957c6767000z",
        "status": "expired",
        "configurations": {
          "duration": 8,
          "maxTimesApproved": 2,
          "maxTimesUse": 4
        },
        "origin": "Apache-HttpClient/4.5.14 (Java/11.0.19)",
        "durationAvailable": 0,
        "timesUsed": 0,
        "timesApproved": 0,
        "key": "2a5694fb2455e82322e92b4e16c79a00"
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


# Delete Txn Sessions Id

Delete a TxnSession.
A TxnSession represents a temporary method of authentication to the API. Each TxnSession expires automatically after 10 minutes of inactivity or by the customizable configurations field.
They are similar to API Keys (/apikeys) in their capabilities and field structure - but unlike API Keys, TxnSessions are not permanent.

```python
def delete_txn_sessions_id(self,
                          id,
                          request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TxnSessionsResponseResult`](../../doc/models/txn-sessions-response-result.md).

## Example Usage

```python
id = 't1_tss_67bc56867a5c6b8f7756d1z'

request_token = '20250423-yourmerchant-refunds-001'

result = txn_sessions_controller.delete_txn_sessions_id(
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
        "id": "t1_tss_67bc56867a5c6b8f7756d1z",
        "created": "2025-02-24 06:22:46.5145",
        "modified": "2025-02-24 07:18:10.9777",
        "creator": "t1_log_65a6bb6506be50d9406eb00",
        "modifier": "t1_log_66cddf6fab39005772ca00z",
        "login": "t1_log_65a6bb6506be50d9406eb00",
        "merchant": "t1_mer_66312e43815957c6767000z",
        "status": "expired",
        "configurations": {
          "duration": 8,
          "maxTimesApproved": 2,
          "maxTimesUse": 4
        },
        "origin": "Apache-HttpClient/4.5.14 (Java/11.0.19)",
        "durationAvailable": 0,
        "timesUsed": 0,
        "timesApproved": 0,
        "key": "2a5694fb2455e82322e92b4e16c79a00"
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


# Get Txn Sessions

Query a TxnSession.
A TxnSession represents a temporary method of authentication to the API. Each TxnSession expires automatically after 10 minutes of inactivity or by the customizable configurations field.
They are similar to API Keys (/apikeys) in their capabilities and field structure - but unlike API Keys, TxnSessions are not permanent.

```python
def get_txn_sessions(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TxnSessionsResponseResult`](../../doc/models/txn-sessions-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = txn_sessions_controller.get_txn_sessions(
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
        "id": "t1_tss_67bc56867a5c6b8f7756d1z",
        "created": "2025-02-24 06:22:46.5145",
        "modified": "2025-02-24 07:18:10.9777",
        "creator": "t1_log_65a6bb6506be50d9406eb00",
        "modifier": "t1_log_66cddf6fab39005772ca00z",
        "login": "t1_log_65a6bb6506be50d9406eb00",
        "merchant": "t1_mer_66312e43815957c6767000z",
        "status": "expired",
        "configurations": {
          "duration": 8,
          "maxTimesApproved": 2,
          "maxTimesUse": 4
        },
        "origin": "Apache-HttpClient/4.5.14 (Java/11.0.19)",
        "durationAvailable": 0,
        "timesUsed": 0,
        "timesApproved": 0,
        "key": "2a5694fb2455e82322e92b4e16c79a00"
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


# Post Txn Sessions

Create a TxnSession.
A TxnSessions represents a temporary method of authentication to the API. Each TxnSession expires automatically after 10 minutes of inactivity or by the customizable configurations field.
They are similar to API Keys (/apikeys) in their capabilities and field structure - but unlike API Keys, TxnSessions are not permanent.

```python
def post_txn_sessions(self,
                     body,
                     request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TxnSessionsPostRequest`](../../doc/models/txn-sessions-post-request.md) | Body, Required | - |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TxnSessionsResponseResult`](../../doc/models/txn-sessions-response-result.md).

## Example Usage

```python
body = TxnSessionsPostRequest(
    login='t1_log_65a6bb6506be50d9406eb00',
    merchant='t1_mer_66312e43815957c6767000z',
    configurations=TxnSessionsConfigurations(
        duration=8,
        max_times_approved=2,
        max_times_use=4
    )
)

request_token = '20250423-yourmerchant-refunds-001'

result = txn_sessions_controller.post_txn_sessions(
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
        "id": "t1_tss_67bc56867a5c6b8f7756d1z",
        "created": "2025-02-24 06:22:46.5145",
        "modified": "2025-02-24 07:18:10.9777",
        "creator": "t1_log_65a6bb6506be50d9406eb00",
        "modifier": "t1_log_66cddf6fab39005772ca00z",
        "login": "t1_log_65a6bb6506be50d9406eb00",
        "merchant": "t1_mer_66312e43815957c6767000z",
        "status": "expired",
        "configurations": {
          "duration": 8,
          "maxTimesApproved": 2,
          "maxTimesUse": 4
        },
        "origin": "Apache-HttpClient/4.5.14 (Java/11.0.19)",
        "durationAvailable": 0,
        "timesUsed": 0,
        "timesApproved": 0,
        "key": "2a5694fb2455e82322e92b4e16c79a00"
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

