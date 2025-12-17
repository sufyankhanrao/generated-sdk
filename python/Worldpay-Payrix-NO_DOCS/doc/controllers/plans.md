# Plans

Resource that represents a recurring type of payment that charges a certain amount on a weekly, monthly, quarterly, or annual basis.

```python
plans_controller = client.plans
```

## Class Name

`PlansController`

## Methods

* [Get Plans Id](../../doc/controllers/plans.md#get-plans-id)
* [Put Plans Id](../../doc/controllers/plans.md#put-plans-id)
* [Delete Plans Id](../../doc/controllers/plans.md#delete-plans-id)
* [Get Plans](../../doc/controllers/plans.md#get-plans)
* [Post Plans](../../doc/controllers/plans.md#post-plans)


# Get Plans Id

Query a Plan that represents a recurring type of payment that charges a certain amount on a weekly, monthly, quarterly, or annual basis, once created, allowing association with a Subscription and user.

```python
def get_plans_id(self,
                id,
                request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this plan. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PlansResponseResult`](../../doc/models/plans-response-result.md).

## Example Usage

```python
id = 'p1_pln_00bdbe193c3abe3b2243695'

request_token = '20250423-yourmerchant-refunds-001'

result = plans_controller.get_plans_id(
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
        "id": "p1_pln_00cb491aa15f9b515c3b59b",
        "created": "2025-03-07 14:29:30.6772",
        "modified": "2025-03-07 14:29:30.6772",
        "creator": "p1_log_000444ad99da5eb18e00207",
        "modifier": "p1_log_000444ad99da5eb18e00207",
        "merchant": "p1_mer_000444add0403c3553f4d20",
        "name": "Lind - Wyman Subscription Plan weekly",
        "description": "regular plan",
        "schedule": 3,
        "scheduleFactor": 1,
        "amount": 9211,
        "inactive": 0,
        "frozen": 0,
        "maxFailures": 2,
        "type": "recurring",
        "txnDescription": "plan txn description",
        "order": "S1 - 1000 - LAST",
        "billing": "p1_bil_00cee36329ead6ae6d31e43",
        "um": "actual"
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


# Put Plans Id

Update a Plan that represents a recurring type of payment that charges a certain amount on a weekly, monthly, quarterly, or annual basis, once created, allowing association with a Subscription and user.

```python
def put_plans_id(self,
                id,
                body,
                request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this plan. |
| `body` | [`PlansPutRequest`](../../doc/models/plans-put-request.md) | Body, Required | Update plan Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PlansResponseResult`](../../doc/models/plans-response-result.md).

## Example Usage

```python
id = 'p1_pln_00bdbe193c3abe3b2243695'

body = PlansPutRequest(
    amount=50000,
    billing='p1_bil_00cee36329ead6ae6d31e43',
    order='S1 - 1000 - LAST',
    txn_description='Payment Plan',
    description='Payment',
    max_failures=2,
    name='Lind - Wyman Subscription Plan weekly',
    schedule=PlanScheduleEnum.DAILY,
    schedule_factor=1,
    um=PlanUmEnum.ACTUAL,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = plans_controller.put_plans_id(
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
        "id": "p1_pln_00cb491aa15f9b515c3b59b",
        "created": "2025-03-07 14:29:30.6772",
        "modified": "2025-03-07 14:29:30.6772",
        "creator": "p1_log_000444ad99da5eb18e00207",
        "modifier": "p1_log_000444ad99da5eb18e00207",
        "merchant": "p1_mer_000444add0403c3553f4d20",
        "name": "Lind - Wyman Subscription Plan weekly",
        "description": "regular plan",
        "schedule": 3,
        "scheduleFactor": 1,
        "amount": 9211,
        "inactive": 0,
        "frozen": 0,
        "maxFailures": 2,
        "type": "recurring",
        "txnDescription": "plan txn description",
        "order": "S1 - 1000 - LAST",
        "billing": "p1_bil_00cee36329ead6ae6d31e43",
        "um": "actual"
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


# Delete Plans Id

Delete a Plan that represents a recurring type of payment that charges a certain amount on a weekly, monthly, quarterly, or annual basis, once created, allowing association with a Subscription and user.

```python
def delete_plans_id(self,
                   id,
                   request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this plan. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PlansResponseResult`](../../doc/models/plans-response-result.md).

## Example Usage

```python
id = 'p1_pln_00bdbe193c3abe3b2243695'

request_token = '20250423-yourmerchant-refunds-001'

result = plans_controller.delete_plans_id(
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
        "id": "p1_pln_00cb491aa15f9b515c3b59b",
        "created": "2025-03-07 14:29:30.6772",
        "modified": "2025-03-07 14:29:30.6772",
        "creator": "p1_log_000444ad99da5eb18e00207",
        "modifier": "p1_log_000444ad99da5eb18e00207",
        "merchant": "p1_mer_000444add0403c3553f4d20",
        "name": "Lind - Wyman Subscription Plan weekly",
        "description": "regular plan",
        "schedule": 3,
        "scheduleFactor": 1,
        "amount": 9211,
        "inactive": 0,
        "frozen": 0,
        "maxFailures": 2,
        "type": "recurring",
        "txnDescription": "plan txn description",
        "order": "S1 - 1000 - LAST",
        "billing": "p1_bil_00cee36329ead6ae6d31e43",
        "um": "actual"
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


# Get Plans

Query a Plan.
A Plan represents a recurring type of payment that charges a certain amount on a weekly, monthly, quarterly, or annual basis.
Once you create a Plan, you can associate a Subscription and user with it.

```python
def get_plans(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PlansResponseResult`](../../doc/models/plans-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = plans_controller.get_plans(
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
        "id": "p1_pln_00cb491aa15f9b515c3b59b",
        "created": "2025-03-07 14:29:30.6772",
        "modified": "2025-03-07 14:29:30.6772",
        "creator": "p1_log_000444ad99da5eb18e00207",
        "modifier": "p1_log_000444ad99da5eb18e00207",
        "merchant": "p1_mer_000444add0403c3553f4d20",
        "name": "Lind - Wyman Subscription Plan weekly",
        "description": "regular plan",
        "schedule": 3,
        "scheduleFactor": 1,
        "amount": 9211,
        "inactive": 0,
        "frozen": 0,
        "maxFailures": 2,
        "type": "recurring",
        "txnDescription": "plan txn description",
        "order": "S1 - 1000 - LAST",
        "billing": "p1_bil_00cee36329ead6ae6d31e43",
        "um": "actual"
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


# Post Plans

Create a Plan that represents a recurring type of payment that charges a certain amount on a weekly, monthly, quarterly, or annual basis, which once created, allows you to associate a Subscription and user with it.

```python
def post_plans(self,
              body,
              request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PlansPostRequest`](../../doc/models/plans-post-request.md) | Body, Required | - |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PlansResponseResult`](../../doc/models/plans-response-result.md).

## Example Usage

```python
body = PlansPostRequest(
    amount=50000,
    merchant='p1_mer_000444add0403c3553f4d20',
    schedule=PlanScheduleEnum.DAILY,
    schedule_factor=1,
    um=PlanUmEnum.ACTUAL,
    mtype=PlanTypeEnum.RECURRING,
    billing='p1_bil_00cee36329ead6ae6d31e43',
    order='S1 - 1000 - LAST',
    txn_description='Payment Plan',
    description='Payment',
    max_failures=2,
    name='Lind - Wyman Subscription Plan weekly',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = plans_controller.post_plans(
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
        "id": "p1_pln_00cb491aa15f9b515c3b59b",
        "created": "2025-03-07 14:29:30.6772",
        "modified": "2025-03-07 14:29:30.6772",
        "creator": "p1_log_000444ad99da5eb18e00207",
        "modifier": "p1_log_000444ad99da5eb18e00207",
        "merchant": "p1_mer_000444add0403c3553f4d20",
        "name": "Lind - Wyman Subscription Plan weekly",
        "description": "regular plan",
        "schedule": 3,
        "scheduleFactor": 1,
        "amount": 9211,
        "inactive": 0,
        "frozen": 0,
        "maxFailures": 2,
        "type": "recurring",
        "txnDescription": "plan txn description",
        "order": "S1 - 1000 - LAST",
        "billing": "p1_bil_00cee36329ead6ae6d31e43",
        "um": "actual"
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

