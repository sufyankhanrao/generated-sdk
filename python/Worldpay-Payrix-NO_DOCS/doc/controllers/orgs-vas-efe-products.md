# Orgs VAS Efe Products

```python
orgs_vas_efe_products_controller = client.orgs_vas_efe_products
```

## Class Name

`OrgsVASEfeProductsController`

## Methods

* [Get Orgs VAS Efe Products Id](../../doc/controllers/orgs-vas-efe-products.md#get-orgs-vas-efe-products-id)
* [Put Orgs VAS Efe Products Id](../../doc/controllers/orgs-vas-efe-products.md#put-orgs-vas-efe-products-id)
* [Delete Orgs VAS Efe Products Id](../../doc/controllers/orgs-vas-efe-products.md#delete-orgs-vas-efe-products-id)
* [Get Orgs VAS Efe Products](../../doc/controllers/orgs-vas-efe-products.md#get-orgs-vas-efe-products)
* [Post Orgs VAS Efe Products](../../doc/controllers/orgs-vas-efe-products.md#post-orgs-vas-efe-products)


# Get Orgs VAS Efe Products Id

Query orgsVASEfeProducts.

```python
def get_orgs_vas_efe_products_id(self,
                                id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource, or the (unknown) ID associated with the Orgs VAS EfeProducts. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgsVASEfeProductsResponseResult`](../../doc/models/orgs-vas-efe-products-response-result.md).

## Example Usage

```python
id = 't1_ove_6862c122527a9042ec000c0'

result = orgs_vas_efe_products_controller.get_orgs_vas_efe_products_id(id)

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
        "id": "t1_ove_6862c122527a9042ec000c0",
        "created": "2025-06-30 12:53:54.3584",
        "modified": "2025-06-30 12:53:54.3584",
        "creator": "t1_log_65c6415ad9791e3796f000c",
        "modifier": "t1_log_65c6415ad9791e3796f000c",
        "org": "t1_org_6862c1211b366bbfe87657c",
        "product": "merchantWorkingCapital",
        "contractType": "{\"residualFeeType\": \"rev_share\"}",
        "platform": "PARAFIN",
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


# Put Orgs VAS Efe Products Id

Update orgsVASEfeProducts.

```python
def put_orgs_vas_efe_products_id(self,
                                id,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this Orgs VAS EfeProducts. |
| `body` | [`OrgsVASEfeProductsPutRequest`](../../doc/models/orgs-vas-efe-products-put-request.md) | Body, Required | Update Orgs VAS EfeProducts |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgsVASEfeProductsResponseResult`](../../doc/models/orgs-vas-efe-products-response-result.md).

## Example Usage

```python
id = 't1_ove_6862c122527a9042ec000c0'

body = OrgsVASEfeProductsPutRequest(
    org='t1_org_6862c1211b366bbfe87657c',
    product=Product3Enum.MERCHANTWORKINGCAPITAL,
    contract_type='{"residualFeeType": "rev_share"}',
    platform=PlatformEnum.PARAFIN,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

result = orgs_vas_efe_products_controller.put_orgs_vas_efe_products_id(
    id,
    body
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
        "id": "t1_ove_6862c122527a9042ec000c0",
        "created": "2025-06-30 12:53:54.3584",
        "modified": "2025-06-30 12:53:54.3584",
        "creator": "t1_log_65c6415ad9791e3796f000c",
        "modifier": "t1_log_65c6415ad9791e3796f000c",
        "org": "t1_org_6862c1211b366bbfe87657c",
        "product": "merchantWorkingCapital",
        "contractType": "{\"residualFeeType\": \"rev_share\"}",
        "platform": "PARAFIN",
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


# Delete Orgs VAS Efe Products Id

Delete orgsVASEfeProducts.

```python
def delete_orgs_vas_efe_products_id(self,
                                   id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this Orgs VAS EfeProducts. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgsVASEfeProductsResponseResult`](../../doc/models/orgs-vas-efe-products-response-result.md).

## Example Usage

```python
id = 't1_ove_6862c122527a9042ec000c0'

result = orgs_vas_efe_products_controller.delete_orgs_vas_efe_products_id(id)

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
        "id": "t1_ove_6862c122527a9042ec000c0",
        "created": "2025-06-30 12:53:54.3584",
        "modified": "2025-06-30 12:53:54.3584",
        "creator": "t1_log_65c6415ad9791e3796f000c",
        "modifier": "t1_log_65c6415ad9791e3796f000c",
        "org": "t1_org_6862c1211b366bbfe87657c",
        "product": "merchantWorkingCapital",
        "contractType": "{\"residualFeeType\": \"rev_share\"}",
        "platform": "PARAFIN",
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


# Get Orgs VAS Efe Products

Query a orgsVASEfeProducts.

```python
def get_orgs_vas_efe_products(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgsVASEfeProductsResponseResult`](../../doc/models/orgs-vas-efe-products-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = orgs_vas_efe_products_controller.get_orgs_vas_efe_products(
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
        "id": "t1_ove_6862c122527a9042ec000c0",
        "created": "2025-06-30 12:53:54.3584",
        "modified": "2025-06-30 12:53:54.3584",
        "creator": "t1_log_65c6415ad9791e3796f000c",
        "modifier": "t1_log_65c6415ad9791e3796f000c",
        "org": "t1_org_6862c1211b366bbfe87657c",
        "product": "merchantWorkingCapital",
        "contractType": "{\"residualFeeType\": \"rev_share\"}",
        "platform": "PARAFIN",
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


# Post Orgs VAS Efe Products

Create a orgsVASEfeProducts.

```python
def post_orgs_vas_efe_products(self,
                              body,
                              request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`OrgsVASEfeProductsPostRequest`](../../doc/models/orgs-vas-efe-products-post-request.md) | Body, Required | - |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgsVASEfeProductsResponseResult`](../../doc/models/orgs-vas-efe-products-response-result.md).

## Example Usage

```python
body = OrgsVASEfeProductsPostRequest(
    org='t1_org_6862c1211b366bbfe87657c',
    product=Product3Enum.MERCHANTWORKINGCAPITAL,
    contract_type='{"residualFeeType": "rev_share"}',
    platform=PlatformEnum.PARAFIN,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = orgs_vas_efe_products_controller.post_orgs_vas_efe_products(
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
        "id": "t1_ove_6862c122527a9042ec000c0",
        "created": "2025-06-30 12:53:54.3584",
        "modified": "2025-06-30 12:53:54.3584",
        "creator": "t1_log_65c6415ad9791e3796f000c",
        "modifier": "t1_log_65c6415ad9791e3796f000c",
        "org": "t1_org_6862c1211b366bbfe87657c",
        "product": "merchantWorkingCapital",
        "contractType": "{\"residualFeeType\": \"rev_share\"}",
        "platform": "PARAFIN",
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

