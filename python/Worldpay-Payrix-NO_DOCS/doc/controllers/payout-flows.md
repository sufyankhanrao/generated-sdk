# Payout Flows

```python
payout_flows_controller = client.payout_flows
```

## Class Name

`PayoutFlowsController`

## Methods

* [Get Payout Flows Id](../../doc/controllers/payout-flows.md#get-payout-flows-id)
* [Put Payout Flows Id](../../doc/controllers/payout-flows.md#put-payout-flows-id)
* [Delete Payout Flows Id](../../doc/controllers/payout-flows.md#delete-payout-flows-id)
* [Get Payout Flows](../../doc/controllers/payout-flows.md#get-payout-flows)
* [Post Payout Flows](../../doc/controllers/payout-flows.md#post-payout-flows)


# Get Payout Flows Id

Query a payoutFlows resource.
A payoutFlows resource represents a way to set up a Payouts resource automatically for an Entity or Org when it is boarded, or when a bank account is associated.
You can set up the schedule and amount for the Payouts in the payoutFlows resource.

```python
def get_payout_flows_id(self,
                       id,
                       request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this payout flow. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PayoutFlowsResponseResult`](../../doc/models/payout-flows-response-result.md).

## Example Usage

```python
id = 't1_pfw_67e2ff129aad30995408a00'

request_token = '20250423-yourmerchant-refunds-001'

result = payout_flows_controller.get_payout_flows_id(
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
        "id": "t1_pfw_67e2ff129aad30995408a00",
        "created": "2025-03-25 15:08:02.6559",
        "modified": "2025-03-25 15:08:02.6559",
        "creator": "t1_log_673245a79517f80bf2e7738",
        "modifier": "t1_log_673245a79517f80bf2e7738",
        "login": "t1_log_673245a79517f80bf2e7738",
        "payoutLogin": "",
        "org": "t1_org_67b8f82d4f96c5a520ef5c8",
        "entity": "p1_ent_00ce6d2c1f773f68e9cbe00",
        "trigger": "board",
        "schedule": "weeks",
        "scheduleFactor": 1,
        "um": "percent",
        "amount": 10000,
        "minimum": 5000,
        "payoutInactive": 0,
        "skipOffDays": 1,
        "inactive": 0,
        "frozen": 0,
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_006834d4d504f11234578f0",
        "secondaryDescriptor": "",
        "billing": "t1_bil_67d9c8a7df33cf77a3e5e0z",
        "start": 20160120,
        "currency": "USD",
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


# Put Payout Flows Id

Update a payoutFlows resource that represents a way to set up a Payouts resource automatically for an Entity or Org when it is boarded, or when a bank account is associated, allowing you to set up the schedule and amount for the Payouts in the payoutFlows resource.

```python
def put_payout_flows_id(self,
                       id,
                       body,
                       request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this payout flow. |
| `body` | [`PayoutFlowsPutRequest`](../../doc/models/payout-flows-put-request.md) | Body, Required | Update Payout Flow Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PayoutFlowsResponseResult`](../../doc/models/payout-flows-response-result.md).

## Example Usage

```python
id = 't1_pfw_67e2ff129aad30995408a00'

body = PayoutFlowsPutRequest(
    login='t1_log_673245a79517f80bf2e7738',
    payout_login='payoutLogin',
    org='t1_org_67b8f82d4f96c5a520ef5c8',
    entity='p1_ent_00ce6d2c1f773f68e9cbe00',
    billing='t1_bil_67d9c8a7df33cf77a3e5e0z',
    trigger=PayoutFlowTriggerEnum.BOARD,
    schedule=PayoutFlowScheduleEnum.WEEKS,
    schedule_factor=1,
    start=20160120,
    um=PayoutFlowUmEnum.PERCENT,
    amount=10000,
    minimum=5000,
    payout_inactive=PayoutInactiveEnum.INACTIVE,
    skip_off_days=SkipOffDaysEnum.DONOTSKIP,
    secondary_descriptor='Wellness',
    currency=CurrencyEnum.USD,
    same_day=SameDayEnum.DISABLED,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = payout_flows_controller.put_payout_flows_id(
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
        "id": "t1_pfw_67e2ff129aad30995408a00",
        "created": "2025-03-25 15:08:02.6559",
        "modified": "2025-03-25 15:08:02.6559",
        "creator": "t1_log_673245a79517f80bf2e7738",
        "modifier": "t1_log_673245a79517f80bf2e7738",
        "login": "t1_log_673245a79517f80bf2e7738",
        "payoutLogin": "",
        "org": "t1_org_67b8f82d4f96c5a520ef5c8",
        "entity": "p1_ent_00ce6d2c1f773f68e9cbe00",
        "trigger": "board",
        "schedule": "weeks",
        "scheduleFactor": 1,
        "um": "percent",
        "amount": 10000,
        "minimum": 5000,
        "payoutInactive": 0,
        "skipOffDays": 1,
        "inactive": 0,
        "frozen": 0,
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_006834d4d504f11234578f0",
        "secondaryDescriptor": "",
        "billing": "t1_bil_67d9c8a7df33cf77a3e5e0z",
        "start": 20160120,
        "currency": "USD",
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


# Delete Payout Flows Id

Delete a payoutFlows resource that represents a way to set up a Payouts resource automatically for an Entity or Org when it is boarded, or when a bank account is associated, allowing you to set up the schedule and amount for the Payouts in the payoutFlows resource.

```python
def delete_payout_flows_id(self,
                          id,
                          request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this payout flow. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PayoutFlowsResponseResult`](../../doc/models/payout-flows-response-result.md).

## Example Usage

```python
id = 't1_pfw_67e2ff129aad30995408a00'

request_token = '20250423-yourmerchant-refunds-001'

result = payout_flows_controller.delete_payout_flows_id(
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
        "id": "t1_pfw_67e2ff129aad30995408a00",
        "created": "2025-03-25 15:08:02.6559",
        "modified": "2025-03-25 15:08:02.6559",
        "creator": "t1_log_673245a79517f80bf2e7738",
        "modifier": "t1_log_673245a79517f80bf2e7738",
        "login": "t1_log_673245a79517f80bf2e7738",
        "payoutLogin": "",
        "org": "t1_org_67b8f82d4f96c5a520ef5c8",
        "entity": "p1_ent_00ce6d2c1f773f68e9cbe00",
        "trigger": "board",
        "schedule": "weeks",
        "scheduleFactor": 1,
        "um": "percent",
        "amount": 10000,
        "minimum": 5000,
        "payoutInactive": 0,
        "skipOffDays": 1,
        "inactive": 0,
        "frozen": 0,
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_006834d4d504f11234578f0",
        "secondaryDescriptor": "",
        "billing": "t1_bil_67d9c8a7df33cf77a3e5e0z",
        "start": 20160120,
        "currency": "USD",
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


# Get Payout Flows

Query a payoutFlows resource.
A payoutFlows resource represents a way to set up a Payouts resource automatically for an Entity or Org when it is boarded, or when a bank account is associated.
You can set up the schedule and amount for the Payouts in the payoutFlows resource.

```python
def get_payout_flows(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PayoutFlowsResponseResult`](../../doc/models/payout-flows-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = payout_flows_controller.get_payout_flows(
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
        "id": "t1_pfw_67e2ff129aad30995408a00",
        "created": "2025-03-25 15:08:02.6559",
        "modified": "2025-03-25 15:08:02.6559",
        "creator": "t1_log_673245a79517f80bf2e7738",
        "modifier": "t1_log_673245a79517f80bf2e7738",
        "login": "t1_log_673245a79517f80bf2e7738",
        "payoutLogin": "",
        "org": "t1_org_67b8f82d4f96c5a520ef5c8",
        "entity": "p1_ent_00ce6d2c1f773f68e9cbe00",
        "trigger": "board",
        "schedule": "weeks",
        "scheduleFactor": 1,
        "um": "percent",
        "amount": 10000,
        "minimum": 5000,
        "payoutInactive": 0,
        "skipOffDays": 1,
        "inactive": 0,
        "frozen": 0,
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_006834d4d504f11234578f0",
        "secondaryDescriptor": "",
        "billing": "t1_bil_67d9c8a7df33cf77a3e5e0z",
        "start": 20160120,
        "currency": "USD",
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


# Post Payout Flows

Create a payoutFlows resource.
A payoutFlows resource represents a way to set up a Payouts resource automatically for an Entity or Org when it is boarded, or when a bank account is associated.
You can set up the schedule and amount for the Payouts in the payoutFlows resource.

```python
def post_payout_flows(self,
                     body,
                     request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PayoutFlowsPostRequest`](../../doc/models/payout-flows-post-request.md) | Body, Required | Create Payout Flow Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PayoutFlowsResponseResult`](../../doc/models/payout-flows-response-result.md).

## Example Usage

```python
body = PayoutFlowsPostRequest(
    login='t1_log_673245a79517f80bf2e7738',
    trigger=PayoutFlowTriggerEnum.BOARD,
    schedule=PayoutFlowScheduleEnum.WEEKS,
    schedule_factor=1,
    um=PayoutFlowUmEnum.PERCENT,
    amount=10000,
    payout_inactive=PayoutInactiveEnum.INACTIVE,
    skip_off_days=SkipOffDaysEnum.DONOTSKIP,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    payout_login='payoutLogin',
    org='t1_org_67b8f82d4f96c5a520ef5c8',
    entity='p1_ent_00ce6d2c1f773f68e9cbe00',
    billing='t1_bil_67d9c8a7df33cf77a3e5e0z',
    start=20160120,
    minimum=5000,
    secondary_descriptor='Wellness',
    currency=CurrencyEnum.USD,
    same_day=SameDayEnum.DISABLED
)

request_token = '20250423-yourmerchant-refunds-001'

result = payout_flows_controller.post_payout_flows(
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
        "id": "t1_pfw_67e2ff129aad30995408a00",
        "created": "2025-03-25 15:08:02.6559",
        "modified": "2025-03-25 15:08:02.6559",
        "creator": "t1_log_673245a79517f80bf2e7738",
        "modifier": "t1_log_673245a79517f80bf2e7738",
        "login": "t1_log_673245a79517f80bf2e7738",
        "payoutLogin": "",
        "org": "t1_org_67b8f82d4f96c5a520ef5c8",
        "entity": "p1_ent_00ce6d2c1f773f68e9cbe00",
        "trigger": "board",
        "schedule": "weeks",
        "scheduleFactor": 1,
        "um": "percent",
        "amount": 10000,
        "minimum": 5000,
        "payoutInactive": 0,
        "skipOffDays": 1,
        "inactive": 0,
        "frozen": 0,
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_006834d4d504f11234578f0",
        "secondaryDescriptor": "",
        "billing": "t1_bil_67d9c8a7df33cf77a3e5e0z",
        "start": 20160120,
        "currency": "USD",
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

