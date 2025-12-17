
# Leads Count Source Common Response

Leads count for selected month range.

## Structure

`LeadsCountSourceCommonResponse`

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
      "source": "source0",
      "count": 46
    },
    {
      "source": "source0",
      "count": 46
    }
  ]
}
```

