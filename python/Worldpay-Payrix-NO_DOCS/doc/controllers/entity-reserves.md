# Entity Reserves

```python
entity_reserves_controller = client.entity_reserves
```

## Class Name

`EntityReservesController`

## Methods

* [Get Entity Reserves Id](../../doc/controllers/entity-reserves.md#get-entity-reserves-id)
* [Put Entity Reserves Id](../../doc/controllers/entity-reserves.md#put-entity-reserves-id)
* [Get Entity Reserves](../../doc/controllers/entity-reserves.md#get-entity-reserves)
* [Post Entity Reserves](../../doc/controllers/entity-reserves.md#post-entity-reserves)


# Get Entity Reserves Id

Query an EntityReserves resource that represents funds held by an Entity in reserve, separately from amounts in any entityFunds.

```python
def get_entity_reserves_id(self,
                          id,
                          request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this entity reserve. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`EntityReservesResponseResult`](../../doc/models/entity-reserves-response-result.md).

## Example Usage

```python
id = 't1_erv_67a0e0072f9c059e59a66b0'

request_token = '20250423-yourmerchant-refunds-001'

result = entity_reserves_controller.get_entity_reserves_id(
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
        "id": "t1_erv_67a0e0072f9c059e59a66b0",
        "created": "2025-02-03 10:25:59.2069",
        "modified": "2025-02-03 10:25:59.2069",
        "creator": "t1_log_5f2d5e3e67a6fb5b3521361",
        "modifier": "t1_log_5f2d5e3e67a6fb5b3521361",
        "login": "t1_log_5f2d5e3e67a6fb5b3521361",
        "fund": "t1_fun_5f20126254c14a171b8d2d0",
        "total": 0,
        "name": "EntityReserve1",
        "description": "EntityReserve",
        "requestSequence": 0,
        "processedSequence": 0
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


# Put Entity Reserves Id

Update an EntityReserves resource, which represents funds held by an Entity in reserve, separately from amounts in any entityFunds.

```python
def put_entity_reserves_id(self,
                          id,
                          body,
                          request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this entity reserve. |
| `body` | [`EntityReservesPutRequest`](../../doc/models/entity-reserves-put-request.md) | Body, Required | Update an Entity Reserve Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`EntityReservesResponseResult`](../../doc/models/entity-reserves-response-result.md).

## Example Usage

```python
id = 't1_erv_67a0e0072f9c059e59a66b0'

body = EntityReservesPutRequest(
    total=0,
    name='EntityReserve1',
    description='EntityReserve'
)

request_token = '20250423-yourmerchant-refunds-001'

result = entity_reserves_controller.put_entity_reserves_id(
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
        "id": "t1_erv_67a0e0072f9c059e59a66b0",
        "created": "2025-02-03 10:25:59.2069",
        "modified": "2025-02-03 10:25:59.2069",
        "creator": "t1_log_5f2d5e3e67a6fb5b3521361",
        "modifier": "t1_log_5f2d5e3e67a6fb5b3521361",
        "login": "t1_log_5f2d5e3e67a6fb5b3521361",
        "fund": "t1_fun_5f20126254c14a171b8d2d0",
        "total": 0,
        "name": "EntityReserve1",
        "description": "EntityReserve",
        "requestSequence": 0,
        "processedSequence": 0
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


# Get Entity Reserves

Query an EntityReserves resource that represents funds held by an Entity in reserve, separately from amounts in any entityFunds.

```python
def get_entity_reserves(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`EntityReservesResponseResult`](../../doc/models/entity-reserves-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = entity_reserves_controller.get_entity_reserves(
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
        "id": "t1_erv_67a0e0072f9c059e59a66b0",
        "created": "2025-02-03 10:25:59.2069",
        "modified": "2025-02-03 10:25:59.2069",
        "creator": "t1_log_5f2d5e3e67a6fb5b3521361",
        "modifier": "t1_log_5f2d5e3e67a6fb5b3521361",
        "login": "t1_log_5f2d5e3e67a6fb5b3521361",
        "fund": "t1_fun_5f20126254c14a171b8d2d0",
        "total": 0,
        "name": "EntityReserve1",
        "description": "EntityReserve",
        "requestSequence": 0,
        "processedSequence": 0
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


# Post Entity Reserves

Create an EntityReserves resource that represents funds held by an Entity in reserve, separately from amounts in any entityFunds.

```python
def post_entity_reserves(self,
                        body,
                        request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`EntityReservesPostRequest`](../../doc/models/entity-reserves-post-request.md) | Body, Required | Create Entity Reserve Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`EntityReservesResponseResult`](../../doc/models/entity-reserves-response-result.md).

## Example Usage

```python
body = EntityReservesPostRequest(
    login='t1_log_5f2d5e3e67a6fb5b3521361',
    fund='t1_fun_5f20126254c14a171b8d2d0',
    total=0,
    name='EntityReserve1',
    description='EntityReserve'
)

request_token = '20250423-yourmerchant-refunds-001'

result = entity_reserves_controller.post_entity_reserves(
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
        "id": "t1_erv_67a0e0072f9c059e59a66b0",
        "created": "2025-02-03 10:25:59.2069",
        "modified": "2025-02-03 10:25:59.2069",
        "creator": "t1_log_5f2d5e3e67a6fb5b3521361",
        "modifier": "t1_log_5f2d5e3e67a6fb5b3521361",
        "login": "t1_log_5f2d5e3e67a6fb5b3521361",
        "fund": "t1_fun_5f20126254c14a171b8d2d0",
        "total": 0,
        "name": "EntityReserve1",
        "description": "EntityReserve",
        "requestSequence": 0,
        "processedSequence": 0
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

