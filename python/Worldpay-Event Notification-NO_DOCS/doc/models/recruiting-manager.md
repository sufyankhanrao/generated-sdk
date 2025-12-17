
# Recruiting Manager

## Structure

`RecruitingManager`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Indicator for recruiting manager enablement |
| `program` | [`Program4Enum`](../../doc/models/program-4-enum.md) | Optional | Name of the program<br><br>**Constraints**: *Maximum Length*: `22` |
| `opt_in_date` | `str` | Optional | Date of Opt In<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-2]{2}-[0-2]{2}` |
| `opt_out_date` | `str` | Optional | Date of Opt Out<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-2]{2}-[0-2]{2}` |
| `billing_start_date` | `str` | Optional | Billing Start Date<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-2]{2}-[0-2]{2}` |

## Example (as JSON)

```json
{
  "enabled": true,
  "program": "FIS RECRUITING MANAGER",
  "billingStartDate": "2020-11-01",
  "optInDate": "optInDate2",
  "optOutDate": "optOutDate0"
}
```

