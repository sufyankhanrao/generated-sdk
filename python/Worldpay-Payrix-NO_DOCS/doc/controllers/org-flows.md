# Org Flows

```python
org_flows_controller = client.org_flows
```

## Class Name

`OrgFlowsController`

## Methods

* [Get Org Flows Id](../../doc/controllers/org-flows.md#get-org-flows-id)
* [Put Org Flows Id](../../doc/controllers/org-flows.md#put-org-flows-id)
* [Delete Org Flows Id](../../doc/controllers/org-flows.md#delete-org-flows-id)
* [Get Org Flows](../../doc/controllers/org-flows.md#get-org-flows)
* [Post Org Flows](../../doc/controllers/org-flows.md#post-org-flows)


# Get Org Flows Id

Query an Org Flow represents a way to trigger the addition or removal of the Merchants associated with a Login to a particular Org, optionally setting this addition or removal to be recursive, affecting all Merchants in any child Logins.

```python
def get_org_flows_id(self,
                    id,
                    request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource, also known as The Org Flow ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgFlowsResponseResult`](../../doc/models/org-flows-response-result.md).

## Example Usage

```python
id = 't1_ofw_67ed51ece84aae1a7d0000z'

request_token = '20250423-yourmerchant-refunds-001'

result = org_flows_controller.get_org_flows_id(
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
        "id": "t1_ofw_67ed51ece84aae1a7d0000z",
        "created": "2025-04-07 09:47:34.4871",
        "modified": "2025-04-07 09:47:34.4871",
        "creator": "t1_log_63335e0e83c545bbb91d9ac",
        "modifier": "t1_log_63335e0e83c545bbb91d9ac",
        "login": "g1577139c2304b7",
        "forlogin": "t1_log_67c203583fbd0a4437d1332",
        "team": "t1_tem_67c202b908935b505104500",
        "division": "t1_div_67c56806728fbbf0bae0b10",
        "recursive": 0,
        "trigger": "create",
        "partition": "t1_ptn_666834d4d504f21414978f5"
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


# Put Org Flows Id

Update an Org Flow. An orgFlows resource represents a way to trigger the addition or removal of the Merchants associated with a Login to a particular Org, optionally set to be recursive, affecting all Merchants in any child Logins.

```python
def put_org_flows_id(self,
                    id,
                    body,
                    request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Org Flow ID. |
| `body` | [`OrgFlowsPutRequest`](../../doc/models/org-flows-put-request.md) | Body, Required | Update an Org Flow Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgFlowsResponseResult`](../../doc/models/org-flows-response-result.md).

## Example Usage

```python
id = 't1_ofw_67ed51ece84aae1a7d0000z'

body = OrgFlowsPutRequest(
    login='g1577139c2304b7',
    trigger=OrgFlowTriggerEnum.CREATE,
    forlogin='t1_log_67c203583fbd0a4437d1332',
    team='t1_tem_67c202b908935b505104500',
    division='t1_div_67c56806728fbbf0bae0b10',
    partition='t1_ptn_666834d4d504f21414978f5'
)

request_token = '20250423-yourmerchant-refunds-001'

result = org_flows_controller.put_org_flows_id(
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
        "id": "t1_ofw_67ed51ece84aae1a7d0000z",
        "created": "2025-04-07 09:47:34.4871",
        "modified": "2025-04-07 09:47:34.4871",
        "creator": "t1_log_63335e0e83c545bbb91d9ac",
        "modifier": "t1_log_63335e0e83c545bbb91d9ac",
        "login": "g1577139c2304b7",
        "forlogin": "t1_log_67c203583fbd0a4437d1332",
        "team": "t1_tem_67c202b908935b505104500",
        "division": "t1_div_67c56806728fbbf0bae0b10",
        "recursive": 0,
        "trigger": "create",
        "partition": "t1_ptn_666834d4d504f21414978f5"
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


# Delete Org Flows Id

Delete an Org Flow.

```python
def delete_org_flows_id(self,
                       id,
                       request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource, also known as The Org Flow ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgFlowsResponseResult`](../../doc/models/org-flows-response-result.md).

## Example Usage

```python
id = 't1_ofw_67ed51ece84aae1a7d0000z'

request_token = '20250423-yourmerchant-refunds-001'

result = org_flows_controller.delete_org_flows_id(
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
        "id": "t1_ofw_67ed51ece84aae1a7d0000z",
        "created": "2025-04-07 09:47:34.4871",
        "modified": "2025-04-07 09:47:34.4871",
        "creator": "t1_log_63335e0e83c545bbb91d9ac",
        "modifier": "t1_log_63335e0e83c545bbb91d9ac",
        "login": "g1577139c2304b7",
        "forlogin": "t1_log_67c203583fbd0a4437d1332",
        "team": "t1_tem_67c202b908935b505104500",
        "division": "t1_div_67c56806728fbbf0bae0b10",
        "recursive": 0,
        "trigger": "create",
        "partition": "t1_ptn_666834d4d504f21414978f5"
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


# Get Org Flows

Query an orgFlows resource.
An orgFlows resource represents a way to trigger the addition or removal of the Merchants associated with a Login to a particular Org.
You can optionally set this addition or removal to be recursive, affecting all Merchants in any child Logins.

```python
def get_org_flows(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgFlowsResponseResult`](../../doc/models/org-flows-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = org_flows_controller.get_org_flows(
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
        "id": "t1_ofw_67ed51ece84aae1a7d0000z",
        "created": "2025-04-07 09:47:34.4871",
        "modified": "2025-04-07 09:47:34.4871",
        "creator": "t1_log_63335e0e83c545bbb91d9ac",
        "modifier": "t1_log_63335e0e83c545bbb91d9ac",
        "login": "g1577139c2304b7",
        "forlogin": "t1_log_67c203583fbd0a4437d1332",
        "team": "t1_tem_67c202b908935b505104500",
        "division": "t1_div_67c56806728fbbf0bae0b10",
        "recursive": 0,
        "trigger": "create",
        "partition": "t1_ptn_666834d4d504f21414978f5"
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


# Post Org Flows

Create an orgFlows resource.
An orgFlows resource represents a way to trigger the addition or removal of the Merchants associated with a Login to a particular Org.
You can optionally set this addition or removal to be recursive, affecting all Merchants in any child Logins.

```python
def post_org_flows(self,
                  body,
                  request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`OrgFlowsPostRequest`](../../doc/models/org-flows-post-request.md) | Body, Required | Create Org Flow Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgFlowsResponseResult`](../../doc/models/org-flows-response-result.md).

## Example Usage

```python
body = OrgFlowsPostRequest(
    login='g1577139c2304b7',
    trigger=OrgFlowTriggerEnum.CREATE,
    forlogin='t1_log_67c203583fbd0a4437d1332',
    team='t1_tem_67c202b908935b505104500',
    division='t1_div_67c56806728fbbf0bae0b10',
    partition='t1_ptn_666834d4d504f21414978f5'
)

request_token = '20250423-yourmerchant-refunds-001'

result = org_flows_controller.post_org_flows(
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
        "id": "t1_ofw_67ed51ece84aae1a7d0000z",
        "created": "2025-04-07 09:47:34.4871",
        "modified": "2025-04-07 09:47:34.4871",
        "creator": "t1_log_63335e0e83c545bbb91d9ac",
        "modifier": "t1_log_63335e0e83c545bbb91d9ac",
        "login": "g1577139c2304b7",
        "forlogin": "t1_log_67c203583fbd0a4437d1332",
        "team": "t1_tem_67c202b908935b505104500",
        "division": "t1_div_67c56806728fbbf0bae0b10",
        "recursive": 0,
        "trigger": "create",
        "partition": "t1_ptn_666834d4d504f21414978f5"
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

