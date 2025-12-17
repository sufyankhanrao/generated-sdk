
# Get Gift Card Response

## Structure

`GetGiftCardResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `gift_cards` | [`List[GiftCard]`](../../doc/models/gift-card.md) | Optional | Contains information about the gift cards. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "GiftCards": [
    {
      "Id": 90,
      "LocationIds": [
        128,
        129
      ],
      "Description": "Description0",
      "EditableByConsumer": false,
      "CardValue": 153.64
    }
  ]
}
```

