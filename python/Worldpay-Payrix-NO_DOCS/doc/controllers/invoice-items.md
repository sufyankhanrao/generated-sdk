# Invoice Items

```python
invoice_items_controller = client.invoice_items
```

## Class Name

`InvoiceItemsController`

## Methods

* [Get Invoice Items Id](../../doc/controllers/invoice-items.md#get-invoice-items-id)
* [Put Invoice Items Id](../../doc/controllers/invoice-items.md#put-invoice-items-id)
* [Delete Invoice Items Id](../../doc/controllers/invoice-items.md#delete-invoice-items-id)
* [Get Invoice Items](../../doc/controllers/invoice-items.md#get-invoice-items)
* [Post Invoice Items](../../doc/controllers/invoice-items.md#post-invoice-items)


# Get Invoice Items Id

Query an Invoice Item or query Invoice Items.

```python
def get_invoice_items_id(self,
                        id,
                        request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this invoice item. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvoiceItemsResponseResult`](../../doc/models/invoice-items-response-result.md).

## Example Usage

```python
id = 't1_ini_67a18bcde1a1b2ec3d9c9az'

request_token = '20250423-yourmerchant-refunds-001'

result = invoice_items_controller.get_invoice_items_id(
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
        "id": "t1_ini_67a18bcde1a1b2ec3d9c9az",
        "created": "2025-01-31 08:42:16.7318",
        "modified": "2025-01-31 08:42:16.7318",
        "creator": "t1_log_8ad114b7edbf6f641b7c2f2",
        "modifier": "t1_log_00d114b7edbf6f641b7c2f2",
        "login": "t1_log_5ed514b7edbf6f641b7c2f2",
        "item": "Jay",
        "description": "Jay",
        "custom": "Sample custom field 1",
        "um": "kilogram",
        "commodityCode": "03000",
        "productCode": "SKU23456",
        "price": 150000,
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


# Put Invoice Items Id

Update an Invoice Item, A InvoiceItem is a resource that stores line item details for an invoice.

```python
def put_invoice_items_id(self,
                        id,
                        body,
                        request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this invoice item. |
| `body` | [`InvoiceItemsPutRequest`](../../doc/models/invoice-items-put-request.md) | Body, Required | Update Invoice Item Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvoiceItemsResponseResult`](../../doc/models/invoice-items-response-result.md).

## Example Usage

```python
id = 't1_ini_67a18bcde1a1b2ec3d9c9az'

body = InvoiceItemsPutRequest(
    login='t1_log_00d514abedbf6f641b7c2f2',
    item='Test Custom Links',
    description='Test Custom Links',
    custom='Sample custom field 1',
    price=1666,
    um='kilogram',
    commodity_code='03000',
    product_code='SKU23456',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = invoice_items_controller.put_invoice_items_id(
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
        "id": "t1_ini_67a18bcde1a1b2ec3d9c9az",
        "created": "2025-01-31 08:42:16.7318",
        "modified": "2025-01-31 08:42:16.7318",
        "creator": "t1_log_8ad114b7edbf6f641b7c2f2",
        "modifier": "t1_log_00d114b7edbf6f641b7c2f2",
        "login": "t1_log_5ed514b7edbf6f641b7c2f2",
        "item": "Jay",
        "description": "Jay",
        "custom": "Sample custom field 1",
        "um": "kilogram",
        "commodityCode": "03000",
        "productCode": "SKU23456",
        "price": 150000,
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


# Delete Invoice Items Id

Delete an Invoice Item or a resource that stores line item details for an invoice.

```python
def delete_invoice_items_id(self,
                           id,
                           request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this invoice item. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvoiceItemsResponseResult`](../../doc/models/invoice-items-response-result.md).

## Example Usage

```python
id = 't1_ini_67a18bcde1a1b2ec3d9c9az'

request_token = '20250423-yourmerchant-refunds-001'

result = invoice_items_controller.delete_invoice_items_id(
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
        "id": "t1_ini_67a18bcde1a1b2ec3d9c9az",
        "created": "2025-01-31 08:42:16.7318",
        "modified": "2025-01-31 08:42:16.7318",
        "creator": "t1_log_8ad114b7edbf6f641b7c2f2",
        "modifier": "t1_log_00d114b7edbf6f641b7c2f2",
        "login": "t1_log_5ed514b7edbf6f641b7c2f2",
        "item": "Jay",
        "description": "Jay",
        "custom": "Sample custom field 1",
        "um": "kilogram",
        "commodityCode": "03000",
        "productCode": "SKU23456",
        "price": 150000,
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


# Get Invoice Items

Query an Invoice Item. A Invoice Item is a resource that stores line item details for an invoice.

```python
def get_invoice_items(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvoiceItemsResponseResult`](../../doc/models/invoice-items-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = invoice_items_controller.get_invoice_items(
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
        "id": "t1_ini_67a18bcde1a1b2ec3d9c9az",
        "created": "2025-01-31 08:42:16.7318",
        "modified": "2025-01-31 08:42:16.7318",
        "creator": "t1_log_8ad114b7edbf6f641b7c2f2",
        "modifier": "t1_log_00d114b7edbf6f641b7c2f2",
        "login": "t1_log_5ed514b7edbf6f641b7c2f2",
        "item": "Jay",
        "description": "Jay",
        "custom": "Sample custom field 1",
        "um": "kilogram",
        "commodityCode": "03000",
        "productCode": "SKU23456",
        "price": 150000,
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


# Post Invoice Items

Create an Invoice Item, a resource that stores line item details for an invoice.

```python
def post_invoice_items(self,
                      body,
                      request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`InvoiceItemsPostRequest`](../../doc/models/invoice-items-post-request.md) | Body, Required | Create Invoice Item Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvoiceItemsResponseResult`](../../doc/models/invoice-items-response-result.md).

## Example Usage

```python
body = InvoiceItemsPostRequest(
    login='t1_log_00d514abedbf6f641b7c2f2',
    item='Test Custom Links',
    price=1666,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    description='Test Custom Links',
    custom='Sample custom field 1',
    um='kilogram',
    commodity_code='03000',
    product_code='SKU23456'
)

request_token = '20250423-yourmerchant-refunds-001'

result = invoice_items_controller.post_invoice_items(
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
        "id": "t1_ini_67a18bcde1a1b2ec3d9c9az",
        "created": "2025-01-31 08:42:16.7318",
        "modified": "2025-01-31 08:42:16.7318",
        "creator": "t1_log_8ad114b7edbf6f641b7c2f2",
        "modifier": "t1_log_00d114b7edbf6f641b7c2f2",
        "login": "t1_log_5ed514b7edbf6f641b7c2f2",
        "item": "Jay",
        "description": "Jay",
        "custom": "Sample custom field 1",
        "um": "kilogram",
        "commodityCode": "03000",
        "productCode": "SKU23456",
        "price": 150000,
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

