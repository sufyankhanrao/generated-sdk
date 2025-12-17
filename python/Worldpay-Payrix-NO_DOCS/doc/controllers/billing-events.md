# Billing Events

```python
billing_events_controller = client.billing_events
```

## Class Name

`BillingEventsController`

## Methods

* [Get Billing Events Id](../../doc/controllers/billing-events.md#get-billing-events-id)
* [Put Billing Events Id](../../doc/controllers/billing-events.md#put-billing-events-id)
* [Delete Billing Events Id](../../doc/controllers/billing-events.md#delete-billing-events-id)
* [Get Billing Events](../../doc/controllers/billing-events.md#get-billing-events)
* [Post Billing Events](../../doc/controllers/billing-events.md#post-billing-events)


# Get Billing Events Id

Query a Billing Event.

```python
def get_billing_events_id(self,
                         id,
                         request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this billing event. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BillingEventsResponseResult`](../../doc/models/billing-events-response-result.md).

## Example Usage

```python
id = 't1_ble_67d9cfac3d58e3fe0414bf0'

request_token = '20250423-yourmerchant-refunds-001'

result = billing_events_controller.get_billing_events_id(
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
        "id": "t1_ble_67d9cfac3d58e3fe0414bf0",
        "created": "2025-03-18 15:55:24.2661",
        "modified": "2025-03-18 15:55:24.2661",
        "creator": "t1_log_5d49bbb9bd62b95c1320003",
        "modifier": "t1_log_5d49bbb9bd62b95c1320003",
        "billing": "t1_bil_67d9cfac37cb75f7c8e0597",
        "event": "fees",
        "eventSchedule": "",
        "deductFromBalance": 0,
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


# Put Billing Events Id

Update a Billing Event.

```python
def put_billing_events_id(self,
                         id,
                         body,
                         request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this billing event. |
| `body` | [`BillingEventsPutRequest`](../../doc/models/billing-events-put-request.md) | Body, Required | Update Billing Event Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BillingEventsResponseResult`](../../doc/models/billing-events-response-result.md).

## Example Usage

```python
id = 't1_ble_67d9cfac3d58e3fe0414bf0'

body = BillingEventsPutRequest(
    billing='t1_bil_67d9cfac37cb75f7c8e0597',
    event=BillingEventEnum.FEES,
    event_schedule='record ID',
    deduct_from_balance=DeductFromBalanceEnum.DONOTDEDUCT,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = billing_events_controller.put_billing_events_id(
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
        "id": "t1_ble_67d9cfac3d58e3fe0414bf0",
        "created": "2025-03-18 15:55:24.2661",
        "modified": "2025-03-18 15:55:24.2661",
        "creator": "t1_log_5d49bbb9bd62b95c1320003",
        "modifier": "t1_log_5d49bbb9bd62b95c1320003",
        "billing": "t1_bil_67d9cfac37cb75f7c8e0597",
        "event": "fees",
        "eventSchedule": "",
        "deductFromBalance": 0,
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


# Delete Billing Events Id

Delete a Billing Event.

```python
def delete_billing_events_id(self,
                            id,
                            request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this billing event. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BillingEventsResponseResult`](../../doc/models/billing-events-response-result.md).

## Example Usage

```python
id = 't1_ble_67d9cfac3d58e3fe0414bf0'

request_token = '20250423-yourmerchant-refunds-001'

result = billing_events_controller.delete_billing_events_id(
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
        "id": "t1_ble_67d9cfac3d58e3fe0414bf0",
        "created": "2025-03-18 15:55:24.2661",
        "modified": "2025-03-18 15:55:24.2661",
        "creator": "t1_log_5d49bbb9bd62b95c1320003",
        "modifier": "t1_log_5d49bbb9bd62b95c1320003",
        "billing": "t1_bil_67d9cfac37cb75f7c8e0597",
        "event": "fees",
        "eventSchedule": "",
        "deductFromBalance": 0,
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


# Get Billing Events

Querying Billing Events.

```python
def get_billing_events(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BillingEventsResponseResult`](../../doc/models/billing-events-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = billing_events_controller.get_billing_events(
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
        "id": "t1_ble_67d9cfac3d58e3fe0414bf0",
        "created": "2025-03-18 15:55:24.2661",
        "modified": "2025-03-18 15:55:24.2661",
        "creator": "t1_log_5d49bbb9bd62b95c1320003",
        "modifier": "t1_log_5d49bbb9bd62b95c1320003",
        "billing": "t1_bil_67d9cfac37cb75f7c8e0597",
        "event": "fees",
        "eventSchedule": "",
        "deductFromBalance": 0,
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


# Post Billing Events

Create a billingEvents.

```python
def post_billing_events(self,
                       body,
                       request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`BillingEventsPostRequest`](../../doc/models/billing-events-post-request.md) | Body, Required | Create Billing Event Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BillingEventsResponseResult`](../../doc/models/billing-events-response-result.md).

## Example Usage

```python
body = BillingEventsPostRequest(
    billing='t1_bil_67d9cfac37cb75f7c8e0597',
    event=BillingEventEnum.FEES,
    deduct_from_balance=DeductFromBalanceEnum.DONOTDEDUCT,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    event_schedule='record ID'
)

request_token = '20250423-yourmerchant-refunds-001'

result = billing_events_controller.post_billing_events(
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
        "id": "t1_ble_67d9cfac3d58e3fe0414bf0",
        "created": "2025-03-18 15:55:24.2661",
        "modified": "2025-03-18 15:55:24.2661",
        "creator": "t1_log_5d49bbb9bd62b95c1320003",
        "modifier": "t1_log_5d49bbb9bd62b95c1320003",
        "billing": "t1_bil_67d9cfac37cb75f7c8e0597",
        "event": "fees",
        "eventSchedule": "",
        "deductFromBalance": 0,
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

