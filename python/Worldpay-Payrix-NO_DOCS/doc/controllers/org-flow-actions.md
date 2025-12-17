# Org Flow Actions

```python
org_flow_actions_controller = client.org_flow_actions
```

## Class Name

`OrgFlowActionsController`

## Methods

* [Get Org Flow Actions Id](../../doc/controllers/org-flow-actions.md#get-org-flow-actions-id)
* [Put Org Flow Actions Id](../../doc/controllers/org-flow-actions.md#put-org-flow-actions-id)
* [Delete Org Flow Actions Id](../../doc/controllers/org-flow-actions.md#delete-org-flow-actions-id)
* [Get Org Flow Actions](../../doc/controllers/org-flow-actions.md#get-org-flow-actions)
* [Post Org Flow Actions](../../doc/controllers/org-flow-actions.md#post-org-flow-actions)


# Get Org Flow Actions Id

Query an Org Flow Actions resource.

```python
def get_org_flow_actions_id(self,
                           id,
                           request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource or The Org Flow Action ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgFlowActionsResponseResult`](../../doc/models/org-flow-actions-response-result.md).

## Example Usage

```python
id = 't1_ofa_67ed51ecf3330d5d808000z'

request_token = '20250423-yourmerchant-refunds-001'

result = org_flow_actions_controller.get_org_flow_actions_id(
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
        "id": "t1_ofa_67ed51ecf3330d5d808000z",
        "created": "2025-04-02 11:04:13.0043",
        "modified": "2025-04-02 11:04:13.0043",
        "creator": "t1_log_63335e0e83c545bbb91d9ac",
        "modifier": "t1_log_63335e0e83c545bbb91d9ac",
        "orgFlow": "t1_ofw_67ed51ece84aae1a7d0783z",
        "org": "t1_org_67c89c538efe67fbf018d00",
        "action": "add"
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


# Put Org Flow Actions Id

Update an Org Flow Action.

```python
def put_org_flow_actions_id(self,
                           id,
                           body,
                           request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource or The Org Flow Action ID. |
| `body` | [`OrgFlowActionsPutRequest`](../../doc/models/org-flow-actions-put-request.md) | Body, Required | Update an Org Flow Action Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgFlowActionsResponseResult`](../../doc/models/org-flow-actions-response-result.md).

## Example Usage

```python
id = 't1_ofa_67ed51ecf3330d5d808000z'

body = OrgFlowActionsPutRequest(
    org_flow='t1_ofw_67ed51ece84aae1a7d0783z',
    org='t1_org_67c89c538efe67fbf018d00',
    action=OrgFlowActionEnum.ADD
)

request_token = '20250423-yourmerchant-refunds-001'

result = org_flow_actions_controller.put_org_flow_actions_id(
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
        "id": "t1_ofa_67ed51ecf3330d5d808000z",
        "created": "2025-04-02 11:04:13.0043",
        "modified": "2025-04-02 11:04:13.0043",
        "creator": "t1_log_63335e0e83c545bbb91d9ac",
        "modifier": "t1_log_63335e0e83c545bbb91d9ac",
        "orgFlow": "t1_ofw_67ed51ece84aae1a7d0783z",
        "org": "t1_org_67c89c538efe67fbf018d00",
        "action": "add"
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


# Delete Org Flow Actions Id

Delete an Org Flow Action.

```python
def delete_org_flow_actions_id(self,
                              id,
                              request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource or The Org Flow Action ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgFlowActionsResponseResult`](../../doc/models/org-flow-actions-response-result.md).

## Example Usage

```python
id = 't1_ofa_67ed51ecf3330d5d808000z'

request_token = '20250423-yourmerchant-refunds-001'

result = org_flow_actions_controller.delete_org_flow_actions_id(
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
        "id": "t1_ofa_67ed51ecf3330d5d808000z",
        "created": "2025-04-02 11:04:13.0043",
        "modified": "2025-04-02 11:04:13.0043",
        "creator": "t1_log_63335e0e83c545bbb91d9ac",
        "modifier": "t1_log_63335e0e83c545bbb91d9ac",
        "orgFlow": "t1_ofw_67ed51ece84aae1a7d0783z",
        "org": "t1_org_67c89c538efe67fbf018d00",
        "action": "add"
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


# Get Org Flow Actions

Query an orgFlowActions resource.
An orgFlowActions resource lets you add an Entity defined in the associated orgFlow to an Org, or remove an Entity identified in the same way from an Org.

```python
def get_org_flow_actions(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgFlowActionsResponseResult`](../../doc/models/org-flow-actions-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = org_flow_actions_controller.get_org_flow_actions(
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
        "id": "t1_ofa_67ed51ecf3330d5d808000z",
        "created": "2025-04-02 11:04:13.0043",
        "modified": "2025-04-02 11:04:13.0043",
        "creator": "t1_log_63335e0e83c545bbb91d9ac",
        "modifier": "t1_log_63335e0e83c545bbb91d9ac",
        "orgFlow": "t1_ofw_67ed51ece84aae1a7d0783z",
        "org": "t1_org_67c89c538efe67fbf018d00",
        "action": "add"
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


# Post Org Flow Actions

Create an Org Flow Action that lets you add an Entity defined in the associated orgFlow to an Org, or remove an Entity identified in the same way from an Org.

```python
def post_org_flow_actions(self,
                         body,
                         request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`OrgFlowActionsPostRequest`](../../doc/models/org-flow-actions-post-request.md) | Body, Required | Create Org Flow Action Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgFlowActionsResponseResult`](../../doc/models/org-flow-actions-response-result.md).

## Example Usage

```python
body = OrgFlowActionsPostRequest(
    org_flow='t1_ofw_67ed51ece84aae1a7d0783z',
    org='t1_org_67c89c538efe67fbf018d00',
    action=OrgFlowActionEnum.ADD
)

request_token = '20250423-yourmerchant-refunds-001'

result = org_flow_actions_controller.post_org_flow_actions(
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
        "id": "t1_ofa_67ed51ecf3330d5d808000z",
        "created": "2025-04-02 11:04:13.0043",
        "modified": "2025-04-02 11:04:13.0043",
        "creator": "t1_log_63335e0e83c545bbb91d9ac",
        "modifier": "t1_log_63335e0e83c545bbb91d9ac",
        "orgFlow": "t1_ofw_67ed51ece84aae1a7d0783z",
        "org": "t1_org_67c89c538efe67fbf018d00",
        "action": "add"
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

