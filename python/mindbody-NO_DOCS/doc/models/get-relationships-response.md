
# Get Relationships Response

Get Relationships Response Model

## Structure

`GetRelationshipsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `relationships` | [`List[Relationship]`](../../doc/models/relationship.md) | Optional | A list of relationships. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "Relationships": [
    {
      "Id": 190,
      "RelationshipName1": "RelationshipName10",
      "RelationshipName2": "RelationshipName22"
    }
  ]
}
```

