# Alerts

This section contains operations related to device alerts.

## Alerts

Alerts analyze incoming data based on a set of rules defined by a user. For example, you can set up rules to check that a data signal is above a certain threshold, or that the data signals of two different units follow the same pattern. This can help you gain a better understanding of your portfolio.

```python
alerts_controller = client.alerts
```

## Class Name

`AlertsController`

## Methods

* [Get Active Alerts](../../doc/controllers/alerts.md#get-active-alerts)
* [Get Alerts](../../doc/controllers/alerts.md#get-alerts)


# Get Active Alerts

Gets active alerts for multiple devices.
The timestamps are in the time zone configured in the Greenbyte Platform.
Use the useUtc flag to get timestamps in UTC.

_🔐 This endpoint requires the **Alerts** endpoint permission._

_This request can also be made using the POST method,
with a request to `activealerts.json` and
a JSON request body instead of query parameters._

```python
def get_active_alerts(self,
                     device_ids,
                     fields=None,
                     sort_by=None,
                     sort_asc=False,
                     page_size=50,
                     page=1,
                     use_utc=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | `List[int]` | Query, Required | What devices to get alerts for.<br><br>**Constraints**: `>= 1` |
| `fields` | `List[str]` | Query, Optional | Which fields to include in the response. Valid fields are those defined in the `AlertItem` schema (See Response Type). By default all fields are included. |
| `sort_by` | `List[str]` | Query, Optional | Which fields to sort the response items by. |
| `sort_asc` | `bool` | Query, Optional | Whether to sort the items in ascending order.<br><br>**Default**: `False` |
| `page_size` | `int` | Query, Optional | The number of items to return per page.<br><br>**Default**: `50` |
| `page` | `int` | Query, Optional | Which page to return when the number of items exceed the page size.<br><br>**Default**: `1` |
| `use_utc` | `bool` | Query, Optional | Set to true to get timestamps in UTC.<br><br>**Default**: `False` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[AlertItem]`](../../doc/models/alert-item.md).

## Example Usage

```python
device_ids = [
    1,
    2,
    3
]

fields = [
    'ruleId',
    'timestampStart'
]

sort_asc = False

page_size = 50

page = 1

use_utc = False

result = alerts_controller.get_active_alerts(
    device_ids,
    fields=fields,
    sort_asc=sort_asc,
    page_size=page_size,
    page=page,
    use_utc=use_utc
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
[
  {
    "deviceId": 179,
    "ruleId": 104,
    "description": "Power curve less than 90%",
    "details": "Evaluation period: 6 hours\nData coverage: 70% of devices\nExclude data during: Active Stop or Warning status\nData condition: The consecutive value of the performance index of Backen 2 is less than 90%\nData condition: The consecutive value of the wind speed of Backen 2 is greater than 5 m/s",
    "timestampStart": "2020-03-18T06:50:00",
    "timestampEnd": "2020-03-18T14:00:00",
    "message": "Low Performance Wind",
    "comment": "A comment"
  },
  {
    "deviceId": 183,
    "ruleId": 104,
    "description": "Power curve less than 90%",
    "details": "Evaluation period: 6 hours\nData coverage: 70% of devices\nExclude data during: Active Stop or Warning status\nData condition: The consecutive value of the performance index of Backen 6 is less than 90%\nData condition: The consecutive value of the wind speed of Backen 6 is greater than 5 m/s",
    "timestampStart": "2020-03-18T07:40:00",
    "timestampEnd": "2020-03-18T14:00:00",
    "message": "Low Performance Wind",
    "comment": "A comment"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be fulfilled due to bad syntax. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | The request is missing a valid API key. | `APIException` |
| 403 | One of the following:<br><br>* The API key does not authorize access to the requested endpoint because of a missing endpoint permission.<br>* The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. | `APIException` |
| 405 | The HTTP method is not allowed for the endpoint. | `APIException` |
| 429 | The API key has been used in too many requests in a given amount<br>of time. The following headers will be set in the response:<br><br>* `X-Rate-Limit-Limit` – The rate limit period (for example<br>  "1m", "12h", or "1d").<br>* `X-Rate-Limit-Remaining` – The remaining number of requests<br>  for this period.<br>* `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601<br>  format) when the remaining number of requests resets.<br><br>The limit is currently 1,000 requests/minute per API key and IP<br>address. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Alerts

Gets alerts for multiple devices and the given time period.
The timestamps are in the time zone configured in the Greenbyte Platform.
Use the useUtc flag to get timestamps in UTC.

_🔐 This endpoint requires the **Alerts** endpoint permission._

_This request can also be made using the POST method,
with a request to `alerts.json` and
a JSON request body instead of query parameters._

