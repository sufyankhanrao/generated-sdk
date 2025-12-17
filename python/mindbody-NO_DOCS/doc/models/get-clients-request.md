
# Get Clients Request

## Structure

`GetClientsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_i_ds` | `List[str]` | Optional | The requested client IDs.<br>Default: **all IDs** that the authenticated user’s access level allows.<br /><br>Note: You can fetch information for maximum 20 clients at once. |
| `search_text` | `str` | Optional | Text to use in the search. Can include FirstName, LastName, and Email. Note that user credentials must be provided. |
| `is_prospect` | `bool` | Optional | When `true`, filters the results to include only those clients marked as prospects for the business.<br /><br>When `false`, indicates that only those clients who are not marked prospects should be returned. |
| `last_modified_date` | `datetime` | Optional | Filters the results to include only the clients that have been modified on or after this date. |
| `unique_ids` | `List[int]` | Optional | Filters results to clients with these `UniqueIDs`. This parameter cannot be used with `ClientIDs` or `SearchText`.<br>Default: **all UniqueIDs** that the authenticated user’s access level allows. |
| `include_inactive` | `bool` | Optional | When `true`, indicates the results to include active and inactive clients.<br /><br>When `false`, indicates that only those clients who are marked as active should be returned.<br>Default: **false** |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ClientIDs": [
    "ClientIDs6",
    "ClientIDs7",
    "ClientIDs8"
  ],
  "SearchText": "SearchText2",
  "IsProspect": false,
  "LastModifiedDate": "2016-03-13T12:52:32.123Z",
  "UniqueIds": [
    180,
    181
  ]
}
```

