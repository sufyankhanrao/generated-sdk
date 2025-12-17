# Fees

Fees are costs for specific timeframes elapsing, such as weekly, or monthly; or as actions taking place, such as a transaction authorization, Merchant onboarding, or chargeback management. These fees are assessed by a Partner or Facilitator to their child entities (such as Partner to Merchant, or Facilitator to Partner or Merchant) when specified actions have occurred or a time interval has elapsed.

```python
fees_controller = client.fees
```

## Class Name

`FeesController`

## Methods

* [Get Fees Id](../../doc/controllers/fees.md#get-fees-id)
* [Put Fees Id](../../doc/controllers/fees.md#put-fees-id)
* [Delete Fees Id](../../doc/controllers/fees.md#delete-fees-id)
* [Get Fees](../../doc/controllers/fees.md#get-fees)
* [Post Fees](../../doc/controllers/fees.md#post-fees)


# Get Fees Id

Query a Fee that is an amount one Entity can charge another Entity according to a particular schedule, or based on certain events.

```python
def get_fees_id(self,
               id,
               request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Fee ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`FeesResponseResult`](../../doc/models/fees-response-result.md).

## Example Usage

```python
id = 't1_fee_67b5422dda39a7c36059988'

request_token = '20250423-yourmerchant-refunds-001'

result = fees_controller.get_fees_id(
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
        "id": "t1_fee_67b5422dda39a7c36059988",
        "created": "2025-02-18 21:30:05.9053",
        "modified": "2025-02-18 21:30:05.9053",
        "creator": "t1_log_0a008e990c7a922100d4f00",
        "modifier": "t1_log_0a008e990c7a922100d4f00",
        "entity": "t1_ent_00758e990d7437d51cdf1aa",
        "forentity": "t1_ent_0088c831a31ca8841c81111",
        "org": "t1_org_00b2ac11ed8bed97fb81111",
        "partition": "t1_ptn_000111d4d504f21414978f0",
        "type": 1,
        "name": "Boarding Fee",
        "description": "Boarding Fee",
        "schedule": 5,
        "scheduleFactor": 1,
        "start": 20160120,
        "finish": 20160120,
        "collection": 2,
        "collectionFactor": 2,
        "collectionOffset": 5,
        "um": 2,
        "amount": 45,
        "currency": "USD",
        "inactive": 0,
        "frozen": 0,
        "txnFee": 0,
        "collectionIncludeCurrent": 0,
        "maximum": 30
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


# Put Fees Id

Update a Fee that is an amount one Entity can charge another Entity according to a particular schedule, or based on certain events.

```python
def put_fees_id(self,
               id,
               body,
               request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Fee ID. |
| `body` | [`FeesPutRequest`](../../doc/models/fees-put-request.md) | Body, Required | Update Fee Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`FeesResponseResult`](../../doc/models/fees-response-result.md).

## Example Usage

```python
id = 't1_fee_67b5422dda39a7c36059988'

body = FeesPutRequest(
    entity='t1_ent_00758e990d7437d51cdf1aa',
    forentity='t1_ent_0088c831a31ca8841c81111',
    org='t1_org_00b2ac11ed8bed97fb81111',
    mtype=FeeTypeEnum.FEE,
    name='Boarding Fee',
    description='Boarding Fee',
    schedule=FeeScheduleEnum.ENUM_5,
    schedule_factor=1,
    start=20160120,
    finish=21160120,
    collection=FeeCollectionEnum.TXNTAXID,
    collection_factor=2,
    collection_offset=5,
    collection_include_current=0,
    um=FeeUmEnum.ACTUAL,
    amount=5,
    maximum=30,
    currency=CurrencyEnum.USD,
    txn_fee=TxnFeeEnum.DISABLED,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = fees_controller.put_fees_id(
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
        "id": "t1_fee_67b5422dda39a7c36059988",
        "created": "2025-02-18 21:30:05.9053",
        "modified": "2025-02-18 21:30:05.9053",
        "creator": "t1_log_0a008e990c7a922100d4f00",
        "modifier": "t1_log_0a008e990c7a922100d4f00",
        "entity": "t1_ent_00758e990d7437d51cdf1aa",
        "forentity": "t1_ent_0088c831a31ca8841c81111",
        "org": "t1_org_00b2ac11ed8bed97fb81111",
        "partition": "t1_ptn_000111d4d504f21414978f0",
        "type": 1,
        "name": "Boarding Fee",
        "description": "Boarding Fee",
        "schedule": 5,
        "scheduleFactor": 1,
        "start": 20160120,
        "finish": 20160120,
        "collection": 2,
        "collectionFactor": 2,
        "collectionOffset": 5,
        "um": 2,
        "amount": 45,
        "currency": "USD",
        "inactive": 0,
        "frozen": 0,
        "txnFee": 0,
        "collectionIncludeCurrent": 0,
        "maximum": 30
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


# Delete Fees Id

Delete a Fee that is an amount one Entity can charge another Entity according to a particular schedule, or based on certain events.

```python
def delete_fees_id(self,
                  id,
                  request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Fee ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`FeesResponseResult`](../../doc/models/fees-response-result.md).

## Example Usage

```python
id = 't1_fee_67b5422dda39a7c36059988'

request_token = '20250423-yourmerchant-refunds-001'

result = fees_controller.delete_fees_id(
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
        "id": "t1_fee_67b5422dda39a7c36059988",
        "created": "2025-02-18 21:30:05.9053",
        "modified": "2025-02-18 21:30:05.9053",
        "creator": "t1_log_0a008e990c7a922100d4f00",
        "modifier": "t1_log_0a008e990c7a922100d4f00",
        "entity": "t1_ent_00758e990d7437d51cdf1aa",
        "forentity": "t1_ent_0088c831a31ca8841c81111",
        "org": "t1_org_00b2ac11ed8bed97fb81111",
        "partition": "t1_ptn_000111d4d504f21414978f0",
        "type": 1,
        "name": "Boarding Fee",
        "description": "Boarding Fee",
        "schedule": 5,
        "scheduleFactor": 1,
        "start": 20160120,
        "finish": 20160120,
        "collection": 2,
        "collectionFactor": 2,
        "collectionOffset": 5,
        "um": 2,
        "amount": 45,
        "currency": "USD",
        "inactive": 0,
        "frozen": 0,
        "txnFee": 0,
        "collectionIncludeCurrent": 0,
        "maximum": 30
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


# Get Fees

Query a Fee that is an amount that one Entity can charge another Entity according to a particular schedule, or based on certain events, such as being charged weekly, after boarding, or when an overdraft is used.

```python
def get_fees(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`FeesResponseResult`](../../doc/models/fees-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = fees_controller.get_fees(
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
        "id": "t1_fee_67b5422dda39a7c36059988",
        "created": "2025-02-18 21:30:05.9053",
        "modified": "2025-02-18 21:30:05.9053",
        "creator": "t1_log_0a008e990c7a922100d4f00",
        "modifier": "t1_log_0a008e990c7a922100d4f00",
        "entity": "t1_ent_00758e990d7437d51cdf1aa",
        "forentity": "t1_ent_0088c831a31ca8841c81111",
        "org": "t1_org_00b2ac11ed8bed97fb81111",
        "partition": "t1_ptn_000111d4d504f21414978f0",
        "type": 1,
        "name": "Boarding Fee",
        "description": "Boarding Fee",
        "schedule": 5,
        "scheduleFactor": 1,
        "start": 20160120,
        "finish": 20160120,
        "collection": 2,
        "collectionFactor": 2,
        "collectionOffset": 5,
        "um": 2,
        "amount": 45,
        "currency": "USD",
        "inactive": 0,
        "frozen": 0,
        "txnFee": 0,
        "collectionIncludeCurrent": 0,
        "maximum": 30
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


# Post Fees

Create a Fee that is an amount one Entity can charge another Entity according to a particular schedule or based on certain events.For example, Fees can be charged on a weekly basis, after boarding, or when an overdraft is used to cover a charge.

```python
def post_fees(self,
             body,
             request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`FeesPostRequest`](../../doc/models/fees-post-request.md) | Body, Required | Create Fee Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`FeesResponseResult`](../../doc/models/fees-response-result.md).

## Example Usage

```python
body = FeesPostRequest(
    entity='t1_ent_00758e990d7437d51cdf1aa',
    mtype=FeeTypeEnum.FEE,
    schedule=FeeScheduleEnum.ENUM_5,
    schedule_factor=1,
    start=20160120,
    collection_factor=2,
    collection_offset=5,
    um=FeeUmEnum.ACTUAL,
    amount=5,
    currency=CurrencyEnum.USD,
    txn_fee=TxnFeeEnum.DISABLED,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    forentity='t1_ent_0088c831a31ca8841c81111',
    org='t1_org_00b2ac11ed8bed97fb81111',
    name='Boarding Fee',
    description='Boarding Fee',
    finish=21160120,
    collection=FeeCollectionEnum.TXNTAXID,
    collection_include_current=0,
    maximum=30
)

request_token = '20250423-yourmerchant-refunds-001'

result = fees_controller.post_fees(
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
        "id": "t1_fee_67b5422dda39a7c36059988",
        "created": "2025-02-18 21:30:05.9053",
        "modified": "2025-02-18 21:30:05.9053",
        "creator": "t1_log_0a008e990c7a922100d4f00",
        "modifier": "t1_log_0a008e990c7a922100d4f00",
        "entity": "t1_ent_00758e990d7437d51cdf1aa",
        "forentity": "t1_ent_0088c831a31ca8841c81111",
        "org": "t1_org_00b2ac11ed8bed97fb81111",
        "partition": "t1_ptn_000111d4d504f21414978f0",
        "type": 1,
        "name": "Boarding Fee",
        "description": "Boarding Fee",
        "schedule": 5,
        "scheduleFactor": 1,
        "start": 20160120,
        "finish": 20160120,
        "collection": 2,
        "collectionFactor": 2,
        "collectionOffset": 5,
        "um": 2,
        "amount": 45,
        "currency": "USD",
        "inactive": 0,
        "frozen": 0,
        "txnFee": 0,
        "collectionIncludeCurrent": 0,
        "maximum": 30
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

