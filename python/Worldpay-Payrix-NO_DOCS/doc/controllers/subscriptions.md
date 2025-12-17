# Subscriptions

Resources that deal with customer subscriptions to a plan. Customers are subscribed to plans to allow for recurring payments to be made from that customer.

```python
subscriptions_controller = client.subscriptions
```

## Class Name

`SubscriptionsController`

## Methods

* [Get Subscriptions Id](../../doc/controllers/subscriptions.md#get-subscriptions-id)
* [Put Subscriptions Id](../../doc/controllers/subscriptions.md#put-subscriptions-id)
* [Delete Subscriptions Id](../../doc/controllers/subscriptions.md#delete-subscriptions-id)
* [Get Subscriptions](../../doc/controllers/subscriptions.md#get-subscriptions)
* [Post Subscriptions](../../doc/controllers/subscriptions.md#post-subscriptions)


# Get Subscriptions Id

Query a Subscription that specifies both starting and ending dates and charges the customer according to the schedule in the associated Plan during the interval between these dates.

```python
def get_subscriptions_id(self,
                        id,
                        request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this subscription. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SubscriptionResponseResult`](../../doc/models/subscription-response-result.md).

## Example Usage

```python
id = 't1_sbn_680064d2db9dbdc8d3e9a0z'

request_token = '20250423-yourmerchant-refunds-001'

result = subscriptions_controller.get_subscriptions_id(
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
        "id": "t1_sbn_680064d2db9dbdc8d3e9a0z",
        "created": "2025-04-16 22:17:54.9157",
        "modified": "2025-04-16 22:17:57.0415",
        "creator": "t1_log_653ae6ec24a9357ace75ebf",
        "modifier": "t1_log_65e23f228adad41b7a2a0a9",
        "plan": "t1_pln_680064c9e9920768c5f7156",
        "start": 20250416,
        "finish": 20250416,
        "tax": 0,
        "descriptor": "",
        "inactive": 0,
        "frozen": 0,
        "failures": 0,
        "maxFailures": 0,
        "origin": 2,
        "firstTxn": "t1_txn_680064d333e8a4e6cc85903",
        "txnDescription": "subscription1",
        "order": "t183l8nsmsiq",
        "authentication": "",
        "authenticationId": "",
        "statementEntity": ""
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


# Put Subscriptions Id

Update a Subscription, A Subscription specifies both starting and ending dates and the customer is charged according to the schedule in the associated Plan during the interval between these dates.

```python
def put_subscriptions_id(self,
                        id,
                        body,
                        request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this subscription. |
| `body` | [`SubscriptionsPutRequest`](../../doc/models/subscriptions-put-request.md) | Body, Required | Update Subscription Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SubscriptionResponseResult`](../../doc/models/subscription-response-result.md).

## Example Usage

```python
id = 't1_sbn_680064d2db9dbdc8d3e9a0z'

body = SubscriptionsPutRequest(
    plan='t1_pln_680064c9e9920768c5f7156',
    statement_entity='paying entity',
    first_txn='t1_txn_680064d333e8a4e6cc85903',
    start=20250416,
    finish=20250416,
    tax=0,
    descriptor='Subscription Descriptor',
    txn_description='subscription1',
    order='t183l8nsmsiq',
    origin=SubscriptionOriginEnum.ECOMMERCE,
    authentication='Authentication token',
    authentication_id='Authentication reference ID',
    failures=0,
    max_failures=0,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = subscriptions_controller.put_subscriptions_id(
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
        "id": "t1_sbn_680064d2db9dbdc8d3e9a0z",
        "created": "2025-04-16 22:17:54.9157",
        "modified": "2025-04-16 22:17:57.0415",
        "creator": "t1_log_653ae6ec24a9357ace75ebf",
        "modifier": "t1_log_65e23f228adad41b7a2a0a9",
        "plan": "t1_pln_680064c9e9920768c5f7156",
        "start": 20250416,
        "finish": 20250416,
        "tax": 0,
        "descriptor": "",
        "inactive": 0,
        "frozen": 0,
        "failures": 0,
        "maxFailures": 0,
        "origin": 2,
        "firstTxn": "t1_txn_680064d333e8a4e6cc85903",
        "txnDescription": "subscription1",
        "order": "t183l8nsmsiq",
        "authentication": "",
        "authenticationId": "",
        "statementEntity": ""
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


# Delete Subscriptions Id

Delete a Subscription. A Subscription is a scheduled invocation of a particular Plan over a certain period of time, specifying both starting and ending dates, and the customer is charged according to the schedule in the associated Plan during the interval between these dates.

```python
def delete_subscriptions_id(self,
                           id,
                           request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this subscription. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SubscriptionResponseResult`](../../doc/models/subscription-response-result.md).

## Example Usage

```python
id = 't1_sbn_680064d2db9dbdc8d3e9a0z'

request_token = '20250423-yourmerchant-refunds-001'

result = subscriptions_controller.delete_subscriptions_id(
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
        "id": "t1_sbn_680064d2db9dbdc8d3e9a0z",
        "created": "2025-04-16 22:17:54.9157",
        "modified": "2025-04-16 22:17:57.0415",
        "creator": "t1_log_653ae6ec24a9357ace75ebf",
        "modifier": "t1_log_65e23f228adad41b7a2a0a9",
        "plan": "t1_pln_680064c9e9920768c5f7156",
        "start": 20250416,
        "finish": 20250416,
        "tax": 0,
        "descriptor": "",
        "inactive": 0,
        "frozen": 0,
        "failures": 0,
        "maxFailures": 0,
        "origin": 2,
        "firstTxn": "t1_txn_680064d333e8a4e6cc85903",
        "txnDescription": "subscription1",
        "order": "t183l8nsmsiq",
        "authentication": "",
        "authenticationId": "",
        "statementEntity": ""
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


# Get Subscriptions

Query a Subscription.
A Subscription is a scheduled invocation of a particular Plan over a certain period of time.
A Subscription specifies both starting and ending dates and the customer is charged according to the schedule in the associated Plan during the interval between these dates.

```python
def get_subscriptions(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SubscriptionResponseResult`](../../doc/models/subscription-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = subscriptions_controller.get_subscriptions(
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
        "id": "t1_sbn_680064d2db9dbdc8d3e9a0z",
        "created": "2025-04-16 22:17:54.9157",
        "modified": "2025-04-16 22:17:57.0415",
        "creator": "t1_log_653ae6ec24a9357ace75ebf",
        "modifier": "t1_log_65e23f228adad41b7a2a0a9",
        "plan": "t1_pln_680064c9e9920768c5f7156",
        "start": 20250416,
        "finish": 20250416,
        "tax": 0,
        "descriptor": "",
        "inactive": 0,
        "frozen": 0,
        "failures": 0,
        "maxFailures": 0,
        "origin": 2,
        "firstTxn": "t1_txn_680064d333e8a4e6cc85903",
        "txnDescription": "subscription1",
        "order": "t183l8nsmsiq",
        "authentication": "",
        "authenticationId": "",
        "statementEntity": ""
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


# Post Subscriptions

Create a Subscription.
A Subscription is a scheduled invocation of a particular Plan over a certain period of time.
A Subscription specifies both starting and ending dates and the customer is charged according to the schedule in the associated Plan during the interval between these dates.

```python
def post_subscriptions(self,
                      body,
                      request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SubscriptionsPostRequest`](../../doc/models/subscriptions-post-request.md) | Body, Required | Create Subscription Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SubscriptionResponseResult`](../../doc/models/subscription-response-result.md).

## Example Usage

```python
body = SubscriptionsPostRequest(
    plan='t1_pln_680064c9e9920768c5f7156',
    start=20250416,
    origin=SubscriptionOriginEnum.ECOMMERCE,
    authentication='Authentication token',
    failures=0,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    statement_entity='paying entity',
    first_txn='t1_txn_680064d333e8a4e6cc85903',
    finish=20250416,
    tax=0,
    descriptor='Subscription Descriptor',
    txn_description='subscription1',
    order='t183l8nsmsiq',
    authentication_id='Authentication reference ID',
    max_failures=0
)

request_token = '20250423-yourmerchant-refunds-001'

result = subscriptions_controller.post_subscriptions(
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
        "id": "t1_sbn_680064d2db9dbdc8d3e9a0z",
        "created": "2025-04-16 22:17:54.9157",
        "modified": "2025-04-16 22:17:57.0415",
        "creator": "t1_log_653ae6ec24a9357ace75ebf",
        "modifier": "t1_log_65e23f228adad41b7a2a0a9",
        "plan": "t1_pln_680064c9e9920768c5f7156",
        "start": 20250416,
        "finish": 20250416,
        "tax": 0,
        "descriptor": "",
        "inactive": 0,
        "frozen": 0,
        "failures": 0,
        "maxFailures": 0,
        "origin": 2,
        "firstTxn": "t1_txn_680064d333e8a4e6cc85903",
        "txnDescription": "subscription1",
        "order": "t183l8nsmsiq",
        "authentication": "",
        "authenticationId": "",
        "statementEntity": ""
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

