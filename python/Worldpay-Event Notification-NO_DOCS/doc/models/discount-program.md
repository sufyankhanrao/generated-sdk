
# Discount Program

## Structure

`DiscountProgram`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Indicator for discount program enablement |
| `program` | [`Program3Enum`](../../doc/models/program-3-enum.md) | Optional | Name of the program<br><br>**Constraints**: *Maximum Length*: `20` |
| `opt_in_date` | `str` | Optional | Date of Opt In<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-2]{2}-[0-2]{2}` |
| `opt_out_date` | `str` | Optional | Date of Opt Out<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-2]{2}-[0-2]{2}` |
| `billing_start_date` | `str` | Optional | Billing Start Date<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-2]{2}-[0-2]{2}` |

## Example (as JSON)

```json
{
  "enabled": true,
  "program": "FIS DISCOUNT PROGRAM",
  "billingStartDate": "2020-11-01",
  "optInDate": "optInDate4",
  "optOutDate": "optOutDate2"
}
```

