
# Gift Card

## Structure

`GiftCard`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The gift card's `ProductID`. |
| `location_ids` | `List[int]` | Optional | The IDs of the locations where the gift card is sold. |
| `description` | `str` | Optional | A description of the gift card. |
| `editable_by_consumer` | `bool` | Optional | When `true`, indicates that the gift card can be edited by the client. |
| `card_value` | `float` | Optional | The value of the gift card. |
| `sale_price` | `float` | Optional | The sale price of the gift card, if applicable. |
| `sold_online` | `bool` | Optional | When `true`, indicates that the gift card is sold online. |
| `membership_restriction_ids` | `List[int]` | Optional | A list of IDs for membership restrictions, if this card is restricted to members with certain types of memberships. |
| `gift_card_terms` | `str` | Optional | The terms of the gift card. |
| `contact_info` | `str` | Optional | Contact information for the gift card. |
| `display_logo` | `bool` | Optional | When `true`, indicates that the logo should be displayed on the gift card. |
| `layouts` | [`List[GiftCardLayout]`](../../doc/models/gift-card-layout.md) | Optional | A list of layouts available for the gift card. |

## Example (as JSON)

```json
{
  "Id": 166,
  "LocationIds": [
    204,
    205
  ],
  "Description": "Description6",
  "EditableByConsumer": false,
  "CardValue": 106.8
}
```

