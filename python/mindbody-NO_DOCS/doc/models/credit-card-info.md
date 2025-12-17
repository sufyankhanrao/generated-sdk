
# Credit Card Info

INformation about an individual credit card

## Structure

`CreditCardInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `credit_card_number` | `str` | Optional | - |
| `exp_month` | `str` | Optional | - |
| `exp_year` | `str` | Optional | - |
| `billing_name` | `str` | Optional | - |
| `billing_address` | `str` | Optional | - |
| `billing_city` | `str` | Optional | - |
| `billing_state` | `str` | Optional | - |
| `billing_postal_code` | `str` | Optional | - |
| `save_info` | `bool` | Optional | - |
| `card_id` | `str` | Optional | Card Id of a stored instruments card |
| `cvv` | `str` | Optional | CVV of the card |

## Example (as JSON)

```json
{
  "CreditCardNumber": "CreditCardNumber4",
  "ExpMonth": "ExpMonth6",
  "ExpYear": "ExpYear4",
  "BillingName": "BillingName0",
  "BillingAddress": "BillingAddress2"
}
```

