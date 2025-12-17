
# Service

## Structure

`Service`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price` | `float` | Optional | The cost of the pricing option when sold at a physical location. |
| `online_price` | `float` | Optional | The cost of the pricing option when sold online. |
| `tax_included` | `float` | Optional | The amount of tax included in the price, if inclusive pricing is enabled. |
| `program_id` | `int` | Optional | The ID of the program that this pricing option applies to. |
| `tax_rate` | `float` | Optional | The tax rate applied to the pricing option. This field is populated only when you include a `LocationID` in the request. |
| `product_id` | `int` | Optional | The unique ID of this pricing option. This is the `PurchasedItems[].Id` returned from GET Sales. |
| `id` | `str` | Optional | The barcode ID of the pricing option. This is the `PurchasedItems[].BarcodeId` returned from GET Sales. |
| `name` | `str` | Optional | The name of the pricing option. |
| `count` | `int` | Optional | The initial count of usages available for the pricing option. |
| `sell_online` | `bool` | Optional | When true, filters to the pricing options that can be sold online.<br>Default: *false* |
| `sale_in_contract_only` | `bool` | Optional | When `true`, indicates that the pricing option is allowed to be purchased in a contract or package.<br>When `false`, indicates that the pricing option is not allowed to be purchased in a contract or package. |
| `mtype` | `str` | Optional | The type of the pricing option, either Drop-in, Series, or Unlimited. |
| `expiration_type` | `str` | Optional | The date the pricing option begins its activation, either the date of sale or the date the client first used it for a visit. |
| `expiration_unit` | `str` | Optional | The unit, either days or months, of `ExpirationLength`, indicating how long the pricing option is active for. |
| `expiration_length` | `int` | Optional | The number of days or months that the pricing option is active for. |
| `revenue_category` | `str` | Optional | The revenue category of the pricing option. |
| `membership_id` | `int` | Optional | The ID that this pricing option grants membership to. |
| `sell_at_location_ids` | `List[int]` | Optional | The location IDs where this pricing option is sold. |
| `use_at_location_ids` | `List[int]` | Optional | The location IDs where this pricing option may be used. |
| `priority` | `str` | Optional | The priority of the pricing option, either High, Medium, or Low. |
| `is_intro_offer` | `bool` | Optional | Indicates if this pricing option is an introductory offer. |
| `intro_offer_type` | `str` | Optional | When `IsIntroOffer` is true, this indicates if this introductory offer may be purchased by new clients or new and existing clients. |
| `is_third_party_discount_pricing` | `bool` | Optional | Indicates whether this pricing option is sold at discounted rates by third-party services, such as ClassPass. |
| `program` | `str` | Optional | The name of the service category the pricing option belongs to. |
| `discontinued` | `bool` | Optional | If the pricing option has been marked discontinued. |
| `restrict_to_membership_ids` | `List[int]` | Optional | Restricted to members of these membership ids. |
| `apply_member_discounts_of_membership_ids` | `List[int]` | Optional | Discounts applied of these membership ids. |

## Example (as JSON)

```json
{
  "Price": 104.72,
  "OnlinePrice": 139.24,
  "TaxIncluded": 212.26,
  "ProgramId": 22,
  "TaxRate": 72.76
}
```

