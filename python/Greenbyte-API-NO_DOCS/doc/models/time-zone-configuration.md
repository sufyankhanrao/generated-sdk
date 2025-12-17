
# Time Zone Configuration

The time zone configuration.

## Structure

`TimeZoneConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `title` | `str` | Required | The title of the time zone. |
| `utc_offset` | `float` | Required | The UTC offset for the time zone. |
| `utc_offset_dst` | `float` | Required | The UTC offset for the time zone during daylight savings time. |
| `dst_timestamp_start` | `datetime` | Required | The start of daylight savings time in the time zone. This timestamp is given in UTC. |
| `dst_timestamp_end` | `datetime` | Required | The end of daylight savings time in the time zone. This timestamp is given in UTC. |

## Example (as JSON)

```json
{
  "title": "Europe/Stockholm",
  "utcOffset": 1.0,
  "utcOffsetDst": 2.0,
  "dstTimestampStart": "03/29/2020 01:00:00",
  "dstTimestampEnd": "10/25/2020 01:00:00"
}
```

