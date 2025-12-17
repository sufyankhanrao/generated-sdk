# API Keys

```python
api_keys_controller = client.api_keys
```

## Class Name

`APIKeysController`

## Methods

* [Get Apikeys Id](../../doc/controllers/api-keys.md#get-apikeys-id)
* [Put Apikeys Id](../../doc/controllers/api-keys.md#put-apikeys-id)
* [Delete Apikeys Id](../../doc/controllers/api-keys.md#delete-apikeys-id)
* [Get Apikeys](../../doc/controllers/api-keys.md#get-apikeys)
* [Post Apikeys](../../doc/controllers/api-keys.md#post-apikeys)


# Get Apikeys Id

Query an API key that represents a permanent method of authentication to the API, remaining active until marked as inactive or deleted.

```python
def get_apikeys_id(self,
                  id,
                  request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of the API Key. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ApikeysResponseResult`](../../doc/models/apikeys-response-result.md).

## Example Usage

```python
id = 't1_api_676a5353d67a6df2c47b198'

request_token = '20250423-yourmerchant-refunds-001'

result = api_keys_controller.get_apikeys_id(
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
        "id": "t1_api_676a5353d67a6df2c47b198",
        "created": "2024-12-24 01:23:15.8882",
        "modified": "2024-12-24 01:23:15.8882",
        "creator": "t1_log_651fec1e202e349386ba321",
        "modifier": "t1_log_651fec1e202e349386ba321",
        "login": "t1_log_651fec1e202e349386ba321",
        "key": "f0d9fd14f9795590c01dd2c8083a35d7",
        "name": "api",
        "description": "API KEYS",
        "public": 0,
        "inactive": 0,
        "frozen": 0,
        "token": 0
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


# Put Apikeys Id

Update an API key, which represents a permanent method of authentication to the API. Each API key remains active until you mark it as inactive or delete it.

```python
def put_apikeys_id(self,
                  id,
                  body,
                  request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The API Key ID. |
| `body` | [`ApiKeysPutRequest`](../../doc/models/api-keys-put-request.md) | Body, Required | Update API Key Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ApikeysResponseResult`](../../doc/models/apikeys-response-result.md).

## Example Usage

```python
id = 't1_api_676a5353d67a6df2c47b198'

body = ApiKeysPutRequest(
    name='api',
    description='API KEYS',
    token=TokenEnum.AUTHTOKENDISABLED,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = api_keys_controller.put_apikeys_id(
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
        "id": "t1_api_676a5353d67a6df2c47b198",
        "created": "2024-12-24 01:23:15.8882",
        "modified": "2024-12-24 01:23:15.8882",
        "creator": "t1_log_651fec1e202e349386ba321",
        "modifier": "t1_log_651fec1e202e349386ba321",
        "login": "t1_log_651fec1e202e349386ba321",
        "key": "f0d9fd14f9795590c01dd2c8083a35d7",
        "name": "api",
        "description": "API KEYS",
        "public": 0,
        "inactive": 0,
        "frozen": 0,
        "token": 0
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


# Delete Apikeys Id

Delete an API key that represents a permanent method of authentication to the API and remains active until marked as inactive or deleted.

```python
def delete_apikeys_id(self,
                     id,
                     request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of the API Key. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ApikeysResponseResult`](../../doc/models/apikeys-response-result.md).

## Example Usage

```python
id = 't1_api_676a5353d67a6df2c47b198'

request_token = '20250423-yourmerchant-refunds-001'

result = api_keys_controller.delete_apikeys_id(
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
        "id": "t1_api_676a5353d67a6df2c47b198",
        "created": "2024-12-24 01:23:15.8882",
        "modified": "2024-12-24 01:23:15.8882",
        "creator": "t1_log_651fec1e202e349386ba321",
        "modifier": "t1_log_651fec1e202e349386ba321",
        "login": "t1_log_651fec1e202e349386ba321",
        "key": "f0d9fd14f9795590c01dd2c8083a35d7",
        "name": "api",
        "description": "API KEYS",
        "public": 0,
        "inactive": 0,
        "frozen": 0,
        "token": 0
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


# Get Apikeys

Query API keys that each represents a permanent method of authentication to the API and remains active until marked as inactive or deleted.

```python
def get_apikeys(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ApikeysResponseResult`](../../doc/models/apikeys-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = api_keys_controller.get_apikeys(
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
        "id": "t1_api_676a5353d67a6df2c47b198",
        "created": "2024-12-24 01:23:15.8882",
        "modified": "2024-12-24 01:23:15.8882",
        "creator": "t1_log_651fec1e202e349386ba321",
        "modifier": "t1_log_651fec1e202e349386ba321",
        "login": "t1_log_651fec1e202e349386ba321",
        "key": "f0d9fd14f9795590c01dd2c8083a35d7",
        "name": "api",
        "description": "API KEYS",
        "public": 0,
        "inactive": 0,
        "frozen": 0,
        "token": 0
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


# Post Apikeys

Create an API key that represents a permanent method of authentication to the API. The API key remains active until marked as inactive or deleted.

```python
def post_apikeys(self,
                body,
                request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ApiKeysPostRequest`](../../doc/models/api-keys-post-request.md) | Body, Required | Create API Key Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ApikeysResponseResult`](../../doc/models/apikeys-response-result.md).

## Example Usage

```python
body = ApiKeysPostRequest(
    login='t1_log_651fec1e202e349386ba321',
    public=ApiKeyPublicEnum.PRIVATEACCESS,
    token=TokenEnum.AUTHTOKENDISABLED,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    name='api',
    description='API KEYS'
)

request_token = '20250423-yourmerchant-refunds-001'

result = api_keys_controller.post_apikeys(
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
        "id": "t1_api_676a5353d67a6df2c47b198",
        "created": "2024-12-24 01:23:15.8882",
        "modified": "2024-12-24 01:23:15.8882",
        "creator": "t1_log_651fec1e202e349386ba321",
        "modifier": "t1_log_651fec1e202e349386ba321",
        "login": "t1_log_651fec1e202e349386ba321",
        "key": "f0d9fd14f9795590c01dd2c8083a35d7",
        "name": "api",
        "description": "API KEYS",
        "public": 0,
        "inactive": 0,
        "frozen": 0,
        "token": 0
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

