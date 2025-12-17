
# Get Promo Codes Response

## Structure

`GetPromoCodesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `promo_codes` | [`List[PromoCode]`](../../doc/models/promo-code.md) | Optional | Contains information about Promocodes at a site |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "PromoCodes": [
    {
      "PromotionID": 12,
      "Name": "Name2",
      "Code": "Code2",
      "Active": false,
      "Discount": {
        "Type": "Type6",
        "Amount": 80.68
      }
    },
    {
      "PromotionID": 12,
      "Name": "Name2",
      "Code": "Code2",
      "Active": false,
      "Discount": {
        "Type": "Type6",
        "Amount": 80.68
      }
    }
  ]
}
```

