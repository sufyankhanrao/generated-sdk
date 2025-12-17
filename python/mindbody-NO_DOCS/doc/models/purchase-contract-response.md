
# Purchase Contract Response

## Structure

`PurchaseContractResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | The ID of the client who is purchasing the contract. |
| `location_id` | `int` | Optional | The ID of the location where the contract is being purchased. |
| `contract_id` | `int` | Optional | The ID of the general contract being purchased. |
| `client_contract_id` | `int` | Optional | The ID of the specific contract being purchased by this specific client, not to be confused with the `ContractId`, which refers to a general contract that the business offers. |
| `totals` | [`PurchaseContractResponseTotals`](../../doc/models/purchase-contract-response-totals.md) | Optional | Totals for the purchase |
| `payment_processing_failures` | [`List[PaymentProcessingFailure]`](../../doc/models/payment-processing-failure.md) | Optional | Contains information only if SCA challenge is indicated. |

## Example (as JSON)

```json
{
  "ClientId": "ClientId6",
  "LocationId": 80,
  "ContractId": 10,
  "ClientContractId": 216,
  "Totals": {
    "Total": 175.82,
    "SubTotal": 122.08,
    "Discount": 113.34,
    "Tax": 78.68
  }
}
```