```python
def get_alerts(self,
              device_ids,
              timestamp_start,
              timestamp_end,
              fields=None,
              sort_by=None,
              sort_asc=False,
              page_size=50,
              page=1,
              use_utc=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | `List[int]` | Query, Required | What devices to get alerts for.<br><br>**Constraints**: `>= 1` |
| `timestamp_start` | `datetime` | Query, Required | The beginning of the time interval to get data for (inclusive),<br>in [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)<br>**date-time** format:<br><br>* Timestamps ending with 'Z' are treated as UTC. Example: "2020-01-01T00:00:00Z"<br>* Time zone (UTC) offset timestamps ending with '+HH:mm'/"-HH:mm" are also supported. Example: "2020-01-01T02:00:00-02:00"<br>* Other timestamps are treated as being in the time zone configured in the Greenbyte Platform. Example: "2020-01-01T00:00:00"<br><br>The start timestamp **is** included in the time interval: for<br>example, to select the full month of March 2020, set<br>`timestampStart` to "2020-03-01T00:00:00" and `timestampEnd` to<br>"2020-04-01T00:00:00".<br><br>Timestamps selected in the portal will by default be in UTC. |
| `timestamp_end` | `datetime` | Query, Required | The end of the time interval to get data for (exclusive),<br>in [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)<br>**date-time** format:<br><br>* Timestamps ending with 'Z' are treated as UTC. Example: "2020-01-01T00:00:00Z"<br>* Time zone (UTC) offset timestamps ending with '+HH:mm'/"-HH:mm" are also supported. Example: "2020-01-01T02:00:00-02:00"<br>* Other timestamps are treated as being in the time zone configured in the Greenbyte Platform. Example: "2020-01-01T00:00:00"<br><br>The end timestamp is **not** included in the time interval: for<br>example, to select the full month of March 2020, set<br>`timestampStart` to "2020-03-01T00:00:00" and `timestampEnd` to<br>"2020-04-01T00:00:00".<br><br>Timestamps selected in the portal will by default be in UTC. |
| `fields` | `List[str]` | Query, Optional | Which fields to include in the response. Valid fields are those defined in the `AlertItem` schema (See Response Type). By default all fields are included. |
| `sort_by` | `List[str]` | Query, Optional | Which fields to sort the response items by. |
| `sort_asc` | `bool` | Query, Optional | Whether to sort the items in ascending order.<br><br>**Default**: `False` |
| `page_size` | `int` | Query, Optional | The number of items to return per page.<br><br>**Default**: `50` |
| `page` | `int` | Query, Optional | Which page to return when the number of items exceed the page size.<br><br>**Default**: `1` |
| `use_utc` | `bool` | Query, Optional | Set to true to get timestamps in UTC.<br><br>**Default**: `False` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[AlertItem]`](../../doc/models/alert-item.md).

## Example Usage

```python
device_ids = [
    1,
    2,
    3
]

timestamp_start = dateutil.parser.parse('01/01/2024 00:00:00')

timestamp_end = dateutil.parser.parse('01/08/2024 00:00:00')

fields = [
    'ruleId',
    'timestampStart'
]

sort_asc = False

page_size = 50

page = 1

use_utc = False

result = alerts_controller.get_alerts(
    device_ids,
    timestamp_start,
    timestamp_end,
    fields=fields,
    sort_asc=sort_asc,
    page_size=page_size,
    page=page,
    use_utc=use_utc
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
[
  {
    "deviceId": 179,
    "ruleId": 104,
    "description": "Power curve less than 90%",
    "details": "Evaluation period: 6 hours\nData coverage: 70% of devices\nExclude data during: Active Stop or Warning status\nData condition: The consecutive value of the performance index of Backen 2 is less than 90%\nData condition: The consecutive value of the wind speed of Backen 2 is greater than 5 m/s",
    "timestampStart": "2020-03-18T06:50:00",
    "timestampEnd": "2020-03-18T14:00:00",
    "message": "Low Performance Wind",
    "comment": "A comment"
  },
  {
    "deviceId": 183,
    "ruleId": 104,
    "description": "Power curve less than 90%",
    "details": "Evaluation period: 6 hours\nData coverage: 70% of devices\nExclude data during: Active Stop or Warning status\nData condition: The consecutive value of the performance index of Backen 6 is less than 90%\nData condition: The consecutive value of the wind speed of Backen 6 is greater than 5 m/s",
    "timestampStart": "2020-03-18T07:40:00",
    "timestampEnd": "2020-03-18T14:00:00",
    "message": "Low Performance Wind",
    "comment": "A comment"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be fulfilled due to bad syntax. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | The request is missing a valid API key. | `APIException` |
| 403 | One of the following:<br><br>* The API key does not authorize access to the requested endpoint because of a missing endpoint permission.<br>* The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. | `APIException` |
| 405 | The HTTP method is not allowed for the endpoint. | `APIException` |
| 429 | The API key has been used in too many requests in a given amount<br>of time. The following headers will be set in the response:<br><br>* `X-Rate-Limit-Limit` – The rate limit period (for example<br>  "1m", "12h", or "1d").<br>* `X-Rate-Limit-Remaining` – The remaining number of requests<br>  for this period.<br>* `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601<br>  format) when the remaining number of requests resets.<br><br>The limit is currently 1,000 requests/minute per API key and IP<br>address. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |

