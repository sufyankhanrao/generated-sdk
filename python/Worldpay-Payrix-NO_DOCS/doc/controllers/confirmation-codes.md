# Confirmation Codes

```python
confirmation_codes_controller = client.confirmation_codes
```

## Class Name

`ConfirmationCodesController`

## Methods

* [Get Confirm Codes Id](../../doc/controllers/confirmation-codes.md#get-confirm-codes-id)
* [Delete Confirm Codes Id](../../doc/controllers/confirmation-codes.md#delete-confirm-codes-id)
* [Get Confirm Codes](../../doc/controllers/confirmation-codes.md#get-confirm-codes)
* [Post Confirm Codes](../../doc/controllers/confirmation-codes.md#post-confirm-codes)


# Get Confirm Codes Id

Query a confirmCode resource, which represents a unique confirmation code issued to an email address, either when a user indicates that they have forgotten their password, or when the system needs to verify the email address associated with a login.

```python
def get_confirm_codes_id(self,
                        id,
                        request_token=None,
                        search=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Confirmation Code ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |
| `search` | `str` | Header, Optional | Set this header to filter or sort the list of resources that the method returns.<br>See [Searches](page:welcome#searches) for detailed information and examples on how to use search header. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ConfirmCodesResponseResult`](../../doc/models/confirm-codes-response-result.md).

## Example Usage

```python
id = 'p1_cfc_67dd2714a9a1fc91f994e00'

request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

result = confirmation_codes_controller.get_confirm_codes_id(
    id,
    request_token=request_token,
    search=search
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
        "id": "p1_cfc_67dd2714a9a1fc91f994e00",
        "created": "2025-03-21 04:45:08.6978",
        "modified": "2025-03-21 04:45:08.6978",
        "creator": "p1_log_00b869779727da108515d99",
        "modifier": "p1_log_00b869779727da108515d99",
        "login": "p1_log_67dd2714959c3331228ffa3",
        "type": "email",
        "key": "fbdf954596b341d18cb4995b70d321f3",
        "email": "vijay.sample@payrix.com",
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


# Delete Confirm Codes Id

Delete a confirmCode resource. A confirmCode resource represents a unique confirmation code issued to an email address, either when a user indicates that they have forgotten their password, or when the system needs to verify the email address associated with a login.

```python
def delete_confirm_codes_id(self,
                           id,
                           request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Confirmation Code ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ConfirmCodesResponseResult`](../../doc/models/confirm-codes-response-result.md).

## Example Usage

```python
id = 'p1_cfc_67dd2714a9a1fc91f994e00'

request_token = '20250423-yourmerchant-refunds-001'

result = confirmation_codes_controller.delete_confirm_codes_id(
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
        "id": "p1_cfc_67dd2714a9a1fc91f994e00",
        "created": "2025-03-21 04:45:08.6978",
        "modified": "2025-03-21 04:45:08.6978",
        "creator": "p1_log_00b869779727da108515d99",
        "modifier": "p1_log_00b869779727da108515d99",
        "login": "p1_log_67dd2714959c3331228ffa3",
        "type": "email",
        "key": "fbdf954596b341d18cb4995b70d321f3",
        "email": "vijay.sample@payrix.com",
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


# Get Confirm Codes

Query a confirmCode resource. A confirmCode resource represents a unique confirmation code issued to an email address, either when a user indicates that they have forgotten their password, or when the system needs to verify the email address associated with a login.

```python
def get_confirm_codes(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ConfirmCodesResponseResult`](../../doc/models/confirm-codes-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = confirmation_codes_controller.get_confirm_codes(
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
        "id": "p1_cfc_67dd2714a9a1fc91f994e00",
        "created": "2025-03-21 04:45:08.6978",
        "modified": "2025-03-21 04:45:08.6978",
        "creator": "p1_log_00b869779727da108515d99",
        "modifier": "p1_log_00b869779727da108515d99",
        "login": "p1_log_67dd2714959c3331228ffa3",
        "type": "email",
        "key": "fbdf954596b341d18cb4995b70d321f3",
        "email": "vijay.sample@payrix.com",
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


# Post Confirm Codes

Create a confirmCode resource that represents a unique confirmation code issued to an email address, either when a user indicates that they have forgotten their password, or when the system needs to verify the email address associated with a login.

```python
def post_confirm_codes(self,
                      body,
                      request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ConfirmCodesPostRequest`](../../doc/models/confirm-codes-post-request.md) | Body, Required | Create Confirmation Code Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ConfirmCodesResponseResult`](../../doc/models/confirm-codes-response-result.md).

## Example Usage

```python
body = ConfirmCodesPostRequest(
    login='p1_log_67dd2714959c3331228ffa3',
    mtype=ConfirmCodeTypeEnum.EMAIL,
    key='fbdf954596b341d18cb4995b70d321f3',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    email='vijay.sample@payrix.com'
)

request_token = '20250423-yourmerchant-refunds-001'

result = confirmation_codes_controller.post_confirm_codes(
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
        "id": "p1_cfc_67dd2714a9a1fc91f994e00",
        "created": "2025-03-21 04:45:08.6978",
        "modified": "2025-03-21 04:45:08.6978",
        "creator": "p1_log_00b869779727da108515d99",
        "modifier": "p1_log_00b869779727da108515d99",
        "login": "p1_log_67dd2714959c3331228ffa3",
        "type": "email",
        "key": "fbdf954596b341d18cb4995b70d321f3",
        "email": "vijay.sample@payrix.com",
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

