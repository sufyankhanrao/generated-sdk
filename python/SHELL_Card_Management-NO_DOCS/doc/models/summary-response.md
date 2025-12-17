
# Summary Response

Encapsulates the details of a Summary response.

## Structure

`SummaryResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `active_cards` | `int` | Optional | Total number of active cards for the given search criteria |
| `blocked_cards` | `int` | Optional | Total number of cards for the given search criteria that are permanently blocked (Blocked) |
| `cancelled_cards` | `int` | Optional | Total number of cards for the given search criteria that are cancelled (at cancelled status) blocked by customer |
| `expired_cards` | `int` | Optional | Total number of expired cards for the given search criteria |
| `expiring_cards` | `int` | Optional | Cards that are active and expiring in X days, X should be configurable |
| `fraud_cards` | `int` | Optional | Totalnumber of Cards in Fraud status for the given search criteria. |
| `new_cards` | `int` | Optional | Total number of cards in New status for the given search criteria. |
| `renewal_pending_cards` | `int` | Optional | Total number of Renewal Pending cards for the given search criteria |
| `replaced_cards` | `int` | Optional | Cards with status Replaced |
| `temporary_block_by_customer` | `int` | Optional | Total number of cards for the given search criteria that are temporarily blocked by customer |
| `temporary_block_by_shell` | `int` | Optional | Total number of cards for the given search criteria that are temporarily blocked by Shell |
| `total_cards` | `int` | Optional | Total number of cards for the given search criteria |

## Example (as JSON)

```json
{
  "ActiveCards": 142,
  "BlockedCards": 238,
  "CancelledCards": 240,
  "ExpiredCards": 238,
  "ExpiringCards": 4
}
```

