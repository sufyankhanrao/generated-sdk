# Data

This section contains operations related to either time-series or aggregated signal data.

## Data signals

Data signals are binary code signals which transmit information like temperature, wind speed, and power from an asset or device to the Greenbyte Platform. In addition the Greenbyte Platform provides KPIs and other advanced calculations that are also exposed as signals.

## Data resolution

Data can be returned in different resolutions, for example ten minute resolution or daily resolution.

## Data aggregation

Different kinds of data are aggregated (combined) in different ways. The calculation mode of the signal determines how individual data points are aggregated. All signals have a default calculation mode, for example:

* *Sum* is used for energy signals, which means data values are summed.
* *Average* for wind speed signals, which means that data values are averaged.
  When combining data from several devices you can also choose if the data is aggregated per individual device or per site or if all of the data is combined into one value.
  [Signal Calculations in the Greenbyte Platform documentation](https://help.greenbyte.com/Greenbyte/en/signal-calculations.html)

```python
data_controller = client.data
```

## Class Name

`DataController`

## Methods

* [Get Data Signals](../../doc/controllers/data.md#get-data-signals)
* [Get Data](../../doc/controllers/data.md#get-data)
* [Get Real Time Data](../../doc/controllers/data.md#get-real-time-data)
* [Get Data Per Category](../../doc/controllers/data.md#get-data-per-category)
* [Get High Res Data](../../doc/controllers/data.md#get-high-res-data)


# Get Data Signals

Gets authorized data signals for one or more devices.

_🔐 This endpoint requires the **Data** endpoint permission._

_This request can also be made using the POST method,
with a request to `datasignals.json` and
a JSON request body instead of query parameters._

```python
def get_data_signals(self,
                    device_ids=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | `List[int]` | Query, Optional | What devices to get data signals for.<br><br>**Constraints**: `>= 1` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[DataSignalItem]`](../../doc/models/data-signal-item.md).

## Example Usage

```python
device_ids = [
    1,
    2,
    3
]

result = data_controller.get_data_signals(
    device_ids=device_ids
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
    "dataSignalId": 1,
    "title": "Wind speed",
    "type": "Wind speed",
    "unit": "m/s",
    "deviceType": {
      "deviceTypeId": 1,
      "title": "Turbine"
    }
  },
  {
    "dataSignalId": 5,
    "title": "Power",
    "type": "Power",
    "unit": "kW",
    "deviceType": {
      "deviceTypeId": 1,
      "title": "Turbine"
    }
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


# Get Data

Gets data for multiple devices and data signals in the given
resolution. The timestamps are in the time zone configured in the Greenbyte Platform.
Use the useUtc flag to get timestamps in UTC for all resolutions other than daily, weekly, monthly and yearly.

_🔐 This endpoint requires the **Data** endpoint permission._

_This request can also be made using the POST method,
with a request to `data.json` and
a JSON request body instead of query parameters._

```python
def get_data(self,
            device_ids,
            data_signal_ids,
            timestamp_start,
            timestamp_end,
            use_utc=False,
            resolution='10minute',
            aggregate='device',
            aggregate_level=0,
            calculation=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | `List[int]` | Query, Required | Which devices to get data for.<br><br>**Constraints**: `>= 1` |
| `data_signal_ids` | `List[int]` | Query, Required | Which data signals to get data for.<br><br>**Constraints**: `>= 1` |
| `timestamp_start` | `datetime` | Query, Required | The beginning of the time interval to get data for (inclusive),<br>in [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)<br>**date-time** format:<br><br>* Timestamps ending with 'Z' are treated as UTC. Example: "2020-01-01T00:00:00Z"<br>* Time zone (UTC) offset timestamps ending with '+HH:mm'/"-HH:mm" are also supported. Example: "2020-01-01T02:00:00-02:00"<br>* Other timestamps are treated as being in the time zone configured in the Greenbyte Platform. Example: "2020-01-01T00:00:00"<br><br>The start timestamp **is** included in the time interval: for<br>example, to select the full month of March 2020, set<br>`timestampStart` to "2020-03-01T00:00:00" and `timestampEnd` to<br>"2020-04-01T00:00:00".<br><br>Timestamps selected in the portal will by default be in UTC. |
| `timestamp_end` | `datetime` | Query, Required | The end of the time interval to get data for (exclusive),<br>in [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)<br>**date-time** format:<br><br>* Timestamps ending with 'Z' are treated as UTC. Example: "2020-01-01T00:00:00Z"<br>* Time zone (UTC) offset timestamps ending with '+HH:mm'/"-HH:mm" are also supported. Example: "2020-01-01T02:00:00-02:00"<br>* Other timestamps are treated as being in the time zone configured in the Greenbyte Platform. Example: "2020-01-01T00:00:00"<br><br>The end timestamp is **not** included in the time interval: for<br>example, to select the full month of March 2020, set<br>`timestampStart` to "2020-03-01T00:00:00" and `timestampEnd` to<br>"2020-04-01T00:00:00".<br><br>Timestamps selected in the portal will by default be in UTC. |
| `use_utc` | `bool` | Query, Optional | Set to true to get timestamps in UTC. UTC timestamps are available for all resolutions other than daily, weekly, monthly and yearly.<br><br>**Default**: `False` |
| `resolution` | [`ResolutionEnum`](../../doc/models/resolution-enum.md) | Query, Optional | The desired data resolution.<br><br>**Default**: `'10minute'` |
| `aggregate` | [`AggregateModeEnum`](../../doc/models/aggregate-mode-enum.md) | Query, Optional | How the data should be aggregated with regards to device(s) or site(s).<br><br>**Default**: `'device'` |
| `aggregate_level` | `int` | Query, Optional | When AggregateMode `siteLevel` is used this parameter controls down to which level in the hierarchy to aggregate.<br><br>**Default**: `0` |
| `calculation` | [`CalculationModeEnum`](../../doc/models/calculation-mode-enum.md) | Query, Optional | The calculation used when aggregating data, both over time and across devices. The default is the data signal default. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[DataItem]`](../../doc/models/data-item.md).

## Example Usage

```python
device_ids = [
    1,
    2,
    3
]

data_signal_ids = [
    1,
    5
]

timestamp_start = dateutil.parser.parse('01/01/2024 00:00:00')

timestamp_end = dateutil.parser.parse('01/08/2024 00:00:00')

use_utc = False

resolution = ResolutionEnum.ENUM_10MINUTE

aggregate = AggregateModeEnum.SITE

aggregate_level = 0

calculation = CalculationModeEnum.SUM

result = data_controller.get_data(
    device_ids,
    data_signal_ids,
    timestamp_start,
    timestamp_end,
    use_utc=use_utc,
    resolution=resolution,
    aggregate=aggregate,
    aggregate_level=aggregate_level,
    calculation=calculation
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
    "aggregate": "device",
    "aggregateId": 1,
    "aggregatePathNames": [],
    "deviceIds": [
      1
    ],
    "resolution": "hourly",
    "calculation": "sum",
    "dataSignal": {
      "dataSignalId": 1,
      "title": "Wind speed",
      "unit": "m/s"
    },
    "data": {
      "2020-01-01T00:00:00": 6.89,
      "2020-01-01T01:00:00": 8.33
    }
  },
  {
    "aggregate": "device",
    "aggregateId": 1,
    "aggregatePathNames": [],
    "deviceIds": [
      1
    ],
    "resolution": "hourly",
    "calculation": "sum",
    "dataSignal": {
      "dataSignalId": 5,
      "title": "Power",
      "unit": "kW"
    },
    "data": {
      "2020-01-01T00:00:00": 584.33,
      "2020-01-01T01:00:00": 1014
    }
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


# Get Real Time Data

Gets the most recent data point for each
specified device and data signal. The timestamps are in UTC.

_🔐 This endpoint requires the **Data** endpoint permission._

_This request can also be made using the POST method,
with a request to `realtimedata.json` and
a JSON request body instead of query parameters._

```python
def get_real_time_data(self,
                      device_ids,
                      data_signal_ids,
                      aggregate='device',
                      aggregate_level=0,
                      calculation=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | `List[int]` | Query, Required | Which devices to get data for.<br><br>**Constraints**: `>= 1` |
| `data_signal_ids` | `List[int]` | Query, Required | Which data signals to get data for.<br><br>**Constraints**: `>= 1` |
| `aggregate` | [`AggregateModeEnum`](../../doc/models/aggregate-mode-enum.md) | Query, Optional | How the data should be aggregated with regards to device(s) or site(s).<br><br>**Default**: `'device'` |
| `aggregate_level` | `int` | Query, Optional | When AggregateMode `siteLevel` is used this parameter controls down to which level in the hierarchy to aggregate.<br><br>**Default**: `0` |
| `calculation` | [`CalculationModeRealTimeEnum`](../../doc/models/calculation-mode-real-time-enum.md) | Query, Optional | The calculation used when aggregating data, both over time and across devices. The default is the data signal default. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[DataRealTimeItem]`](../../doc/models/data-real-time-item.md).

## Example Usage

```python
device_ids = [
    1,
    2,
    3
]

data_signal_ids = [
    1,
    5
]

aggregate = AggregateModeEnum.SITE

aggregate_level = 0

calculation = CalculationModeRealTimeEnum.SUM

result = data_controller.get_real_time_data(
    device_ids,
    data_signal_ids,
    aggregate=aggregate,
    aggregate_level=aggregate_level,
    calculation=calculation
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
    "aggregate": "device",
    "aggregateId": 24,
    "aggregatePathNames": [],
    "deviceIds": [
      24
    ],
    "calculation": "sum",
    "dataSignal": {
      "dataSignalId": 5,
      "title": "Power",
      "unit": "kW"
    },
    "data": {
      "2020-03-17T12:50:02Z": 2174
    }
  },
  {
    "aggregate": "device",
    "aggregateId": 24,
    "aggregatePathNames": [],
    "deviceIds": [
      24
    ],
    "calculation": "sum",
    "dataSignal": {
      "dataSignalId": 1,
      "title": "Wind speed",
      "unit": "m/s"
    },
    "data": {
      "2020-03-17T12:50:02Z": 12.2
    }
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


# Get Data Per Category

Gets signal data aggregated per availability contract category.

_🔐 This endpoint requires the **Data** and **Statuses** endpoint permissions._

_This request can also be made using the POST method,
with a request to `datapercategory.json` and
a JSON request body instead of query parameters._

```python
def get_data_per_category(self,
                         device_ids,
                         data_signal_id,
                         timestamp_start,
                         timestamp_end,
                         aggregate='device',
                         aggregate_level=0,
                         category=None,
                         contract_type='service')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | `List[int]` | Query, Required | Which devices to get data for.<br><br>**Constraints**: `>= 1` |
| `data_signal_id` | `int` | Query, Required | Which signal to get data for; only Lost Production signals are supported at the moment.<br><br>**Constraints**: `>= 1` |
| `timestamp_start` | `datetime` | Query, Required | The beginning of the time interval to get data for (inclusive),<br>in [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)<br>**date-time** format:<br><br>* Timestamps ending with 'Z' are treated as UTC. Example: "2020-01-01T00:00:00Z"<br>* Time zone (UTC) offset timestamps ending with '+HH:mm'/"-HH:mm" are also supported. Example: "2020-01-01T02:00:00-02:00"<br>* Other timestamps are treated as being in the time zone configured in the Greenbyte Platform. Example: "2020-01-01T00:00:00"<br><br>The start timestamp **is** included in the time interval: for<br>example, to select the full month of March 2020, set<br>`timestampStart` to "2020-03-01T00:00:00" and `timestampEnd` to<br>"2020-04-01T00:00:00".<br><br>Timestamps selected in the portal will by default be in UTC. |
| `timestamp_end` | `datetime` | Query, Required | The end of the time interval to get data for (exclusive),<br>in [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)<br>**date-time** format:<br><br>* Timestamps ending with 'Z' are treated as UTC. Example: "2020-01-01T00:00:00Z"<br>* Time zone (UTC) offset timestamps ending with '+HH:mm'/"-HH:mm" are also supported. Example: "2020-01-01T02:00:00-02:00"<br>* Other timestamps are treated as being in the time zone configured in the Greenbyte Platform. Example: "2020-01-01T00:00:00"<br><br>The end timestamp is **not** included in the time interval: for<br>example, to select the full month of March 2020, set<br>`timestampStart` to "2020-03-01T00:00:00" and `timestampEnd` to<br>"2020-04-01T00:00:00".<br><br>Timestamps selected in the portal will by default be in UTC. |
| `aggregate` | [`AggregateModeEnum`](../../doc/models/aggregate-mode-enum.md) | Query, Optional | How the data should be aggregated with regards to device(s) or site(s).<br><br>**Default**: `'device'` |
| `aggregate_level` | `int` | Query, Optional | When AggregateMode `siteLevel` is used this parameter controls down to which level in the hierarchy to aggregate.<br><br>**Default**: `0` |
| `category` | [`List[StatusCategoryEnum]`](../../doc/models/status-category-enum.md) | Query, Optional | Which status categories to include. By default all categories are included. |
| `contract_type` | [`ContractTypeEnum`](../../doc/models/contract-type-enum.md) | Query, Optional | Which contract type to use if using multiple availability contracts.<br><br>**Default**: `'service'` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DataPerCategoryResponse`](../../doc/models/data-per-category-response.md).

## Example Usage

```python
device_ids = [
    1,
    2,
    3
]

data_signal_id = 248

timestamp_start = dateutil.parser.parse('01/01/2024 00:00:00')

timestamp_end = dateutil.parser.parse('01/08/2024 00:00:00')

aggregate = AggregateModeEnum.SITE

aggregate_level = 0

category = [
    StatusCategoryEnum.STOP
]

contract_type = ContractTypeEnum.SERVICE

result = data_controller.get_data_per_category(
    device_ids,
    data_signal_id,
    timestamp_start,
    timestamp_end,
    aggregate=aggregate,
    aggregate_level=aggregate_level,
    category=category,
    contract_type=contract_type
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "dataSignal": {
    "dataSignalId": 248,
    "title": "Lost Production (Contractual)",
    "unit": "kWh"
  },
  "calculation": "sum",
  "data": [
    {
      "aggregateId": 6,
      "aggregatePathNames": [],
      "deviceIds": [
        1,
        2,
        3
      ],
      "contractTitle": "Vestas 1",
      "categoryTitle": "Icing",
      "categoryTime": "available",
      "value": 104.55,
      "duration": 150
    },
    {
      "aggregateId": 6,
      "aggregatePathNames": [],
      "deviceIds": [
        1,
        2,
        3
      ],
      "contractTitle": "Vestas 1",
      "categoryTitle": "Utility",
      "categoryTime": "excluded",
      "value": 73,
      "duration": 50.3
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be fulfilled due to bad syntax. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | The request is missing a valid API key. | `APIException` |
| 403 | One of the following:<br><br>* The API key does not authorize access to the requested endpoint because of a missing endpoint permission.<br>* The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. | `APIException` |
| 405 | The HTTP method is not allowed for the endpoint. | `APIException` |
| 429 | The API key has been used in too many requests in a given amount<br>of time. The following headers will be set in the response:<br><br>* `X-Rate-Limit-Limit` – The rate limit period (for example<br>  "1m", "12h", or "1d").<br>* `X-Rate-Limit-Remaining` – The remaining number of requests<br>  for this period.<br>* `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601<br>  format) when the remaining number of requests resets.<br><br>The limit is currently 1,000 requests/minute per API key and IP<br>address. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get High Res Data

Gets high resolution data for a data signal for each
specified device. The timestamps are in UTC.

The endpoint returns up to an hour's worth of high resolution data for the provided device IDs and data signal ID.
It is possible to request data for up to 10 separate devices and one data signal ID.
Timestamp start and end are optional. The default time span returned is the latest hour.
If supplied, timestamp start must be within the past 12 hours.
Timestamp end will by default be an hour after timestamp start but can be set for shorter intervals.

There is no high resolution data available for data signals that are calculated.
The data for those signals can be retrieved through the data endpoint.

_🔐 This endpoint requires the **HighResolution** endpoint permission._

```python
def get_high_res_data(self,
                     device_ids,
                     data_signal_id,
                     timestamp_start=None,
                     timestamp_end=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | `List[int]` | Query, Required | Which devices to get data for.<br><br>**Constraints**: `>= 1` |
| `data_signal_id` | `int` | Query, Required | Which data signal to get data for.<br><br>**Constraints**: `>= 1` |
| `timestamp_start` | `datetime` | Query, Optional | The beginning of the time interval to get data for (inclusive),<br>in [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)<br>**date-time** format:<br><br>* Timestamps ending with 'Z' are treated as UTC. Example: "2020-01-01T00:00:00Z"<br>* Time zone (UTC) offset timestamps ending with '+HH:mm'/"-HH:mm" are also supported. Example: "2020-01-01T02:00:00-02:00"<br>* Other timestamps are treated as being in the time zone configured in the Greenbyte Platform. Example: "2020-01-01T00:00:00"<br><br>The start timestamp **is** included in the time interval: for<br>example, to select the full month of March 2020, set<br>`timestampStart` to "2020-03-01T00:00:00" and `timestampEnd` to<br>"2020-04-01T00:00:00".<br><br>Timestamps selected in the portal will by default be in UTC. |
| `timestamp_end` | `datetime` | Query, Optional | The end of the time interval to get data for (exclusive),<br>in [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)<br>**date-time** format:<br><br>* Timestamps ending with 'Z' are treated as UTC. Example: "2020-01-01T00:00:00Z"<br>* Time zone (UTC) offset timestamps ending with '+HH:mm'/"-HH:mm" are also supported. Example: "2020-01-01T02:00:00-02:00"<br>* Other timestamps are treated as being in the time zone configured in the Greenbyte Platform. Example: "2020-01-01T00:00:00"<br><br>The end timestamp is **not** included in the time interval: for<br>example, to select the full month of March 2020, set<br>`timestampStart` to "2020-03-01T00:00:00" and `timestampEnd` to<br>"2020-04-01T00:00:00".<br><br>Timestamps selected in the portal will by default be in UTC. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[HighresdataResponse]`](../../doc/models/highresdata-response.md).

## Example Usage

```python
device_ids = [
    1,
    2,
    3
]

data_signal_id = 1

timestamp_start = dateutil.parser.parse('01/01/2024 00:00:00')

timestamp_end = dateutil.parser.parse('01/08/2024 00:00:00')

result = data_controller.get_high_res_data(
    device_ids,
    data_signal_id,
    timestamp_start=timestamp_start,
    timestamp_end=timestamp_end
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
    "deviceId": 24,
    "dataSignal": {
      "dataSignalId": 1,
      "title": "Wind speed",
      "unit": "m/s"
    },
    "data": {
      "2021-04-09T04:14:18Z": 6.21827459335327,
      "2021-04-09T04:14:48Z": 6.46509933471681,
      "2021-04-09T04:15:18Z": 7.41247510910034,
      "2021-04-09T04:15:48Z": 6.71687459945679,
      "2021-04-09T04:16:20Z": 5.66159963607788
    }
  },
  {
    "deviceId": 25,
    "dataSignal": {
      "dataSignalId": 1,
      "title": "Wind speed",
      "unit": "m/s"
    },
    "data": {
      "2021-04-09T04:14:18Z": 5.81789970397949,
      "2021-04-09T04:14:48Z": 5.43127489089966,
      "2021-04-09T04:15:18Z": 7.41247510910034,
      "2021-04-09T04:15:48Z": 5.58427476882935,
      "2021-04-09T04:16:20Z": 6.80189990997314
    }
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

