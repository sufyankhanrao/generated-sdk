
# Business Security Products

This aggregate field includes details of Security products

## Structure

`BusinessSecurityProducts`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `safer_payments` | [`BusinessSecurityProductsSaferPayments`](../../doc/models/business-security-products-safer-payments.md) | Optional | This aggregate field includes details of Saferpayment Security product |

## Example (as JSON)

```json
{
  "saferPayments": {
    "enabled": false,
    "program": "No PCI product",
    "programCode": "P"
  }
}
```

