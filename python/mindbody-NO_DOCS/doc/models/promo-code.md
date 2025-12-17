
# Promo Code

## Structure

`PromoCode`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `promotion_id` | `int` | Optional | ID of the promo code |
| `name` | `str` | Optional | Name of the promo code |
| `code` | `str` | Optional | The code of the promocode. |
| `active` | `bool` | Optional | Indicates that promocode is active. |
| `discount` | [`Discount`](../../doc/models/discount.md) | Optional | Discount for a promo code |
| `activation_date` | `datetime` | Optional | The promocode activation date. |
| `expiration_date` | `datetime` | Optional | The promocode expiration date. |
| `max_uses` | `int` | Optional | The maximun number of uses. |
| `number_of_autopays` | `int` | Optional | Number of Autopays |
| `days_after_close_date` | `int` | Optional | The number of days a client has to use a promocode after they are no longer a prospect. |
| `allow_online` | `bool` | Optional | Indicates if promocode to be redeemed online in consumer mode. |
| `last_modified_date_time` | `datetime` | Optional | Promo code last modified date and time |
| `days_valid` | [`List[DaysValidEnum]`](../../doc/models/days-valid-enum.md) | Optional | What days the promo code can be used |
| `applicable_items` | [`List[ApplicableItem]`](../../doc/models/applicable-item.md) | Optional | Contains information about a promocode applicable items. |

## Example (as JSON)

```json
{
  "PromotionID": 0,
  "Name": "Name4",
  "Code": "Code4",
  "Active": false,
  "Discount": {
    "Type": "Type6",
    "Amount": 80.68
  }
}
```

