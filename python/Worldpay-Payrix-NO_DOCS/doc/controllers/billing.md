# Billing

The billing deals with billing configuration for an entity, org, division or partition. A billing configuration determines how an entity is billed for their payables within Payrix Pro.

```python
billing_controller = client.billing
```

## Class Name

`BillingController`

## Methods

* [Get Billings Id](../../doc/controllers/billing.md#get-billings-id)
* [Put Billings Id](../../doc/controllers/billing.md#put-billings-id)
* [Delete Billings Id](../../doc/controllers/billing.md#delete-billings-id)
* [Get Billings](../../doc/controllers/billing.md#get-billings)
* [Post Billings](../../doc/controllers/billing.md#post-billings)


# Get Billings Id

Query a Billing that is a means to collect and invoice for any funds owed for a particular period of time, such as setting up a billing to collect fees and create a statement on a monthly basis.

```python
def get_billings_id(self,
                   id,
                   request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Billing ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BillingsResponseResult`](../../doc/models/billings-response-result.md).

## Example Usage

```python
id = 't1_bil_67dbdc94ee1b1a43e6ab400'

request_token = '20250423-yourmerchant-refunds-001'

result = billing_controller.get_billings_id(
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
        "id": "t1_bil_67dbdc94ee1b1a43e6ab400",
        "created": "2025-03-20 05:15:00.9831",
        "modified": "2025-03-20 05:15:00.9831",
        "creator": "t1_log_5cd987a73478a6179b95008",
        "modifier": "t1_log_5cd987a73478a6179b95008",
        "login": "t1_log_5cd987a73478a6179b95008",
        "entity": "t1_ent_5cd987a735c33bab09e7570",
        "org": "t1_org_5b0e08025ec790d3f9b8c00",
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_666834d4d504f21414970z0",
        "description": "Monthly Billing",
        "schedule": "months",
        "scheduleFactor": 1,
        "start": 20250401,
        "finish": 20250401,
        "collection": "entity",
        "collectionFactor": "months",
        "collectionOffset": 1,
        "collectionIncludeCurrent": 0,
        "currency": "USD",
        "inactive": 0,
        "frozen": 0,
        "forentity": "t1_ent_67dbdc7bb6b1dd5dbf396e0"
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


# Put Billings Id

Update a Billing, which is a means to collect and invoice for any funds owed for a particular period of time, such as setting up a billing to collect fees and create a statement on a monthly basis.

```python
def put_billings_id(self,
                   id,
                   body,
                   request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Billing ID. |
| `body` | [`BillingsPutRequest`](../../doc/models/billings-put-request.md) | Body, Required | Update Billing Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BillingsResponseResult`](../../doc/models/billings-response-result.md).

## Example Usage

```python
id = 't1_bil_67dbdc94ee1b1a43e6ab400'

body = BillingsPutRequest(
    login='t1_log_5cd987a73478a6179b95008',
    entity='identifier',
    forentity='t1_ent_67dbdc7bb6b1dd5dbf396e0',
    org='t1_org_5b0e08025ec790d3f9b8c00',
    division='t1_div_67c56806728fbbf0bae0b00',
    partition='t1_ptn_666834d4d504f21414970z0',
    description='Monthly Billing',
    schedule=BillingScheduleEnum.MONTHS,
    schedule_factor=1,
    start=20250401,
    finish=20250401,
    collection=BillingCollectionEnum.ENTITY,
    collection_factor=CollectionFactorEnum.MONTHS,
    collection_offset=1,
    collection_include_current=CollectionIncludeCurrentEnum.EXCLUDECURRENTPERIOD,
    currency=CurrencyEnum.USD,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = billing_controller.put_billings_id(
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
        "id": "t1_bil_67dbdc94ee1b1a43e6ab400",
        "created": "2025-03-20 05:15:00.9831",
        "modified": "2025-03-20 05:15:00.9831",
        "creator": "t1_log_5cd987a73478a6179b95008",
        "modifier": "t1_log_5cd987a73478a6179b95008",
        "login": "t1_log_5cd987a73478a6179b95008",
        "entity": "t1_ent_5cd987a735c33bab09e7570",
        "org": "t1_org_5b0e08025ec790d3f9b8c00",
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_666834d4d504f21414970z0",
        "description": "Monthly Billing",
        "schedule": "months",
        "scheduleFactor": 1,
        "start": 20250401,
        "finish": 20250401,
        "collection": "entity",
        "collectionFactor": "months",
        "collectionOffset": 1,
        "collectionIncludeCurrent": 0,
        "currency": "USD",
        "inactive": 0,
        "frozen": 0,
        "forentity": "t1_ent_67dbdc7bb6b1dd5dbf396e0"
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


# Delete Billings Id

Delete a Billing that is a means to collect and invoice for any funds owed for a particular period of time, such as setting up a billing to collect fees and create a statement on a monthly basis.

```python
def delete_billings_id(self,
                      id,
                      request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Billing ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BillingsResponseResult`](../../doc/models/billings-response-result.md).

## Example Usage

```python
id = 't1_bil_67dbdc94ee1b1a43e6ab400'

request_token = '20250423-yourmerchant-refunds-001'

result = billing_controller.delete_billings_id(
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
        "id": "t1_bil_67dbdc94ee1b1a43e6ab400",
        "created": "2025-03-20 05:15:00.9831",
        "modified": "2025-03-20 05:15:00.9831",
        "creator": "t1_log_5cd987a73478a6179b95008",
        "modifier": "t1_log_5cd987a73478a6179b95008",
        "login": "t1_log_5cd987a73478a6179b95008",
        "entity": "t1_ent_5cd987a735c33bab09e7570",
        "org": "t1_org_5b0e08025ec790d3f9b8c00",
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_666834d4d504f21414970z0",
        "description": "Monthly Billing",
        "schedule": "months",
        "scheduleFactor": 1,
        "start": 20250401,
        "finish": 20250401,
        "collection": "entity",
        "collectionFactor": "months",
        "collectionOffset": 1,
        "collectionIncludeCurrent": 0,
        "currency": "USD",
        "inactive": 0,
        "frozen": 0,
        "forentity": "t1_ent_67dbdc7bb6b1dd5dbf396e0"
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


# Get Billings

Query a Billing is a means to collect and invoice for any funds owed for a particular period of time, such as setting up a billing to collect fees and create a statement on a monthly basis.

```python
def get_billings(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BillingsResponseResult`](../../doc/models/billings-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = billing_controller.get_billings(
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
        "id": "t1_bil_67dbdc94ee1b1a43e6ab400",
        "created": "2025-03-20 05:15:00.9831",
        "modified": "2025-03-20 05:15:00.9831",
        "creator": "t1_log_5cd987a73478a6179b95008",
        "modifier": "t1_log_5cd987a73478a6179b95008",
        "login": "t1_log_5cd987a73478a6179b95008",
        "entity": "t1_ent_5cd987a735c33bab09e7570",
        "org": "t1_org_5b0e08025ec790d3f9b8c00",
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_666834d4d504f21414970z0",
        "description": "Monthly Billing",
        "schedule": "months",
        "scheduleFactor": 1,
        "start": 20250401,
        "finish": 20250401,
        "collection": "entity",
        "collectionFactor": "months",
        "collectionOffset": 1,
        "collectionIncludeCurrent": 0,
        "currency": "USD",
        "inactive": 0,
        "frozen": 0,
        "forentity": "t1_ent_67dbdc7bb6b1dd5dbf396e0"
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


# Post Billings

Create a Billing that is a means to collect and invoice for any funds owed for a particular period of time, such as statement of fees collected on a monthly basis.

```python
def post_billings(self,
                 body,
                 request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`BillingsPostRequest`](../../doc/models/billings-post-request.md) | Body, Required | Create Billing Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BillingsResponseResult`](../../doc/models/billings-response-result.md).

## Example Usage

```python
body = BillingsPostRequest(
    login='t1_log_5cd987a73478a6179b95008',
    entity='identifier',
    schedule=BillingScheduleEnum.MONTHS,
    schedule_factor=1,
    start=20250401,
    collection='entity',
    collection_factor=CollectionFactorEnum.MONTHS,
    collection_offset=1,
    collection_include_current=CollectionIncludeCurrentEnum.EXCLUDECURRENTPERIOD,
    currency=CurrencyEnum.USD,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    forentity='t1_ent_67dbdc7bb6b1dd5dbf396e0',
    org='t1_org_5b0e08025ec790d3f9b8c00',
    division='t1_div_67c56806728fbbf0bae0b00',
    partition='t1_ptn_666834d4d504f21414970z0',
    description='Monthly Billing',
    finish=20250401
)

request_token = '20250423-yourmerchant-refunds-001'

result = billing_controller.post_billings(
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
        "id": "t1_bil_67dbdc94ee1b1a43e6ab400",
        "created": "2025-03-20 05:15:00.9831",
        "modified": "2025-03-20 05:15:00.9831",
        "creator": "t1_log_5cd987a73478a6179b95008",
        "modifier": "t1_log_5cd987a73478a6179b95008",
        "login": "t1_log_5cd987a73478a6179b95008",
        "entity": "t1_ent_5cd987a735c33bab09e7570",
        "org": "t1_org_5b0e08025ec790d3f9b8c00",
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_666834d4d504f21414970z0",
        "description": "Monthly Billing",
        "schedule": "months",
        "scheduleFactor": 1,
        "start": 20250401,
        "finish": 20250401,
        "collection": "entity",
        "collectionFactor": "months",
        "collectionOffset": 1,
        "collectionIncludeCurrent": 0,
        "currency": "USD",
        "inactive": 0,
        "frozen": 0,
        "forentity": "t1_ent_67dbdc7bb6b1dd5dbf396e0"
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

