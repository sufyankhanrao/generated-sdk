# Invoice Parameters

```python
invoice_parameters_controller = client.invoice_parameters
```

## Class Name

`InvoiceParametersController`

## Methods

* [Get Invoice Parameters Id](../../doc/controllers/invoice-parameters.md#get-invoice-parameters-id)
* [Put Invoice Parameters Id](../../doc/controllers/invoice-parameters.md#put-invoice-parameters-id)
* [Delete Invoice Parameters Id](../../doc/controllers/invoice-parameters.md#delete-invoice-parameters-id)
* [Get Invoice Parameters](../../doc/controllers/invoice-parameters.md#get-invoice-parameters)
* [Post Invoice Parameters](../../doc/controllers/invoice-parameters.md#post-invoice-parameters)


# Get Invoice Parameters Id

Query an invoice parameter that holds a certain configuration used for creating an invoice such as dba, address, and apikey.

```python
def get_invoice_parameters_id(self,
                             id,
                             request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this invoice parameter. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvoiceParametersResponseResult`](../../doc/models/invoice-parameters-response-result.md).

## Example Usage

```python
id = 't1_inp_67e46c1f4245ca0a6398000'

request_token = '20250423-yourmerchant-refunds-001'

result = invoice_parameters_controller.get_invoice_parameters_id(
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
        "id": "t1_inp_67e46c1f4245ca0a6398000",
        "created": "2025-03-26 17:05:35.3009",
        "modified": "2025-03-26 17:05:35.3009",
        "creator": "t1_log_67c272f9078d060d291fdeb",
        "modifier": "t1_log_67c272f9078d060d291fdeb",
        "login": "t1_log_67c272f9078d060d291fdez",
        "entity": "t1_ent_67c272f920c1724d2709c0b",
        "org": "t1_org_67b736ad7d05922340000cf",
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_666834d4d504f11234578f0",
        "type": "apikey",
        "value": "ecfb12e30dcfc1421a2e6c18345cb0a6",
        "locked": 0,
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


# Put Invoice Parameters Id

Update an invoice parameter.

```python
def put_invoice_parameters_id(self,
                             id,
                             body,
                             request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this invoice parameter. |
| `body` | [`InvoiceParametersPutRequest`](../../doc/models/invoice-parameters-put-request.md) | Body, Required | Update Invoice Parameter Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvoiceParametersResponseResult`](../../doc/models/invoice-parameters-response-result.md).

## Example Usage

```python
id = 't1_inp_67e46c1f4245ca0a6398000'

body = InvoiceParametersPutRequest(
    login='t1_log_67c272f9078d060d291fdez',
    entity='t1_ent_67c272f920c1724d2709c0b',
    division='t1_div_67c56806728fbbf0bae0b00',
    org='t1_org_67b736ad7d05922340000cf',
    partition='t1_ptn_666834d4d504f11234578f0',
    locked=InvoiceParameterLockedEnum.NOTLOCKED,
    mtype=InvoiceParameterTypeEnum.APIKEY,
    value='ecfb12e30dcfc1421a2e6c18345cb0a6',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = invoice_parameters_controller.put_invoice_parameters_id(
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
        "id": "t1_inp_67e46c1f4245ca0a6398000",
        "created": "2025-03-26 17:05:35.3009",
        "modified": "2025-03-26 17:05:35.3009",
        "creator": "t1_log_67c272f9078d060d291fdeb",
        "modifier": "t1_log_67c272f9078d060d291fdeb",
        "login": "t1_log_67c272f9078d060d291fdez",
        "entity": "t1_ent_67c272f920c1724d2709c0b",
        "org": "t1_org_67b736ad7d05922340000cf",
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_666834d4d504f11234578f0",
        "type": "apikey",
        "value": "ecfb12e30dcfc1421a2e6c18345cb0a6",
        "locked": 0,
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


# Delete Invoice Parameters Id

Delete an Invoice Parameter.

```python
def delete_invoice_parameters_id(self,
                                id,
                                request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this invoice parameter. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvoiceParametersResponseResult`](../../doc/models/invoice-parameters-response-result.md).

## Example Usage

```python
id = 't1_inp_67e46c1f4245ca0a6398000'

request_token = '20250423-yourmerchant-refunds-001'

result = invoice_parameters_controller.delete_invoice_parameters_id(
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
        "id": "t1_inp_67e46c1f4245ca0a6398000",
        "created": "2025-03-26 17:05:35.3009",
        "modified": "2025-03-26 17:05:35.3009",
        "creator": "t1_log_67c272f9078d060d291fdeb",
        "modifier": "t1_log_67c272f9078d060d291fdeb",
        "login": "t1_log_67c272f9078d060d291fdez",
        "entity": "t1_ent_67c272f920c1724d2709c0b",
        "org": "t1_org_67b736ad7d05922340000cf",
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_666834d4d504f11234578f0",
        "type": "apikey",
        "value": "ecfb12e30dcfc1421a2e6c18345cb0a6",
        "locked": 0,
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


# Get Invoice Parameters

Query an invoice parameter resource that holds a certain configuration used for creating an invoice, including dba, address, and api key.

```python
def get_invoice_parameters(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvoiceParametersResponseResult`](../../doc/models/invoice-parameters-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = invoice_parameters_controller.get_invoice_parameters(
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
        "id": "t1_inp_67e46c1f4245ca0a6398000",
        "created": "2025-03-26 17:05:35.3009",
        "modified": "2025-03-26 17:05:35.3009",
        "creator": "t1_log_67c272f9078d060d291fdeb",
        "modifier": "t1_log_67c272f9078d060d291fdeb",
        "login": "t1_log_67c272f9078d060d291fdez",
        "entity": "t1_ent_67c272f920c1724d2709c0b",
        "org": "t1_org_67b736ad7d05922340000cf",
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_666834d4d504f11234578f0",
        "type": "apikey",
        "value": "ecfb12e30dcfc1421a2e6c18345cb0a6",
        "locked": 0,
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


# Post Invoice Parameters

Create an Invoice Parameter that holds a certain configuration used for creating an invoice such as dba, address, and apikey.

```python
def post_invoice_parameters(self,
                           body,
                           request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`InvoiceParametersPostRequest`](../../doc/models/invoice-parameters-post-request.md) | Body, Required | Create Invoice Parameter Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvoiceParametersResponseResult`](../../doc/models/invoice-parameters-response-result.md).

## Example Usage

```python
body = InvoiceParametersPostRequest(
    login='t1_log_67c272f9078d060d291fdez',
    locked=InvoiceParameterLockedEnum.NOTLOCKED,
    mtype=InvoiceParameterTypeEnum.APIKEY,
    value='ecfb12e30dcfc1421a2e6c18345cb0a6',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    entity='t1_ent_67c272f920c1724d2709c0b',
    division='t1_div_67c56806728fbbf0bae0b00',
    org='t1_org_67b736ad7d05922340000cf',
    partition='t1_ptn_666834d4d504f11234578f0'
)

request_token = '20250423-yourmerchant-refunds-001'

result = invoice_parameters_controller.post_invoice_parameters(
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
        "id": "t1_inp_67e46c1f4245ca0a6398000",
        "created": "2025-03-26 17:05:35.3009",
        "modified": "2025-03-26 17:05:35.3009",
        "creator": "t1_log_67c272f9078d060d291fdeb",
        "modifier": "t1_log_67c272f9078d060d291fdeb",
        "login": "t1_log_67c272f9078d060d291fdez",
        "entity": "t1_ent_67c272f920c1724d2709c0b",
        "org": "t1_org_67b736ad7d05922340000cf",
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_666834d4d504f11234578f0",
        "type": "apikey",
        "value": "ecfb12e30dcfc1421a2e6c18345cb0a6",
        "locked": 0,
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

