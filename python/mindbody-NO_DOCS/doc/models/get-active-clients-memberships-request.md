
# Get Active Clients Memberships Request

## Structure

`GetActiveClientsMembershipsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_ids` | `List[str]` | Required | The ID of the client for whom memberships are returned. Maximum allowed : 200. |
| `location_id` | `int` | Optional | Filters results to memberships that can be used to pay for scheduled services at that location. This parameter can not be passed when `CrossRegionalLookup` is `true`. |
| `cross_regional_lookup` | `bool` | Optional | Used to retrieve a client’s memberships from multiple sites within an organization. When included and set to `true`, it searches a maximum of ten sites with which this client is associated. When a client is associated with more than ten sites, use `ClientAssociatedSitesOffset` as many times as needed to search the additional sites with which the client is associated. You can use the `CrossRegionalClientAssociations` value from `GET CrossRegionalClientAssociations` to determine how many sites the client is associated with. Note that a `SiteID` is returned and populated in the `ClientServices` response when `CrossRegionalLookup` is set to `true`.<br>Default: **false** |
| `client_associated_sites_offset` | `int` | Optional | Used to retrieve a client’s memberships from multiple sites within an organization when the client is associated with more than ten sites. To change which ten sites are searched, change this offset value. A value of 0 means that no sites are skipped and the first ten sites are returned. You can use the `CrossRegionalClientAssociations` value from `GET CrossRegionalClientAssociations` to determine how many sites the client is associated with. Note that you must always have `CrossRegionalLookup` set to `true` to use this parameter.<br /><br>Default: **0**<br><br>For example, if a client is associated with 25 sites, you need to call `GetClientServices` three times, as follows:<br><br>* Use `GET CrossRegionalClientAssociations` to determine how many sites a client is associated with, which tells you how many additional calls you need to make.<br>* Either omit `ClientAssociatedSitesOffset` or set it to 0 to return the client’s services (pricing options) from sites 1-10.<br>* Set `ClientAssociatedSitesOffset` to 10 to return the client pricing options from sites 11-20<br>* Set `ClientAssociatedSitesOffset` to 20 to return the client pricing options from sites 21-25 |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ClientIds": [
    "ClientIds1"
  ],
  "LocationId": 160,
  "CrossRegionalLookup": false,
  "ClientAssociatedSitesOffset": 222,
  "Limit": 110,
  "Offset": 176
}
```

