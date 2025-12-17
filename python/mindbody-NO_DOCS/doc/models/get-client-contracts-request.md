
# Get Client Contracts Request

## Structure

`GetClientContractsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Required | The ID of the client (RssId). |
| `cross_regional_lookup` | `bool` | Optional | When `true`, indicates that the requesting client’s cross regional contracts are returned, if any.<br /><br>When `false`, indicates that cross regional contracts are not returned. |
| `client_associated_sites_offset` | `int` | Optional | Determines how many sites are skipped over when retrieving a client’s cross regional contracts. Used when a client ID is linked to more than ten sites in an organization. Only a maximum of ten site databases are queried when this call is made and `CrossRegionalLookup` is set to `true`. To change which sites are queried, change this offset value.<br>Default: **0** |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ClientId": "ClientId2",
  "CrossRegionalLookup": false,
  "ClientAssociatedSitesOffset": 36,
  "Limit": 148,
  "Offset": 82
}
```

