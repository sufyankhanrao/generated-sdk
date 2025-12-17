# Subscription Tokens

```python
subscription_tokens_controller = client.subscription_tokens
```

## Class Name

`SubscriptionTokensController`

## Methods

* [Get Subscription Tokens Id](../../doc/controllers/subscription-tokens.md#get-subscription-tokens-id)
* [Put Subscription Tokens Id](../../doc/controllers/subscription-tokens.md#put-subscription-tokens-id)
* [Delete Subscription Tokens Id](../../doc/controllers/subscription-tokens.md#delete-subscription-tokens-id)
* [Get Subscription Tokens](../../doc/controllers/subscription-tokens.md#get-subscription-tokens)
* [Post Subscription Tokens](../../doc/controllers/subscription-tokens.md#post-subscription-tokens)


# Get Subscription Tokens Id

Query a Subscription Token, which represents an association between a Subscription and a means of payment (Token) for that Subscription.

```python
def get_subscription_tokens_id(self,
                              id,
                              request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this subscription token. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SubscriptionTokensResponseResult`](../../doc/models/subscription-tokens-response-result.md).

## Example Usage

```python
id = 't1_stn_680064d2e16ab367d7dffz0'

request_token = '20250423-yourmerchant-refunds-001'

result = subscription_tokens_controller.get_subscription_tokens_id(
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
        "id": "t1_stn_680064d2e16ab367d7dffz0",
        "created": "2025-04-16 22:17:54.9444",
        "modified": "2025-04-16 22:17:54.9444",
        "creator": "t1_log_653ae6ec24a9357ace75ebf",
        "modifier": "t1_log_653ae6ec24a9357ace75ebf",
        "subscription": "t1_sbn_680064d2db9dbdc8d3e9a2b",
        "token": "95d4205826ef9e5e45891182220136ee",
        "inactive": 0,
        "frozen": 0
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


# Put Subscription Tokens Id

Update a Subscription Token, which represents an association between a Subscription and a means of payment (Token) for that Subscription.

```python
def put_subscription_tokens_id(self,
                              id,
                              body,
                              request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource or The Subscription Token ID. |
| `body` | [`SubscriptionTokensPutRequest`](../../doc/models/subscription-tokens-put-request.md) | Body, Required | Update Subscription Token Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SubscriptionTokensResponseResult`](../../doc/models/subscription-tokens-response-result.md).

## Example Usage

```python
id = 't1_stn_680064d2e16ab367d7dffz0'

body = SubscriptionTokensPutRequest(
    token='ae1abb3aaa18e4c374ca83fa75a7fff6',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = subscription_tokens_controller.put_subscription_tokens_id(
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
        "id": "t1_stn_680064d2e16ab367d7dffz0",
        "created": "2025-04-16 22:17:54.9444",
        "modified": "2025-04-16 22:17:54.9444",
        "creator": "t1_log_653ae6ec24a9357ace75ebf",
        "modifier": "t1_log_653ae6ec24a9357ace75ebf",
        "subscription": "t1_sbn_680064d2db9dbdc8d3e9a2b",
        "token": "95d4205826ef9e5e45891182220136ee",
        "inactive": 0,
        "frozen": 0
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


# Delete Subscription Tokens Id

Delete a Subscription Token, which represents an association between a Subscription and a means of payment (Token) for that Subscription.

```python
def delete_subscription_tokens_id(self,
                                 id,
                                 request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource or The Subscription Token ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SubscriptionTokensResponseResult`](../../doc/models/subscription-tokens-response-result.md).

## Example Usage

```python
id = 't1_stn_680064d2e16ab367d7dffz0'

request_token = '20250423-yourmerchant-refunds-001'

result = subscription_tokens_controller.delete_subscription_tokens_id(
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
        "id": "t1_stn_680064d2e16ab367d7dffz0",
        "created": "2025-04-16 22:17:54.9444",
        "modified": "2025-04-16 22:17:54.9444",
        "creator": "t1_log_653ae6ec24a9357ace75ebf",
        "modifier": "t1_log_653ae6ec24a9357ace75ebf",
        "subscription": "t1_sbn_680064d2db9dbdc8d3e9a2b",
        "token": "95d4205826ef9e5e45891182220136ee",
        "inactive": 0,
        "frozen": 0
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


# Get Subscription Tokens

Query a Subscription Tokens resource.
A Subscription Tokens resource represents an association between a Subscription and a means of payment (Token) for that Subscription.

```python
def get_subscription_tokens(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SubscriptionTokensResponseResult`](../../doc/models/subscription-tokens-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = subscription_tokens_controller.get_subscription_tokens(
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
        "id": "t1_stn_680064d2e16ab367d7dffz0",
        "created": "2025-04-16 22:17:54.9444",
        "modified": "2025-04-16 22:17:54.9444",
        "creator": "t1_log_653ae6ec24a9357ace75ebf",
        "modifier": "t1_log_653ae6ec24a9357ace75ebf",
        "subscription": "t1_sbn_680064d2db9dbdc8d3e9a2b",
        "token": "95d4205826ef9e5e45891182220136ee",
        "inactive": 0,
        "frozen": 0
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


# Post Subscription Tokens

Create a Subscription Tokens resource.
A Subscription Tokens resource represents an association between a Subscription and a means of payment (Token) for that Subscription.

```python
def post_subscription_tokens(self,
                            body,
                            request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SubscriptionTokensPostRequest`](../../doc/models/subscription-tokens-post-request.md) | Body, Required | Create Subscription Token Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SubscriptionTokensResponseResult`](../../doc/models/subscription-tokens-response-result.md).

## Example Usage

```python
body = SubscriptionTokensPostRequest(
    subscription='p1_sbn_5a1ef5e556583e67e5d55a2',
    token='e41272ec5464d9ec81cc85c854837472'
)

result = subscription_tokens_controller.post_subscription_tokens(body)

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
        "id": "t1_stn_680064d2e16ab367d7dffz0",
        "created": "2025-04-16 22:17:54.9444",
        "modified": "2025-04-16 22:17:54.9444",
        "creator": "t1_log_653ae6ec24a9357ace75ebf",
        "modifier": "t1_log_653ae6ec24a9357ace75ebf",
        "subscription": "t1_sbn_680064d2db9dbdc8d3e9a2b",
        "token": "95d4205826ef9e5e45891182220136ee",
        "inactive": 0,
        "frozen": 0
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

