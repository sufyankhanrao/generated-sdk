
# Debt Security Entity

Information about the debt security specific to the type of security

*This model accepts additional fields of type Any.*

## Structure

`DebtSecurityEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `par_value` | `float` | Optional | Par value amount |
| `debt_type` | [`DebtType`](../../doc/models/debt-type.md) | Optional | Debt type |
| `debt_class` | [`DebtClass`](../../doc/models/debt-class.md) | Optional | Classification of debt |
| `coupon_rate` | `float` | Optional | Bond coupon rate for next closest call date |
| `coupon_date` | `datetime` | Optional | Maturity date for next coupon |
| `coupon_mature_frequency` | [`CouponMatureFrequency`](../../doc/models/coupon-mature-frequency.md) | Optional | When coupons mature |
| `call_price` | `float` | Optional | Bond call price |
| `yield_to_call` | `float` | Optional | Yield to next call |
| `call_date` | `datetime` | Optional | Next call date |
| `call_type` | [`CallType`](../../doc/models/call-type.md) | Optional | Type of next call |
| `yield_to_maturity` | `float` | Optional | Yield to maturity |
| `bond_maturity_date` | `datetime` | Optional | Bond Maturity date |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "parValue": 18.14,
  "debtType": "ASSET",
  "debtClass": "CORPORATE",
  "couponRate": 229.02,
  "couponDate": "2016-03-13T12:52:32.123Z",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

