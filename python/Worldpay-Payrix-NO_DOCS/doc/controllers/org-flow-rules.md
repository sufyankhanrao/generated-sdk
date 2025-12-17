# Org Flow Rules

```python
org_flow_rules_controller = client.org_flow_rules
```

## Class Name

`OrgFlowRulesController`

## Methods

* [Get Org Flow Rules Id](../../doc/controllers/org-flow-rules.md#get-org-flow-rules-id)
* [Put Org Flow Rules Id](../../doc/controllers/org-flow-rules.md#put-org-flow-rules-id)
* [Delete Org Flow Rules Id](../../doc/controllers/org-flow-rules.md#delete-org-flow-rules-id)
* [Get Org Flow Rules](../../doc/controllers/org-flow-rules.md#get-org-flow-rules)
* [Post Org Flow Rules](../../doc/controllers/org-flow-rules.md#post-org-flow-rules)


# Get Org Flow Rules Id

Query an Org Flow Rules resource.

```python
def get_org_flow_rules_id(self,
                         id,
                         request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgFlowRulesResponseResult`](../../doc/models/org-flow-rules-response-result.md).

## Example Usage

```python
id = 't1_ofr_6810c6e4dad2480c7733b00'

request_token = '20250423-yourmerchant-refunds-001'

result = org_flow_rules_controller.get_org_flow_rules_id(
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
        "id": "t1_ofr_6810c6e4dad2480c7733b00",
        "created": "2025-04-29 08:32:36.9093",
        "modified": "2025-04-29 08:37:03.2240",
        "creator": "t1_log_656d51cd565edf13a27c494",
        "modifier": "t1_log_656d51cd565edf13a27c494",
        "orgFlow": "t1_ofw_6810c6cfc7699f50be577dc",
        "name": "test1",
        "description": "test1 description",
        "type": "MCC",
        "value": "5552",
        "grouping": "portalgroup_2",
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


# Put Org Flow Rules Id

Update an Org Flow Rule.

```python
def put_org_flow_rules_id(self,
                         id,
                         body,
                         request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource or The Org Flow Rule ID. |
| `body` | [`OrgFlowRulesPutRequest`](../../doc/models/org-flow-rules-put-request.md) | Body, Required | Update an Org Flow Rule Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgFlowRulesResponseResult`](../../doc/models/org-flow-rules-response-result.md).

## Example Usage

```python
id = 't1_ofr_6810c6e4dad2480c7733b00'

body = OrgFlowRulesPutRequest(
    org_flow='t1_ofr_6810c6e4dad2480c7733b00',
    name='Test1',
    description='Test1 Description',
    mtype=OrgFlowRulesTypeEnum.MCC,
    value='0742',
    grouping='portalgroup_2',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = org_flow_rules_controller.put_org_flow_rules_id(
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
        "id": "t1_ofr_6810c6e4dad2480c7733b00",
        "created": "2025-04-29 08:32:36.9093",
        "modified": "2025-04-29 08:37:03.2240",
        "creator": "t1_log_656d51cd565edf13a27c494",
        "modifier": "t1_log_656d51cd565edf13a27c494",
        "orgFlow": "t1_ofw_6810c6cfc7699f50be577dc",
        "name": "test1",
        "description": "test1 description",
        "type": "MCC",
        "value": "5552",
        "grouping": "portalgroup_2",
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


# Delete Org Flow Rules Id

Delete an Org Flow Rule.

```python
def delete_org_flow_rules_id(self,
                            id,
                            request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgFlowRulesResponseResult`](../../doc/models/org-flow-rules-response-result.md).

## Example Usage

```python
id = 't1_ofr_6810c6e4dad2480c7733b00'

request_token = '20250423-yourmerchant-refunds-001'

result = org_flow_rules_controller.delete_org_flow_rules_id(
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
        "id": "t1_ofr_6810c6e4dad2480c7733b00",
        "created": "2025-04-29 08:32:36.9093",
        "modified": "2025-04-29 08:37:03.2240",
        "creator": "t1_log_656d51cd565edf13a27c494",
        "modifier": "t1_log_656d51cd565edf13a27c494",
        "orgFlow": "t1_ofw_6810c6cfc7699f50be577dc",
        "name": "test1",
        "description": "test1 description",
        "type": "MCC",
        "value": "5552",
        "grouping": "portalgroup_2",
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


# Get Org Flow Rules

Query an orgFlowRules resource.

```python
def get_org_flow_rules(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgFlowRulesResponseResult`](../../doc/models/org-flow-rules-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = org_flow_rules_controller.get_org_flow_rules(
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
        "id": "t1_ofr_6810c6e4dad2480c7733b00",
        "created": "2025-04-29 08:32:36.9093",
        "modified": "2025-04-29 08:37:03.2240",
        "creator": "t1_log_656d51cd565edf13a27c494",
        "modifier": "t1_log_656d51cd565edf13a27c494",
        "orgFlow": "t1_ofw_6810c6cfc7699f50be577dc",
        "name": "test1",
        "description": "test1 description",
        "type": "MCC",
        "value": "5552",
        "grouping": "portalgroup_2",
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


# Post Org Flow Rules

Create an Org Flow Rule.

```python
def post_org_flow_rules(self,
                       body,
                       request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`OrgFlowRulesPostRequest`](../../doc/models/org-flow-rules-post-request.md) | Body, Required | Create Org Flow Rule Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgFlowRulesResponseResult`](../../doc/models/org-flow-rules-response-result.md).

## Example Usage

```python
body = OrgFlowRulesPostRequest(
    org_flow='t1_ofr_6810c6e4dad2480c7733b00',
    name='Test1',
    description='Test1 Description',
    mtype=OrgFlowRulesTypeEnum.MCC,
    value='0742',
    grouping='portalgroup_2',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = org_flow_rules_controller.post_org_flow_rules(
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
        "id": "t1_ofr_6810c6e4dad2480c7733b00",
        "created": "2025-04-29 08:32:36.9093",
        "modified": "2025-04-29 08:37:03.2240",
        "creator": "t1_log_656d51cd565edf13a27c494",
        "modifier": "t1_log_656d51cd565edf13a27c494",
        "orgFlow": "t1_ofw_6810c6cfc7699f50be577dc",
        "name": "test1",
        "description": "test1 description",
        "type": "MCC",
        "value": "5552",
        "grouping": "portalgroup_2",
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

