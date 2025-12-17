# Assets

This section contains operations related to assets, such as sites and devices.

## Devices

In this context, *devices* are power-producing devices such as wind turbines and inverters as well as instruments such as met masts and grid meters, which measure, record, and communicate data and metadata for a site or device.

## Power curves

Power curves are graphs which indicate how large the electrical power output of a wind turbine will be at different wind speeds.

Power curves are used for potential power calculation and for performance KPIs. The default power curve is defined when the wind turbine is installed in the Greenbyte Platform, but you can alter the default or add power curves as needed. Having multiple power curves enables calculations in the system to adapt to different circumstances, like curtailment, sector management, or technical management.

```python
assets_controller = client.assets
```

## Class Name

`AssetsController`

## Methods

* [Get Devices](../../doc/controllers/assets.md#get-devices)
* [Get Devices Published After Date](../../doc/controllers/assets.md#get-devices-published-after-date)
* [Get Sites](../../doc/controllers/assets.md#get-sites)
* [Get Power Curves](../../doc/controllers/assets.md#get-power-curves)


# Get Devices

Gets a list of devices that the API key has permissions for.

_🔐 This endpoint requires the **Assets** endpoint permission._

_This request can also be made using the POST method,
with a request to `devices.json` and
a JSON request body instead of query parameters._

```python
def get_devices(self,
               device_type_ids=None,
               site_ids=None,
               parent_ids=None,
               fields=None,
               page_size=50,
               page=1,
               use_utc=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_type_ids` | `List[int]` | Query, Optional | Only include devices of these types.<br>Examples:<br><br>* 1 - Wind turbine<br>* 2 - Production meter<br>* 3 - Met mast<br>* 4 - Inverter<br>* 10 - Device group<br>* 11 - Grid meter<br>* 12 - Combiner box<br>* 23 - String<br>* 27 - Virtual Meteo Sensor<br><br>**Constraints**: `>= 1` |
| `site_ids` | `List[int]` | Query, Optional | Only include devices at these sites.<br><br>**Constraints**: `>= 1` |
| `parent_ids` | `List[int]` | Query, Optional | Only include devices with these parent devices.<br><br>**Constraints**: `>= 1` |
| `fields` | `List[str]` | Query, Optional | Which fields to include in the response. Valid fields are those defined in the `Device` schema (See Response Type). By default all fields are included. |
| `page_size` | `int` | Query, Optional | The number of items to return per page.<br><br>**Default**: `50` |
| `page` | `int` | Query, Optional | Which page to return when the number of items exceed the page size.<br><br>**Default**: `1` |
| `use_utc` | `bool` | Query, Optional | Set to true to get timestamps in UTC.<br><br>**Default**: `False` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[Device]`](../../doc/models/device.md).

## Example Usage

```python
device_type_ids = [
    1,
    2,
    3
]

site_ids = [
    1,
    2,
    3
]

parent_ids = [
    1,
    2,
    3
]

page_size = 50

page = 1

use_utc = False

result = assets_controller.get_devices(
    device_type_ids=device_type_ids,
    site_ids=site_ids,
    parent_ids=parent_ids,
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
    "deviceId": 1121,
    "title": "Enerburg group A",
    "altTitle": null,
    "identity": null,
    "site": {
      "siteId": 7,
      "title": "Enerburg"
    },
    "deviceType": "Group",
    "deviceTypeId": 10,
    "parentId": null,
    "childIds": [
      69,
      70
    ],
    "deviceModel": {
      "deviceModelId": 41,
      "manufacturer": "Generic group",
      "model": "Generic"
    },
    "maxPower": 0,
    "timestampStart": "2013-10-01T02:00:00",
    "latitude": "32.36431",
    "longitude": "-88.7037",
    "elevation": "0",
    "metadata": []
  },
  {
    "deviceId": 69,
    "title": "Enerburg 1",
    "altTitle": null,
    "identity": null,
    "site": {
      "siteId": 7,
      "title": "Enerburg"
    },
    "deviceType": "Turbine",
    "deviceTypeId": 1,
    "parentId": 1121,
    "childIds": [],
    "deviceModel": null,
    "turbineType": {
      "turbineTypeId": 1,
      "title": "Enercon E-82 E2 2.3MW",
      "manufacturer": "Enercon",
      "model": "E-82",
      "controller": "CS82a",
      "ratedPower": 2300,
      "maxRotorSpeed": 18
    },
    "maxPower": 2300,
    "biddingArea": null,
    "timestampStart": "2013-10-01T02:00:00",
    "latitude": "32.36431",
    "longitude": "-88.7037",
    "elevation": "0",
    "targetAvailability": 97,
    "metadata": [
      {
        "key": "Hub Height",
        "value": "120"
      },
      {
        "key": "Direct Drive",
        "value": "no"
      },
      {
        "key": "Blade Heating",
        "value": "yes"
      }
    ]
  },
  {
    "deviceId": 70,
    "title": "Enerburg 2",
    "altTitle": null,
    "identity": null,
    "site": {
      "siteId": 7,
      "title": "Enerburg"
    },
    "deviceType": "Turbine",
    "deviceTypeId": 1,
    "parentId": 1121,
    "childIds": [],
    "deviceModel": null,
    "turbineType": {
      "turbineTypeId": 1,
      "title": "Enercon E-82 E2 2.3MW",
      "manufacturer": "Enercon",
      "model": "E-82",
      "controller": "CS82a",
      "ratedPower": 2300,
      "maxRotorSpeed": 18
    },
    "maxPower": 2300,
    "biddingArea": null,
    "timestampStart": "2013-10-01T02:00:00",
    "latitude": "32.3602",
    "longitude": "-88.7194",
    "elevation": "0",
    "targetAvailability": null,
    "metadata": [
      {
        "key": "Hub Height",
        "value": "120"
      },
      {
        "key": "Direct Drive",
        "value": "no"
      },
      {
        "key": "Blade Heating",
        "value": "yes"
      }
    ]
  },
  {
    "deviceId": 71,
    "title": "Enerburg 3",
    "altTitle": null,
    "identity": null,
    "site": {
      "siteId": 7,
      "title": "Enerburg"
    },
    "deviceType": "Turbine",
    "deviceModel": null,
    "parentId": null,
    "childIds": [],
    "deviceTypeId": 1,
    "turbineType": {
      "turbineTypeId": 1,
      "title": "Enercon E-82 E2 2.3MW",
      "manufacturer": "Enercon",
      "model": "E-82",
      "controller": "CS82a",
      "ratedPower": 2300,
      "maxRotorSpeed": 18
    },
    "maxPower": 2300,
    "biddingArea": null,
    "timestampStart": "2013-10-01T02:00:00",
    "latitude": "32.35697",
    "longitude": "-88.7182",
    "elevation": "0",
    "targetAvailability": null,
    "metadata": []
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


# Get Devices Published After Date

Gets the number of devices published on a site after a certain date as well as the IDs of the authorized devices.

_🔐 This endpoint requires the **Assets** endpoint permission._

```python
def get_devices_published_after_date(self,
                                    site_id,
                                    date)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `int` | Query, Required | **Constraints**: `>= 1` |
| `date` | `datetime` | Query, Required | Date after which published devices will be fetched. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DevicesPublishedAfterDateResponse`](../../doc/models/devices-published-after-date-response.md).

## Example Usage

```python
site_id = 222

date = dateutil.parser.parse('04/01/2023 00:00:00')

result = assets_controller.get_devices_published_after_date(
    site_id,
    date
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "numberOfDevices": 4,
  "authorizedDeviceIds": [
    2,
    3,
    4
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


# Get Sites

Gets a list of sites that the API key has permissions
for.

_🔐 This endpoint requires the **Assets** endpoint permission._

_This request can also be made using the POST method,
with a request to `sites.json` and
a JSON request body instead of query parameters._

```python
def get_sites(self,
             fields=None,
             page_size=50,
             page=1)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fields` | `List[str]` | Query, Optional | Which fields to include in the response. Valid fields are those defined in the `SiteWithData` schema (See Response Type). By default all fields are included. |
| `page_size` | `int` | Query, Optional | The number of items to return per page.<br><br>**Default**: `50` |
| `page` | `int` | Query, Optional | Which page to return when the number of items exceed the page size.<br><br>**Default**: `1` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[SiteWithData]`](../../doc/models/site-with-data.md).

## Example Usage

```python
fields = [
    'siteId',
    'title'
]

page_size = 50

page = 1

result = assets_controller.get_sites(
    fields=fields,
    page_size=page_size,
    page=page
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
    "siteId": 1,
    "title": "Wind farm 1",
    "country": "Sweden",
    "identity": "SE-WF1",
    "metadata": [
      {
        "key": "Address",
        "value": "Wind Street 123"
      },
      {
        "key": "Phone",
        "value": "555 123 456"
      }
    ]
  },
  {
    "siteId": 2,
    "title": "Solar site 1",
    "country": "Spain",
    "identity": "ES-SS1",
    "metadata": [
      {
        "key": "Address",
        "value": "Sun Street 456"
      },
      {
        "key": "Phone",
        "value": "555 456 789"
      }
    ]
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


# Get Power Curves

Gets the default or learned power curves for wind turbines.
Other device types are not supported.

_🔐 This endpoint requires the **PowerCurves** endpoint permission._

_This request can also be made using the POST method,
with a request to `powercurves.json` and
a JSON request body instead of query parameters._

```python
def get_power_curves(self,
                    device_ids,
                    timestamp=None,
                    learned=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | `List[int]` | Query, Required | What devices to get power curves for. Only wind turbines are supported.<br><br>**Constraints**: `>= 1` |
| `timestamp` | `date` | Query, Optional | The date for which to get power curves. The default is the current date. |
| `learned` | `bool` | Query, Optional | Whether to get learned power curves instead of default power curves.<br><br>**Default**: `False` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[PowerCurve]`](../../doc/models/power-curve.md).

## Example Usage

```python
device_ids = [
    1,
    2,
    3
]

timestamp = dateutil.parser.parse('2023-03-01').date()

learned = False

result = assets_controller.get_power_curves(
    device_ids,
    timestamp=timestamp,
    learned=learned
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
    "deviceId": 1,
    "title": "Enercon E-82 Noise mode 0",
    "values": [
      {
        "windSpeed": 1,
        "power": 0
      },
      {
        "windSpeed": 4,
        "power": 88
      },
      {
        "windSpeed": 5,
        "power": 205
      },
      {
        "windSpeed": 6,
        "power": 371
      },
      {
        "windSpeed": 7,
        "power": 601
      },
      {
        "windSpeed": 8,
        "power": 901
      },
      {
        "windSpeed": 9,
        "power": 1243
      },
      {
        "windSpeed": 10,
        "power": 1591
      },
      {
        "windSpeed": 11,
        "power": 1876
      },
      {
        "windSpeed": 12,
        "power": 1979
      },
      {
        "windSpeed": 13,
        "power": 1999
      },
      {
        "windSpeed": 14,
        "power": 2000
      },
      {
        "windSpeed": 15,
        "power": 2000
      },
      {
        "windSpeed": 16,
        "power": 2000
      },
      {
        "windSpeed": 17,
        "power": 2000
      },
      {
        "windSpeed": 18,
        "power": 2000
      },
      {
        "windSpeed": 19,
        "power": 2000
      },
      {
        "windSpeed": 20,
        "power": 2000
      },
      {
        "windSpeed": 21,
        "power": 2000
      },
      {
        "windSpeed": 22,
        "power": 2000
      },
      {
        "windSpeed": 23,
        "power": 2000
      },
      {
        "windSpeed": 24,
        "power": 2000
      },
      {
        "windSpeed": 25,
        "power": 2000
      }
    ]
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

