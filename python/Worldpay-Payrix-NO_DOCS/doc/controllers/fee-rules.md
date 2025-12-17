# Fee Rules

```python
fee_rules_controller = client.fee_rules
```

## Class Name

`FeeRulesController`

## Methods

* [Get Fee Rules Id](../../doc/controllers/fee-rules.md#get-fee-rules-id)
* [Put Fee Rules Id](../../doc/controllers/fee-rules.md#put-fee-rules-id)
* [Delete Fee Rules Id](../../doc/controllers/fee-rules.md#delete-fee-rules-id)
* [Get Fee Rules](../../doc/controllers/fee-rules.md#get-fee-rules)
* [Post Fee Rules](../../doc/controllers/fee-rules.md#post-fee-rules)


# Get Fee Rules Id

Query a Fee Rule that makes a Fee apply only in certain circumstances, such as applying an administration charge if a payment is under $50.

```python
def get_fee_rules_id(self,
                    id,
                    request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this fee rule. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`FeeRulesResponseResult`](../../doc/models/fee-rules-response-result.md).

## Example Usage

```python
id = 't1_frl_67ce8623bc70042ef58f400'

request_token = '20250423-yourmerchant-refunds-001'

result = fee_rules_controller.get_fee_rules_id(
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
        "id": "t1_frl_67ce8623bc70042ef58f400",
        "created": "2025-03-10 02:26:43.7799",
        "modified": "2025-03-10 02:26:43.7799",
        "creator": "t1_log_6653ed35b0d6b78d0d02a4d",
        "modifier": "t1_log_6653ed35b0d6b78d0d02a4d",
        "fee": "t1_fee_67ce8623b048d0d5284a886",
        "name": "test1",
        "description": "test1 description",
        "type": 1,
        "application": "both",
        "value": "1",
        "inactive": 0,
        "frozen": 0,
        "grouping": "Fee Rule Group1"
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


# Put Fee Rules Id

Update a Fee Rule that makes a Fee apply only in certain circumstances, for example, applying an administration charge if a payment is under $50.

```python
def put_fee_rules_id(self,
                    id,
                    body,
                    request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this fee rule. |
| `body` | [`FeeRulesPutRequest`](../../doc/models/fee-rules-put-request.md) | Body, Required | Update Fee Rule Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`FeeRulesResponseResult`](../../doc/models/fee-rules-response-result.md).

## Example Usage

```python
id = 't1_frl_67ce8623bc70042ef58f400'

body = FeeRulesPutRequest(
    fee='t1_fee_67ce8623b048d0d5284a886',
    name='Fee Rule1',
    description='Fee Rule',
    mtype=FeeRuleTypeEnum.SALE,
    application=FeeApplicationEnum.BOTH,
    value='1',
    grouping='Fee Rule Group1',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = fee_rules_controller.put_fee_rules_id(
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
        "id": "t1_frl_67ce8623bc70042ef58f400",
        "created": "2025-03-10 02:26:43.7799",
        "modified": "2025-03-10 02:26:43.7799",
        "creator": "t1_log_6653ed35b0d6b78d0d02a4d",
        "modifier": "t1_log_6653ed35b0d6b78d0d02a4d",
        "fee": "t1_fee_67ce8623b048d0d5284a886",
        "name": "test1",
        "description": "test1 description",
        "type": 1,
        "application": "both",
        "value": "1",
        "inactive": 0,
        "frozen": 0,
        "grouping": "Fee Rule Group1"
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


# Delete Fee Rules Id

Delete a Fee Rule that makes a Fee apply only in certain circumstances, such as applying an administration charge if a payment is under $50.

```python
def delete_fee_rules_id(self,
                       id,
                       request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this fee rule. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`FeeRulesResponseResult`](../../doc/models/fee-rules-response-result.md).

## Example Usage

```python
id = 't1_frl_67ce8623bc70042ef58f400'

request_token = '20250423-yourmerchant-refunds-001'

result = fee_rules_controller.delete_fee_rules_id(
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
        "id": "t1_frl_67ce8623bc70042ef58f400",
        "created": "2025-03-10 02:26:43.7799",
        "modified": "2025-03-10 02:26:43.7799",
        "creator": "t1_log_6653ed35b0d6b78d0d02a4d",
        "modifier": "t1_log_6653ed35b0d6b78d0d02a4d",
        "fee": "t1_fee_67ce8623b048d0d5284a886",
        "name": "test1",
        "description": "test1 description",
        "type": 1,
        "application": "both",
        "value": "1",
        "inactive": 0,
        "frozen": 0,
        "grouping": "Fee Rule Group1"
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


# Get Fee Rules

Query a Fee Rule that makes a Fee apply only in certain circumstances, such as applying an administration charge if a payment is under $50.

```python
def get_fee_rules(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`FeeRulesResponseResult`](../../doc/models/fee-rules-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = fee_rules_controller.get_fee_rules(
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
        "id": "t1_frl_67ce8623bc70042ef58f400",
        "created": "2025-03-10 02:26:43.7799",
        "modified": "2025-03-10 02:26:43.7799",
        "creator": "t1_log_6653ed35b0d6b78d0d02a4d",
        "modifier": "t1_log_6653ed35b0d6b78d0d02a4d",
        "fee": "t1_fee_67ce8623b048d0d5284a886",
        "name": "test1",
        "description": "test1 description",
        "type": 1,
        "application": "both",
        "value": "1",
        "inactive": 0,
        "frozen": 0,
        "grouping": "Fee Rule Group1"
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


# Post Fee Rules

Create a conditional Fee Rule that makes fees apply only in certain circumstances, such as applying an administration charge if a payment is under $50.

```python
def post_fee_rules(self,
                  body,
                  request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`FeeRulesPostRequest`](../../doc/models/fee-rules-post-request.md) | Body, Required | Create Fee Rule Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`FeeRulesResponseResult`](../../doc/models/fee-rules-response-result.md).

## Example Usage

```python
body = FeeRulesPostRequest(
    fee='t1_fee_67ce8623b048d0d5284a886',
    mtype=FeeRuleTypeEnum.SALE,
    application=FeeApplicationEnum.BOTH,
    value='1',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    name='Fee Rule1',
    description='Fee Rule',
    grouping='Fee Rule Group1'
)

request_token = '20250423-yourmerchant-refunds-001'

result = fee_rules_controller.post_fee_rules(
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
        "id": "t1_frl_67ce8623bc70042ef58f400",
        "created": "2025-03-10 02:26:43.7799",
        "modified": "2025-03-10 02:26:43.7799",
        "creator": "t1_log_6653ed35b0d6b78d0d02a4d",
        "modifier": "t1_log_6653ed35b0d6b78d0d02a4d",
        "fee": "t1_fee_67ce8623b048d0d5284a886",
        "name": "test1",
        "description": "test1 description",
        "type": 1,
        "application": "both",
        "value": "1",
        "inactive": 0,
        "frozen": 0,
        "grouping": "Fee Rule Group1"
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

