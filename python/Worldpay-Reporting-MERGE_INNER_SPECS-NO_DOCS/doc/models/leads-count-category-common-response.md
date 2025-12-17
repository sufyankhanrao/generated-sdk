
# Leads Count Category Common Response

Leads count for the selected month range.

## Structure

`LeadsCountCategoryCommonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_count` | `int` | Optional | Total number of leads generated for the independent sales channel(s) for the selected range of month.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |

## Example (as JSON)

```json
{
  "totalCount": 35781,
  "counts": [
    {
      "category": "category8",
      "count": 46
    },
    {
      "category": "category8",
      "count": 46
    }
  ]
}
```

