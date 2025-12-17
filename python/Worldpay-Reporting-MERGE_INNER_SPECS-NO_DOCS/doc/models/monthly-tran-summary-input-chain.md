
# Monthly Tran Summary Input CHAIN

## Structure

`MonthlyTranSummaryInputCHAIN`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `chain_code` | `str` | Required | The Chain Code is the level of the merchant hierarchy that groups merchant identifiers (MIDs) and any related roll-up values under a common identifier for settlement, billing and reporting. Chain Code is the primary identifier for merchants boarded in MDB (Merchant Database) system.<br><br>**Constraints**: *Maximum Length*: `6` |
| `date_range` | [`MonthRange`](../../doc/models/month-range.md) | Required | Refers to date range. |

## Example (as JSON)

```json
{
  "chainCode": "OkLV1",
  "dateRange": {
    "startMonth": "2022-01",
    "endMonth": "2022-06"
  }
}
```

