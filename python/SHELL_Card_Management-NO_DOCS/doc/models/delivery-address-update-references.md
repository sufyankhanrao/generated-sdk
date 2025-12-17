
# Delivery Address Update References

List of Delivery address update entity. The fields of this entity are described below.

## Structure

`DeliveryAddressUpdateReferences`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_id` | `int` | Optional | CardId |
| `card_pan` | `str` | Optional | PAN of the card. |
| `account_id` | `int` | Optional | AccountId |
| `account_number` | `str` | Optional | Account number |
| `reference_id` | `int` | Optional | Individual delivery address update reference number for the delivery address update request. |
| `error_info` | `str` | Optional | Individual error information for the delivery address update request. |

## Example (as JSON)

```json
{
  "CardId": 12345,
  "CardPAN": "7002051006629889654",
  "AccountId": 12356,
  "AccountNumber": "GB000000124",
  "ReferenceId": 573567,
  "ErrorInfo": "null"
}
```

