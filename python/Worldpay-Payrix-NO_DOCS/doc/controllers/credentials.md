# Credentials

Represents an authorization that a given Entity has to connect to an integration to perform a particular action, such as send Transactions to the processor, or board a Merchant with the processor.

```python
credentials_controller = client.credentials
```

## Class Name

`CredentialsController`

## Methods

* [Get Credentials Id](../../doc/controllers/credentials.md#get-credentials-id)
* [Put Credentials Id](../../doc/controllers/credentials.md#put-credentials-id)
* [Delete Credentials Id](../../doc/controllers/credentials.md#delete-credentials-id)
* [Get Credentials](../../doc/controllers/credentials.md#get-credentials)
* [Post Credentials](../../doc/controllers/credentials.md#post-credentials)


# Get Credentials Id

Query a Credential resource that represents an authorization that a given Entity has to connect to an integration to perform a particular action, such as send Transactions to the processor, or board a Merchant with the processor.

```python
def get_credentials_id(self,
                      id,
                      request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Credential ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CredentialsResponseResult`](../../doc/models/credentials-response-result.md).

## Example Usage

```python
id = 't1_cdt_67e152d9f0ef564f9b2c0d0'

request_token = '20250423-yourmerchant-refunds-001'

result = credentials_controller.get_credentials_id(
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
        "id": "t1_cdt_67e152d9f0ef564f9b2c0d0",
        "created": "2025-03-24 08:40:57.9902",
        "modified": "2025-03-24 08:40:57.9902",
        "creator": "t1_log_67e152cfb94fe8d3c4bc950",
        "modifier": "t1_log_67e152cfb94fe8d3c4bc950",
        "entity": "t1_ent_67e152cfd598c814ed8f2e0",
        "name": "",
        "description": "",
        "username": "JDoe123",
        "password": "password1",
        "connectUsername": "",
        "connectPassword": "password",
        "integration": "VANTIV",
        "type": "transaction",
        "inactive": 0,
        "frozen": 0,
        "secret": ""
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


# Put Credentials Id

Update a Credential resource represents an authorization that a given Entity has to connect to an integration to perform a particular action.

```python
def put_credentials_id(self,
                      id,
                      body,
                      request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Credential ID. |
| `body` | [`CredentialsPutRequest`](../../doc/models/credentials-put-request.md) | Body, Required | Update Credential Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CredentialsResponseResult`](../../doc/models/credentials-response-result.md).

## Example Usage

```python
id = 't1_cdt_67e152d9f0ef564f9b2c0d0'

body = CredentialsPutRequest(
    name='name of Credential resource',
    description='description of Credential resource',
    username='JDoe123',
    password='password',
    connect_username='username connecting to integration',
    connect_password='password',
    secret='secret resource identifier',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = credentials_controller.put_credentials_id(
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
        "id": "t1_cdt_67e152d9f0ef564f9b2c0d0",
        "created": "2025-03-24 08:40:57.9902",
        "modified": "2025-03-24 08:40:57.9902",
        "creator": "t1_log_67e152cfb94fe8d3c4bc950",
        "modifier": "t1_log_67e152cfb94fe8d3c4bc950",
        "entity": "t1_ent_67e152cfd598c814ed8f2e0",
        "name": "",
        "description": "",
        "username": "JDoe123",
        "password": "password1",
        "connectUsername": "",
        "connectPassword": "password",
        "integration": "VANTIV",
        "type": "transaction",
        "inactive": 0,
        "frozen": 0,
        "secret": ""
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


# Delete Credentials Id

Delete a Credential resource. A Credential resource represents an authorization that a given Entity has to connect to an integration to perform a particular action, such as delete a Credential resource.

```python
def delete_credentials_id(self,
                         id,
                         request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Credential ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CredentialsResponseResult`](../../doc/models/credentials-response-result.md).

## Example Usage

```python
id = 't1_cdt_67e152d9f0ef564f9b2c0d0'

request_token = '20250423-yourmerchant-refunds-001'

result = credentials_controller.delete_credentials_id(
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
        "id": "t1_cdt_67e152d9f0ef564f9b2c0d0",
        "created": "2025-03-24 08:40:57.9902",
        "modified": "2025-03-24 08:40:57.9902",
        "creator": "t1_log_67e152cfb94fe8d3c4bc950",
        "modifier": "t1_log_67e152cfb94fe8d3c4bc950",
        "entity": "t1_ent_67e152cfd598c814ed8f2e0",
        "name": "",
        "description": "",
        "username": "JDoe123",
        "password": "password1",
        "connectUsername": "",
        "connectPassword": "password",
        "integration": "VANTIV",
        "type": "transaction",
        "inactive": 0,
        "frozen": 0,
        "secret": ""
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


# Get Credentials

Query a Credential resource. A Credential resource represents an authorization that a given Entity has to connect to an integration to perform a particular action, such as send Transactions to the processor, or board a Merchant with the processor

```python
def get_credentials(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CredentialsResponseResult`](../../doc/models/credentials-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = credentials_controller.get_credentials(
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
        "id": "t1_cdt_67e152d9f0ef564f9b2c0d0",
        "created": "2025-03-24 08:40:57.9902",
        "modified": "2025-03-24 08:40:57.9902",
        "creator": "t1_log_67e152cfb94fe8d3c4bc950",
        "modifier": "t1_log_67e152cfb94fe8d3c4bc950",
        "entity": "t1_ent_67e152cfd598c814ed8f2e0",
        "name": "",
        "description": "",
        "username": "JDoe123",
        "password": "password1",
        "connectUsername": "",
        "connectPassword": "password",
        "integration": "VANTIV",
        "type": "transaction",
        "inactive": 0,
        "frozen": 0,
        "secret": ""
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


# Post Credentials

Create a Credential resource that represents an authorization that a given Entity has to connect to an integration to perform a particular action, such as send Transactions to the processor, or board a Merchant with the processor.

```python
def post_credentials(self,
                    body,
                    request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CredentialsPostRequest`](../../doc/models/credentials-post-request.md) | Body, Required | Create Credential Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CredentialsResponseResult`](../../doc/models/credentials-response-result.md).

## Example Usage

```python
body = CredentialsPostRequest(
    entity='t1_ent_67e152cfd598c814ed8f2e0',
    username='JDoe123',
    integration=CredentialIntegrationEnum.VANTIV,
    mtype=CredentialTypeEnum.TRANSACTION,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    name='name of Credential resource',
    description='description of Credential resource',
    password='password',
    connect_username='username connecting to integration',
    connect_password='password',
    secret='secret resource identifier'
)

request_token = '20250423-yourmerchant-refunds-001'

result = credentials_controller.post_credentials(
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
        "id": "t1_cdt_67e152d9f0ef564f9b2c0d0",
        "created": "2025-03-24 08:40:57.9902",
        "modified": "2025-03-24 08:40:57.9902",
        "creator": "t1_log_67e152cfb94fe8d3c4bc950",
        "modifier": "t1_log_67e152cfb94fe8d3c4bc950",
        "entity": "t1_ent_67e152cfd598c814ed8f2e0",
        "name": "",
        "description": "",
        "username": "JDoe123",
        "password": "password1",
        "connectUsername": "",
        "connectPassword": "password",
        "integration": "VANTIV",
        "type": "transaction",
        "inactive": 0,
        "frozen": 0,
        "secret": ""
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

