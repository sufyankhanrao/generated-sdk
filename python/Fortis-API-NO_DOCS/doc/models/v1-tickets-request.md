
# V1 Tickets Request

## Structure

`V1TicketsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_name` | `str` | Optional | Account holder name<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `32` |
| `exp_date` | `str` | Required | The Expiration Date for the credit card. |
| `cvv` | `str` | Optional | CVV<br><br>**Constraints**: *Maximum Length*: `4` |
| `account_number` | `str` | Required | Account number<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `19`, *Pattern*: `^[\d]+$` |
| `billing_address` | [`BillingAddress5`](../../doc/models/billing-address-5.md) | Optional | Billing Address Object |
| `contact_id` | `str` | Optional | Used to associate the Ticket with a Contact.<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `contact_api_id` | `str` | Optional | Used to associate the Ticket with a Contact. |
| `location_id` | str \| None | Optional | This is a container for any-of cases. |
| `location_api_id` | `str` | Optional | Location Api Id |

## Example (as JSON)

```json
{
  "account_holder_name": "John Smith",
  "exp_date": "0722",
  "account_number": "545454545454545",
  "contact_id": "11e95f8ec39de8fbdb0a4f1a",
  "cvv": "cvv6",
  "billing_address": {
    "postal_code": "postal_code0",
    "street": "street8"
  },
  "contact_api_id": "contact_api_id6"
}
```

