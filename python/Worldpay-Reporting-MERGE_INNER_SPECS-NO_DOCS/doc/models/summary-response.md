
# Summary Response

Summary Response details

## Structure

`SummaryResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date` | `str` | Optional | **Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}` |
| `settlement_category` | [`CodeAndDescription2`](../../doc/models/code-and-description-2.md) | Optional | Settlement Category Details |
| `funding_method` | `str` | Optional | Refers to the method used for deposits.<br><br>**Constraints**: *Maximum Length*: `12` |

## Example (as JSON)

```json
{
  "date": "2017-01-25",
  "fundingMethod": "ACH",
  "settlementCategory": {
    "code": "code6",
    "description": "description8"
  },
  "traceId": "traceId6",
  "routingNumber": 10000000,
  "ddaNumber": 10000000,
  "creditedAmount": 156.9,
  "debitedAmount": 226.86
}
```

