
# Client Relationship

A relation between two clients.

## Structure

`ClientRelationship`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `related_client_id` | `str` | Optional | The RSSID of the related client. |
| `relationship` | [`Relationship`](../../doc/models/relationship.md) | Optional | Jim is a RelationshipName1 of John. John is a RelationshipName2 of Jim. |
| `relationship_name` | `str` | Optional | The name of the relationship of the related client. |
| `delete` | `bool` | Optional | When true, the associated relationship is removed from the client’s list of relationships.<br>This property is ignored in all other use cases.<br>Default: *false* |

## Example (as JSON)

```json
{
  "RelatedClientId": "RelatedClientId0",
  "Relationship": {
    "Id": 156,
    "RelationshipName1": "RelationshipName14",
    "RelationshipName2": "RelationshipName26"
  },
  "RelationshipName": "RelationshipName6",
  "Delete": false
}
```

