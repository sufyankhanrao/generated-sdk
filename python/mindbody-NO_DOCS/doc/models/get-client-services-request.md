
# Get Client Services Request

## Structure

`GetClientServicesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Required | The ID of the client to query. The results are a list of pricing options that the client has purchased. Note that “service” and “pricing option” are synonymous in this section of the documentation. |
| `client_ids` | `List[str]` | Optional | The IDs of the clients to query. The results are a list of pricing options that the clients have purchased.<br>ClientId parameter takes priority over ClientIds due to backward compatibility.<br>So if you want to use ClientIds, then ClientId needs to be empty.<br>Either of ClientId or ClientIds need to be specified |
| `class_id` | `int` | Optional | Filters results to only those pricing options that can be used to pay for this class. |
| `program_ids` | `List[int]` | Optional | Filters results to pricing options that belong to one of the given program IDs. |
| `session_type_id` | `int` | Optional | Filters results to pricing options that will pay for the given session type ID. Use this to find pricing options that will pay for a specific appointment type. |
| `location_ids` | `List[int]` | Optional | Filters results to pricing options that can be used at the listed location IDs. |
| `visit_count` | `int` | Optional | A filter on the minimum number of visits a service can pay for. |
| `start_date` | `datetime` | Optional | Filters results to pricing options that are purchased on or after this date.<br>Default: **today’s date** |
| `end_date` | `datetime` | Optional | Filters results to pricing options that are purchased on or before this date.<br>Default: **today’s date** |
| `show_active_only` | `bool` | Optional | When `true`, includes active services only.<br>Default: **false** |
| `cross_regional_lookup` | `bool` | Optional | Used to retrieve a client’s pricing options from multiple sites within an organization. When included and set to `true`, it searches a maximum of ten sites with which this client is associated. When a client is associated with more than ten sites, use `ClientAssociatedSitesOffset` as many times as needed to search the additional sites with which the client is associated. You can use the `CrossRegionalClientAssociations` value from `GET CrossRegionalClientAssociations` to determine how many sites the client is associated with. Note that a `SiteID` is returned and populated in the `ClientServices` response when `CrossRegionalLookup` is set to `true`.<br>Default: **false** |
| `ignore_cross_regional_site_limit` | `bool` | Optional | Used to specify if the number of cross regional sites used to search for client’s pricing options should be ignored.<br>Default: **false** |
| `client_associated_sites_offset` | `int` | Optional | Used to retrieve a client’s pricing options from multiple sites within an organization when the client is associated with more than ten sites. To change which ten sites are searched, change this offset value. A value of 0 means that no sites are skipped and the first ten sites are returned. You can use the `CrossRegionalClientAssociations` value from `GET CrossRegionalClientAssociations` to determine how many sites the client is associated with. Note that you must always have `CrossRegionalLookup` set to `true` to use this parameter.<br /><br>Default: **0**<br><br>For example, if a client is associated with 25 sites, you need to call `GetClientServices` three times, as follows:<br><br>* Use `GET CrossRegionalClientAssociations` to determine how many sites a client is associated with, which tells you how many additional calls you need to make.<br>* Either omit `ClientAssociatedSitesOffset` or set it to 0 to return the client’s services (pricing options) from sites 1-10.<br>* Set `ClientAssociatedSitesOffset` to 10 to return the client pricing options from sites 11-20<br>* Set `ClientAssociatedSitesOffset` to 20 to return the client pricing options from sites 21-25 |
| `use_activate_date` | `bool` | Optional | When this flag is set to true the date filtering will use activate date to filter the pricing options<br>When this flag is set to false the date filtering will use purchase date to filter the pricing options [ Existing logic ] |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ClientId": "ClientId4",
  "ClientIds": [
    "ClientIds7"
  ],
  "ClassId": 82,
  "ProgramIds": [
    230,
    231,
    232
  ],
  "SessionTypeId": 74,
  "LocationIds": [
    208
  ]
}
```

