# Alerts

Web alerts, also known as webhooks, are automated notifications sent from the API server when triggered by a specific action that occurs in your portfolio. You can configure the actions that trigger the alerts to notify you of any event that's important to your business model.

```python
alerts_controller = client.alerts
```

## Class Name

`AlertsController`

## Methods

* [Get Alerts Id](../../doc/controllers/alerts.md#get-alerts-id)
* [Put Alerts Id](../../doc/controllers/alerts.md#put-alerts-id)
* [Delete Alerts Id](../../doc/controllers/alerts.md#delete-alerts-id)
* [Get Alerts](../../doc/controllers/alerts.md#get-alerts)
* [Post Alerts](../../doc/controllers/alerts.md#post-alerts)


# Get Alerts Id

Query an Alert resource, which represents a particular event notification delivered to a user, and you can invoke alerts by setting up triggers in an alertTriggers resource.

```python
def get_alerts_id(self,
                 id,
                 request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this alert. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AlertsResponseResult`](../../doc/models/alerts-response-result.md).

## Example Usage

```python
id = 't1_alt_67d1a66d3af03677cdc7db0'

request_token = '20250423-yourmerchant-refunds-001'

result = alerts_controller.get_alerts_id(
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
        "id": "t1_alt_67d1a66d3af03677cdc7db0",
        "created": "2025-03-12 11:21:17.2576",
        "modified": "2025-03-12 11:21:28.4944",
        "creator": "t1_log_61f2efc258eb7bf6d380000",
        "modifier": "t1_log_61f2efc258eb7bf6d380000",
        "login": "t1_log_61f2efc258eb7bf6d380000",
        "forlogin": "t1_log_61f2efc258eb7bf6d380000",
        "team": "t1_tem_67c202b908935b505104500",
        "name": "williamson",
        "description": "Used by the FrontDesk system to keep information up to date via webhook alerts",
        "inactive": 0,
        "frozen": 0,
        "division": "t1_div_67c56806728fbbf0bae0z00",
        "partition": "t1_ptn_666834d4d504f21414978f0"
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


# Put Alerts Id

Update an Alert resource, which represents a particular event notification delivered to a user, and you can invoke alerts by setting up triggers in an alertTriggers resource.

```python
def put_alerts_id(self,
                 id,
                 body,
                 request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this alert. |
| `body` | [`AlertsPutRequest`](../../doc/models/alerts-put-request.md) | Body, Required | Update Alert Configuration Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AlertsResponseResult`](../../doc/models/alerts-response-result.md).

## Example Usage

```python
id = 't1_alt_67d1a66d3af03677cdc7db0'

body = AlertsPutRequest(
    login='t1_log_61f2efc258eb7bf6d380000',
    forlogin='t1_log_61f2efc258eb7bf6d380000',
    team='t1_tem_67c202b908935b505104500',
    division='t1_div_67c56806728fbbf0bae0z00',
    partition='t1_ptn_666834d4d504f21414978f0',
    name='williamson',
    description='Used by the FrontDesk system to keep information up to date via webhook alerts',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = alerts_controller.put_alerts_id(
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
        "id": "t1_alt_67d1a66d3af03677cdc7db0",
        "created": "2025-03-12 11:21:17.2576",
        "modified": "2025-03-12 11:21:28.4944",
        "creator": "t1_log_61f2efc258eb7bf6d380000",
        "modifier": "t1_log_61f2efc258eb7bf6d380000",
        "login": "t1_log_61f2efc258eb7bf6d380000",
        "forlogin": "t1_log_61f2efc258eb7bf6d380000",
        "team": "t1_tem_67c202b908935b505104500",
        "name": "williamson",
        "description": "Used by the FrontDesk system to keep information up to date via webhook alerts",
        "inactive": 0,
        "frozen": 0,
        "division": "t1_div_67c56806728fbbf0bae0z00",
        "partition": "t1_ptn_666834d4d504f21414978f0"
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


# Delete Alerts Id

Delete an Alert resource, which represents a particular event notification delivered to a user, and you can invoke alerts by setting up triggers in an alertTriggers resource.

```python
def delete_alerts_id(self,
                    id,
                    request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this alert. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AlertsResponseResult`](../../doc/models/alerts-response-result.md).

## Example Usage

```python
id = 't1_alt_67d1a66d3af03677cdc7db0'

request_token = '20250423-yourmerchant-refunds-001'

result = alerts_controller.delete_alerts_id(
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
        "id": "t1_alt_67d1a66d3af03677cdc7db0",
        "created": "2025-03-12 11:21:17.2576",
        "modified": "2025-03-12 11:21:28.4944",
        "creator": "t1_log_61f2efc258eb7bf6d380000",
        "modifier": "t1_log_61f2efc258eb7bf6d380000",
        "login": "t1_log_61f2efc258eb7bf6d380000",
        "forlogin": "t1_log_61f2efc258eb7bf6d380000",
        "team": "t1_tem_67c202b908935b505104500",
        "name": "williamson",
        "description": "Used by the FrontDesk system to keep information up to date via webhook alerts",
        "inactive": 0,
        "frozen": 0,
        "division": "t1_div_67c56806728fbbf0bae0z00",
        "partition": "t1_ptn_666834d4d504f21414978f0"
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


# Get Alerts

Query an Alert resource, which represents a particular event notification delivered to a user; you can invoke alerts by setting up triggers in an alertTriggers resource.

```python
def get_alerts(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AlertsResponseResult`](../../doc/models/alerts-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = alerts_controller.get_alerts(
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
        "id": "t1_alt_67d1a66d3af03677cdc7db0",
        "created": "2025-03-12 11:21:17.2576",
        "modified": "2025-03-12 11:21:28.4944",
        "creator": "t1_log_61f2efc258eb7bf6d380000",
        "modifier": "t1_log_61f2efc258eb7bf6d380000",
        "login": "t1_log_61f2efc258eb7bf6d380000",
        "forlogin": "t1_log_61f2efc258eb7bf6d380000",
        "team": "t1_tem_67c202b908935b505104500",
        "name": "williamson",
        "description": "Used by the FrontDesk system to keep information up to date via webhook alerts",
        "inactive": 0,
        "frozen": 0,
        "division": "t1_div_67c56806728fbbf0bae0z00",
        "partition": "t1_ptn_666834d4d504f21414978f0"
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


# Post Alerts

Create an Alert resource, which represents a particular event notification delivered to a user. You can invoke alerts by setting up triggers in an [AlertTriggers](../../doc/controllers/alert-triggers.md#post-alert-triggers) resource and specify the delivery method through an alertActions resource. [Alert Actions]($h/Alert%20Actions/_overview) represent particular instances of an Alert sent out through specific channels, such as SMS, mobile application notifications, or email. Each Alert Action is associated with an Alert resource.

```python
def post_alerts(self,
               body,
               request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AlertsPostRequest`](../../doc/models/alerts-post-request.md) | Body, Required | Create Alert Configuration Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AlertsResponseResult`](../../doc/models/alerts-response-result.md).

## Example Usage

```python
body = AlertsPostRequest(
    login='t1_log_61f2efc258eb7bf6d380000',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    forlogin='t1_log_61f2efc258eb7bf6d380000',
    team='t1_tem_67c202b908935b505104500',
    division='t1_div_67c56806728fbbf0bae0z00',
    partition='t1_ptn_666834d4d504f21414978f0',
    name='williamson',
    description='Used by the FrontDesk system to keep information up to date via webhook alerts'
)

request_token = '20250423-yourmerchant-refunds-001'

result = alerts_controller.post_alerts(
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
        "id": "t1_alt_67d1a66d3af03677cdc7db0",
        "created": "2025-03-12 11:21:17.2576",
        "modified": "2025-03-12 11:21:28.4944",
        "creator": "t1_log_61f2efc258eb7bf6d380000",
        "modifier": "t1_log_61f2efc258eb7bf6d380000",
        "login": "t1_log_61f2efc258eb7bf6d380000",
        "forlogin": "t1_log_61f2efc258eb7bf6d380000",
        "team": "t1_tem_67c202b908935b505104500",
        "name": "williamson",
        "description": "Used by the FrontDesk system to keep information up to date via webhook alerts",
        "inactive": 0,
        "frozen": 0,
        "division": "t1_div_67c56806728fbbf0bae0z00",
        "partition": "t1_ptn_666834d4d504f21414978f0"
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

