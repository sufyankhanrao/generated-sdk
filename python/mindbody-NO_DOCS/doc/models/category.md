
# Category

## Structure

`Category`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The category Id used for api calls. |
| `category_name` | `str` | Optional | Category Name |
| `description` | `str` | Optional | Category Description |
| `service` | `bool` | Optional | Category service |
| `active` | `bool` | Optional | Check if Category is active. |
| `is_primary` | `bool` | Optional | Check if Category is of primary type. |
| `is_secondary` | `bool` | Optional | Check if Category is of secondary type. |
| `created_date_time_utc` | `datetime` | Optional | Category Created DateTime UTC |
| `modified_date_time_utc` | `datetime` | Optional | Category Modified DateTime UTC |
| `sub_categories` | [`List[SubCategory]`](../../doc/models/sub-category.md) | Optional | Contains the SubCategory objects, each of which describes the subcategories for a category. |
| `total_count` | `int` | Optional | Get total number of rows |

## Example (as JSON)

```json
{
  "Id": 30,
  "CategoryName": "CategoryName0",
  "Description": "Description8",
  "Service": false,
  "Active": false
}
```

