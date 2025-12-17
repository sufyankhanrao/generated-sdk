# Terminals

Resources for dealing with transaction that occur on physical terminals, such as a table or register.

```python
terminals_controller = client.terminals
```

## Class Name

`TerminalsController`

## Methods

* [Get Terminals Id](../../doc/controllers/terminals.md#get-terminals-id)
* [Put Terminals Id](../../doc/controllers/terminals.md#put-terminals-id)
* [Delete Terminals Id](../../doc/controllers/terminals.md#delete-terminals-id)
* [Get Terminals](../../doc/controllers/terminals.md#get-terminals)
* [Post Terminals](../../doc/controllers/terminals.md#post-terminals)


# Get Terminals Id

Query a Terminal resource.

```python
def get_terminals_id(self,
                    id,
                    request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Terminal ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalsResponseResult`](../../doc/models/terminals-response-result.md).

## Example Usage

```python
id = 't1_tml_67c12924f339facb1c80000'

request_token = '20250423-yourmerchant-refunds-001'

result = terminals_controller.get_terminals_id(
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
        "id": "t1_tml_67c12924f339facb1c80000",
        "created": "2025-02-27 22:10:29.0043",
        "modified": "2025-02-27 22:10:29.0043",
        "creator": "t1_log_5cd987a73478a6179b95000",
        "modifier": "t1_log_5cd987a73478a6179b95000",
        "merchant": "t1_mer_67c127497499df129bfc68b",
        "type": "paxSp30Casio",
        "capability": 1,
        "environment": 1,
        "autoClose": 2,
        "autoCloseTime": 2355,
        "name": "",
        "description": "",
        "address1": "",
        "address2": "",
        "city": "",
        "state": "AB",
        "zip": "",
        "country": "CAN",
        "timezone": "est",
        "status": 1,
        "phone": "",
        "serial": "",
        "cloudEnabled": 0,
        "token": ""
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


# Put Terminals Id

Update a Terminal resource.

```python
def put_terminals_id(self,
                    id,
                    body,
                    request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Terminal ID. |
| `body` | [`TerminalsPutRequest`](../../doc/models/terminals-put-request.md) | Body, Required | Update Terminal Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalsResponseResult`](../../doc/models/terminals-response-result.md).

## Example Usage

```python
id = 't1_tml_67c12924f339facb1c80000'

body = TerminalsPutRequest(
    mtype=TerminalTypeEnum.PAXSP30CASIO,
    capability=CapabilityEnum.KEYED,
    environment=TerminalEnvironmentEnum.RETAIL,
    auto_close=AutoCloseEnum.ENUM_NONE,
    auto_close_time=2355,
    cloud_enabled=CloudEnabledEnum.CLOUDSERVICESDISABLED,
    serial='serial number',
    token='token',
    name='name of this terminal',
    description='description of the Terminal',
    address_1='first line of the address',
    address_2='second line of the address',
    city='city name',
    state='AB',
    zip='zip code',
    country=CountryEnum.CAN,
    phone='phone number',
    timezone=TimezoneEnum.EST,
    status=TerminalStatusEnum.ACTIVE
)

request_token = '20250423-yourmerchant-refunds-001'

result = terminals_controller.put_terminals_id(
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
        "id": "t1_tml_67c12924f339facb1c80000",
        "created": "2025-02-27 22:10:29.0043",
        "modified": "2025-02-27 22:10:29.0043",
        "creator": "t1_log_5cd987a73478a6179b95000",
        "modifier": "t1_log_5cd987a73478a6179b95000",
        "merchant": "t1_mer_67c127497499df129bfc68b",
        "type": "paxSp30Casio",
        "capability": 1,
        "environment": 1,
        "autoClose": 2,
        "autoCloseTime": 2355,
        "name": "",
        "description": "",
        "address1": "",
        "address2": "",
        "city": "",
        "state": "AB",
        "zip": "",
        "country": "CAN",
        "timezone": "est",
        "status": 1,
        "phone": "",
        "serial": "",
        "cloudEnabled": 0,
        "token": ""
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


# Delete Terminals Id

Delete a terminal resource that represents a device/software that will be used to process transactions.

```python
def delete_terminals_id(self,
                       id,
                       request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Terminal ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalsResponseResult`](../../doc/models/terminals-response-result.md).

## Example Usage

```python
id = 't1_tml_67c12924f339facb1c80000'

request_token = '20250423-yourmerchant-refunds-001'

result = terminals_controller.delete_terminals_id(
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
        "id": "t1_tml_67c12924f339facb1c80000",
        "created": "2025-02-27 22:10:29.0043",
        "modified": "2025-02-27 22:10:29.0043",
        "creator": "t1_log_5cd987a73478a6179b95000",
        "modifier": "t1_log_5cd987a73478a6179b95000",
        "merchant": "t1_mer_67c127497499df129bfc68b",
        "type": "paxSp30Casio",
        "capability": 1,
        "environment": 1,
        "autoClose": 2,
        "autoCloseTime": 2355,
        "name": "",
        "description": "",
        "address1": "",
        "address2": "",
        "city": "",
        "state": "AB",
        "zip": "",
        "country": "CAN",
        "timezone": "est",
        "status": 1,
        "phone": "",
        "serial": "",
        "cloudEnabled": 0,
        "token": ""
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


# Get Terminals

Query a terminal resource.
A terminal resource represents a device/software that will be used to process transactions.

```python
def get_terminals(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalsResponseResult`](../../doc/models/terminals-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = terminals_controller.get_terminals(
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
        "id": "t1_tml_67c12924f339facb1c80000",
        "created": "2025-02-27 22:10:29.0043",
        "modified": "2025-02-27 22:10:29.0043",
        "creator": "t1_log_5cd987a73478a6179b95000",
        "modifier": "t1_log_5cd987a73478a6179b95000",
        "merchant": "t1_mer_67c127497499df129bfc68b",
        "type": "paxSp30Casio",
        "capability": 1,
        "environment": 1,
        "autoClose": 2,
        "autoCloseTime": 2355,
        "name": "",
        "description": "",
        "address1": "",
        "address2": "",
        "city": "",
        "state": "AB",
        "zip": "",
        "country": "CAN",
        "timezone": "est",
        "status": 1,
        "phone": "",
        "serial": "",
        "cloudEnabled": 0,
        "token": ""
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


# Post Terminals

Create a terminal resource.
A terminal resource represents a device/software that will be used to process transactions.

```python
def post_terminals(self,
                  body,
                  request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TerminalsPostRequest`](../../doc/models/terminals-post-request.md) | Body, Required | Create Terminal Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalsResponseResult`](../../doc/models/terminals-response-result.md).

## Example Usage

```python
body = TerminalsPostRequest(
    merchant='t1_mer_67c127497499df129bfc68b',
    mtype=TerminalTypeEnum.PAXSP30CASIO,
    auto_close=AutoCloseEnum.ENUM_NONE,
    auto_close_time=2355,
    status=TerminalStatusEnum.ACTIVE,
    capability=CapabilityEnum.KEYED,
    environment=TerminalEnvironmentEnum.RETAIL,
    cloud_enabled=CloudEnabledEnum.CLOUDSERVICESDISABLED,
    serial='serial number',
    token='token',
    name='name of this terminal',
    description='description of the Terminal',
    address_1='first line of the address',
    address_2='second line of the address',
    city='city name',
    state='AB',
    zip='zip code',
    country=CountryEnum.CAN,
    phone='phone number',
    timezone=TimezoneEnum.EST
)

request_token = '20250423-yourmerchant-refunds-001'

result = terminals_controller.post_terminals(
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
        "id": "t1_tml_67c12924f339facb1c80000",
        "created": "2025-02-27 22:10:29.0043",
        "modified": "2025-02-27 22:10:29.0043",
        "creator": "t1_log_5cd987a73478a6179b95000",
        "modifier": "t1_log_5cd987a73478a6179b95000",
        "merchant": "t1_mer_67c127497499df129bfc68b",
        "type": "paxSp30Casio",
        "capability": 1,
        "environment": 1,
        "autoClose": 2,
        "autoCloseTime": 2355,
        "name": "",
        "description": "",
        "address1": "",
        "address2": "",
        "city": "",
        "state": "AB",
        "zip": "",
        "country": "CAN",
        "timezone": "est",
        "status": 1,
        "phone": "",
        "serial": "",
        "cloudEnabled": 0,
        "token": ""
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

