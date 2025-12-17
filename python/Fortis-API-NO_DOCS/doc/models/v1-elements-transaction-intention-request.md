
# V1 Elements Transaction Intention Request

## Structure

`V1ElementsTransactionIntentionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action` | [`ActionEnum`](../../doc/models/action-enum.md) | Optional | The action to be performed<br><br>**Default**: `'sale'` |
| `digital_wallets_only` | `bool` | Optional | **Default**: `False` |
| `methods` | [`List[Method40]`](../../doc/models/method-40.md) | Optional | By default the system will try to offer all the availables payment methods from your account. But if you like, you can specify exactly what services you want to use.<br><br>**Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `amount` | `int` | Optional | The total amount to be charged. Allowed on the actions: `sale`, `auth-only`, `refund`<br><br>**Constraints**: `>= 1`, `<= 999999999` |
| `tax_amount` | int \| None | Optional | This is a container for any-of cases.<br><br>**Constraints**: `>= 1`, `<= 999999999` |
| `secondary_amount` | int \| None | Optional | This is a container for any-of cases.<br><br>**Constraints**: `>= 0`, `<= 999999999` |
| `location_id` | `str` | Optional | Location ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `contact_id` | `str` | Optional | Contact ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `save_account` | bool \| None | Optional | This is a container for any-of cases. |
| `save_account_title` | str \| None | Optional | This is a container for any-of cases.<br><br>**Constraints**: *Maximum Length*: `16` |
| `title` | str \| None | Optional | This is a container for any-of cases.<br><br>**Constraints**: *Maximum Length*: `16` |
| `ach_sec_code` | [`AchSecCodeEnum`](../../doc/models/ach-sec-code-enum.md) | Optional | SEC code for the transaction if it's an ACH transaction<br><br>**Default**: `'WEB'` |
| `bank_funded_only_override` | bool \| None | Optional | This is a container for any-of cases. |
| `allow_partial_authorization_override` | bool \| None | Optional | This is a container for any-of cases. |
| `auto_decline_cvv_override` | bool \| None | Optional | This is a container for any-of cases. |
| `auto_decline_street_override` | bool \| None | Optional | This is a container for any-of cases. |
| `auto_decline_zip_override` | bool \| None | Optional | This is a container for any-of cases. |
| `message` | `str` | Optional | A custom text message that displays after the payment is processed.<br><br>**Constraints**: *Maximum Length*: `120` |

## Example (as JSON)

```json
{
  "action": "sale",
  "digitalWalletsOnly": false,
  "amount": 1099,
  "location_id": "11e95f8ec39de8fbdb0a4f1a",
  "contact_id": "11e95f8ec39de8fbdb0a4f1a",
  "ach_sec_code": "WEB",
  "methods": [
    {
      "type": "ach",
      "product_transaction_id": "product_transaction_id4"
    }
  ],
  "tax_amount": 50
}
```

