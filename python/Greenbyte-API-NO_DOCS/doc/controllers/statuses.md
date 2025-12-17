# Statuses

This section contains operations related to device statuses. Device statuses are related to availability contracts.
[Availability contracts in the Greenbyte Platform documentation](https://help.greenbyte.com/Greenbyte/en/availability-contracts.html)

```python
statuses_controller = client.statuses
```

## Class Name

`StatusesController`

## Methods

* [Get Statuses](../../doc/controllers/statuses.md#get-statuses)
* [Get Active Statuses](../../doc/controllers/statuses.md#get-active-statuses)


# Get Statuses

Gets statuses for multiple devices during the given time period.
The timestamps are in the time zone configured in the Greenbyte Platform.
Use the useUtc flag to get timestamps in UTC.

_🔐 This endpoint requires the **Statuses** endpoint permission._

_This request can also be made using the POST method,
with a request to `status.json` and
a JSON request body instead of query parameters._

```python
def get_statuses(self,
                device_ids,
                timestamp_start,
                timestamp_end,
                category=None,
                lost_production_signal_id=None,
                fields=None,
                sort_by=None,
                sort_asc=False,
                page_size=50,
                page=1,
                use_utc=False,
                contract_type="service")
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | `List[int]` | Query, Required | Which devices to get statuses for.<br><br>**Constraints**: `>= 1` |
| `timestamp_start` | `datetime` | Query, Required | The beginning of the time interval to get data for (inclusive),<br>in [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)<br>**date-time** format:<br><br>* Timestamps ending with 'Z' are treated as UTC. Example: "2020-01-01T00:00:00Z"<br>* Time zone (UTC) offset timestamps ending with '+HH:mm'/"-HH:mm" are also supported. Example: "2020-01-01T02:00:00-02:00"<br>* Other timestamps are treated as being in the time zone configured in the Greenbyte Platform. Example: "2020-01-01T00:00:00"<br><br>The start timestamp **is** included in the time interval: for<br>example, to select the full month of March 2020, set<br>`timestampStart` to "2020-03-01T00:00:00" and `timestampEnd` to<br>"2020-04-01T00:00:00".<br><br>Timestamps selected in the portal will by default be in UTC. |
| `timestamp_end` | `datetime` | Query, Required | The end of the time interval to get data for (exclusive),<br>in [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)<br>**date-time** format:<br><br>* Timestamps ending with 'Z' are treated as UTC. Example: "2020-01-01T00:00:00Z"<br>* Time zone (UTC) offset timestamps ending with '+HH:mm'/"-HH:mm" are also supported. Example: "2020-01-01T02:00:00-02:00"<br>* Other timestamps are treated as being in the time zone configured in the Greenbyte Platform. Example: "2020-01-01T00:00:00"<br><br>The end timestamp is **not** included in the time interval: for<br>example, to select the full month of March 2020, set<br>`timestampStart` to "2020-03-01T00:00:00" and `timestampEnd` to<br>"2020-04-01T00:00:00".<br><br>Timestamps selected in the portal will by default be in UTC. |
| `category` | [`List[StatusCategoryEnum]`](../../doc/models/status-category-enum.md) | Query, Optional | Which status categories to get statuses for. |
| `lost_production_signal_id` | `int` | Query, Optional | Which data signal to use for calculating lost production. Defaults to the configured default lost production signal.<br><br>**Constraints**: `>= 1` |
| `fields` | `List[str]` | Query, Optional | Which fields to include in the response. Valid fields are those defined in the `StatusItem` schema (See Response Type). By default all fields are included. |
| `sort_by` | `List[str]` | Query, Optional | Which fields to sort the response items by. |
| `sort_asc` | `bool` | Query, Optional | Whether to sort the items in ascending order.<br><br>**Default**: `False` |
| `page_size` | `int` | Query, Optional | The number of items to return per page.<br><br>**Default**: `50` |
| `page` | `int` | Query, Optional | Which page to return when the number of items exceed the page size.<br><br>**Default**: `1` |
| `use_utc` | `bool` | Query, Optional | Set to true to get timestamps in UTC.<br><br>**Default**: `False` |
| `contract_type` | [`ContractTypeEnum`](../../doc/models/contract-type-enum.md) | Query, Optional | Which contract type to use if using multiple availability contracts.<br><br>**Default**: `"service"` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[StatusItem]`](../../doc/models/status-item.md).

## Example Usage

```python
device_ids = [
    1,
    2,
    3
]

timestamp_start = dateutil.parser.parse('01/01/2024 00:00:00')

timestamp_end = dateutil.parser.parse('01/08/2024 00:00:00')

lost_production_signal_id = 432

fields = [
    'deviceId',
    'message',
    'lostProduction'
]

sort_asc = False

page_size = 50

page = 1

use_utc = False

contract_type = ContractTypeEnum.SERVICE

result = statuses_controller.get_statuses(
    device_ids,
    timestamp_start,
    timestamp_end,
    lost_production_signal_id=lost_production_signal_id,
    fields=fields,
    sort_asc=sort_asc,
    page_size=page_size,
    page=page,
    use_utc=use_utc,
    contract_type=contract_type
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
    "turbineStatusId": 8983231,
    "lostProductionSignal": {
      "dataSignalId": 432,
      "title": "Lost Production to Downtime",
      "unit": "kWh"
    },
    "lostProduction": 3899.5309669995286,
    "categoryIec": "Requested Shutdown",
    "categoryContract": "Preventive Maintenance",
    "categoryGlobalContract": null,
    "categoryCustomContract": null,
    "subStatus": [],
    "deviceId": 25,
    "timestampStart": "2021-12-12T22:07:10",
    "timestampEnd": "2021-12-13T07:16:48",
    "hasTimestampEnd": true,
    "category": "stop",
    "code": 615,
    "message": "Maintenance: Maintenance",
    "comment": null,
    "acknowledged": false,
    "component": {
      "componentId": 123,
      "componentName": "Converter System",
      "componentTag": "MSE"
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


# Get Active Statuses

Gets active statuses for multiple devices.
The timestamps are in the time zone configured in the Greenbyte Platform.
Use the useUtc flag to get timestamps in UTC.

_🔐 This endpoint requires the **Statuses** endpoint permission._

_This request can also be made using the POST method,
with a request to `activestatus.json` and
a JSON request body instead of query parameters._

```python
def get_active_statuses(self,
                       device_ids,
                       category=None,
                       lost_production_signal_id=None,
                       fields=None,
                       sort_by=None,
                       sort_asc=False,
                       page_size=50,
                       page=1,
                       use_utc=False,
                       contract_type="service")
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | `List[int]` | Query, Required | Which devices to get statuses for.<br><br>**Constraints**: `>= 1` |
| `category` | [`List[StatusCategoryEnum]`](../../doc/models/status-category-enum.md) | Query, Optional | Which status categories to get statuses for. |
| `lost_production_signal_id` | `int` | Query, Optional | Which data signal to use for calculating lost production. Defaults to the configured default lost production signal.<br><br>**Constraints**: `>= 1` |
| `fields` | `List[str]` | Query, Optional | Which fields to include in the response. Valid fields are those defined in the `StatusItem` schema (See Response Type). By default all fields are included. |
| `sort_by` | `List[str]` | Query, Optional | Which fields to sort the response items by. |
| `sort_asc` | `bool` | Query, Optional | Whether to sort the items in ascending order.<br><br>**Default**: `False` |
| `page_size` | `int` | Query, Optional | The number of items to return per page.<br><br>**Default**: `50` |
| `page` | `int` | Query, Optional | Which page to return when the number of items exceed the page size.<br><br>**Default**: `1` |
| `use_utc` | `bool` | Query, Optional | Set to true to get timestamps in UTC.<br><br>**Default**: `False` |
| `contract_type` | [`ContractTypeEnum`](../../doc/models/contract-type-enum.md) | Query, Optional | Which contract type to use if using multiple availability contracts.<br><br>**Default**: `"service"` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[StatusItem]`](../../doc/models/status-item.md).

## Example Usage

```python
device_ids = [
    1,
    2,
    3
]

lost_production_signal_id = 432

fields = [
    'deviceId',
    'message',
    'lostProduction'
]

sort_asc = False

page_size = 50

page = 1

use_utc = False

contract_type = ContractTypeEnum.SERVICE

result = statuses_controller.get_active_statuses(
    device_ids,
    lost_production_signal_id=lost_production_signal_id,
    fields=fields,
    sort_asc=sort_asc,
    page_size=page_size,
    page=page,
    use_utc=use_utc,
    contract_type=contract_type
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
    "lostProduction": 696.16,
    "lostProductionSignal": {
      "dataSignalId": 432,
      "title": "Lost Production to Downtime",
      "unit": "kWh"
    },
    "deviceId": 4,
    "code": 8000,
    "message": "Maintenance: Maintenance"
  },
  {
    "lostProduction": 0,
    "lostProductionSignal": {
      "dataSignalId": 432,
      "title": "Lost Production to Downtime",
      "unit": "kWh"
    },
    "deviceId": 4,
    "code": 21001,
    "message": "Cable twisted: Left (2-3 turns)"
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

