
# Get Client Complete Info Request

request for GetClientCompleteInfoRequest

## Structure

`GetClientCompleteInfoRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Required | Filters results to client with these ID. |
| `start_date` | `datetime` | Optional | Filters results to pricing options that are purchased on or after this date.<br>Default: **today’s date**. |
| `end_date` | `datetime` | Optional | Filters results to pricing options that are purchased on or before this date.<br>Default: **today’s date**. |
| `cross_regional_lookup` | `bool` | Optional | Used to retrieve a clients pricing options from multiple sites within an organization.When included and set to `true`,<br>it searches a maximum of ten sites with which this client is associated.When a client is associated with more than ten sites, use `ClientAssociatedSitesOffset` as many times as needed to search the additional sites with which the client is associated.<br>You can use the `CrossRegionalClientAssociations` value from `GET CrossRegionalClientAssociations` to determine how many sites the client is associated with.<br>Note that a `SiteID` is returned and populated in the `ClientServices` response when `CrossRegionalLookup` is set to `true`.<br>Default: **false** |
| `client_associated_sites_offset` | `int` | Optional | Used to retrieve a client’s pricing options from multiple sites within an organization when the client is associated with more than ten sites. To change which ten sites are searched, change this offset value. A value of 0 means that no sites are skipped and the first ten sites are returned. You can use the `CrossRegionalClientAssociations` value from `GET CrossRegionalClientAssociations` to determine how many sites the client is associated with. Note that you must always have `CrossRegionalLookup` set to `true` to use this parameter.<br /><br>Default: **0**<br><br>For example, if a client is associated with 25 sites, you need to call `GetClientServices` three times, as follows:<br><br>* Use `GET CrossRegionalClientAssociations` to determine how many sites a client is associated with, which tells you how many additional calls you need to make.<br>* Either omit `ClientAssociatedSitesOffset` or set it to 0 to return the client’s services (pricing options) from sites 1-10.<br>* Set `ClientAssociatedSitesOffset` to 10 to return the client pricing options from sites 11-20<br>* Set `ClientAssociatedSitesOffset` to 20 to return the client pricing options from sites 21-25 |
| `required_client_data` | `List[str]` | Optional | Used to retrieve list of purchased services, contract details, membership details and arrival programs for a specific client.<br>Default `ClientServices`, `ClientContracts`, `ClientMemberships` and `ClientArrivals` will be returned when `RequiredClientDatais` not set.<br>When `RequiredClientData` is set to `Contracts` then only `ClientContracts` will be returned in the response.<br>When `RequiredClientData` is set to Services then only `ClientServices` will be returned in the response.<br>When `RequiredClientData` is set to `Memberships` then only `ClientMemberships` will be returned in the response.<br>When `RequiredClientData` is set to `ArrivalPrograms` then only `ClientArrivals` will be returned in the response. |
| `exclude_inactive_sites` | `bool` | Optional | Used to exclude inactive and deleted sites from the results |

## Example (as JSON)

```json
{
  "ClientId": "ClientId8",
  "StartDate": "2016-03-13T12:52:32.123Z",
  "EndDate": "2016-03-13T12:52:32.123Z",
  "CrossRegionalLookup": false,
  "ClientAssociatedSitesOffset": 6,
  "RequiredClientData": [
    "RequiredClientData1",
    "RequiredClientData2",
    "RequiredClientData3"
  ]
}
```

