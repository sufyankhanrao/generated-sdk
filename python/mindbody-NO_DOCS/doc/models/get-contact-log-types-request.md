
# Get Contact Log Types Request

## Structure

`GetContactLogTypesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contact_log_type_id` | `int` | Optional | The requested ContactLogType ID.<br>Default: **all** IDs that the authenticated user’s access level allows. |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ContactLogTypeId": 110,
  "Limit": 206,
  "Offset": 16
}
```

