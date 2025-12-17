
# Get Session Types Request

## Structure

`GetSessionTypesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `program_i_ds` | `List[int]` | Optional | Filters results to session types that belong to one of the given program IDs. If omitted, all program IDs return. |
| `online_only` | `bool` | Optional | When `true`, indicates that only the session types that can be booked online should be returned.<br /><br>Default: **false** |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ProgramIDs": [
    136
  ],
  "OnlineOnly": false,
  "Limit": 232,
  "Offset": 42
}
```

