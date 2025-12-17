
# Add Promo Code Request

## Structure

`AddPromoCodeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Required | The code of the promocode. |
| `name` | `str` | Required | The name of the promocode. |
| `active` | `bool` | Optional | Indicates that promocode is active. Default: **true** |
| `discount` | [`Discount`](../../doc/models/discount.md) | Optional | Discount for a promo code |
| `activation_date` | `datetime` | Optional | The date of the promocode activation. Default: **today’s date** |
| `expiration_date` | `datetime` | Optional | The date of the promocode expiration. Default: **a months from today’s date** |
| `max_uses` | `int` | Optional | The maximun number of uses. A use is considered a single sale. |
| `days_after_close_date` | `int` | Optional | The number of days a client has to use a promocode after they are no longer a prospect. |
| `allow_online` | `bool` | Optional | Indicates if promocode can be redeemed online in consumer mode. Default: **false** |
| `days_valid` | `List[str]` | Optional | Indicates what days of the week promocode is valid. Defaults to 7 days of the week. Possible values are:<br><br>* Monday<br>* Tuesday<br>* Wednesday<br>* Thursday<br>* Friday<br>* Saturday<br>* Sunday |
| `applicable_items` | [`List[ApplicableItem]`](../../doc/models/applicable-item.md) | Optional | Contains information about a promocode applicable items.<br>See ApplicableItems for a details of the `ApplicableItems` object. |

## Example (as JSON)

```json
{
  "Code": "Code8",
  "Name": "Name8",
  "Active": false,
  "Discount": {
    "Type": "Type6",
    "Amount": 80.68
  },
  "ActivationDate": "2016-03-13T12:52:32.123Z",
  "ExpirationDate": "2016-03-13T12:52:32.123Z",
  "MaxUses": 92
}
```

