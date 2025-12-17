
# Bank Account

## Structure

`BankAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dda_type` | [`DdaTypeEnum`](../../doc/models/dda-type-enum.md) | Required | Direct Deposit Account Type |
| `ach_type` | [`AchTypeEnum`](../../doc/models/ach-type-enum.md) | Optional | Check deposit Type |
| `account_number` | `str` | Required | Direct Deposit Account Number.<br><br>**Constraints**: *Maximum Length*: `17`, *Pattern*: `^\d{1,17}$` |
| `routing_number` | `str` | Required | Bank Routing Number. Must be 9 characters.<br><br>**Constraints**: *Pattern*: `^\d{9}$` |

## Example (as JSON)

```json
{
  "ddaType": "Chequing",
  "accountNumber": "12345678910",
  "routingNumber": "123456789",
  "achType": "CommercialChecking"
}
```

