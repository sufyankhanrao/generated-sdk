# Divisions

Divisions contains a list of user divisions associated with an account. It allows for an additional and optional layer of separation within a partition.

```python
divisions_controller = client.divisions
```

## Class Name

`DivisionsController`

## Methods

* [Get Divisions Id](../../doc/controllers/divisions.md#get-divisions-id)
* [Put Divisions Id](../../doc/controllers/divisions.md#put-divisions-id)
* [Get Divisions](../../doc/controllers/divisions.md#get-divisions)
* [Post Divisions](../../doc/controllers/divisions.md#post-divisions)


# Get Divisions Id

Query a Division.

```python
def get_divisions_id(self,
                    id,
                    request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource, The Division ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DivisionsResponseResult`](../../doc/models/divisions-response-result.md).

## Example Usage

```python
id = 't1_div_67e151c6b0210514824000a'

request_token = '20250423-yourmerchant-refunds-001'

result = divisions_controller.get_divisions_id(
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
        "id": "t1_div_67e151c6b0210514824000a",
        "created": "2025-03-24 08:36:22.7392",
        "modified": "2025-03-24 08:36:22.7392",
        "creator": "t1_log_663ce214b2f25f2325a9935",
        "modifier": "t1_log_663ce214b2f25f2325a9935",
        "login": "t1_log_67e150467ee225924163f18",
        "name": "sampleDivision",
        "email": "testuse1@example.com",
        "minPasswordLength": 9,
        "minPasswordComplexity": 1,
        "changeManagementEnabled": 0,
        "canUsePlaidWrapperMicroservice": 0,
        "simplifiedDepositEnabled": 1
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


# Put Divisions Id

Update a Division.

```python
def put_divisions_id(self,
                    id,
                    body,
                    request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource, The Division ID. |
| `body` | [`DivisionsPutRequest`](../../doc/models/divisions-put-request.md) | Body, Required | Update Division Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DivisionsResponseResult`](../../doc/models/divisions-response-result.md).

## Example Usage

```python
id = 't1_div_67e151c6b0210514824000a'

body = DivisionsPutRequest(
    login='t1_log_67e150467ee225924163f18',
    name='sampleDivision',
    email='testuse1@example.com',
    change_management_enabled=ChangeManagementEnabledEnum.DISABLED,
    min_password_length=9,
    min_password_complexity=MinPasswordComplexityEnum.ONE
)

request_token = '20250423-yourmerchant-refunds-001'

result = divisions_controller.put_divisions_id(
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
        "id": "t1_div_67e151c6b0210514824000a",
        "created": "2025-03-24 08:36:22.7392",
        "modified": "2025-03-24 08:36:22.7392",
        "creator": "t1_log_663ce214b2f25f2325a9935",
        "modifier": "t1_log_663ce214b2f25f2325a9935",
        "login": "t1_log_67e150467ee225924163f18",
        "name": "sampleDivision",
        "email": "testuse1@example.com",
        "minPasswordLength": 9,
        "minPasswordComplexity": 1,
        "changeManagementEnabled": 0,
        "canUsePlaidWrapperMicroservice": 0,
        "simplifiedDepositEnabled": 1
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


# Get Divisions

Query Division.

```python
def get_divisions(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DivisionsResponseResult`](../../doc/models/divisions-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = divisions_controller.get_divisions(
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
        "id": "t1_div_67e151c6b0210514824000a",
        "created": "2025-03-24 08:36:22.7392",
        "modified": "2025-03-24 08:36:22.7392",
        "creator": "t1_log_663ce214b2f25f2325a9935",
        "modifier": "t1_log_663ce214b2f25f2325a9935",
        "login": "t1_log_67e150467ee225924163f18",
        "name": "sampleDivision",
        "email": "testuse1@example.com",
        "minPasswordLength": 9,
        "minPasswordComplexity": 1,
        "changeManagementEnabled": 0,
        "canUsePlaidWrapperMicroservice": 0,
        "simplifiedDepositEnabled": 1
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


# Post Divisions

Create a Division.

```python
def post_divisions(self,
                  body,
                  request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DivisionsPostRequest`](../../doc/models/divisions-post-request.md) | Body, Required | Create Division Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DivisionsResponseResult`](../../doc/models/divisions-response-result.md).

## Example Usage

```python
body = DivisionsPostRequest(
    login='t1_log_67e150467ee225924163f18',
    name='sampleDivision',
    email='testuse1@example.com',
    change_management_enabled=ChangeManagementEnabledEnum.DISABLED,
    min_password_length=9,
    min_password_complexity=MinPasswordComplexityEnum.ONE
)

request_token = '20250423-yourmerchant-refunds-001'

result = divisions_controller.post_divisions(
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
        "id": "t1_div_67e151c6b0210514824000a",
        "created": "2025-03-24 08:36:22.7392",
        "modified": "2025-03-24 08:36:22.7392",
        "creator": "t1_log_663ce214b2f25f2325a9935",
        "modifier": "t1_log_663ce214b2f25f2325a9935",
        "login": "t1_log_67e150467ee225924163f18",
        "name": "sampleDivision",
        "email": "testuse1@example.com",
        "minPasswordLength": 9,
        "minPasswordComplexity": 1,
        "changeManagementEnabled": 0,
        "canUsePlaidWrapperMicroservice": 0,
        "simplifiedDepositEnabled": 1
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

