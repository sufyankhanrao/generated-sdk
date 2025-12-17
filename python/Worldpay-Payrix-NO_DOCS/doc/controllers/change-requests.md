# Change Requests

```python
change_requests_controller = client.change_requests
```

## Class Name

`ChangeRequestsController`

## Methods

* [Get Change Requests Id](../../doc/controllers/change-requests.md#get-change-requests-id)
* [Delete Change Requests Id](../../doc/controllers/change-requests.md#delete-change-requests-id)
* [Get Change Requests](../../doc/controllers/change-requests.md#get-change-requests)


# Get Change Requests Id

Query a Change Request.
ChangeRequests is a resource that manages changes to a certain resource.

```python
def get_change_requests_id(self,
                          id,
                          request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ChangeRequestsResponseResult`](../../doc/models/change-requests-response-result.md).

## Example Usage

```python
id = 't1_chr_67461c21ce3bae674b5500a'

request_token = '20250423-yourmerchant-refunds-001'

result = change_requests_controller.get_change_requests_id(
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
        "id": "t1_chr_67461c21ce3bae674b5500a",
        "created": "2024-11-26 14:06:09.8529",
        "modified": "2024-11-26 14:06:10.1982",
        "creator": "t1_log_5c758e990c7a922100d4f36",
        "modifier": "t1_log_5c758e990c7a922100d4f36",
        "deleted": "2024-11-26 14:06:10",
        "login": "t1_log_5c758e990c7a922100d4f36",
        "operation": "update",
        "status": "manualReview",
        "reason": "",
        "changes": "{\"account\":{\"method\":8,\"number\":\"4444\",\"routing\":\"3123\"},\"primary\":1}",
        "model": "accounts",
        "recordId": "t1_act_6491d8a2bbbae477f00e5d0",
        "reasonType": "",
        "analyst": "",
        "reviewed": "2024-11-26 14:06:10",
        "entity": "t1_ent_6491d8a2b75c8b71b1d6c96",
        "authType": 3
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


# Delete Change Requests Id

Delete a Change Request.
ChangeRequests is a resource that manages changes to a certain resource.

```python
def delete_change_requests_id(self,
                             id,
                             request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ChangeRequestsResponseResult`](../../doc/models/change-requests-response-result.md).

## Example Usage

```python
id = 't1_chr_67461c21ce3bae674b5500a'

request_token = '20250423-yourmerchant-refunds-001'

result = change_requests_controller.delete_change_requests_id(
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
        "id": "t1_chr_67461c21ce3bae674b5500a",
        "created": "2024-11-26 14:06:09.8529",
        "modified": "2024-11-26 14:06:10.1982",
        "creator": "t1_log_5c758e990c7a922100d4f36",
        "modifier": "t1_log_5c758e990c7a922100d4f36",
        "deleted": "2024-11-26 14:06:10",
        "login": "t1_log_5c758e990c7a922100d4f36",
        "operation": "update",
        "status": "manualReview",
        "reason": "",
        "changes": "{\"account\":{\"method\":8,\"number\":\"4444\",\"routing\":\"3123\"},\"primary\":1}",
        "model": "accounts",
        "recordId": "t1_act_6491d8a2bbbae477f00e5d0",
        "reasonType": "",
        "analyst": "",
        "reviewed": "2024-11-26 14:06:10",
        "entity": "t1_ent_6491d8a2b75c8b71b1d6c96",
        "authType": 3
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


# Get Change Requests

Query a Change Request.
ChangeRequests is a resource that manages changes to a certain resource.

```python
def get_change_requests(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ChangeRequestsResponseResult`](../../doc/models/change-requests-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = change_requests_controller.get_change_requests(
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
        "id": "t1_chr_67461c21ce3bae674b5500a",
        "created": "2024-11-26 14:06:09.8529",
        "modified": "2024-11-26 14:06:10.1982",
        "creator": "t1_log_5c758e990c7a922100d4f36",
        "modifier": "t1_log_5c758e990c7a922100d4f36",
        "deleted": "2024-11-26 14:06:10",
        "login": "t1_log_5c758e990c7a922100d4f36",
        "operation": "update",
        "status": "manualReview",
        "reason": "",
        "changes": "{\"account\":{\"method\":8,\"number\":\"4444\",\"routing\":\"3123\"},\"primary\":1}",
        "model": "accounts",
        "recordId": "t1_act_6491d8a2bbbae477f00e5d0",
        "reasonType": "",
        "analyst": "",
        "reviewed": "2024-11-26 14:06:10",
        "entity": "t1_ent_6491d8a2b75c8b71b1d6c96",
        "authType": 3
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

