# Decision Actions

```python
decision_actions_controller = client.decision_actions
```

## Class Name

`DecisionActionsController`

## Methods

* [Get Decision Actions Id](../../doc/controllers/decision-actions.md#get-decision-actions-id)
* [Put Decision Actions Id](../../doc/controllers/decision-actions.md#put-decision-actions-id)
* [Delete Decision Actions Id](../../doc/controllers/decision-actions.md#delete-decision-actions-id)
* [Get Decision Actions](../../doc/controllers/decision-actions.md#get-decision-actions)
* [Post Decision Actions](../../doc/controllers/decision-actions.md#post-decision-actions)


# Get Decision Actions Id

Query a Decision Action, which is a piece of conditional logic that makes a VerificationResult change the application and the decision action in certain circumstances.

```python
def get_decision_actions_id(self,
                           id,
                           request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Decision Action ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DecisionActionsResponseResult`](../../doc/models/decision-actions-response-result.md).

## Example Usage

```python
id = 't1_dca_67ddc0163f51a4ffd1ea3d0'

request_token = '20250423-yourmerchant-refunds-001'

result = decision_actions_controller.get_decision_actions_id(
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
        "id": "p1_dca_67e284e38e9613fb4b69e6d",
        "created": "2025-03-25 06:26:43.5877",
        "modified": "2025-03-25 06:26:43.5877",
        "creator": "t1_log_61e72ab44fd39df9483aa2c",
        "modifier": "t1_log_61e72ab44fd39df9483aa2c",
        "decision": "t1_dcs_67ddc0163a32ae0c5c33bfc",
        "action": 1,
        "application": "account",
        "scoreType": "low",
        "type": "less",
        "field": "score",
        "score": "20",
        "data": "dummy@dummy.neoncrm.com",
        "message": "Required",
        "code": "I602",
        "grouping": "bademail",
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


# Put Decision Actions Id

Update a Decision Action, which is a piece of conditional logic that makes a VerificationResult change the application and the decision action in certain circumstances.

```python
def put_decision_actions_id(self,
                           id,
                           body,
                           request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Decision Action ID. |
| `body` | [`DecisionActionsPutRequest`](../../doc/models/decision-actions-put-request.md) | Body, Required | Update Decision Action Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DecisionActionsResponseResult`](../../doc/models/decision-actions-response-result.md).

## Example Usage

```python
id = 't1_dca_67ddc0163f51a4ffd1ea3d0'

body = DecisionActionsPutRequest(
    decision='t1_dcs_67ddc0163a32ae0c5c33bfc',
    action=DescisionActionsActionEnum.BLOCK,
    application=ApplicationEnum.ACCOUNT,
    score_type=ScoreTypeEnum.LOW,
    mtype=DecisionActionTypeEnum.LESS,
    field='score',
    score='20',
    data='dummy@dummy.neoncrm.com',
    message='Required',
    code='I602',
    grouping='bademail',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = decision_actions_controller.put_decision_actions_id(
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
        "id": "p1_dca_67e284e38e9613fb4b69e6d",
        "created": "2025-03-25 06:26:43.5877",
        "modified": "2025-03-25 06:26:43.5877",
        "creator": "t1_log_61e72ab44fd39df9483aa2c",
        "modifier": "t1_log_61e72ab44fd39df9483aa2c",
        "decision": "t1_dcs_67ddc0163a32ae0c5c33bfc",
        "action": 1,
        "application": "account",
        "scoreType": "low",
        "type": "less",
        "field": "score",
        "score": "20",
        "data": "dummy@dummy.neoncrm.com",
        "message": "Required",
        "code": "I602",
        "grouping": "bademail",
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


# Delete Decision Actions Id

Delete a Decision Action. A Decision Action is a piece of conditional logic that makes a VerificationResult change the application and the decision action in certain circumstances.

```python
def delete_decision_actions_id(self,
                              id,
                              request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Decision Action ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DecisionActionsResponseResult`](../../doc/models/decision-actions-response-result.md).

## Example Usage

```python
id = 't1_dca_67ddc0163f51a4ffd1ea3d0'

request_token = '20250423-yourmerchant-refunds-001'

result = decision_actions_controller.delete_decision_actions_id(
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
        "id": "p1_dca_67e284e38e9613fb4b69e6d",
        "created": "2025-03-25 06:26:43.5877",
        "modified": "2025-03-25 06:26:43.5877",
        "creator": "t1_log_61e72ab44fd39df9483aa2c",
        "modifier": "t1_log_61e72ab44fd39df9483aa2c",
        "decision": "t1_dcs_67ddc0163a32ae0c5c33bfc",
        "action": 1,
        "application": "account",
        "scoreType": "low",
        "type": "less",
        "field": "score",
        "score": "20",
        "data": "dummy@dummy.neoncrm.com",
        "message": "Required",
        "code": "I602",
        "grouping": "bademail",
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


# Get Decision Actions

Query a Decision Action, A Decision Action is a piece of conditional logic that makes a VerificationResult change the application and the decision action in certain circumstances.

```python
def get_decision_actions(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DecisionActionsResponseResult`](../../doc/models/decision-actions-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = decision_actions_controller.get_decision_actions(
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
        "id": "p1_dca_67e284e38e9613fb4b69e6d",
        "created": "2025-03-25 06:26:43.5877",
        "modified": "2025-03-25 06:26:43.5877",
        "creator": "t1_log_61e72ab44fd39df9483aa2c",
        "modifier": "t1_log_61e72ab44fd39df9483aa2c",
        "decision": "t1_dcs_67ddc0163a32ae0c5c33bfc",
        "action": 1,
        "application": "account",
        "scoreType": "low",
        "type": "less",
        "field": "score",
        "score": "20",
        "data": "dummy@dummy.neoncrm.com",
        "message": "Required",
        "code": "I602",
        "grouping": "bademail",
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


# Post Decision Actions

Create a Decision Action in conjunction with This resource, which is used to further tune the reactions based on conditions defined in the DecisionAction.

```python
def post_decision_actions(self,
                         body,
                         request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DecisionActionsPostRequest`](../../doc/models/decision-actions-post-request.md) | Body, Required | Create Decision Action Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DecisionActionsResponseResult`](../../doc/models/decision-actions-response-result.md).

## Example Usage

```python
body = DecisionActionsPostRequest(
    decision='t1_dcs_67ddc0163a32ae0c5c33bfc',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    action=DescisionActionsActionEnum.BLOCK,
    application=ApplicationEnum.ACCOUNT,
    score_type=ScoreTypeEnum.LOW,
    mtype=DecisionActionTypeEnum.LESS,
    field='score',
    score='20',
    data='dummy@dummy.neoncrm.com',
    message='Required',
    code='I602',
    grouping='bademail'
)

request_token = '20250423-yourmerchant-refunds-001'

result = decision_actions_controller.post_decision_actions(
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
        "id": "p1_dca_67e284e38e9613fb4b69e6d",
        "created": "2025-03-25 06:26:43.5877",
        "modified": "2025-03-25 06:26:43.5877",
        "creator": "t1_log_61e72ab44fd39df9483aa2c",
        "modifier": "t1_log_61e72ab44fd39df9483aa2c",
        "decision": "t1_dcs_67ddc0163a32ae0c5c33bfc",
        "action": 1,
        "application": "account",
        "scoreType": "low",
        "type": "less",
        "field": "score",
        "score": "20",
        "data": "dummy@dummy.neoncrm.com",
        "message": "Required",
        "code": "I602",
        "grouping": "bademail",
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

