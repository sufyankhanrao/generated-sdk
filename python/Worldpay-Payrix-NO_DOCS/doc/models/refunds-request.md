
# Refunds Request

## Structure

`RefundsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entry` | `str` | Required | The identifier of the Entries resource that is being refunded. |
| `description` | `str` | Optional | A description of this Refund.<br>This field is stored as a text string and must be between 0 and 100 characters long. |
| `amount` | `float` | Required | The amount of this Refund.<br>This field is specified in cents(up to three decimal points)<br>This field is optional. If it is not set, then the API uses the amount that is specified in the related Entry resource. |

## Example (as JSON)

```json
{
  "entry": "t1_etr_6785d50e925b93e699f1234",
  "description": "Negative Tax Reimbursement",
  "amount": 248.0
}
```

