
# Rej Real Time Transaction

Details of Real time rejected transaction

## Structure

`RejRealTimeTransaction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `return_date` | `str` | Optional | Indicates the date when the deposit was reject.<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}` |
| `effective_date` | `str` | Optional | Effective date of the transaction.<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}` |
| `funding_method` | `str` | Optional | Refers to the method used for the deposits. Possible Values-<br><br>**Constraints**: *Maximum Length*: `12` |
| `rejection_reason` | [`CodeAndDescription2`](../../doc/models/code-and-description-2.md) | Optional | Reason why the payment was not processed. |
| `routing_number` | `int` | Optional | The Routing number is a 9 digit number that is used to identify the financial organization or bank where the account resides.<br><br>**Constraints**: `>= 100000000`, `<= 999999999` |
| `amount` | `float` | Optional | The amount rejected in the process of being deposited.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `hierarchy` | [`MerchantDetail1`](../../doc/models/merchant-detail-1.md) | Optional | - |

## Example (as JSON)

```json
{
  "returnDate": "2022-07-19",
  "effectiveDate": "2022-07-19",
  "fundingMethod": "ACH",
  "amount": 120.01,
  "rejectionReason": {
    "code": "code8",
    "description": "description0"
  },
  "routingNumber": 100000000
}
```

