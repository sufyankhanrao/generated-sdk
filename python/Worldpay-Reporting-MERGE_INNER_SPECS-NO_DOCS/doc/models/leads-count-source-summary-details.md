
# Leads Count Source Summary Details

Leads count grouped by source.

## Structure

`LeadsCountSourceSummaryDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `source` | `str` | Optional | Source from where leads are generated.<br><br>**Constraints**: *Maximum Length*: `10000` |
| `count` | `int` | Optional | Number of leads generated from a specific source.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |

## Example (as JSON)

```json
{
  "source": "List - Bank",
  "count": 2563
}
```

