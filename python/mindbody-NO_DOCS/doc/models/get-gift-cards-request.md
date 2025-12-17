
# Get Gift Cards Request

## Structure

`GetGiftCardsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `int` | Optional | When included, returns gift cards that are sold at the provided location ID. |
| `sold_online` | `bool` | Optional | When `true`, only returns gift cards that are sold online.<br /><br>Default: **false** |
| `include_custom_layouts` | `bool` | Optional | When `true`, includes custom gift card layouts.<br /><br>When `false`, includes only system layouts.<br>Default: **false** |
| `ids` | `List[int]` | Optional | Filters the results to the requested gift card IDs.<br /><br>Default: **all** gift cards. |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "LocationId": 222,
  "SoldOnline": false,
  "IncludeCustomLayouts": false,
  "Ids": [
    1
  ],
  "Limit": 16
}
```

