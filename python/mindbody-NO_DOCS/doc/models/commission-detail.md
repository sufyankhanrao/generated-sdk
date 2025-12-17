
# Commission Detail

## Structure

`CommissionDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `commission_type` | `str` | Optional | The type of commission earned. Possible values are:<br><br>* ItemStandardPercentageCommission<br>* ItemStandardFlatCommission<br>* ItemPromotionalPercentageCommission<br>* ItemPromotionalFlatCommission<br>* StaffStandardPercentageCommission<br>* StaffStandardFlatCommission<br>* StaffPromotionalPercentageCommission<br>* StaffPromotionalFlatCommission |
| `commission_earnings` | `float` | Optional | The portion of `Earnings` earned by this `CommissionType`. |

## Example (as JSON)

```json
{
  "CommissionType": "CommissionType4",
  "CommissionEarnings": 190.88
}
```

