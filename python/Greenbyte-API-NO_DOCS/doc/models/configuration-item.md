
# Configuration Item

Your configuration data.

## Structure

`ConfigurationItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client` | [`ClientConfiguration`](../../doc/models/client-configuration.md) | Required | General configuration data. |
| `time_zone` | [`TimeZoneConfiguration`](../../doc/models/time-zone-configuration.md) | Required | The time zone configuration. |
| `data_signals` | [`DataSignalConfiguration`](../../doc/models/data-signal-configuration.md) | Required | Your data signal configuration. These only apply to wind devices. |

## Example (as JSON)

```json
{
  "client": {
    "title": "intro",
    "tag": "intro",
    "urlWeb": "https://intro.greenbyte.cloud/",
    "urlApi": "https://intro.greenbyte.cloud/api/2/"
  },
  "timeZone": {
    "title": "Europe/Stockholm",
    "utcOffset": 1.0,
    "utcOffsetDst": 2.0,
    "dstTimestampStart": "03/29/2020 01:00:00",
    "dstTimestampEnd": "10/25/2020 01:00:00"
  },
  "dataSignals": {
    "availabilityTimeDataSignalId": 202,
    "availabilityProductionDataSignalId": 74,
    "lostProductionDataSignalId": 130,
    "performanceDataSignalId": 30
  }
}
```

