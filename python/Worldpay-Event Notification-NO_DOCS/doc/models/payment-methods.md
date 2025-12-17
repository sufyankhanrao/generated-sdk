
# Payment Methods

## Structure

`PaymentMethods`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accepted_cards` | [`List[AcceptedCardEnum]`](../../doc/models/accepted-card-enum.md) | Optional | Accepted card types |
| `valutec_enabled` | `bool` | Optional | Indicator for Valuetec enablement |
| `valutec` | [`Valutec`](../../doc/models/valutec.md) | Optional | This aggregate field includes valutec related data |
| `premier_issue_gift_card_enabled` | `bool` | Optional | This flag will let us know if a merchant has opted for premier issue gift card or not. |
| `svs_gift_card_enabled` | `bool` | Optional | This flag will let us know if a merchant has opted for SVS gift card or not. |
| `additional_accepted_card_info` | [`AdditionalAcceptedCardInfo`](../../doc/models/additional-accepted-card-info.md) | Optional | This aggregate field includes additional accepted card data |

## Example (as JSON)

```json
{
  "valutecEnabled": true,
  "premierIssueGiftCardEnabled": true,
  "svsGiftCardEnabled": true,
  "acceptedCards": [
    "VISA",
    "MASTERCARD"
  ],
  "valutec": {
    "groupId": "groupId2",
    "billingAccountNumber": "billingAccountNumber4",
    "billingRoutingNumber": "billingRoutingNumber4",
    "settlementAccountNumber": "settlementAccountNumber6",
    "settlementRoutingNumber": "settlementRoutingNumber6",
    "lastUpdatedDateTime": "lastUpdatedDateTime4"
  }
}
```

