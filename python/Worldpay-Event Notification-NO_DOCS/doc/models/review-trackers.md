
# Review Trackers

## Structure

`ReviewTrackers`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Indicator for review trackers enablement |
| `program` | [`Program2Enum`](../../doc/models/program-2-enum.md) | Optional | Name of the program<br><br>**Constraints**: *Maximum Length*: `33` |
| `opt_in_date` | `str` | Optional | Date of Opt In<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-2]{2}-[0-2]{2}` |
| `opt_out_date` | `str` | Optional | Date of Opt Out<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-2]{2}-[0-2]{2}` |
| `billing_start_date` | `str` | Optional | Billing Start Date<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-2]{2}-[0-2]{2}` |

## Example (as JSON)

```json
{
  "enabled": true,
  "program": "REVIEW TRACKERS",
  "billingStartDate": "2020-11-01",
  "optInDate": "optInDate8",
  "optOutDate": "optOutDate4"
}
```

