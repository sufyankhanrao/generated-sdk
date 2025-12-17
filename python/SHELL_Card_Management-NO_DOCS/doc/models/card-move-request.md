
# Card Move Request

## Structure

`CardMoveRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `col_co_code` | `int` | Optional | - |
| `col_co_id` | `int` | Optional | - |
| `col_co_country_code` | `str` | Optional | - |
| `payer_number` | `str` | Optional | - |
| `payer_id` | `int` | Optional | - |
| `cards` | [`List[CardMoveRequestCardsItems]`](../../doc/models/card-move-request-cards-items.md) | Optional | - |
| `target_account_id` | `int` | Optional | - |
| `target_account_number` | `str` | Optional | - |
| `target_card_group_id` | `int` | Optional | - |
| `target_new_card_group_name` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "ColCoCode": 166,
  "ColCoId": 152,
  "ColCoCountryCode": "ColCoCountryCode0",
  "PayerNumber": "PayerNumber2",
  "PayerId": 200
}
```

