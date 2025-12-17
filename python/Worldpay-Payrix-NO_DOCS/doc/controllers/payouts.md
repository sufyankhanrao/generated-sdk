# Payouts

Resource that tracks details that allow a Disbursement to be paid or debited.

```python
payouts_controller = client.payouts
```

## Class Name

`PayoutsController`

## Methods

* [Get Payouts Id](../../doc/controllers/payouts.md#get-payouts-id)
* [Put Payouts Id](../../doc/controllers/payouts.md#put-payouts-id)
* [Delete Payouts Id](../../doc/controllers/payouts.md#delete-payouts-id)
* [Get Payouts](../../doc/controllers/payouts.md#get-payouts)
* [Post Payouts](../../doc/controllers/payouts.md#post-payouts)


# Get Payouts Id

Query a Payout. A Payout is a resource that represents all the details that allow a Disbursement to be paid or debited; these details include the schedule or trigger, the beneficiary account and the amount.

```python
def get_payouts_id(self,
                  id,
                  request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this payout. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PayoutsResponseResult`](../../doc/models/payouts-response-result.md).

## Example Usage

```python
id = 'p1_pay_00ce7e77b58ffe7d31b250e'

request_token = '20250423-yourmerchant-refunds-001'

result = payouts_controller.get_payouts_id(
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
        "id": "p1_pay_00ce6d57cf453b53a8b5d19",
        "created": "2025-03-10 00:40:55.8743",
        "modified": "2025-03-10 00:40:55.8743",
        "creator": "p1_log_0a4e8c7d3a625ed0f4ee1e0",
        "modifier": "p1_log_0a4e8c7d3a625ed0f4ee1e0",
        "login": "p1_log_0a4e8c7d3a625ed0f4ee1e0",
        "account": "8ccbda671ad9463f2d7cab3119010000",
        "entity": "p1_ent_00ce6d2c1f773f68e9cbe05",
        "billing": "p1_bil_0078b6a1899f8d14f58d7c5",
        "payoutFlow": "p1_pfw_000f0148a5d61a4dec3f108",
        "name": "Automatically generated payout schedule",
        "description": "payout schedule description",
        "schedule": 1,
        "scheduleFactor": 1,
        "start": 20250312,
        "currency": "USD",
        "um": 1,
        "amount": 100,
        "minimum": 10,
        "maximum": 100,
        "float": 0,
        "secondaryDescriptor": "Wellness",
        "skipOffDays": 0,
        "inactive": 0,
        "frozen": 0,
        "sameDay": 0
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


# Put Payouts Id

Update a Payout. A Payout is a resource that represents all the details that allow a Disbursement to be paid or debited. These details include the schedule or trigger, the beneficiary account and the amount.

```python
def put_payouts_id(self,
                  id,
                  body,
                  request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this payout. |
| `body` | [`PayoutPutRequest`](../../doc/models/payout-put-request.md) | Body, Required | Update Payout Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PayoutsResponseResult`](../../doc/models/payouts-response-result.md).

## Example Usage

```python
id = 'p1_pay_00ce7e77b58ffe7d31b250e'

body = PayoutPutRequest(
    login='p1_log_0af4e8c7d3a625ed0f4ee1e0',
    account='8ccbda671ad9463f2d7cab3119010000',
    entity='p1_ent_00ce6d2c1f773f68e9cbe05',
    billing='p1_bil_0078b6a1899f8d14f58d7c5',
    payout_flow='p1_pfw_000f0148a5d61a4dec3f108',
    name='Automatically generated payout schedule',
    description='payout schedule description',
    schedule=PayoutScheduleEnum.DAILY,
    schedule_factor=1,
    start=20250312,
    currency=CurrencyEnum.USD,
    um=PayoutUmEnum.PERCENTAGE,
    amount=100,
    minimum=0,
    maximum=0,
    float=0,
    secondary_descriptor='Wellness',
    skip_off_days=SkipOffDaysEnum.DONOTSKIP,
    same_day=SameDayEnum.DISABLED,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = payouts_controller.put_payouts_id(
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
        "id": "p1_pay_00ce6d57cf453b53a8b5d19",
        "created": "2025-03-10 00:40:55.8743",
        "modified": "2025-03-10 00:40:55.8743",
        "creator": "p1_log_0a4e8c7d3a625ed0f4ee1e0",
        "modifier": "p1_log_0a4e8c7d3a625ed0f4ee1e0",
        "login": "p1_log_0a4e8c7d3a625ed0f4ee1e0",
        "account": "8ccbda671ad9463f2d7cab3119010000",
        "entity": "p1_ent_00ce6d2c1f773f68e9cbe05",
        "billing": "p1_bil_0078b6a1899f8d14f58d7c5",
        "payoutFlow": "p1_pfw_000f0148a5d61a4dec3f108",
        "name": "Automatically generated payout schedule",
        "description": "payout schedule description",
        "schedule": 1,
        "scheduleFactor": 1,
        "start": 20250312,
        "currency": "USD",
        "um": 1,
        "amount": 100,
        "minimum": 10,
        "maximum": 100,
        "float": 0,
        "secondaryDescriptor": "Wellness",
        "skipOffDays": 0,
        "inactive": 0,
        "frozen": 0,
        "sameDay": 0
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


# Delete Payouts Id

Delete a Payout. A Payout is a resource that represents all the details that allow a Disbursement to be paid or debited. These details include the schedule or trigger, the beneficiary account and the amount.

```python
def delete_payouts_id(self,
                     id,
                     request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this payout. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PayoutsResponseResult`](../../doc/models/payouts-response-result.md).

## Example Usage

```python
id = 'p1_pay_00ce7e77b58ffe7d31b250e'

request_token = '20250423-yourmerchant-refunds-001'

result = payouts_controller.delete_payouts_id(
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
        "id": "p1_pay_00ce6d57cf453b53a8b5d19",
        "created": "2025-03-10 00:40:55.8743",
        "modified": "2025-03-10 00:40:55.8743",
        "creator": "p1_log_0a4e8c7d3a625ed0f4ee1e0",
        "modifier": "p1_log_0a4e8c7d3a625ed0f4ee1e0",
        "login": "p1_log_0a4e8c7d3a625ed0f4ee1e0",
        "account": "8ccbda671ad9463f2d7cab3119010000",
        "entity": "p1_ent_00ce6d2c1f773f68e9cbe05",
        "billing": "p1_bil_0078b6a1899f8d14f58d7c5",
        "payoutFlow": "p1_pfw_000f0148a5d61a4dec3f108",
        "name": "Automatically generated payout schedule",
        "description": "payout schedule description",
        "schedule": 1,
        "scheduleFactor": 1,
        "start": 20250312,
        "currency": "USD",
        "um": 1,
        "amount": 100,
        "minimum": 10,
        "maximum": 100,
        "float": 0,
        "secondaryDescriptor": "Wellness",
        "skipOffDays": 0,
        "inactive": 0,
        "frozen": 0,
        "sameDay": 0
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


# Get Payouts

Query a Payout. A Payout is a resource that represents all the details that allow a Disbursement to be paid or debited. These details include the schedule or trigger, the beneficiary account and the amount.

```python
def get_payouts(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PayoutsResponseResult`](../../doc/models/payouts-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = payouts_controller.get_payouts(
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
        "id": "p1_pay_00ce6d57cf453b53a8b5d19",
        "created": "2025-03-10 00:40:55.8743",
        "modified": "2025-03-10 00:40:55.8743",
        "creator": "p1_log_0a4e8c7d3a625ed0f4ee1e0",
        "modifier": "p1_log_0a4e8c7d3a625ed0f4ee1e0",
        "login": "p1_log_0a4e8c7d3a625ed0f4ee1e0",
        "account": "8ccbda671ad9463f2d7cab3119010000",
        "entity": "p1_ent_00ce6d2c1f773f68e9cbe05",
        "billing": "p1_bil_0078b6a1899f8d14f58d7c5",
        "payoutFlow": "p1_pfw_000f0148a5d61a4dec3f108",
        "name": "Automatically generated payout schedule",
        "description": "payout schedule description",
        "schedule": 1,
        "scheduleFactor": 1,
        "start": 20250312,
        "currency": "USD",
        "um": 1,
        "amount": 100,
        "minimum": 10,
        "maximum": 100,
        "float": 0,
        "secondaryDescriptor": "Wellness",
        "skipOffDays": 0,
        "inactive": 0,
        "frozen": 0,
        "sameDay": 0
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


# Post Payouts

Create a Payout. A Payout is a resource that represents all the details that allow a Disbursement to be paid or debited; these details include the schedule or trigger, the beneficiary account and the amount.

```python
def post_payouts(self,
                body,
                request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PayoutPostRequest`](../../doc/models/payout-post-request.md) | Body, Required | Create Payout Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PayoutsResponseResult`](../../doc/models/payouts-response-result.md).

## Example Usage

```python
body = PayoutPostRequest(
    account='8ccbda671ad9463f2d7cab3119010000',
    entity='p1_ent_00ce6d2c1f773f68e9cbe05',
    schedule=PayoutScheduleEnum.DAILY,
    schedule_factor=1,
    start=20250312,
    um=PayoutUmEnum.PERCENTAGE,
    amount=100,
    float=0,
    skip_off_days=SkipOffDaysEnum.DONOTSKIP,
    same_day=SameDayEnum.DISABLED,
    login='p1_log_0af4e8c7d3a625ed0f4ee1e0',
    billing='p1_bil_0078b6a1899f8d14f58d7c5',
    payout_flow='p1_pfw_000f0148a5d61a4dec3f108',
    name='Automatically generated payout schedule',
    description='payout schedule description',
    currency=CurrencyEnum.USD,
    minimum=0,
    maximum=0,
    secondary_descriptor='Wellness',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = payouts_controller.post_payouts(
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
        "id": "p1_pay_00ce6d57cf453b53a8b5d19",
        "created": "2025-03-10 00:40:55.8743",
        "modified": "2025-03-10 00:40:55.8743",
        "creator": "p1_log_0a4e8c7d3a625ed0f4ee1e0",
        "modifier": "p1_log_0a4e8c7d3a625ed0f4ee1e0",
        "login": "p1_log_0a4e8c7d3a625ed0f4ee1e0",
        "account": "8ccbda671ad9463f2d7cab3119010000",
        "entity": "p1_ent_00ce6d2c1f773f68e9cbe05",
        "billing": "p1_bil_0078b6a1899f8d14f58d7c5",
        "payoutFlow": "p1_pfw_000f0148a5d61a4dec3f108",
        "name": "Automatically generated payout schedule",
        "description": "payout schedule description",
        "schedule": 1,
        "scheduleFactor": 1,
        "start": 20250312,
        "currency": "USD",
        "um": 1,
        "amount": 100,
        "minimum": 10,
        "maximum": 100,
        "float": 0,
        "secondaryDescriptor": "Wellness",
        "skipOffDays": 0,
        "inactive": 0,
        "frozen": 0,
        "sameDay": 0
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

