# Predict

```python
predict_controller = client.predict
```

## Class Name

`PredictController`


# Get Predict Alerts

Gets a list of Predict alerts based on filter criteria. The timestamps are in the time zone configured in the Greenbyte Platform. Use the useUtc flag to get timestamps in UTC.

_🔐 This endpoint requires the **Predict** endpoint permission._

_This is a beta feature. Some details might change before it is
released as a stable version._

```python
def get_predict_alerts(self,
                      device_ids,
                      timestamp_start,
                      timestamp_end,
                      site_ids=None,
                      component_ids=None,
                      status=None,
                      severity=None,
                      fields=None,
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
| `site_ids` | `List[int]` | Query, Optional | What sites to get alerts for.<br><br>**Constraints**: `>= 1` |
| `component_ids` | `List[int]` | Query, Optional | What components to get alerts for.<br><br>**Constraints**: `>= 1` |
| `status` | [`PredictStatusEnum`](../../doc/models/predict-status-enum.md) | Query, Optional | Which alert status to get alerts for. |
| `severity` | [`PredictSeverityEnum`](../../doc/models/predict-severity-enum.md) | Query, Optional | What severity of alerts to get: high severity or low severity. If<br>not set, both high and low severity alerts are included. |
| `fields` | `List[str]` | Query, Optional | Which fields to include in the response. Valid fields are those defined in the `PredictAlert` schema (See Response Type). By default all fields are included. |
| `page_size` | `int` | Query, Optional | The number of items to return per page.<br><br>**Default**: `50` |
| `page` | `int` | Query, Optional | Which page to return when the number of items exceed the page size.<br><br>**Default**: `1` |
| `use_utc` | `bool` | Query, Optional | Set to true to get timestamps in UTC.<br><br>**Default**: `False` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[PredictAlertsResponse]`](../../doc/models/predict-alerts-response.md).

## Example Usage

```python
device_ids = [
    1,
    2,
    3
]

timestamp_start = dateutil.parser.parse('01/01/2024 00:00:00')

timestamp_end = dateutil.parser.parse('01/08/2024 00:00:00')

site_ids = [
    1,
    2,
    3
]

component_ids = [
    1,
    2,
    3
]

status = PredictStatusEnum.ACTIVE

severity = PredictSeverityEnum.HIGH

fields = [
    'deviceId',
    'highSeverity'
]

page_size = 50

page = 1

use_utc = False

result = predict_controller.get_predict_alerts(
    device_ids,
    timestamp_start,
    timestamp_end,
    site_ids=site_ids,
    component_ids=component_ids,
    status=status,
    severity=severity,
    fields=fields,
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
    "deviceId": 260,
    "siteId": 19,
    "componentAlert": {
      "componentId": 46,
      "componentName": "Main gear oil system"
    },
    "highSeverity": true,
    "status": "resolved",
    "comments": [
      {
        "text": "Found high temperatures. Reported to OM team.",
        "userName": "Bill Bao",
        "timestamp": "2019-04-16T12:48:16"
      }
    ],
    "resolvedBy": "Jens Genberg",
    "timestampResolved": "2019-10-25T09:29:55",
    "actionTaken": "Replacement",
    "componentResolved": {
      "componentId": 77,
      "componentName": "Main gear oil system"
    },
    "dismissedBy": null,
    "timestampDismissed": null,
    "recommendations": null
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

