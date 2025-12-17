# Invoice Results

```python
invoice_results_controller = client.invoice_results
```

## Class Name

`InvoiceResultsController`

## Methods

* [Get Invoice Results Id](../../doc/controllers/invoice-results.md#get-invoice-results-id)
* [Get Invoice Results](../../doc/controllers/invoice-results.md#get-invoice-results)
* [Post Invoice Results](../../doc/controllers/invoice-results.md#post-invoice-results)


# Get Invoice Results Id

Query an invoiceResults resource that represents the result of an invoice processing, which is generated when a customer pays for an invoice.

```python
def get_invoice_results_id(self,
                          id,
                          request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this invoice result. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvoiceResultsResponseResult`](../../doc/models/invoice-results-response-result.md).

## Example Usage

```python
id = 't1_inr_00a18bcde1a1b2ec3d9c9az'

request_token = '20250423-yourmerchant-refunds-001'

result = invoice_results_controller.get_invoice_results_id(
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
        "id": "t1_inr_00a18bcde1a1b2ec3d9c9az",
        "created": "2025-01-31 08:42:16.7318",
        "modified": "2025-01-31 08:42:16.7318",
        "creator": "t1_log_0092b50e8812b18e41d511s",
        "modifier": "t1_log_0092b50e8812b18e41d511s",
        "invoice": "t1_inv_67b7c41d9d166b99ac02b36",
        "txn": "p1_txn_00b7c41d9d166b99ac01b10",
        "status": "success",
        "message": "Invoice Paid",
        "shippingFirst": "John",
        "shippingMiddle": "M",
        "shippingLast": "Doe",
        "shippingCompany": "Doe Shipping Co.",
        "shippingAddress1": "123 Main st.",
        "shippingAddress2": "Suite 100",
        "shippingCity": "Springfield",
        "shippingState": "TX",
        "shippingZip": "62701",
        "shippingCountry": "USA",
        "shippingPhone": "+11234567845",
        "shippingFax": "+11234567845",
        "authorization": "Test Authorization with a field name = :field: and a replace text = :replace:",
        "authorizationData": "{\"field\":\"field\",\"replace\":\"replace\"}",
        "signature": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAYEBQYFBAYGBQYHB7A1mFUdV1dy+LOL9C6HE7XK5uPW945ne06NVJ+dt4HsRr9u33igKE411GteR5/fsVtkFVJNZmAz1gaDAX7AdGDvYcCSORyWv"
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


# Get Invoice Results

Query InvoiceResults resource that represents the result of an invoice processing. In other words, when the customer pays for an invoice it will then generate an invoice result.

```python
def get_invoice_results(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvoiceResultsResponseResult`](../../doc/models/invoice-results-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = invoice_results_controller.get_invoice_results(
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
        "id": "t1_inr_00a18bcde1a1b2ec3d9c9az",
        "created": "2025-01-31 08:42:16.7318",
        "modified": "2025-01-31 08:42:16.7318",
        "creator": "t1_log_0092b50e8812b18e41d511s",
        "modifier": "t1_log_0092b50e8812b18e41d511s",
        "invoice": "t1_inv_67b7c41d9d166b99ac02b36",
        "txn": "p1_txn_00b7c41d9d166b99ac01b10",
        "status": "success",
        "message": "Invoice Paid",
        "shippingFirst": "John",
        "shippingMiddle": "M",
        "shippingLast": "Doe",
        "shippingCompany": "Doe Shipping Co.",
        "shippingAddress1": "123 Main st.",
        "shippingAddress2": "Suite 100",
        "shippingCity": "Springfield",
        "shippingState": "TX",
        "shippingZip": "62701",
        "shippingCountry": "USA",
        "shippingPhone": "+11234567845",
        "shippingFax": "+11234567845",
        "authorization": "Test Authorization with a field name = :field: and a replace text = :replace:",
        "authorizationData": "{\"field\":\"field\",\"replace\":\"replace\"}",
        "signature": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAYEBQYFBAYGBQYHB7A1mFUdV1dy+LOL9C6HE7XK5uPW945ne06NVJ+dt4HsRr9u33igKE411GteR5/fsVtkFVJNZmAz1gaDAX7AdGDvYcCSORyWv"
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


# Post Invoice Results

create a invoiceResult.

```python
def post_invoice_results(self,
                        body,
                        request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`InvoiceResultPostRequest`](../../doc/models/invoice-result-post-request.md) | Body, Required | Create Invoice Result Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvoiceResultsResponseResult`](../../doc/models/invoice-results-response-result.md).

## Example Usage

```python
body = InvoiceResultPostRequest(
    invoice='t1_inv_00b62cb82db90057aae4157',
    txn='p1_txn_67b7c41d9d166b99ac02b36',
    status=InvoiceResultStatusEnum.SUCCESS,
    message='Invoice Paid',
    shipping_first='John',
    shipping_middle='M',
    shipping_last='Doe',
    shipping_company='Doe Shippin Co.',
    shipping_address_1='123 Mai st.',
    shipping_address_2='Suite 10',
    shipping_city='Springfield',
    shipping_state='TX',
    shipping_zip='62701',
    shipping_country=ShippingCountryEnum.USA,
    shipping_phone='+1123456784',
    shipping_fax='+1123456784',
    authorization='Test Authorization with a field name = :field: and a replace text = :replace:',
    authorization_data='{"field":"field", "replace":"replace"}',
    signature='/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAYEBQYFBAYGBQYHBwYIChAKCgkJChQODwwQFxQYGBcUFhYaHSUfGhsjHBYWICwgIyYnKSop'
)

request_token = '20250423-yourmerchant-refunds-001'

result = invoice_results_controller.post_invoice_results(
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
        "id": "t1_inr_00a18bcde1a1b2ec3d9c9az",
        "created": "2025-01-31 08:42:16.7318",
        "modified": "2025-01-31 08:42:16.7318",
        "creator": "t1_log_0092b50e8812b18e41d511s",
        "modifier": "t1_log_0092b50e8812b18e41d511s",
        "invoice": "t1_inv_67b7c41d9d166b99ac02b36",
        "txn": "p1_txn_00b7c41d9d166b99ac01b10",
        "status": "success",
        "message": "Invoice Paid",
        "shippingFirst": "John",
        "shippingMiddle": "M",
        "shippingLast": "Doe",
        "shippingCompany": "Doe Shipping Co.",
        "shippingAddress1": "123 Main st.",
        "shippingAddress2": "Suite 100",
        "shippingCity": "Springfield",
        "shippingState": "TX",
        "shippingZip": "62701",
        "shippingCountry": "USA",
        "shippingPhone": "+11234567845",
        "shippingFax": "+11234567845",
        "authorization": "Test Authorization with a field name = :field: and a replace text = :replace:",
        "authorizationData": "{\"field\":\"field\",\"replace\":\"replace\"}",
        "signature": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAYEBQYFBAYGBQYHB7A1mFUdV1dy+LOL9C6HE7XK5uPW945ne06NVJ+dt4HsRr9u33igKE411GteR5/fsVtkFVJNZmAz1gaDAX7AdGDvYcCSORyWv"
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

