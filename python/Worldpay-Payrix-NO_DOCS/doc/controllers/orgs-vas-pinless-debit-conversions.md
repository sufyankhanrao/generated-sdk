# Orgs VAS Pinless Debit Conversions

```python
orgs_vas_pinless_debit_conversions_controller = client.orgs_vas_pinless_debit_conversions
```

## Class Name

`OrgsVASPinlessDebitConversionsController`

## Methods

* [Get Orgs VAS Pinless Debit Conversions Id](../../doc/controllers/orgs-vas-pinless-debit-conversions.md#get-orgs-vas-pinless-debit-conversions-id)
* [Put Orgs VAS Pinless Debit Conversions Id](../../doc/controllers/orgs-vas-pinless-debit-conversions.md#put-orgs-vas-pinless-debit-conversions-id)
* [Get Orgs VAS Pinless Debit Conversions](../../doc/controllers/orgs-vas-pinless-debit-conversions.md#get-orgs-vas-pinless-debit-conversions)
* [Post Orgs VAS Pinless Debit Conversions](../../doc/controllers/orgs-vas-pinless-debit-conversions.md#post-orgs-vas-pinless-debit-conversions)


# Get Orgs VAS Pinless Debit Conversions Id

Query orgsVASPinlessDebitConversions.

```python
def get_orgs_vas_pinless_debit_conversions_id(self,
                                             id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource, or the (unknown) ID associated with the Orgs VAS Pinless Debit Conversions. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgsVASPinlessDebitConversionsResponseResult`](../../doc/models/orgs-vas-pinless-debit-conversions-response-result.md).

## Example Usage

```python
id = 't1_ovp_680bfd41d139cba791290z0'

result = orgs_vas_pinless_debit_conversions_controller.get_orgs_vas_pinless_debit_conversions_id(id)

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
        "id": "t1_ovp_680bfd41d139cba791290z0",
        "created": "2025-04-25 17:23:13.8787",
        "modified": "2025-04-25 17:23:13.8787",
        "creator": "t1_log_66db672e98bceb86ecbb000",
        "modifier": "t1_log_66db672e98bceb86ecbb000",
        "org": "t1_org_680bfd2cea2729081810000",
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


# Put Orgs VAS Pinless Debit Conversions Id

Update orgsVASPinlessDebitConversions.

```python
def put_orgs_vas_pinless_debit_conversions_id(self,
                                             id,
                                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this Orgs VAS Pinless Debit Conversions. |
| `body` | [`OrgsVASPinlessDebitConversionsPutRequest`](../../doc/models/orgs-vas-pinless-debit-conversions-put-request.md) | Body, Required | Update Orgs VAS Pinless Debit Conversions |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgsVASPinlessDebitConversionsResponseResult`](../../doc/models/orgs-vas-pinless-debit-conversions-response-result.md).

## Example Usage

```python
id = 't1_ovp_680bfd41d139cba791290z0'

body = OrgsVASPinlessDebitConversionsPutRequest(
    org='t1_org_680bfd2cea2729081810000',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

result = orgs_vas_pinless_debit_conversions_controller.put_orgs_vas_pinless_debit_conversions_id(
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
        "id": "t1_ovp_680bfd41d139cba791290z0",
        "created": "2025-04-25 17:23:13.8787",
        "modified": "2025-04-25 17:23:13.8787",
        "creator": "t1_log_66db672e98bceb86ecbb000",
        "modifier": "t1_log_66db672e98bceb86ecbb000",
        "org": "t1_org_680bfd2cea2729081810000",
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


# Get Orgs VAS Pinless Debit Conversions

Query a orgsVASPinlessDebitConversions.

```python
def get_orgs_vas_pinless_debit_conversions(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgsVASPinlessDebitConversionsResponseResult`](../../doc/models/orgs-vas-pinless-debit-conversions-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = orgs_vas_pinless_debit_conversions_controller.get_orgs_vas_pinless_debit_conversions(
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
        "id": "t1_ovp_680bfd41d139cba791290z0",
        "created": "2025-04-25 17:23:13.8787",
        "modified": "2025-04-25 17:23:13.8787",
        "creator": "t1_log_66db672e98bceb86ecbb000",
        "modifier": "t1_log_66db672e98bceb86ecbb000",
        "org": "t1_org_680bfd2cea2729081810000",
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


# Post Orgs VAS Pinless Debit Conversions

Create a orgsVASPinlessDebitConversions.

```python
def post_orgs_vas_pinless_debit_conversions(self,
                                           body,
                                           request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`OrgsVASPinlessDebitConversionsPostRequest`](../../doc/models/orgs-vas-pinless-debit-conversions-post-request.md) | Body, Required | - |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgsVASPinlessDebitConversionsResponseResult`](../../doc/models/orgs-vas-pinless-debit-conversions-response-result.md).

## Example Usage

```python
body = OrgsVASPinlessDebitConversionsPostRequest(
    org='t1_org_680bfd2cea2729081815573',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = orgs_vas_pinless_debit_conversions_controller.post_orgs_vas_pinless_debit_conversions(
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
        "id": "t1_ovp_680bfd41d139cba791290z0",
        "created": "2025-04-25 17:23:13.8787",
        "modified": "2025-04-25 17:23:13.8787",
        "creator": "t1_log_66db672e98bceb86ecbb000",
        "modifier": "t1_log_66db672e98bceb86ecbb000",
        "org": "t1_org_680bfd2cea2729081810000",
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

