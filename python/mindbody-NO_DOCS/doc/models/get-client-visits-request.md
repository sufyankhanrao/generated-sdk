
# Get Client Visits Request

## Structure

`GetClientVisitsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Required | The ID of the requested client. |
| `client_associated_sites_offset` | `int` | Optional | The number of sites to skip when returning the site associated with a client. |
| `cross_regional_lookup` | `bool` | Optional | When `true`, indicates that past and scheduled client visits across all sites in the region are returned.<br /><br>When `false`, indicates that only visits at the current site are returned. |
| `end_date` | `datetime` | Optional | The date past which class visits are not returned.<br>Default: **today’s date** |
| `start_date` | `datetime` | Optional | The date before which class visits are not returned.<br>Default: **the end date** |
| `unpaids_only` | `bool` | Optional | When `true`, indicates that only visits that have not been paid for are returned.<br /><br>When `false`, indicates that all visits are returned, regardless of whether they have been paid for.<br /><br>Default: **false** |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ClientId": "ClientId0",
  "ClientAssociatedSitesOffset": 92,
  "CrossRegionalLookup": false,
  "EndDate": "2016-03-13T12:52:32.123Z",
  "StartDate": "2016-03-13T12:52:32.123Z",
  "UnpaidsOnly": false
}
```

