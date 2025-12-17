# Invoice Line Items

```python
invoice_line_items_controller = client.invoice_line_items
```

## Class Name

`InvoiceLineItemsController`

## Methods

* [Get Invoice Line Items Id](../../doc/controllers/invoice-line-items.md#get-invoice-line-items-id)
* [Put Invoice Line Items Id](../../doc/controllers/invoice-line-items.md#put-invoice-line-items-id)
* [Delete Invoice Line Items Id](../../doc/controllers/invoice-line-items.md#delete-invoice-line-items-id)
* [Get Invoice Line Items](../../doc/controllers/invoice-line-items.md#get-invoice-line-items)
* [Post Invoice Line Items](../../doc/controllers/invoice-line-items.md#post-invoice-line-items)


# Get Invoice Line Items Id

Query an InvoiceLineItem or Invoice Line Item.

```python
def get_invoice_line_items_id(self,
                             id,
                             request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this invoice line item. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvoiceLineItemsResponseResult`](../../doc/models/invoice-line-items-response-result.md).

## Example Usage

```python
id = 't1_ini_00a18bcde1a1b2ec1d9c9az'

request_token = '20250423-yourmerchant-refunds-001'

result = invoice_line_items_controller.get_invoice_line_items_id(
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
        "id": "t1_ini_00a18bcde1a1b2ec1d9c9az",
        "created": "2025-01-31 08:42:16.7318",
        "modified": "2025-01-31 08:42:16.7318",
        "creator": "t1_log_8ad114b7edbf6f641b7c2f2",
        "modifier": "t1_log_00d114b7edbf6f641b7c2f2",
        "invoice": "t1_inv_00b62cb82db90057aae7000",
        "invoiceItem": "t1_ini_00b62cb7d3b3a7e6a841000",
        "quantity": 1,
        "price": 50000,
        "discount": 100,
        "total": 49900
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


# Put Invoice Line Items Id

Update an InvoiceLineItem or Invoice Line Item.

```python
def put_invoice_line_items_id(self,
                             id,
                             body,
                             request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this invoice line item. |
| `body` | [`InvoiceLineItemsPutRequest`](../../doc/models/invoice-line-items-put-request.md) | Body, Required | Update Invoice Line Item Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvoiceLineItemsResponseResult`](../../doc/models/invoice-line-items-response-result.md).

## Example Usage

```python
id = 't1_ini_00a18bcde1a1b2ec1d9c9az'

body = InvoiceLineItemsPutRequest(
    invoice='t1_inv_00b62cb82db90057aae7000',
    invoice_item='t1_ini_00b62cb7d3b3a7e6a841000',
    quantity=1,
    price=50000,
    discount=100
)

request_token = '20250423-yourmerchant-refunds-001'

result = invoice_line_items_controller.put_invoice_line_items_id(
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
        "id": "t1_ini_00a18bcde1a1b2ec1d9c9az",
        "created": "2025-01-31 08:42:16.7318",
        "modified": "2025-01-31 08:42:16.7318",
        "creator": "t1_log_8ad114b7edbf6f641b7c2f2",
        "modifier": "t1_log_00d114b7edbf6f641b7c2f2",
        "invoice": "t1_inv_00b62cb82db90057aae7000",
        "invoiceItem": "t1_ini_00b62cb7d3b3a7e6a841000",
        "quantity": 1,
        "price": 50000,
        "discount": 100,
        "total": 49900
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


# Delete Invoice Line Items Id

Delete an InvoiceLineItem or Invoice Line Item.

```python
def delete_invoice_line_items_id(self,
                                id,
                                request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this invoice line item. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvoiceLineItemsResponseResult`](../../doc/models/invoice-line-items-response-result.md).

## Example Usage

```python
id = 't1_ini_00a18bcde1a1b2ec1d9c9az'

request_token = '20250423-yourmerchant-refunds-001'

result = invoice_line_items_controller.delete_invoice_line_items_id(
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
        "id": "t1_ini_00a18bcde1a1b2ec1d9c9az",
        "created": "2025-01-31 08:42:16.7318",
        "modified": "2025-01-31 08:42:16.7318",
        "creator": "t1_log_8ad114b7edbf6f641b7c2f2",
        "modifier": "t1_log_00d114b7edbf6f641b7c2f2",
        "invoice": "t1_inv_00b62cb82db90057aae7000",
        "invoiceItem": "t1_ini_00b62cb7d3b3a7e6a841000",
        "quantity": 1,
        "price": 50000,
        "discount": 100,
        "total": 49900
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


# Get Invoice Line Items

Query an InvoiceLineItem. InvoiceLineItem is a resource that relates an invoice item with an invoice. It holds information such as quantity, and price each item.

```python
def get_invoice_line_items(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvoiceLineItemsResponseResult`](../../doc/models/invoice-line-items-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = invoice_line_items_controller.get_invoice_line_items(
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
        "id": "t1_ini_00a18bcde1a1b2ec1d9c9az",
        "created": "2025-01-31 08:42:16.7318",
        "modified": "2025-01-31 08:42:16.7318",
        "creator": "t1_log_8ad114b7edbf6f641b7c2f2",
        "modifier": "t1_log_00d114b7edbf6f641b7c2f2",
        "invoice": "t1_inv_00b62cb82db90057aae7000",
        "invoiceItem": "t1_ini_00b62cb7d3b3a7e6a841000",
        "quantity": 1,
        "price": 50000,
        "discount": 100,
        "total": 49900
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


# Post Invoice Line Items

Create an InvoiceLineItem or Invoice Line Item.InvoiceLineItem is a resource that relates an invoice item with an invoice. It holds information such as quantity, and price each item.

```python
def post_invoice_line_items(self,
                           body,
                           request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`InvoiceLineItemsPostRequest`](../../doc/models/invoice-line-items-post-request.md) | Body, Required | Create Invoice Line Item Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvoiceLineItemsResponseResult`](../../doc/models/invoice-line-items-response-result.md).

## Example Usage

```python
body = InvoiceLineItemsPostRequest(
    invoice='t1_inv_00b62cb82db90057aae7000',
    invoice_item='t1_ini_00b62cb7d3b3a7e6a841000',
    quantity=1,
    price=50000,
    discount=100
)

request_token = '20250423-yourmerchant-refunds-001'

result = invoice_line_items_controller.post_invoice_line_items(
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
        "id": "t1_ini_00a18bcde1a1b2ec1d9c9az",
        "created": "2025-01-31 08:42:16.7318",
        "modified": "2025-01-31 08:42:16.7318",
        "creator": "t1_log_8ad114b7edbf6f641b7c2f2",
        "modifier": "t1_log_00d114b7edbf6f641b7c2f2",
        "invoice": "t1_inv_00b62cb82db90057aae7000",
        "invoiceItem": "t1_ini_00b62cb7d3b3a7e6a841000",
        "quantity": 1,
        "price": 50000,
        "discount": 100,
        "total": 49900
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

