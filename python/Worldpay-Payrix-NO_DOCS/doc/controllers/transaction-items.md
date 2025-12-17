# Transaction Items

```python
transaction_items_controller = client.transaction_items
```

## Class Name

`TransactionItemsController`

## Methods

* [Get Items Id](../../doc/controllers/transaction-items.md#get-items-id)
* [Put Items Id](../../doc/controllers/transaction-items.md#put-items-id)
* [Delete Items Id](../../doc/controllers/transaction-items.md#delete-items-id)
* [Get Items](../../doc/controllers/transaction-items.md#get-items)
* [Post Items](../../doc/controllers/transaction-items.md#post-items)


# Get Items Id

Query an Item.
An Item is a line item that is associated with a particular Transaction. It allows you to describe the cost, quantity and other details of each line in the Transaction.

```python
def get_items_id(self,
                id,
                request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ItemsResponseResult`](../../doc/models/items-response-result.md).

## Example Usage

```python
id = 't1_itm_67b48390abd89e15be2d000'

request_token = '20250423-yourmerchant-refunds-001'

result = transaction_items_controller.get_items_id(
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
        "id": "t1_itm_67b48390abd89e15be2d000",
        "created": "2025-02-18 07:56:48.7124",
        "modified": "2025-02-18 07:56:48.7124",
        "creator": "t1_log_5f49777509d5d1d7c22e000",
        "modifier": "t1_log_5f49777509d5d1d7c22e000",
        "txn": "t1_txn_67b483904b280af5311234a",
        "item": "Line Item 21",
        "description": "A description of this Item",
        "custom": "Identifier",
        "quantity": 1,
        "price": 471,
        "inactive": 0,
        "frozen": 0,
        "um": "EACH",
        "commodityCode": "9717123",
        "total": 471,
        "discount": 0,
        "productCode": "Prorated Tenant Protection Fee"
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


# Put Items Id

Update an Item.
An Item is a line item that is associated with a particular Transaction. It allows you to describe the cost, quantity and other details of each line in the Transaction.

```python
def put_items_id(self,
                id,
                body,
                request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource. |
| `body` | [`ItemsPutRequest`](../../doc/models/items-put-request.md) | Body, Required | Update Item Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ItemsResponseResult`](../../doc/models/items-response-result.md).

## Example Usage

```python
id = 't1_itm_67b48390abd89e15be2d000'

body = ItemsPutRequest(
    item='Line Item 21',
    description='A description of Item',
    custom='Identifier',
    quantity=1,
    price=471,
    um='EACH',
    total=471,
    commodity_code='9717123',
    product_code='Prorated Tenant Protection Fee',
    discount=0,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = transaction_items_controller.put_items_id(
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
        "id": "t1_itm_67b48390abd89e15be2d000",
        "created": "2025-02-18 07:56:48.7124",
        "modified": "2025-02-18 07:56:48.7124",
        "creator": "t1_log_5f49777509d5d1d7c22e000",
        "modifier": "t1_log_5f49777509d5d1d7c22e000",
        "txn": "t1_txn_67b483904b280af5311234a",
        "item": "Line Item 21",
        "description": "A description of this Item",
        "custom": "Identifier",
        "quantity": 1,
        "price": 471,
        "inactive": 0,
        "frozen": 0,
        "um": "EACH",
        "commodityCode": "9717123",
        "total": 471,
        "discount": 0,
        "productCode": "Prorated Tenant Protection Fee"
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


# Delete Items Id

Delete an Item.
An Item is a line item that is associated with a particular Transaction. It allows you to describe the cost, quantity and other details of each line in the Transaction.

```python
def delete_items_id(self,
                   id,
                   request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ItemsResponseResult`](../../doc/models/items-response-result.md).

## Example Usage

```python
id = 't1_itm_67b48390abd89e15be2d000'

request_token = '20250423-yourmerchant-refunds-001'

result = transaction_items_controller.delete_items_id(
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
        "id": "t1_itm_67b48390abd89e15be2d000",
        "created": "2025-02-18 07:56:48.7124",
        "modified": "2025-02-18 07:56:48.7124",
        "creator": "t1_log_5f49777509d5d1d7c22e000",
        "modifier": "t1_log_5f49777509d5d1d7c22e000",
        "txn": "t1_txn_67b483904b280af5311234a",
        "item": "Line Item 21",
        "description": "A description of this Item",
        "custom": "Identifier",
        "quantity": 1,
        "price": 471,
        "inactive": 0,
        "frozen": 0,
        "um": "EACH",
        "commodityCode": "9717123",
        "total": 471,
        "discount": 0,
        "productCode": "Prorated Tenant Protection Fee"
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


# Get Items

Query an Item.
An Item is a line item that is associated with a particular Transaction. It allows you to describe the cost, quantity and other details of each line in the Transaction.

```python
def get_items(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ItemsResponseResult`](../../doc/models/items-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = transaction_items_controller.get_items(
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
        "id": "t1_itm_67b48390abd89e15be2d000",
        "created": "2025-02-18 07:56:48.7124",
        "modified": "2025-02-18 07:56:48.7124",
        "creator": "t1_log_5f49777509d5d1d7c22e000",
        "modifier": "t1_log_5f49777509d5d1d7c22e000",
        "txn": "t1_txn_67b483904b280af5311234a",
        "item": "Line Item 21",
        "description": "A description of this Item",
        "custom": "Identifier",
        "quantity": 1,
        "price": 471,
        "inactive": 0,
        "frozen": 0,
        "um": "EACH",
        "commodityCode": "9717123",
        "total": 471,
        "discount": 0,
        "productCode": "Prorated Tenant Protection Fee"
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


# Post Items

Create an Item.
An Item is a line item that is associated with a particular Transaction. It allows you to describe the cost, quantity and other details of each line in the Transaction.

```python
def post_items(self,
              body,
              request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ItemsPostRequest`](../../doc/models/items-post-request.md) | Body, Required | Create an Item Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ItemsResponseResult`](../../doc/models/items-response-result.md).

## Example Usage

```python
body = ItemsPostRequest(
    txn='t1_txn_00b483904b280af5316218a',
    item='Line Item 21',
    quantity=1,
    price=471,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    description='A description of Item',
    custom='Identifier',
    um='EACH',
    total=471,
    commodity_code='9717123',
    product_code='Prorated Tenant Protection Fee',
    discount=0
)

request_token = '20250423-yourmerchant-refunds-001'

result = transaction_items_controller.post_items(
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
        "id": "t1_itm_67b48390abd89e15be2d000",
        "created": "2025-02-18 07:56:48.7124",
        "modified": "2025-02-18 07:56:48.7124",
        "creator": "t1_log_5f49777509d5d1d7c22e000",
        "modifier": "t1_log_5f49777509d5d1d7c22e000",
        "txn": "t1_txn_67b483904b280af5311234a",
        "item": "Line Item 21",
        "description": "A description of this Item",
        "custom": "Identifier",
        "quantity": 1,
        "price": 471,
        "inactive": 0,
        "frozen": 0,
        "um": "EACH",
        "commodityCode": "9717123",
        "total": 471,
        "discount": 0,
        "productCode": "Prorated Tenant Protection Fee"
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

