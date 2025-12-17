
# Get Products Request

## Structure

`GetProductsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_ids` | `List[str]` | Optional | The barcode number of the product to be filter by. |
| `search_text` | `str` | Optional | A search filter, used for searching by term. |
| `category_ids` | `List[int]` | Optional | A list of revenue category IDs to filter by. Use this ID when calling the GET Categories endpoint.<br><br>**Note:** The values for these are not currently retrievable through the API. |
| `sub_category_ids` | `List[int]` | Optional | A list of subcategory IDs to filter by. Use this ID when calling the GET Categories endpoint.<br><br>**Note:** The values for these are not currently retrievable through the API. |
| `sell_online` | `bool` | Optional | When `true`, only products that can be sold online are returned.<br /><br>When `false`, all products are returned.<br /><br>Default: **false** |
| `location_id` | `int` | Optional | The location ID to use to determine the tax for the products that this request returns.<br /><br>Default: **online store** |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ProductIds": [
    "ProductIds2"
  ],
  "SearchText": "SearchText0",
  "CategoryIds": [
    247,
    248,
    249
  ],
  "SubCategoryIds": [
    178,
    179
  ],
  "SellOnline": false
}
```

