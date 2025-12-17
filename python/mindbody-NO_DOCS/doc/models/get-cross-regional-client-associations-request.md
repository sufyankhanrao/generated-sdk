
# Get Cross Regional Client Associations Request

## Structure

`GetCrossRegionalClientAssociationsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Looks up the cross regional associations by the client’s ID. Either `ClientId` or `Email` must be provided. If both are provided, the `ClientId` is used by default. |
| `email` | `str` | Optional | Looks up the cross regional associations by the client’s email address. Either `ClientId` or `Email` must be provided. If both are provided, the `ClientId` is used by default. |
| `first_name` | `str` | Optional | First name (used for email queries) |
| `last_name` | `str` | Optional | Last name (used for email queries) |
| `v_2` | `bool` | Optional | Use newer method |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ClientId": "ClientId8",
  "Email": "Email0",
  "FirstName": "FirstName0",
  "LastName": "LastName0",
  "V2": false
}
```

