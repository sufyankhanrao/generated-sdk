
# Search Total Response

## Structure

`SearchTotalResponse`

## Inherits From

[`SummaryResponse`](../../doc/models/summary-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trace_id` | `str` | Optional | A trace number is a 15 digit number used to track amount transfers. It is issued by the sender and can be provided to receiver to track the impending transfer even before it has arrived in their system.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `256` |
| `routing_number` | `int` | Optional | Routing number is a 9 digit number that is used to identify a financial organization or bank.<br><br>**Constraints**: `>= 10000000`, `<= 99999999` |
| `dda_number` | `int` | Optional | Demand deposit account (DDA) is a type of bank account that offers access to deposited funds without advance notice.<br><br>**Constraints**: `>= 10000000`, `<= 99999999` |
| `credited_amount` | `float` | Optional | The credit amount is the amount being deposited to an account increasing the overall account balance.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `debited_amount` | `float` | Optional | The debited amount is the amount taken from an account which lowers the overall account balance.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `hierarchy` | [`MerchantDetail1`](../../doc/models/merchant-detail-1.md) | Optional | - |

## Example (as JSON)

```json
{
  "date": "2017-01-25",
  "fundingMethod": "ACH",
  "traceId": "121301014009120",
  "routingNumber": 71304804,
  "creditedAmount": 223.35,
  "debitedAmount": 2.94,
  "settlementCategory": {
    "code": "code6",
    "description": "description8"
  },
  "ddaNumber": 10000000
}
```

