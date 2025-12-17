# Decision Rules

```python
decision_rules_controller = client.decision_rules
```

## Class Name

`DecisionRulesController`

## Methods

* [Get Decision Rules Id](../../doc/controllers/decision-rules.md#get-decision-rules-id)
* [Put Decision Rules Id](../../doc/controllers/decision-rules.md#put-decision-rules-id)
* [Delete Decision Rules Id](../../doc/controllers/decision-rules.md#delete-decision-rules-id)
* [Get Decision Rules](../../doc/controllers/decision-rules.md#get-decision-rules)
* [Post Decision Rules](../../doc/controllers/decision-rules.md#post-decision-rules)


# Get Decision Rules Id

Query a Decision Rule that makes a Decision apply only in certain circumstances, such as applying an administration charge if a payment is under $50.

```python
def get_decision_rules_id(self,
                         id,
                         request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Decision Rule ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DecisionRulesResponseResult`](../../doc/models/decision-rules-response-result.md).

## Example Usage

```python
id = 't1_drl_67d9836cb20781126c769f0'

request_token = '20250423-yourmerchant-refunds-001'

result = decision_rules_controller.get_decision_rules_id(
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
        "id": "t1_drl_67d9836cb20781126c769f0",
        "created": "2025-03-18 10:30:04.7380",
        "modified": "2025-03-18 10:30:04.7380",
        "creator": "t1_log_5ade08dbe7c74ccfa14e832",
        "modifier": "t1_log_5ade08dbe7c74ccfa14e832",
        "decision": "t1_dcs_67d97ed1a0fc6848c89d537",
        "name": "DecisionRule11",
        "description": "Rule Description",
        "type": "type",
        "value": 8,
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


# Put Decision Rules Id

Update a Decision Rule that makes a Decision apply only in certain circumstances, for example, applying an administration charge if a payment is under $50.

```python
def put_decision_rules_id(self,
                         id,
                         body,
                         request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Decision Rule ID. |
| `body` | [`DecisionRulesPutRequest`](../../doc/models/decision-rules-put-request.md) | Body, Required | Update Decision Rule Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DecisionRulesResponseResult`](../../doc/models/decision-rules-response-result.md).

## Example Usage

```python
id = 't1_drl_67d9836cb20781126c769f0'

body = DecisionRulesPutRequest(
    decision='t1_dcs_67d97ed1a0fc6848c89d537',
    name='DecisionRule11',
    description='Rule Description',
    mtype=DecisionRuleTypeEnum.TYPE,
    value=8,
    grouping='portalgroup_2',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = decision_rules_controller.put_decision_rules_id(
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
        "id": "t1_drl_67d9836cb20781126c769f0",
        "created": "2025-03-18 10:30:04.7380",
        "modified": "2025-03-18 10:30:04.7380",
        "creator": "t1_log_5ade08dbe7c74ccfa14e832",
        "modifier": "t1_log_5ade08dbe7c74ccfa14e832",
        "decision": "t1_dcs_67d97ed1a0fc6848c89d537",
        "name": "DecisionRule11",
        "description": "Rule Description",
        "type": "type",
        "value": 8,
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


# Delete Decision Rules Id

Delete a Decision Rule that makes a Decision apply only in certain circumstances, for example, applying an administration charge if a payment is under $50.

```python
def delete_decision_rules_id(self,
                            id,
                            request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Decision Rule ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DecisionRulesResponseResult`](../../doc/models/decision-rules-response-result.md).

## Example Usage

```python
id = 't1_drl_67d9836cb20781126c769f0'

request_token = '20250423-yourmerchant-refunds-001'

result = decision_rules_controller.delete_decision_rules_id(
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
        "id": "t1_drl_67d9836cb20781126c769f0",
        "created": "2025-03-18 10:30:04.7380",
        "modified": "2025-03-18 10:30:04.7380",
        "creator": "t1_log_5ade08dbe7c74ccfa14e832",
        "modifier": "t1_log_5ade08dbe7c74ccfa14e832",
        "decision": "t1_dcs_67d97ed1a0fc6848c89d537",
        "name": "DecisionRule11",
        "description": "Rule Description",
        "type": "type",
        "value": 8,
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


# Get Decision Rules

Query a Decision Rule; A Decision Rule is a piece of conditional logic that makes a Decision apply only in certain circumstances, For example, a Decision Rule could apply an administration charge if a payment is under $50.

```python
def get_decision_rules(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DecisionRulesResponseResult`](../../doc/models/decision-rules-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = decision_rules_controller.get_decision_rules(
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
        "id": "t1_drl_67d9836cb20781126c769f0",
        "created": "2025-03-18 10:30:04.7380",
        "modified": "2025-03-18 10:30:04.7380",
        "creator": "t1_log_5ade08dbe7c74ccfa14e832",
        "modifier": "t1_log_5ade08dbe7c74ccfa14e832",
        "decision": "t1_dcs_67d97ed1a0fc6848c89d537",
        "name": "DecisionRule11",
        "description": "Rule Description",
        "type": "type",
        "value": 8,
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


# Post Decision Rules

Create a Decision Rule that makes a Decision apply only in certain circumstances, such as applying an administration charge if a payment is under $50.

```python
def post_decision_rules(self,
                       body,
                       request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DecisionRulesPostRequest`](../../doc/models/decision-rules-post-request.md) | Body, Required | Create Decision Rule Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DecisionRulesResponseResult`](../../doc/models/decision-rules-response-result.md).

## Example Usage

```python
body = DecisionRulesPostRequest(
    decision='t1_dcs_67d97ed1a0fc6848c89d537',
    mtype=DecisionRuleTypeEnum.TYPE,
    value=8,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    name='DecisionRule11',
    description='Rule Description',
    grouping='portalgroup_2'
)

request_token = '20250423-yourmerchant-refunds-001'

result = decision_rules_controller.post_decision_rules(
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
        "id": "t1_drl_67d9836cb20781126c769f0",
        "created": "2025-03-18 10:30:04.7380",
        "modified": "2025-03-18 10:30:04.7380",
        "creator": "t1_log_5ade08dbe7c74ccfa14e832",
        "modifier": "t1_log_5ade08dbe7c74ccfa14e832",
        "decision": "t1_dcs_67d97ed1a0fc6848c89d537",
        "name": "DecisionRule11",
        "description": "Rule Description",
        "type": "type",
        "value": 8,
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

