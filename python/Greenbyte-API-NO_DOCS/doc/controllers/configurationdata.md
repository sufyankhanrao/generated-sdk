# Configurationdata

```python
configurationdata_controller = client.configurationdata
```

## Class Name

`ConfigurationdataController`


# Get Configuration

Gets your system-wide configuration data.

_🔐 This endpoint requires the **Configuration** endpoint permission._

_This request can also be made using the POST method,
with a request to `configuration.json` and
a JSON request body instead of query parameters._

```python
def get_configuration(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[ConfigurationItem]`](../../doc/models/configuration-item.md).

## Example Usage

```python
result = configuration_data_controller.get_configuration()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
[
  {
    "client": {
      "title": "Intro (Greenbyte AB)",
      "tag": "intro",
      "urlWeb": "https://intro.greenbyte.cloud/",
      "urlApi": "https://intro.greenbyte.cloud/api/2/"
    },
    "timeZone": {
      "title": "Europe/Stockholm",
      "utcOffset": 1,
      "utcOffsetDst": 2,
      "dstTimestampStart": "2020-03-29T01:00:00",
      "dstTimestampEnd": "2020-10-25T01:00:00"
    },
    "dataSignals": {
      "availabilityTimeDataSignalId": 430,
      "availabilityProductionDataSignalId": 445,
      "lostProductionDataSignalId": 432,
      "performanceDataSignalId": 436
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

