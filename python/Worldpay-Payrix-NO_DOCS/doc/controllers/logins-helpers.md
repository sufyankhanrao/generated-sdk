# Logins Helpers

```python
logins_helpers_controller = client.logins_helpers
```

## Class Name

`LoginsHelpersController`

## Methods

* [Get Logins Helpers Id](../../doc/controllers/logins-helpers.md#get-logins-helpers-id)
* [Put Logins Helpers Id](../../doc/controllers/logins-helpers.md#put-logins-helpers-id)
* [Get Logins Helpers](../../doc/controllers/logins-helpers.md#get-logins-helpers)


# Get Logins Helpers Id

Query a loginsHelper.

```python
def get_logins_helpers_id(self,
                         id,
                         request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`LoginsHelpersResponseResult`](../../doc/models/logins-helpers-response-result.md).

## Example Usage

```python
id = 't1_lgh_67ee09c7402cff94765db3c'

request_token = '20250423-yourmerchant-refunds-001'

result = logins_helpers_controller.get_logins_helpers_id(
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
        "id": "t1_lgh_67ee09c7402cff94765db3c",
        "created": "2025-04-03 00:08:39.2707",
        "modified": "2025-04-03 00:08:39.2707",
        "creator": "t1_log_65b2c8c108ac3cd41432a1e",
        "modifier": "t1_log_65b2c8c108ac3cd41432a1e",
        "login": "t1_log_67ee09bbc22011eaae4ddd9",
        "mfaSmsCode": "code",
        "mfaSmsCodeUnixTime": 623,
        "mfaSmsCodeAttempts": 0,
        "mfaSmsCodesCount": 0,
        "mfaSmsWindow": 0,
        "loginAsEnabled": 0
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


# Put Logins Helpers Id

Update a loginsHelper.

```python
def put_logins_helpers_id(self,
                         id,
                         body,
                         request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource. |
| `body` | [`LoginsHelpersPutRequest`](../../doc/models/logins-helpers-put-request.md) | Body, Required | - |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`LoginsHelpersResponseResult`](../../doc/models/logins-helpers-response-result.md).

## Example Usage

```python
id = 't1_lgh_67ee09c7402cff94765db3c'

body = LoginsHelpersPutRequest(
    login_as_enabled=LoginAsEnabledEnum.OFF
)

request_token = '20250423-yourmerchant-refunds-001'

result = logins_helpers_controller.put_logins_helpers_id(
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
        "id": "t1_lgh_67ee09c7402cff94765db3c",
        "created": "2025-04-03 00:08:39.2707",
        "modified": "2025-04-03 00:08:39.2707",
        "creator": "t1_log_65b2c8c108ac3cd41432a1e",
        "modifier": "t1_log_65b2c8c108ac3cd41432a1e",
        "login": "t1_log_67ee09bbc22011eaae4ddd9",
        "mfaSmsCode": "code",
        "mfaSmsCodeUnixTime": 623,
        "mfaSmsCodeAttempts": 0,
        "mfaSmsCodesCount": 0,
        "mfaSmsWindow": 0,
        "loginAsEnabled": 0
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


# Get Logins Helpers

Query loginsHelpers.

```python
def get_logins_helpers(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`LoginsHelpersResponseResult`](../../doc/models/logins-helpers-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = logins_helpers_controller.get_logins_helpers(
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
        "id": "t1_lgh_67ee09c7402cff94765db3c",
        "created": "2025-04-03 00:08:39.2707",
        "modified": "2025-04-03 00:08:39.2707",
        "creator": "t1_log_65b2c8c108ac3cd41432a1e",
        "modifier": "t1_log_65b2c8c108ac3cd41432a1e",
        "login": "t1_log_67ee09bbc22011eaae4ddd9",
        "mfaSmsCode": "code",
        "mfaSmsCodeUnixTime": 623,
        "mfaSmsCodeAttempts": 0,
        "mfaSmsCodesCount": 0,
        "mfaSmsWindow": 0,
        "loginAsEnabled": 0
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

