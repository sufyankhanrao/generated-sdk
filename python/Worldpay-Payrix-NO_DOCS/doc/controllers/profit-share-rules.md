# Profit Share Rules

```python
profit_share_rules_controller = client.profit_share_rules
```

## Class Name

`ProfitShareRulesController`

## Methods

* [Get Profit Share Rules Id](../../doc/controllers/profit-share-rules.md#get-profit-share-rules-id)
* [Put Profit Share Rules Id](../../doc/controllers/profit-share-rules.md#put-profit-share-rules-id)
* [Delete Profit Share Rules Id](../../doc/controllers/profit-share-rules.md#delete-profit-share-rules-id)
* [Get Profit Share Rules](../../doc/controllers/profit-share-rules.md#get-profit-share-rules)
* [Post Profit Share Rules](../../doc/controllers/profit-share-rules.md#post-profit-share-rules)


# Get Profit Share Rules Id

Query a ProfitShare Rule, which is a piece of conditional logic that makes a ProfitShare apply only in certain circumstances.

```python
def get_profit_share_rules_id(self,
                             id,
                             request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Profit Share Rule ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ProfitShareRulesResponseResult`](../../doc/models/profit-share-rules-response-result.md).

## Example Usage

```python
id = 't1_psl_63de0f98555d322f0513b00'

request_token = '20250423-yourmerchant-refunds-001'

result = profit_share_rules_controller.get_profit_share_rules_id(
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
        "id": "t1_psl_63de0f98555d322f0513b00",
        "created": "2023-02-04 02:56:08.3497",
        "modified": "2023-02-04 02:56:08.3497",
        "creator": "t1_log_63d25f51ea7ddb271d78304",
        "modifier": "t1_log_63d25f51ea7ddb271d78304",
        "profitShare": "t1_psh_63de0ece4959d9de8194a4d",
        "name": "Test2",
        "description": "Test2",
        "type": "less",
        "value": "5",
        "grouping": "",
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


# Put Profit Share Rules Id

Update a ProfitShare Rule, which is a piece of conditional logic that makes a ProfitShare apply only in certain circumstances.

```python
def put_profit_share_rules_id(self,
                             id,
                             body,
                             request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Profit Share Rule ID. |
| `body` | [`ProfitShareRulesPutRequest`](../../doc/models/profit-share-rules-put-request.md) | Body, Required | Update Profit Share Rule Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ProfitShareRulesResponseResult`](../../doc/models/profit-share-rules-response-result.md).

## Example Usage

```python
id = 't1_psl_63de0f98555d322f0513b00'

body = ProfitShareRulesPutRequest(
    profit_share='t1_psh_63de0ece4959d9de8194a4d',
    name='Test2',
    description='Test2',
    mtype=ProfitShareRuleTypeEnum.LESS,
    value='5',
    grouping='group1',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = profit_share_rules_controller.put_profit_share_rules_id(
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
        "id": "t1_psl_63de0f98555d322f0513b00",
        "created": "2023-02-04 02:56:08.3497",
        "modified": "2023-02-04 02:56:08.3497",
        "creator": "t1_log_63d25f51ea7ddb271d78304",
        "modifier": "t1_log_63d25f51ea7ddb271d78304",
        "profitShare": "t1_psh_63de0ece4959d9de8194a4d",
        "name": "Test2",
        "description": "Test2",
        "type": "less",
        "value": "5",
        "grouping": "",
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


# Delete Profit Share Rules Id

Delete a ProfitShare Rule, which is a piece of conditional logic that makes a ProfitShare apply only in certain circumstances.

```python
def delete_profit_share_rules_id(self,
                                id,
                                request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Profit Share Rule ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ProfitShareRulesResponseResult`](../../doc/models/profit-share-rules-response-result.md).

## Example Usage

```python
id = 't1_psl_63de0f98555d322f0513b00'

request_token = '20250423-yourmerchant-refunds-001'

result = profit_share_rules_controller.delete_profit_share_rules_id(
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
        "id": "t1_psl_63de0f98555d322f0513b00",
        "created": "2023-02-04 02:56:08.3497",
        "modified": "2023-02-04 02:56:08.3497",
        "creator": "t1_log_63d25f51ea7ddb271d78304",
        "modifier": "t1_log_63d25f51ea7ddb271d78304",
        "profitShare": "t1_psh_63de0ece4959d9de8194a4d",
        "name": "Test2",
        "description": "Test2",
        "type": "less",
        "value": "5",
        "grouping": "",
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


# Get Profit Share Rules

Query a ProfitShare Rule.
A ProfitShare Rule is a piece of conditional logic that makes a ProfitShare apply only in certain circumstances.

```python
def get_profit_share_rules(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ProfitShareRulesResponseResult`](../../doc/models/profit-share-rules-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = profit_share_rules_controller.get_profit_share_rules(
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
        "id": "t1_psl_63de0f98555d322f0513b00",
        "created": "2023-02-04 02:56:08.3497",
        "modified": "2023-02-04 02:56:08.3497",
        "creator": "t1_log_63d25f51ea7ddb271d78304",
        "modifier": "t1_log_63d25f51ea7ddb271d78304",
        "profitShare": "t1_psh_63de0ece4959d9de8194a4d",
        "name": "Test2",
        "description": "Test2",
        "type": "less",
        "value": "5",
        "grouping": "",
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


# Post Profit Share Rules

Create a ProfitShare Rule.
A ProfitShare Rule is a piece of conditional logic that makes a ProfitShare apply only in certain circumstances.

```python
def post_profit_share_rules(self,
                           body,
                           request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ProfitShareRulesPostRequest`](../../doc/models/profit-share-rules-post-request.md) | Body, Required | Create Profit Share Rule Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ProfitShareRulesResponseResult`](../../doc/models/profit-share-rules-response-result.md).

## Example Usage

```python
body = ProfitShareRulesPostRequest(
    profit_share='t1_psh_63de0ece4959d9de8194a4d',
    mtype=ProfitShareRuleTypeEnum.LESS,
    value='5',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    name='Test2',
    description='Test2',
    grouping='group1'
)

request_token = '20250423-yourmerchant-refunds-001'

result = profit_share_rules_controller.post_profit_share_rules(
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
        "id": "t1_psl_63de0f98555d322f0513b00",
        "created": "2023-02-04 02:56:08.3497",
        "modified": "2023-02-04 02:56:08.3497",
        "creator": "t1_log_63d25f51ea7ddb271d78304",
        "modifier": "t1_log_63d25f51ea7ddb271d78304",
        "profitShare": "t1_psh_63de0ece4959d9de8194a4d",
        "name": "Test2",
        "description": "Test2",
        "type": "less",
        "value": "5",
        "grouping": "",
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

