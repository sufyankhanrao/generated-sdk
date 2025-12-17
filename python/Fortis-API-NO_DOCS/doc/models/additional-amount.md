
# Additional Amount

## Structure

`AdditionalAmount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type52Enum`](../../doc/models/type-52-enum.md) | Optional | type of the amount [4S-Healthcare(Visa and MC Only), 4U-Prescription/Rx(Visa and MC Only), 4V-Vision/Optical(Visa Only), 4W-clinic/other qualified medical(Visa Only) ,4X-Dental(Visa Only)]. |
| `amount` | `int` | Optional | The amount of additional amount. |
| `account_type` | [`AccountTypeEnum`](../../doc/models/account-type-enum.md) | Optional | Account Type |
| `currency` | `float` | Optional | Currency Code |

## Example (as JSON)

```json
{
  "type": "cashback",
  "amount": 10,
  "account_type": "credit",
  "currency": 840.0
}
```

