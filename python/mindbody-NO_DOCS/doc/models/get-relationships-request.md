
# Get Relationships Request

Get Relationships Request Model

## Structure

`GetRelationshipsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `active` | `bool` | Optional | When `true`, the response only contains relationships which are activated.<br>When `false`, only deactivated relationships are returned.<br>Default: **All Relationships** |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "Active": false,
  "Limit": 34,
  "Offset": 100
}
```

