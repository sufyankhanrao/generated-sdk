
# Hosted Payment Page

Hosted Payment Page Information on `expand`

## Structure

`HostedPaymentPage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `str` | Optional | User ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `location_id` | `str` | Optional | Location ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `location_api_id` | `str` | Optional | Location Api Id |
| `product_transaction_id` | `str` | Optional | Product Transaction ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `title` | `str` | Optional | Title<br><br>**Constraints**: *Maximum Length*: `64` |
| `redirect_url_delay` | `float` | Optional | Redirect Url Delay<br><br>**Default**: `15`<br><br>**Constraints**: `<= 15` |
| `min_payment_amount` | `int` | Optional | Min Payment Amount<br><br>**Constraints**: `>= 0` |
| `max_payment_amount` | `int` | Optional | Max Payment Amount<br><br>**Default**: `9999999999`<br><br>**Constraints**: `<= 9999999999` |
| `redirect_url_on_approve` | `str` | Optional | Redirect Url On Approval |
| `redirect_url_on_decline` | `str` | Optional | Redirect Url On Decline |
| `field_configuration` | [`FieldConfiguration`](../../doc/models/field-configuration.md) | Optional | field_configuration |
| `encryption_key` | `str` | Optional | Encryption Key<br><br>**Constraints**: *Minimum Length*: `32`, *Maximum Length*: `32` |
| `stylesheet_url` | `str` | Optional | Stylesheet Url |
| `parent_send_message` | `bool` | Optional | Parent Send Message |
| `hide_optional_fields` | `bool` | Optional | Hide Optional Fields |
| `id` | `str` | Optional | Hosted Payment Page Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `created_ts` | `int` | Optional | Created Time Stamp |
| `modified_ts` | `int` | Optional | Modified Time Stamp |
| `created_user_id` | `str` | Optional | System generated id for user who created record<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `modified_user_id` | `str` | Optional | System generated id for user who created record<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |

## Example (as JSON)

```json
{
  "user_id": "11e95f8ec39de8fbdb0a4f1a",
  "location_id": "11e95f8ec39de8fbdb0a4f1a",
  "product_transaction_id": "11e95f8ec39de8fbdb0a4f1a",
  "title": "Sample title",
  "redirect_url_delay": 15,
  "min_payment_amount": 0,
  "max_payment_amount": 9999999999,
  "parent_send_message": true,
  "hide_optional_fields": true,
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "created_ts": 1422040992,
  "modified_ts": 1422040992,
  "created_user_id": "11e95f8ec39de8fbdb0a4f1a",
  "modified_user_id": "11e95f8ec39de8fbdb0a4f1a",
  "location_api_id": "location_api_id2"
}
```

