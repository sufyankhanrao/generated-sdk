
# Data Per Category Item

Data for a single aggregate group and contract category combination.

## Structure

`DataPerCategoryItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aggregate_id` | `int` | Required | The id of this aggregate group: device id, site id, or the constant -1 for portfolio. For `siteLevel` aggregation a generated unique id is used. |
| `aggregate_path_names` | `List[str]` | Optional | For `siteLevel` aggregation this contains the title for each level in the hierarchy. For other types of aggregation it will be empty. |
| `device_ids` | `List[int]` | Required | The ids of the devices in this aggregate group.<br><br>**Constraints**: `>= 1` |
| `contract_title` | `str` | Required | - |
| `category_title` | `str` | Required | - |
| `category_time` | [`CategoryTimeEnum`](../../doc/models/category-time-enum.md) | Required | - |
| `value` | `float` | Required | The aggregated value of the selected data signal. |
| `duration` | `float` | Optional | The summed duration in seconds allocated to this contract category and aggregate group. |

## Example (as JSON)

```json
{
  "aggregateId": 6,
  "deviceIds": [
    1,
    2,
    3
  ],
  "contractTitle": "Vestas 1",
  "categoryTitle": "Icing",
  "categoryTime": "available",
  "value": 104.55,
  "duration": 150.0,
  "aggregatePathNames": [
    "aggregatePathNames2"
  ]
}
```

