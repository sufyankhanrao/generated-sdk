# Alert Triggers

```python
alert_triggers_controller = client.alert_triggers
```

## Class Name

`AlertTriggersController`

## Methods

* [Get Alert Triggers Id](../../doc/controllers/alert-triggers.md#get-alert-triggers-id)
* [Put Alert Triggers Id](../../doc/controllers/alert-triggers.md#put-alert-triggers-id)
* [Delete Alert Triggers Id](../../doc/controllers/alert-triggers.md#delete-alert-triggers-id)
* [Get Alert Triggers](../../doc/controllers/alert-triggers.md#get-alert-triggers)
* [Post Alert Triggers](../../doc/controllers/alert-triggers.md#post-alert-triggers)


# Get Alert Triggers Id

Query an alertTrigger resource that represents a set of triggers causing an Alert to be sent, for example, the levying of a Fee or a Payout occurring, each linked to a particular Alert, with the action to take when triggered set up in the alertActions resource.

```python
def get_alert_triggers_id(self,
                         id,
                         request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this alert trigger. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AlertTriggersResponseResult`](../../doc/models/alert-triggers-response-result.md).

## Example Usage

```python
id = 't1_alr_67d489a76383d013e6295c0'

request_token = '20250423-yourmerchant-refunds-001'

result = alert_triggers_controller.get_alert_triggers_id(
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
        "id": "t1_alr_67d489a76383d013e6295c0",
        "created": "2025-03-14 15:55:19.4151",
        "modified": "2025-03-14 15:55:19.4151",
        "creator": "t1_log_66b14333927997a2f3cf7b2",
        "modifier": "t1_log_66b14333927997a2f3cf7b2",
        "alert": "t1_alt_67d489a72e5e8fdec85a910",
        "event": "delete",
        "resource": 9,
        "name": "name of alertTrigger",
        "description": "description of alertTrigger",
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


# Put Alert Triggers Id

Update an alertTrigger resource that represents a set of triggers causing an Alert to be sent, for example levying a Fee or a Payout occurring, with each trigger linked to a particular Alert and the action taken when triggered set up in the alertActions resource.

```python
def put_alert_triggers_id(self,
                         id,
                         body,
                         request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this alert trigger. |
| `body` | [`AlertTriggersPutRequest`](../../doc/models/alert-triggers-put-request.md) | Body, Required | Update Alert Trigger Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AlertTriggersResponseResult`](../../doc/models/alert-triggers-response-result.md).

## Example Usage

```python
id = 't1_alr_67d489a76383d013e6295c0'

body = AlertTriggersPutRequest(
    alert='t1_alt_67d489a72e5e8fdec85a910',
    event=AlertTriggerEventEnum.DELETE,
    resource=ResourceEnum.MERCHANTS,
    name='name of alertTrigger',
    description='description of alertTrigger',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = alert_triggers_controller.put_alert_triggers_id(
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
        "id": "t1_alr_67d489a76383d013e6295c0",
        "created": "2025-03-14 15:55:19.4151",
        "modified": "2025-03-14 15:55:19.4151",
        "creator": "t1_log_66b14333927997a2f3cf7b2",
        "modifier": "t1_log_66b14333927997a2f3cf7b2",
        "alert": "t1_alt_67d489a72e5e8fdec85a910",
        "event": "delete",
        "resource": 9,
        "name": "name of alertTrigger",
        "description": "description of alertTrigger",
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


# Delete Alert Triggers Id

Delete an alertTrigger resource that represents a set of triggers causing an Alert to be sent, for example levying a Fee or a Payout occurring, each linked to a particular Alert with the action to take set up in the alertActions resource.

```python
def delete_alert_triggers_id(self,
                            id,
                            request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this alert trigger. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AlertTriggersResponseResult`](../../doc/models/alert-triggers-response-result.md).

## Example Usage

```python
id = 't1_alr_67d489a76383d013e6295c0'

request_token = '20250423-yourmerchant-refunds-001'

result = alert_triggers_controller.delete_alert_triggers_id(
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
        "id": "t1_alr_67d489a76383d013e6295c0",
        "created": "2025-03-14 15:55:19.4151",
        "modified": "2025-03-14 15:55:19.4151",
        "creator": "t1_log_66b14333927997a2f3cf7b2",
        "modifier": "t1_log_66b14333927997a2f3cf7b2",
        "alert": "t1_alt_67d489a72e5e8fdec85a910",
        "event": "delete",
        "resource": 9,
        "name": "name of alertTrigger",
        "description": "description of alertTrigger",
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


# Get Alert Triggers

Query an alertTrigger resource that represents a set of triggers that cause an Alert to be sent, where for example this could be the levying of a Fee or a Payout occurring, and each alertTrigger is linked to a particular Alert, with the action to take when an Alert is triggered set up in the alertActions resource.

```python
def get_alert_triggers(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AlertTriggersResponseResult`](../../doc/models/alert-triggers-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = alert_triggers_controller.get_alert_triggers(
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
        "id": "t1_alr_67d489a76383d013e6295c0",
        "created": "2025-03-14 15:55:19.4151",
        "modified": "2025-03-14 15:55:19.4151",
        "creator": "t1_log_66b14333927997a2f3cf7b2",
        "modifier": "t1_log_66b14333927997a2f3cf7b2",
        "alert": "t1_alt_67d489a72e5e8fdec85a910",
        "event": "delete",
        "resource": 9,
        "name": "name of alertTrigger",
        "description": "description of alertTrigger",
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


# Post Alert Triggers

Create an alertTrigger resource that represents a set of triggers causing an Alert to be sent, such as the levying of a Fee or a Payout occurring, and each alertTrigger is linked to a particular Alert with actions set up in the alertActions resource.

```python
def post_alert_triggers(self,
                       body,
                       request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AlertTriggersPostRequest`](../../doc/models/alert-triggers-post-request.md) | Body, Required | Create Alert Trigger Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AlertTriggersResponseResult`](../../doc/models/alert-triggers-response-result.md).

## Example Usage

```python
body = AlertTriggersPostRequest(
    alert='t1_alt_67d489a72e5e8fdec85a910',
    event=AlertTriggerEventEnum.DELETE,
    resource=ResourceEnum.MERCHANTS,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    name='name of alertTrigger',
    description='description of alertTrigger'
)

request_token = '20250423-yourmerchant-refunds-001'

result = alert_triggers_controller.post_alert_triggers(
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
        "id": "t1_alr_67d489a76383d013e6295c0",
        "created": "2025-03-14 15:55:19.4151",
        "modified": "2025-03-14 15:55:19.4151",
        "creator": "t1_log_66b14333927997a2f3cf7b2",
        "modifier": "t1_log_66b14333927997a2f3cf7b2",
        "alert": "t1_alt_67d489a72e5e8fdec85a910",
        "event": "delete",
        "resource": 9,
        "name": "name of alertTrigger",
        "description": "description of alertTrigger",
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

