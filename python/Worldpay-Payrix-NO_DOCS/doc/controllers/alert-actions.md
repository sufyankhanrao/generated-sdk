# Alert Actions

```python
alert_actions_controller = client.alert_actions
```

## Class Name

`AlertActionsController`

## Methods

* [Get Alert Actions Id](../../doc/controllers/alert-actions.md#get-alert-actions-id)
* [Put Alert Actions Id](../../doc/controllers/alert-actions.md#put-alert-actions-id)
* [Delete Alert Actions Id](../../doc/controllers/alert-actions.md#delete-alert-actions-id)
* [Get Alert Actions](../../doc/controllers/alert-actions.md#get-alert-actions)
* [Post Alert Actions](../../doc/controllers/alert-actions.md#post-alert-actions)


# Get Alert Actions Id

Query an alertAction; An alertAction resource represents a particular instance of an Alert that is sent out through one particular channel, for example, SMS, mobile application notification, or email, each alertAction being associated with an Alert resource.

```python
def get_alert_actions_id(self,
                        id,
                        request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Alert Action ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AlertActionsResponseResult`](../../doc/models/alert-actions-response-result.md).

## Example Usage

```python
id = 't1_ala_67d0924f1919ec362341d00'

request_token = '20250423-yourmerchant-refunds-001'

result = alert_actions_controller.get_alert_actions_id(
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
        "id": "t1_ala_67d0924f1919ec362341d00",
        "created": "2025-03-11 15:43:11.1194",
        "modified": "2025-03-11 15:43:11.1194",
        "creator": "t1_log_65b2c883d793216616f16ab",
        "modifier": "t1_log_65b2c883d793216616f16ab",
        "type": "web",
        "options": "JSON",
        "value": "https://test.payrix.com/apix/test/t1",
        "alert": "t1_alt_65fddb118236188e055d54c",
        "retries": 3,
        "headerName": "Authorization",
        "headerValue": "SecretToken123!",
        "maxAttemptsTempDisabled": 0,
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


# Put Alert Actions Id

Update an alertAction representing a particular instance of an Alert that is sent out through one particular channel, for example, SMS, mobile application notification, or email, each being associated with an Alert resource.

```python
def put_alert_actions_id(self,
                        id,
                        body,
                        request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Alert Action ID. |
| `body` | [`AlertActionsPutRequest`](../../doc/models/alert-actions-put-request.md) | Body, Required | Update Alert Action Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AlertActionsResponseResult`](../../doc/models/alert-actions-response-result.md).

## Example Usage

```python
id = 't1_ala_67d0924f1919ec362341d00'

body = AlertActionsPutRequest(
    alert='t1_alt_65fddb118236188e055d54c',
    header_name='Authorization',
    header_value='SecrtToken1234!',
    options='JSON',
    value='https://test.payrix.com/apix/test/t1',
    retries=3,
    max_attempts_temp_disabled=MaxAttemptsTempDisabledEnum.NOTTEMPORARILYDISABLED,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = alert_actions_controller.put_alert_actions_id(
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
        "id": "t1_ala_67d0924f1919ec362341d00",
        "created": "2025-03-11 15:43:11.1194",
        "modified": "2025-03-11 15:43:11.1194",
        "creator": "t1_log_65b2c883d793216616f16ab",
        "modifier": "t1_log_65b2c883d793216616f16ab",
        "type": "web",
        "options": "JSON",
        "value": "https://test.payrix.com/apix/test/t1",
        "alert": "t1_alt_65fddb118236188e055d54c",
        "retries": 3,
        "headerName": "Authorization",
        "headerValue": "SecretToken123!",
        "maxAttemptsTempDisabled": 0,
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


# Delete Alert Actions Id

Delete an alertAction.

```python
def delete_alert_actions_id(self,
                           id,
                           request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Alert Action ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AlertActionsResponseResult`](../../doc/models/alert-actions-response-result.md).

## Example Usage

```python
id = 't1_ala_67d0924f1919ec362341d00'

request_token = '20250423-yourmerchant-refunds-001'

result = alert_actions_controller.delete_alert_actions_id(
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
        "id": "t1_ala_67d0924f1919ec362341d00",
        "created": "2025-03-11 15:43:11.1194",
        "modified": "2025-03-11 15:43:11.1194",
        "creator": "t1_log_65b2c883d793216616f16ab",
        "modifier": "t1_log_65b2c883d793216616f16ab",
        "type": "web",
        "options": "JSON",
        "value": "https://test.payrix.com/apix/test/t1",
        "alert": "t1_alt_65fddb118236188e055d54c",
        "retries": 3,
        "headerName": "Authorization",
        "headerValue": "SecretToken123!",
        "maxAttemptsTempDisabled": 0,
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


# Get Alert Actions

Query an alertAction representing a particular instance of an Alert that is sent out through one particular channel. For example, SMS, mobile application notification, or email, each being associated with an Alert resource.

```python
def get_alert_actions(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AlertActionsResponseResult`](../../doc/models/alert-actions-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = alert_actions_controller.get_alert_actions(
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
        "id": "t1_ala_67d0924f1919ec362341d00",
        "created": "2025-03-11 15:43:11.1194",
        "modified": "2025-03-11 15:43:11.1194",
        "creator": "t1_log_65b2c883d793216616f16ab",
        "modifier": "t1_log_65b2c883d793216616f16ab",
        "type": "web",
        "options": "JSON",
        "value": "https://test.payrix.com/apix/test/t1",
        "alert": "t1_alt_65fddb118236188e055d54c",
        "retries": 3,
        "headerName": "Authorization",
        "headerValue": "SecretToken123!",
        "maxAttemptsTempDisabled": 0,
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


# Post Alert Actions

Create an alertAction, which represents a particular instance of an Alert sent out through one particular channel, such as SMS, mobile application notification, or email, and each alertAction is associated with an Alert resource.

```python
def post_alert_actions(self,
                      body,
                      request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AlertActionsPostRequest`](../../doc/models/alert-actions-post-request.md) | Body, Required | Create Alert Action Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AlertActionsResponseResult`](../../doc/models/alert-actions-response-result.md).

## Example Usage

```python
body = AlertActionsPostRequest(
    alert='t1_alt_65fddb118236188e055d54c',
    mtype=AlertActionTypeEnum.WEB,
    options='JSON',
    value='https://test.payrix.com/apix/test/t1',
    max_attempts_temp_disabled=MaxAttemptsTempDisabledEnum.NOTTEMPORARILYDISABLED,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    header_name='Authorization',
    header_value='SecretToken123!',
    retries=3
)

request_token = '20250423-yourmerchant-refunds-001'

result = alert_actions_controller.post_alert_actions(
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
        "id": "t1_ala_67d0924f1919ec362341d00",
        "created": "2025-03-11 15:43:11.1194",
        "modified": "2025-03-11 15:43:11.1194",
        "creator": "t1_log_65b2c883d793216616f16ab",
        "modifier": "t1_log_65b2c883d793216616f16ab",
        "type": "web",
        "options": "JSON",
        "value": "https://test.payrix.com/apix/test/t1",
        "alert": "t1_alt_65fddb118236188e055d54c",
        "retries": 3,
        "headerName": "Authorization",
        "headerValue": "SecretToken123!",
        "maxAttemptsTempDisabled": 0,
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

