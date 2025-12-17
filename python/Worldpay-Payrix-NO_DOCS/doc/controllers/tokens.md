# Tokens

Tokens provide the means through which to safely and securely store payment methods (e.g. credit cards or bank accounts) for later use.

```python
tokens_controller = client.tokens
```

## Class Name

`TokensController`

## Methods

* [Get Tokens Id](../../doc/controllers/tokens.md#get-tokens-id)
* [Put Tokens Id](../../doc/controllers/tokens.md#put-tokens-id)
* [Delete Tokens Id](../../doc/controllers/tokens.md#delete-tokens-id)
* [Get Tokens](../../doc/controllers/tokens.md#get-tokens)
* [Post Tokens](../../doc/controllers/tokens.md#post-tokens)


# Get Tokens Id

Query a Token, which is a resource that acts as a storage place for credit card and customer information, allowing you to run Transactions.

```python
def get_tokens_id(self,
                 id,
                 request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this token. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TokensResponseResult`](../../doc/models/tokens-response-result.md).

## Example Usage

```python
id = 'p1_tok_00c82eb304b0067620c82be'

request_token = '20250423-yourmerchant-refunds-001'

result = tokens_controller.get_tokens_id(
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
        "id": "p1_tok_00c82eb304b0067620c82be",
        "created": "2025-03-05 06:00:03.0273",
        "modified": "2025-03-05 06:00:03.0273",
        "creator": "t1_log_00c82eb304b0067620c8",
        "modifier": "t1_log_00c82eb304b0067620c8",
        "customer": "t1_cus_00c82eb304b0067620c7",
        "payment": "p1_pmt_67c802b1b662567771cf8e0",
        "status": "pending",
        "token": "11c6a6d85f0a20c31e4c49e461066850",
        "omnitoken": "123",
        "track": "",
        "cvv": "",
        "expiration": "0123",
        "name": "test",
        "description": "test Token",
        "custom": "Custom Token Processor 1",
        "authTokenCustomer": "",
        "inactive": 0,
        "frozen": 0,
        "origin": "2",
        "entryMode": 2
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


# Put Tokens Id

Update a Token, which is a resource that acts as a storage place for credit card and customer information, allowing you to run Transactions.

```python
def put_tokens_id(self,
                 id,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this Token. |
| `body` | [`TokenPutRequest`](../../doc/models/token-put-request.md) | Body, Required | Update Token Request |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TokensResponseResult`](../../doc/models/tokens-response-result.md).

## Example Usage

```python
id = 'p1_tok_00c82eb304b0067620c82be'

body = TokenPutRequest(
    customer='t1_cus_00c82eb304b0067620c7',
    payment=TokenPaymentParam(
        method=MethodEnum.AMEX,
        number='378734493671000',
        routing='code'
    ),
    status=TokenStatusEnum.PENDING,
    token='11c6a6d85f0a20c31e4c49e461066850',
    expiration='0123',
    name='test1',
    description='test Token',
    custom='Custom Token Processor 1',
    auth_token_customer='authToken',
    origin=2,
    entry_mode=2,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

result = tokens_controller.put_tokens_id(
    id,
    body
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
        "id": "p1_tok_00c82eb304b0067620c82be",
        "created": "2025-03-05 06:00:03.0273",
        "modified": "2025-03-05 06:00:03.0273",
        "creator": "t1_log_00c82eb304b0067620c8",
        "modifier": "t1_log_00c82eb304b0067620c8",
        "customer": "t1_cus_00c82eb304b0067620c7",
        "payment": "p1_pmt_67c802b1b662567771cf8e0",
        "status": "pending",
        "token": "11c6a6d85f0a20c31e4c49e461066850",
        "omnitoken": "123",
        "track": "",
        "cvv": "",
        "expiration": "0123",
        "name": "test",
        "description": "test Token",
        "custom": "Custom Token Processor 1",
        "authTokenCustomer": "",
        "inactive": 0,
        "frozen": 0,
        "origin": "2",
        "entryMode": 2
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


# Delete Tokens Id

Delete a Token, which is a resource that acts as a storage place for credit card and customer information, allowing you to run Transactions.

```python
def delete_tokens_id(self,
                    id,
                    request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this token. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TokensResponseResult`](../../doc/models/tokens-response-result.md).

## Example Usage

```python
id = 'p1_tok_00c82eb304b0067620c82be'

request_token = '20250423-yourmerchant-refunds-001'

result = tokens_controller.delete_tokens_id(
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
        "id": "p1_tok_00c82eb304b0067620c82be",
        "created": "2025-03-05 06:00:03.0273",
        "modified": "2025-03-05 06:00:03.0273",
        "creator": "t1_log_00c82eb304b0067620c8",
        "modifier": "t1_log_00c82eb304b0067620c8",
        "customer": "t1_cus_00c82eb304b0067620c7",
        "payment": "p1_pmt_67c802b1b662567771cf8e0",
        "status": "pending",
        "token": "11c6a6d85f0a20c31e4c49e461066850",
        "omnitoken": "123",
        "track": "",
        "cvv": "",
        "expiration": "0123",
        "name": "test",
        "description": "test Token",
        "custom": "Custom Token Processor 1",
        "authTokenCustomer": "",
        "inactive": 0,
        "frozen": 0,
        "origin": "2",
        "entryMode": 2
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


# Get Tokens

Query a Token. A Token is a resource that acts as a storage place for credit card and customer information. You can use a Token to run Transactions.

```python
def get_tokens(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TokensResponseResult`](../../doc/models/tokens-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = tokens_controller.get_tokens(
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
        "id": "p1_tok_00c82eb304b0067620c82be",
        "created": "2025-03-05 06:00:03.0273",
        "modified": "2025-03-05 06:00:03.0273",
        "creator": "t1_log_00c82eb304b0067620c8",
        "modifier": "t1_log_00c82eb304b0067620c8",
        "customer": "t1_cus_00c82eb304b0067620c7",
        "payment": "p1_pmt_67c802b1b662567771cf8e0",
        "status": "pending",
        "token": "11c6a6d85f0a20c31e4c49e461066850",
        "omnitoken": "123",
        "track": "",
        "cvv": "",
        "expiration": "0123",
        "name": "test",
        "description": "test Token",
        "custom": "Custom Token Processor 1",
        "authTokenCustomer": "",
        "inactive": 0,
        "frozen": 0,
        "origin": "2",
        "entryMode": 2
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


# Post Tokens

Create a Token. A Token is a resource that acts as a storage place for credit card and customer information. You can use a Token to run Transactions.

```python
def post_tokens(self,
               body,
               request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TokenPostRequest`](../../doc/models/token-post-request.md) | Body, Required | Create Token Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TokensResponseResult`](../../doc/models/tokens-response-result.md).

## Example Usage

```python
body = TokenPostRequest(
    customer='t1_cus_00c82eb304b0067620c7',
    payment=TokenPaymentParam(
        method=MethodEnum.AMEX,
        number='378734493671000',
        routing='code'
    ),
    status=TokenStatusEnum.PENDING,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    expiration='0123',
    name='test',
    description='test Token',
    custom='Custom Token Processor 2',
    auth_token_customer='authToken',
    origin=2,
    entry_mode=2,
    omnitoken='123'
)

request_token = '20250423-yourmerchant-refunds-001'

result = tokens_controller.post_tokens(
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
        "id": "p1_tok_00c82eb304b0067620c82be",
        "created": "2025-03-05 06:00:03.0273",
        "modified": "2025-03-05 06:00:03.0273",
        "creator": "t1_log_00c82eb304b0067620c8",
        "modifier": "t1_log_00c82eb304b0067620c8",
        "customer": "t1_cus_00c82eb304b0067620c7",
        "payment": "p1_pmt_67c802b1b662567771cf8e0",
        "status": "pending",
        "token": "11c6a6d85f0a20c31e4c49e461066850",
        "omnitoken": "123",
        "track": "",
        "cvv": "",
        "expiration": "0123",
        "name": "test",
        "description": "test Token",
        "custom": "Custom Token Processor 1",
        "authTokenCustomer": "",
        "inactive": 0,
        "frozen": 0,
        "origin": "2",
        "entryMode": 2
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

