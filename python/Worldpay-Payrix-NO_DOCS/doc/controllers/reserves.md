# Reserves

Resources that deals with reserve activity. Reserving means to withhold funds from an entity by removing the ability to extract the funds from the control of the financial institution.

```python
reserves_controller = client.reserves
```

## Class Name

`ReservesController`

## Methods

* [Get Reserves Id](../../doc/controllers/reserves.md#get-reserves-id)
* [Put Reserves Id](../../doc/controllers/reserves.md#put-reserves-id)
* [Delete Reserves Id](../../doc/controllers/reserves.md#delete-reserves-id)
* [Get Reserves](../../doc/controllers/reserves.md#get-reserves)
* [Post Reserves](../../doc/controllers/reserves.md#post-reserves)


# Get Reserves Id

Query a Reserve resource that represents a way to reserve funds from an Entity or Org automatically and to release them automatically according to a pre-determined schedule.

```python
def get_reserves_id(self,
                   id,
                   request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this reserve. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ReservesResponseResult`](../../doc/models/reserves-response-result.md).

## Example Usage

```python
id = 't1_rsv_66f27fca06f8a777998c000'

request_token = '20250423-yourmerchant-refunds-001'

result = reserves_controller.get_reserves_id(
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
        "id": "t1_rsv_66f27fca06f8a777998c000",
        "created": "2024-09-24 05:00:58.0528",
        "modified": "2024-09-24 05:00:58.0528",
        "creator": "t1_log_611e6ca320fae7afab2f000",
        "modifier": "t1_log_611e6ca320fae7afab2f000",
        "login": "t1_log_611e6ca320fae7afab2f256",
        "org": "t1_org_5fada4629c317f80bc9cb00",
        "entity": "t1_ent_5f9058fe8c8d21ead8f68dc",
        "name": "Additional Underwriting Review Required",
        "description": "Will release the reserve once all information is verified.",
        "percent": 10000,
        "release": "never",
        "releaseFactor": 1,
        "finish": 20160120,
        "inactive": 0,
        "frozen": 0,
        "max": 0,
        "start": 20160120,
        "hold": "t1_hld_66f27fca0236545c4f125d2",
        "division": "t1_div_67b51635da21f7399ce2az0",
        "partition": "t1_ptn_000834d4d504f11234578f0",
        "level": "merchant",
        "status": 1
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


# Put Reserves Id

Update a Reserves or Reserve resource, which represents a way to reserve funds from an Entity or Org automatically and to release them automatically according to a pre-determined schedule.

```python
def put_reserves_id(self,
                   id,
                   body,
                   request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this reserve. |
| `body` | [`ReservesPutRequest`](../../doc/models/reserves-put-request.md) | Body, Required | Update a Reserve Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ReservesResponseResult`](../../doc/models/reserves-response-result.md).

## Example Usage

```python
id = 't1_rsv_66f27fca06f8a777998c000'

body = ReservesPutRequest(
    login='t1_log_611e6ca320fae7afab2f256',
    org='t1_org_5fada4629c317f80bc9cb00',
    division='t1_div_67b51635da21f7399ce2az0',
    partition='t1_ptn_000834d4d504f11234578f0',
    level=LevelEnum.MERCHANT,
    entity='t1_ent_5f9058fe8c8d21ead8f68dc',
    hold='t1_hld_66f27fca0236545c4f125d2',
    name='Additional Underwriting Review Required',
    description='Will release the reserve once all information is verified.',
    percent=10000,
    release=ReleaseEnum.NEVER,
    release_factor=1,
    start=20160120,
    finish=20160120,
    max=0,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = reserves_controller.put_reserves_id(
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
        "id": "t1_rsv_66f27fca06f8a777998c000",
        "created": "2024-09-24 05:00:58.0528",
        "modified": "2024-09-24 05:00:58.0528",
        "creator": "t1_log_611e6ca320fae7afab2f000",
        "modifier": "t1_log_611e6ca320fae7afab2f000",
        "login": "t1_log_611e6ca320fae7afab2f256",
        "org": "t1_org_5fada4629c317f80bc9cb00",
        "entity": "t1_ent_5f9058fe8c8d21ead8f68dc",
        "name": "Additional Underwriting Review Required",
        "description": "Will release the reserve once all information is verified.",
        "percent": 10000,
        "release": "never",
        "releaseFactor": 1,
        "finish": 20160120,
        "inactive": 0,
        "frozen": 0,
        "max": 0,
        "start": 20160120,
        "hold": "t1_hld_66f27fca0236545c4f125d2",
        "division": "t1_div_67b51635da21f7399ce2az0",
        "partition": "t1_ptn_000834d4d504f11234578f0",
        "level": "merchant",
        "status": 1
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


# Delete Reserves Id

Delete a Reserves or Reserve resource that represents a way to reserve funds from an Entity or Org automatically and to release them automatically according to a pre-determined schedule.

```python
def delete_reserves_id(self,
                      id,
                      request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this reserve. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ReservesResponseResult`](../../doc/models/reserves-response-result.md).

## Example Usage

```python
id = 't1_rsv_66f27fca06f8a777998c000'

request_token = '20250423-yourmerchant-refunds-001'

result = reserves_controller.delete_reserves_id(
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
        "id": "t1_rsv_66f27fca06f8a777998c000",
        "created": "2024-09-24 05:00:58.0528",
        "modified": "2024-09-24 05:00:58.0528",
        "creator": "t1_log_611e6ca320fae7afab2f000",
        "modifier": "t1_log_611e6ca320fae7afab2f000",
        "login": "t1_log_611e6ca320fae7afab2f256",
        "org": "t1_org_5fada4629c317f80bc9cb00",
        "entity": "t1_ent_5f9058fe8c8d21ead8f68dc",
        "name": "Additional Underwriting Review Required",
        "description": "Will release the reserve once all information is verified.",
        "percent": 10000,
        "release": "never",
        "releaseFactor": 1,
        "finish": 20160120,
        "inactive": 0,
        "frozen": 0,
        "max": 0,
        "start": 20160120,
        "hold": "t1_hld_66f27fca0236545c4f125d2",
        "division": "t1_div_67b51635da21f7399ce2az0",
        "partition": "t1_ptn_000834d4d504f11234578f0",
        "level": "merchant",
        "status": 1
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


# Get Reserves

Query a Reserves resource.
A Reserves resource represents a way to reserve funds from an Entity or Org automatically and to release them automatically according to a pre-determined schedule.

```python
def get_reserves(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ReservesResponseResult`](../../doc/models/reserves-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = reserves_controller.get_reserves(
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
        "id": "t1_rsv_66f27fca06f8a777998c000",
        "created": "2024-09-24 05:00:58.0528",
        "modified": "2024-09-24 05:00:58.0528",
        "creator": "t1_log_611e6ca320fae7afab2f000",
        "modifier": "t1_log_611e6ca320fae7afab2f000",
        "login": "t1_log_611e6ca320fae7afab2f256",
        "org": "t1_org_5fada4629c317f80bc9cb00",
        "entity": "t1_ent_5f9058fe8c8d21ead8f68dc",
        "name": "Additional Underwriting Review Required",
        "description": "Will release the reserve once all information is verified.",
        "percent": 10000,
        "release": "never",
        "releaseFactor": 1,
        "finish": 20160120,
        "inactive": 0,
        "frozen": 0,
        "max": 0,
        "start": 20160120,
        "hold": "t1_hld_66f27fca0236545c4f125d2",
        "division": "t1_div_67b51635da21f7399ce2az0",
        "partition": "t1_ptn_000834d4d504f11234578f0",
        "level": "merchant",
        "status": 1
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


# Post Reserves

Create a Reserves resource.
A Reserves resource represents a way to reserve funds from an Entity or Org automatically and to release them automatically according to a pre-determined schedule.

```python
def post_reserves(self,
                 body,
                 request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ReservesPostRequest`](../../doc/models/reserves-post-request.md) | Body, Required | Create Reserve Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ReservesResponseResult`](../../doc/models/reserves-response-result.md).

## Example Usage

```python
body = ReservesPostRequest(
    login='t1_log_611e6ca320fae7afab2f256',
    level=LevelEnum.MERCHANT,
    percent=10000,
    release=ReleaseEnum.NEVER,
    release_factor=1,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    org='t1_org_5fada4629c317f80bc9cb00',
    division='t1_div_67b51635da21f7399ce2az0',
    partition='t1_ptn_000834d4d504f11234578f0',
    entity='t1_ent_5f9058fe8c8d21ead8f68dc',
    hold='t1_hld_66f27fca0236545c4f125d2',
    name='Additional Underwriting Review Required',
    description='Will release the reserve once all information is verified.',
    start=20160120,
    finish=20160120,
    max=0
)

request_token = '20250423-yourmerchant-refunds-001'

result = reserves_controller.post_reserves(
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
        "id": "t1_rsv_66f27fca06f8a777998c000",
        "created": "2024-09-24 05:00:58.0528",
        "modified": "2024-09-24 05:00:58.0528",
        "creator": "t1_log_611e6ca320fae7afab2f000",
        "modifier": "t1_log_611e6ca320fae7afab2f000",
        "login": "t1_log_611e6ca320fae7afab2f256",
        "org": "t1_org_5fada4629c317f80bc9cb00",
        "entity": "t1_ent_5f9058fe8c8d21ead8f68dc",
        "name": "Additional Underwriting Review Required",
        "description": "Will release the reserve once all information is verified.",
        "percent": 10000,
        "release": "never",
        "releaseFactor": 1,
        "finish": 20160120,
        "inactive": 0,
        "frozen": 0,
        "max": 0,
        "start": 20160120,
        "hold": "t1_hld_66f27fca0236545c4f125d2",
        "division": "t1_div_67b51635da21f7399ce2az0",
        "partition": "t1_ptn_000834d4d504f11234578f0",
        "level": "merchant",
        "status": 1
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

