
# Leads Count Category Summary Details

Leads count grouped by category.

## Structure

`LeadsCountCategorySummaryDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `category` | `str` | Optional | Refers to the status of the lead.<br><br>**Constraints**: *Maximum Length*: `26` |
| `count` | `int` | Optional | Number of leads of specific lead category.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |

## Example (as JSON)

```json
{
  "category": "IN_PROGRESS_LEADS",
  "count": 2563
}
```

