
# Get Categories Request

Get Categories Request Model

## Structure

`GetCategoriesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `category_ids` | `List[int]` | Optional | When included, the response only contains details about the specified category Ids. |
| `sub_category_ids` | `List[int]` | Optional | When included, the response only contains details about the specified subcategory Ids. |
| `service` | `bool` | Optional | When `true`, the response only contains details about Revenue Categories.<br>When `false`, only Product Revenue Categories are returned.<br>Default: **All Categories** |
| `active` | `bool` | Optional | When `true`, the response only contains categories which are activated.<br>When `false`, only deactivated categories are returned.<br>Default: **All Categories** |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "CategoryIds": [
    189,
    190,
    191
  ],
  "SubCategoryIds": [
    120,
    121
  ],
  "Service": false,
  "Active": false,
  "Limit": 142
}
```

