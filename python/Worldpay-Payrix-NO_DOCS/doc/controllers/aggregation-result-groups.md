# Aggregation Result Groups

```python
aggregation_result_groups_controller = client.aggregation_result_groups
```

## Class Name

`AggregationResultGroupsController`

## Methods

* [Get Aggregation Result Groups Id](../../doc/controllers/aggregation-result-groups.md#get-aggregation-result-groups-id)
* [Delete Aggregation Result Groups Id](../../doc/controllers/aggregation-result-groups.md#delete-aggregation-result-groups-id)
* [Get Aggregation Result Groups](../../doc/controllers/aggregation-result-groups.md#get-aggregation-result-groups)


# Get Aggregation Result Groups Id

Query an AggregationResultGroup resource, which holds data regarding a processed aggregation.

```python
def get_aggregation_result_groups_id(self,
                                    id,
                                    request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource or The Aggregation Result Group ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AggregationResultsGroupsResponseResult`](../../doc/models/aggregation-results-groups-response-result.md).

## Example Usage

```python
id = 't1_arg_66ebb2d6c50b04f8956be00'

request_token = '20250423-yourmerchant-refunds-001'

result = aggregation_result_groups_controller.get_aggregation_result_groups_id(
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
        "id": "t1_arg_66ebb2d6c50b04f8956be00",
        "created": "2024-09-19 01:12:54.8084",
        "modified": "2024-09-19 01:12:54.8084",
        "creator": "t1_log_0092b50e8812b18e41d511s",
        "modifier": "t1_log_0092b50e8812b18e41d511s",
        "aggregation": "t1_agg_66eb3bbb34fcd59400728ba",
        "resource": 27,
        "search": "created[like]={{\"expand\": [{\"type\": \"date\",\"value\": \"-1 days\",\"format\": \"Y-m-d\",\"relativeTimestamp\":\"1726719301\"}]}}%",
        "totals": "sum[0]=amount&count[0]=id&groups[0]=event&groups[1]=isFee",
        "lastModified": "2024-09-19 01:12:54",
        "effective": 202409190010,
        "default": 1,
        "type": "entityEntryEventMerchant",
        "level": "merchant",
        "degrouping": "groups[0]="
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


# Delete Aggregation Result Groups Id

Delete an Aggregation Result Group, which holds data regarding a processed aggregation.

```python
def delete_aggregation_result_groups_id(self,
                                       id,
                                       request_token=None,
                                       search_filter=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource or The Aggregation Result Group ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |
| `search_filter` | `str` | Header, Optional | Set this header to filter or sort the list of resources that the method returns.<br>For example, to find all resources that have a property of 'public' set to '1', set this header to 'public[equals]=1'. You can use the operators 'equals', 'greater', 'less', 'like', 'in' and 'sort'. To sort the resources, use the keywords 'asc' (for an ascending sort) or 'desc' (for a descending sort).<br>You may also use explicit 'and/or' querying by passing arrays of or and arrays of and parameters. For example, to find all resources that have a property of 'public' set to '1' or a property of 'active' set to '0', set this header to 'or[][public][equals]=1&or[][active][equals]=0'. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AggregationResultsGroupsResponseResult`](../../doc/models/aggregation-results-groups-response-result.md).

## Example Usage

```python
id = 't1_arg_66ebb2d6c50b04f8956be00'

request_token = '20250423-yourmerchant-refunds-001'

search_filter = 'created[equals]=2025-01-01'

result = aggregation_result_groups_controller.delete_aggregation_result_groups_id(
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
        "id": "t1_arg_66ebb2d6c50b04f8956be00",
        "created": "2024-09-19 01:12:54.8084",
        "modified": "2024-09-19 01:12:54.8084",
        "creator": "t1_log_0092b50e8812b18e41d511s",
        "modifier": "t1_log_0092b50e8812b18e41d511s",
        "aggregation": "t1_agg_66eb3bbb34fcd59400728ba",
        "resource": 27,
        "search": "created[like]={{\"expand\": [{\"type\": \"date\",\"value\": \"-1 days\",\"format\": \"Y-m-d\",\"relativeTimestamp\":\"1726719301\"}]}}%",
        "totals": "sum[0]=amount&count[0]=id&groups[0]=event&groups[1]=isFee",
        "lastModified": "2024-09-19 01:12:54",
        "effective": 202409190010,
        "default": 1,
        "type": "entityEntryEventMerchant",
        "level": "merchant",
        "degrouping": "groups[0]="
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


# Get Aggregation Result Groups

Query an AggregationResultGroup resource, which holds data regarding a processed aggregation.

```python
def get_aggregation_result_groups(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AggregationResultsGroupsResponseResult`](../../doc/models/aggregation-results-groups-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = aggregation_result_groups_controller.get_aggregation_result_groups(
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
        "id": "t1_arg_66ebb2d6c50b04f8956be00",
        "created": "2024-09-19 01:12:54.8084",
        "modified": "2024-09-19 01:12:54.8084",
        "creator": "t1_log_0092b50e8812b18e41d511s",
        "modifier": "t1_log_0092b50e8812b18e41d511s",
        "aggregation": "t1_agg_66eb3bbb34fcd59400728ba",
        "resource": 27,
        "search": "created[like]={{\"expand\": [{\"type\": \"date\",\"value\": \"-1 days\",\"format\": \"Y-m-d\",\"relativeTimestamp\":\"1726719301\"}]}}%",
        "totals": "sum[0]=amount&count[0]=id&groups[0]=event&groups[1]=isFee",
        "lastModified": "2024-09-19 01:12:54",
        "effective": 202409190010,
        "default": 1,
        "type": "entityEntryEventMerchant",
        "level": "merchant",
        "degrouping": "groups[0]="
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

