
# Accelerated Products

## Structure

`AcceleratedProducts`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `everday_funding` | [`EverdayFundingInfo`](../../doc/models/everday-funding-info.md) | Optional | This aggregate field includes everyday funding data |
| `payment_accelerator` | [`PaymentAcceleraterDetail`](../../doc/models/payment-accelerater-detail.md) | Optional | This aggregate field includes payment accelerator data |

## Example (as JSON)

```json
{
  "everdayFunding": {
    "statusCode": "N",
    "statusDescription": "PENDING",
    "lastUpdatedDateTime": "lastUpdatedDateTime4"
  },
  "paymentAccelerator": {
    "statusCode": "X",
    "statusDescription": "DISABLED",
    "lastUpdatedDateTime": "lastUpdatedDateTime8",
    "splitPercentageToBankAccount": 95.0
  }
}
```

