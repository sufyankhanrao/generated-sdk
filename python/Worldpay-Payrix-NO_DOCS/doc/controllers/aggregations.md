# Aggregations

Aggregations acts as a scheduler, ithey contains needed parameters to properly generate results containing the calculated totals and keeps such record in the aggregation results resource.

```python
aggregations_controller = client.aggregations
```

## Class Name

`AggregationsController`

## Methods

* [Get Aggregations Id](../../doc/controllers/aggregations.md#get-aggregations-id)
* [Put Aggregations Id](../../doc/controllers/aggregations.md#put-aggregations-id)
* [Delete Aggregations Id](../../doc/controllers/aggregations.md#delete-aggregations-id)
* [Get Aggregations](../../doc/controllers/aggregations.md#get-aggregations)
* [Post Aggregations](../../doc/controllers/aggregations.md#post-aggregations)


# Get Aggregations Id

Query an Aggregation resource that uses a search to query for records on the given resource and applies the desired calculations (count, sum, min, and/or max) to the field in question.

```python
def get_aggregations_id(self,
                       id,
                       request_token=None,
                       search_filter=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource or The Aggregation ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |
| `search_filter` | `str` | Header, Optional | Set this header to filter or sort the list of resources that the method returns.<br>For example, to find all resources that have a property of 'public' set to '1', set this header to 'public[equals]=1'. You can use the operators 'equals', 'greater', 'less', 'like', 'in' and 'sort'. To sort the resources, use the keywords 'asc' (for an ascending sort) or 'desc' (for a descending sort).<br>You may also use explicit 'and/or' querying by passing arrays of or and arrays of and parameters. For example, to find all resources that have a property of 'public' set to '1' or a property of 'active' set to '0', set this header to 'or[][public][equals]=1&or[][active][equals]=0'. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AggregationsResponseResult`](../../doc/models/aggregations-response-result.md).

## Example Usage

```python
id = 't1_agg_67b339d00940f0d12b000b7'

request_token = '20250423-yourmerchant-refunds-001'

search_filter = 'created[equals]=2025-01-01'

result = aggregations_controller.get_aggregations_id(
    id,
    request_token=request_token,
    search_filter=search_filter
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
        "id": "t1_agg_67b339d00940f0d12b000b7",
        "created": "2025-02-17 08:30:00.5718",
        "modified": "2025-02-17 08:30:00.5718",
        "creator": "t1_log_6279a44f109090941bbc4c0",
        "modifier": "t1_log_6279a44f109090941bbc4c0",
        "login": "t1_log_67b339d2dc878984b96b225",
        "name": "Default merchantTxnFailedAll",
        "description": "Automatically created aggregation",
        "resource": 18,
        "search": "status[equals]=2",
        "totals": "sum[0]=total&count[0]=id&groups[0]=merchant&groups[1]=type&groups[2][payment][0]=method",
        "status": "ready",
        "schedule": "days",
        "scheduleFactor": 1,
        "start": 202502180000,
        "inactive": 0,
        "frozen": 0,
        "entity": "t1_ent_676057654c1b7452e4884f0",
        "forlogin": "t1_log_67b339d2dc878984b96b225",
        "org": "t1_org_67b736ad7d05922343246cf",
        "team": "teamBoarding",
        "division": "t1_div_67b51635da21f7399ce2af1",
        "partition": "t1_ptn_666834d4d504f11234578f5",
        "type": "merchantTxnFailedAll",
        "level": "merchant",
        "default": 1,
        "degrouping": "groups[0]=merchant&groups[1][payment][0]=method"
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


# Put Aggregations Id

Update an Aggregation resource or Update an Aggregation.

```python
def put_aggregations_id(self,
                       id,
                       body,
                       request_token=None,
                       search_filter=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource or The Aggregation ID. |
| `body` | [`AggregationsPutRequest`](../../doc/models/aggregations-put-request.md) | Body, Required | Update Aggregation Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |
| `search_filter` | `str` | Header, Optional | Set this header to filter or sort the list of resources that the method returns.<br>For example, to find all resources that have a property of 'public' set to '1', set this header to 'public[equals]=1'. You can use the operators 'equals', 'greater', 'less', 'like', 'in' and 'sort'. To sort the resources, use the keywords 'asc' (for an ascending sort) or 'desc' (for a descending sort).<br>You may also use explicit 'and/or' querying by passing arrays of or and arrays of and parameters. For example, to find all resources that have a property of 'public' set to '1' or a property of 'active' set to '0', set this header to 'or[][public][equals]=1&or[][active][equals]=0'. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AggregationsResponseResult`](../../doc/models/aggregations-response-result.md).

## Example Usage

```python
id = 't1_agg_67b339d00940f0d12b000b7'

body = AggregationsPutRequest(
    login='t1_log_67b5002a5de3b716ad97e07',
    entity='t1_ent_676057654c1b7452e4884f0',
    forlogin='t1_log_67b5002a5de3b716ad97e07',
    org='t1_org_67b736ad7d05922343246cf',
    team='teamBoarding',
    division='t1_div_67b51635da21f7399ce2af1',
    partition='t1_ptn_666834d4d504f11234578f5',
    mtype=AggregationTypeEnum.MERCHANTTXNFAILEDALL,
    level=LevelEnum.MERCHANT,
    name='Default merchantTxnFailedAll',
    description='Automatically created aggregation',
    resource=ResourceEnum.TXNS,
    search='status[equals]=2&created[like]={{"expand": [{"type": "date","value": "-1 days","format": "Y-m-d","relativeTimestamp":":effective:"}]}}%',
    totals='sum[0]=total&count[0]=id&groups[0]=merchant&groups[1]=type&groups[2][payment][0]=method',
    degrouping='groups[0]=merchant&groups[1][payment][0]=method',
    status=AggregationStatusEnum.READY,
    schedule=AggregationScheduleEnum.DAYS,
    schedule_factor=1,
    start=202502200000,
    default=DefaultEnum.AUTOMATICALLYCREATED,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

search_filter = 'created[equals]=2025-01-01'

result = aggregations_controller.put_aggregations_id(
    id,
    body,
    request_token=request_token,
    search_filter=search_filter
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
        "id": "t1_agg_67b339d00940f0d12b000b7",
        "created": "2025-02-17 08:30:00.5718",
        "modified": "2025-02-17 08:30:00.5718",
        "creator": "t1_log_6279a44f109090941bbc4c0",
        "modifier": "t1_log_6279a44f109090941bbc4c0",
        "login": "t1_log_67b339d2dc878984b96b225",
        "name": "Default merchantTxnFailedAll",
        "description": "Automatically created aggregation",
        "resource": 18,
        "search": "status[equals]=2",
        "totals": "sum[0]=total&count[0]=id&groups[0]=merchant&groups[1]=type&groups[2][payment][0]=method",
        "status": "ready",
        "schedule": "days",
        "scheduleFactor": 1,
        "start": 202502180000,
        "inactive": 0,
        "frozen": 0,
        "entity": "t1_ent_676057654c1b7452e4884f0",
        "forlogin": "t1_log_67b339d2dc878984b96b225",
        "org": "t1_org_67b736ad7d05922343246cf",
        "team": "teamBoarding",
        "division": "t1_div_67b51635da21f7399ce2af1",
        "partition": "t1_ptn_666834d4d504f11234578f5",
        "type": "merchantTxnFailedAll",
        "level": "merchant",
        "default": 1,
        "degrouping": "groups[0]=merchant&groups[1][payment][0]=method"
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


# Delete Aggregations Id

Delete an Aggregation resource or an Aggregation.

```python
def delete_aggregations_id(self,
                          id,
                          request_token=None,
                          search_filter=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource or The Aggregation ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |
| `search_filter` | `str` | Header, Optional | Set this header to filter or sort the list of resources that the method returns.<br>For example, to find all resources that have a property of 'public' set to '1', set this header to 'public[equals]=1'. You can use the operators 'equals', 'greater', 'less', 'like', 'in' and 'sort'. To sort the resources, use the keywords 'asc' (for an ascending sort) or 'desc' (for a descending sort).<br>You may also use explicit 'and/or' querying by passing arrays of or and arrays of and parameters. For example, to find all resources that have a property of 'public' set to '1' or a property of 'active' set to '0', set this header to 'or[][public][equals]=1&or[][active][equals]=0'. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AggregationsResponseResult`](../../doc/models/aggregations-response-result.md).

## Example Usage

```python
id = 't1_agg_67b339d00940f0d12b000b7'

request_token = '20250423-yourmerchant-refunds-001'

search_filter = 'created[equals]=2025-01-01'

result = aggregations_controller.delete_aggregations_id(
    id,
    request_token=request_token,
    search_filter=search_filter
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
        "id": "t1_agg_67b339d00940f0d12b000b7",
        "created": "2025-02-17 08:30:00.5718",
        "modified": "2025-02-17 08:30:00.5718",
        "creator": "t1_log_6279a44f109090941bbc4c0",
        "modifier": "t1_log_6279a44f109090941bbc4c0",
        "login": "t1_log_67b339d2dc878984b96b225",
        "name": "Default merchantTxnFailedAll",
        "description": "Automatically created aggregation",
        "resource": 18,
        "search": "status[equals]=2",
        "totals": "sum[0]=total&count[0]=id&groups[0]=merchant&groups[1]=type&groups[2][payment][0]=method",
        "status": "ready",
        "schedule": "days",
        "scheduleFactor": 1,
        "start": 202502180000,
        "inactive": 0,
        "frozen": 0,
        "entity": "t1_ent_676057654c1b7452e4884f0",
        "forlogin": "t1_log_67b339d2dc878984b96b225",
        "org": "t1_org_67b736ad7d05922343246cf",
        "team": "teamBoarding",
        "division": "t1_div_67b51635da21f7399ce2af1",
        "partition": "t1_ptn_666834d4d504f11234578f5",
        "type": "merchantTxnFailedAll",
        "level": "merchant",
        "default": 1,
        "degrouping": "groups[0]=merchant&groups[1][payment][0]=method"
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


# Get Aggregations

Query an Aggregation resource using the search to query for records on the given resource and apply desired calculations (count, sum, min, and/or max) to the specified field.

```python
def get_aggregations(self,
                    request_token=None,
                    page_number=None,
                    page_limit=None,
                    search_filter=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |
| `page_number` | `int` | Query, Optional | Set this path parameter to request a specific page of records.<br>For example, set `?page[number]=2` to retrieve the second page of records for this request. |
| `page_limit` | `int` | Query, Optional | Set this path parameter to request up to a specific amount of records. By default 30 records are retrieved per page. The maximum limit that can be set is 100.<br>For example, set `?page[limit]=50` to retrieve up to 50 records for this request. |
| `search_filter` | `str` | Header, Optional | Set this header to filter or sort the list of resources that the method returns.<br>For example, to find all resources that have a property of 'public' set to '1', set this header to 'public[equals]=1'. You can use the operators 'equals', 'greater', 'less', 'like', 'in' and 'sort'. To sort the resources, use the keywords 'asc' (for an ascending sort) or 'desc' (for a descending sort).<br>You may also use explicit 'and/or' querying by passing arrays of or and arrays of and parameters. For example, to find all resources that have a property of 'public' set to '1' or a property of 'active' set to '0', set this header to 'or[][public][equals]=1&or[][active][equals]=0'. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AggregationsResponseResult`](../../doc/models/aggregations-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

search_filter = 'created[greater]=2024-01-01'

result = aggregations_controller.get_aggregations(
    request_token=request_token,
    page_number=page_number,
    page_limit=page_limit,
    search_filter=search_filter
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
        "id": "t1_agg_67b339d00940f0d12b000b7",
        "created": "2025-02-17 08:30:00.5718",
        "modified": "2025-02-17 08:30:00.5718",
        "creator": "t1_log_6279a44f109090941bbc4c0",
        "modifier": "t1_log_6279a44f109090941bbc4c0",
        "login": "t1_log_67b339d2dc878984b96b225",
        "name": "Default merchantTxnFailedAll",
        "description": "Automatically created aggregation",
        "resource": 18,
        "search": "status[equals]=2",
        "totals": "sum[0]=total&count[0]=id&groups[0]=merchant&groups[1]=type&groups[2][payment][0]=method",
        "status": "ready",
        "schedule": "days",
        "scheduleFactor": 1,
        "start": 202502180000,
        "inactive": 0,
        "frozen": 0,
        "entity": "t1_ent_676057654c1b7452e4884f0",
        "forlogin": "t1_log_67b339d2dc878984b96b225",
        "org": "t1_org_67b736ad7d05922343246cf",
        "team": "teamBoarding",
        "division": "t1_div_67b51635da21f7399ce2af1",
        "partition": "t1_ptn_666834d4d504f11234578f5",
        "type": "merchantTxnFailedAll",
        "level": "merchant",
        "default": 1,
        "degrouping": "groups[0]=merchant&groups[1][payment][0]=method"
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


# Post Aggregations

Create an Aggregation resource that uses the search to query for records on a given resource and applies the desired calculations (count, sum, min, and/or max) to the field in question.

```python
def post_aggregations(self,
                     body,
                     request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AggregationsPostRequest`](../../doc/models/aggregations-post-request.md) | Body, Required | Create Aggregation Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AggregationsResponseResult`](../../doc/models/aggregations-response-result.md).

## Example Usage

```python
body = AggregationsPostRequest(
    login='t1_log_67b5002a5de3b716ad97e07',
    resource=ResourceEnum.TXNS,
    totals='sum[0]=total&count[0]=id&groups[0]=merchant&groups[1]=type&groups[2][payment][0]=method',
    status=AggregationStatusEnum.READY,
    schedule=AggregationScheduleEnum.DAYS,
    schedule_factor=1,
    start=202502200000,
    default=DefaultEnum.AUTOMATICALLYCREATED,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    entity='t1_ent_676057654c1b7452e4884f0',
    forlogin='t1_log_67b5002a5de3b716ad97e07',
    org='t1_org_67b736ad7d05922343246cf',
    team='teamBoarding',
    division='t1_div_67b51635da21f7399ce2af1',
    partition='t1_ptn_666834d4d504f11234578f5',
    mtype=AggregationTypeEnum.MERCHANTTXNFAILEDALL,
    level=LevelEnum.MERCHANT,
    name='Default merchantTxnFailedAll',
    description='Automatically created aggregation',
    search='status[equals]=2&created[like]={{"expand": [{"type": "date","value": "-1 days","format": "Y-m-d","relativeTimestamp":":effective:"}]}}%',
    degrouping='groups[0]=merchant&groups[1][payment][0]=method'
)

request_token = '20250423-yourmerchant-refunds-001'

result = aggregations_controller.post_aggregations(
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
        "id": "t1_agg_67b339d00940f0d12b000b7",
        "created": "2025-02-17 08:30:00.5718",
        "modified": "2025-02-17 08:30:00.5718",
        "creator": "t1_log_6279a44f109090941bbc4c0",
        "modifier": "t1_log_6279a44f109090941bbc4c0",
        "login": "t1_log_67b339d2dc878984b96b225",
        "name": "Default merchantTxnFailedAll",
        "description": "Automatically created aggregation",
        "resource": 18,
        "search": "status[equals]=2",
        "totals": "sum[0]=total&count[0]=id&groups[0]=merchant&groups[1]=type&groups[2][payment][0]=method",
        "status": "ready",
        "schedule": "days",
        "scheduleFactor": 1,
        "start": 202502180000,
        "inactive": 0,
        "frozen": 0,
        "entity": "t1_ent_676057654c1b7452e4884f0",
        "forlogin": "t1_log_67b339d2dc878984b96b225",
        "org": "t1_org_67b736ad7d05922343246cf",
        "team": "teamBoarding",
        "division": "t1_div_67b51635da21f7399ce2af1",
        "partition": "t1_ptn_666834d4d504f11234578f5",
        "type": "merchantTxnFailedAll",
        "level": "merchant",
        "default": 1,
        "degrouping": "groups[0]=merchant&groups[1][payment][0]=method"
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

