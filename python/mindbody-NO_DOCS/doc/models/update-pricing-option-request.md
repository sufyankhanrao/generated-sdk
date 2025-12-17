
# Update Pricing Option Request

To Update pricing option data

## Structure

`UpdatePricingOptionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `float` | Required | The id of the pricing option (legacy Id in mongo db) |
| `name` | `str` | Optional | Pricing option name.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `100` |
| `price` | `float` | Optional | Price of this Pricing option. |
| `online_price` | `float` | Optional | Online price of this Pricing option. |
| `count` | `int` | Optional | Number of sessions for this pricing option<br><br>**Constraints**: `>= 1`, `<= 2147483647` |
| `sell_online` | `bool` | Optional | Whether this pricing option sell online or not |
| `revenue_category` | `str` | Optional | Revenue Category of this pricing option<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |
| `discontinued` | `bool` | Optional | Whether this pricing option active or inactive |
| `membership_id` | `int` | Optional | The ID of the membership required to purchase the pricing option<br>Default is -1 and will not update Membership if it is not passed in body |
| `is_third_party_discount_pricing` | `bool` | Optional | Is this pricing option sold at discounted rates by third-parties<br>Once set to true it cannot be changed |
| `priority` | `str` | Optional | The priority of the pricing option<br>Priority can be set to Low(-1), Medium (0), High(1) |
| `sell_at_location_ids` | `List[int]` | Optional | The location IDs where this pricing option is sold<br>(default is null and will not update SellAtLocation if it is not passed in body) |
| `use_at_location_ids` | `List[int]` | Optional | The location IDs where this pricing option is used<br>(default is null and will not update UseAtLocation if it is not passed in body) |
| `expiration_unit` | `str` | Optional | The Expiration unit, either Days or Months |
| `expiration_length` | `int` | Optional | The number of days or months that the pricing option is active for.<br><br>**Constraints**: `>= 1`, `<= 32767` |
| `expiration_type` | `str` | Optional | The date the pricing option begins its activation,<br>either the SaleDate or DateOfClientFirstVisit |
| `restricted_membership_ids` | `List[int]` | Optional | This pricing option can be used under these memberships only<br>If null/empty then not restricted to any membership |

## Example (as JSON)

```json
{
  "ProductId": 111.88,
  "Name": "Name8",
  "Price": 35.12,
  "OnlinePrice": 69.64,
  "Count": 30,
  "SellOnline": false
}
```

