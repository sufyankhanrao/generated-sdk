
# Get Sites Request

## Structure

`GetSitesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_ids` | `List[int]` | Optional | List of the requested site IDs. When omitted, returns all sites that the source has access to. |
| `include_lead_channels` | `bool` | Optional | This is an optional parameter to get lead channels for a Site. |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "SiteIds": [
    251,
    252,
    253
  ],
  "IncludeLeadChannels": false,
  "Limit": 26,
  "Offset": 92
}
```

