# Rev Share Schedules

```python
rev_share_schedules_controller = client.rev_share_schedules
```

## Class Name

`RevShareSchedulesController`

## Methods

* [Get Rev Share Schedules Id](../../doc/controllers/rev-share-schedules.md#get-rev-share-schedules-id)
* [Put Rev Share Schedules Id](../../doc/controllers/rev-share-schedules.md#put-rev-share-schedules-id)
* [Delete Rev Share Schedules Id](../../doc/controllers/rev-share-schedules.md#delete-rev-share-schedules-id)
* [Get Rev Share Schedules](../../doc/controllers/rev-share-schedules.md#get-rev-share-schedules)
* [Post Rev Share Schedules](../../doc/controllers/rev-share-schedules.md#post-rev-share-schedules)


# Get Rev Share Schedules Id

Query a revShareSchedule.

```python
def get_rev_share_schedules_id(self,
                              id,
                              request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`RevShareSchedulesResponseResult`](../../doc/models/rev-share-schedules-response-result.md).

## Example Usage

```python
id = 't1_rsc_6800f8590a3fc6c0caed9zz'

request_token = '20250423-yourmerchant-refunds-001'

result = rev_share_schedules_controller.get_rev_share_schedules_id(
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
        "id": "t1_rsc_6800f8590a3fc6c0caed9zz",
        "created": "2025-04-17 08:47:21.0625",
        "modified": "2025-04-17 08:47:21.0625",
        "creator": "t1_log_670d8844ef246e80758e762",
        "modifier": "t1_log_670d8844ef246e80758e762",
        "entity": "g157715bca1f55c",
        "forentity": "t1_ent_67c96d183e9b9aa6c6f190c",
        "start": "2025-04-17 18:17:20",
        "end": "2025-04-17 18:17:20",
        "share": 2000,
        "event": 84,
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


# Put Rev Share Schedules Id

Update a revShareSchedule.

```python
def put_rev_share_schedules_id(self,
                              id,
                              body,
                              request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource. |
| `body` | [`RevShareSchedulesPutRequest`](../../doc/models/rev-share-schedules-put-request.md) | Body, Required | - |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`RevShareSchedulesResponseResult`](../../doc/models/rev-share-schedules-response-result.md).

## Example Usage

```python
id = 't1_rsc_6800f8590a3fc6c0caed9zz'

body = RevShareSchedulesPutRequest(
    entity='t1_ent_5f9058fe8c8d21ead8f68dc',
    forentity='t1_ent_67c96d183e9b9aa6c6f190c',
    start='2025-04-17 18:17:20',
    end='2025-04-17 18:17:20',
    share=2000,
    event=RevShareScheduleEventEnum.REVSHARECARD,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = rev_share_schedules_controller.put_rev_share_schedules_id(
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
        "id": "t1_rsc_6800f8590a3fc6c0caed9zz",
        "created": "2025-04-17 08:47:21.0625",
        "modified": "2025-04-17 08:47:21.0625",
        "creator": "t1_log_670d8844ef246e80758e762",
        "modifier": "t1_log_670d8844ef246e80758e762",
        "entity": "g157715bca1f55c",
        "forentity": "t1_ent_67c96d183e9b9aa6c6f190c",
        "start": "2025-04-17 18:17:20",
        "end": "2025-04-17 18:17:20",
        "share": 2000,
        "event": 84,
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


# Delete Rev Share Schedules Id

Delete a revShareSchedule.

```python
def delete_rev_share_schedules_id(self,
                                 id,
                                 request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`RevShareSchedulesResponseResult`](../../doc/models/rev-share-schedules-response-result.md).

## Example Usage

```python
id = 't1_rsc_6800f8590a3fc6c0caed9zz'

request_token = '20250423-yourmerchant-refunds-001'

result = rev_share_schedules_controller.delete_rev_share_schedules_id(
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
        "id": "t1_rsc_6800f8590a3fc6c0caed9zz",
        "created": "2025-04-17 08:47:21.0625",
        "modified": "2025-04-17 08:47:21.0625",
        "creator": "t1_log_670d8844ef246e80758e762",
        "modifier": "t1_log_670d8844ef246e80758e762",
        "entity": "g157715bca1f55c",
        "forentity": "t1_ent_67c96d183e9b9aa6c6f190c",
        "start": "2025-04-17 18:17:20",
        "end": "2025-04-17 18:17:20",
        "share": 2000,
        "event": 84,
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


# Get Rev Share Schedules

Query revShareSchedules.

```python
def get_rev_share_schedules(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`RevShareSchedulesResponseResult`](../../doc/models/rev-share-schedules-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = rev_share_schedules_controller.get_rev_share_schedules(
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
        "id": "t1_rsc_6800f8590a3fc6c0caed9zz",
        "created": "2025-04-17 08:47:21.0625",
        "modified": "2025-04-17 08:47:21.0625",
        "creator": "t1_log_670d8844ef246e80758e762",
        "modifier": "t1_log_670d8844ef246e80758e762",
        "entity": "g157715bca1f55c",
        "forentity": "t1_ent_67c96d183e9b9aa6c6f190c",
        "start": "2025-04-17 18:17:20",
        "end": "2025-04-17 18:17:20",
        "share": 2000,
        "event": 84,
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


# Post Rev Share Schedules

Create a revShareSchedules.

```python
def post_rev_share_schedules(self,
                            body,
                            request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`RevShareSchedulesPostRequest`](../../doc/models/rev-share-schedules-post-request.md) | Body, Required | - |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`RevShareSchedulesResponseResult`](../../doc/models/rev-share-schedules-response-result.md).

## Example Usage

```python
body = RevShareSchedulesPostRequest(
    entity='t1_ent_5f9058fe8c8d21ead8f68dc',
    forentity='t1_ent_67c96d183e9b9aa6c6f190c',
    start='2025-04-17 18:17:20',
    share=2000,
    event=RevShareScheduleEventEnum.REVSHARECARD,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    end='2025-04-17 18:17:20'
)

request_token = '20250423-yourmerchant-refunds-001'

result = rev_share_schedules_controller.post_rev_share_schedules(
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
        "id": "t1_rsc_6800f8590a3fc6c0caed9zz",
        "created": "2025-04-17 08:47:21.0625",
        "modified": "2025-04-17 08:47:21.0625",
        "creator": "t1_log_670d8844ef246e80758e762",
        "modifier": "t1_log_670d8844ef246e80758e762",
        "entity": "g157715bca1f55c",
        "forentity": "t1_ent_67c96d183e9b9aa6c6f190c",
        "start": "2025-04-17 18:17:20",
        "end": "2025-04-17 18:17:20",
        "share": 2000,
        "event": 84,
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

