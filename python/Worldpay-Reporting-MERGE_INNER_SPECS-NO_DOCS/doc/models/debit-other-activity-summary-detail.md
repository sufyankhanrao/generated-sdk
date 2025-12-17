
# Debit Other Activity Summary Detail

This object is used to retrieve settlement activity summary

## Structure

`DebitOtherActivitySummaryDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reversed_count` | `int` | Optional | Reversed count refers to the merchant returns funds to the customer's bank.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `reversed_amount` | `float` | Optional | Reversed amount refers to the merchant returns funds to the customer's bank.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `inquiry_count` | `int` | Optional | Inquiry count refers to the list of recent transactions done through the account during a specific reporting period.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `inquiry_amount` | `float` | Optional | Inquiry amount refers to the list of recent transactions done through the account during a specific reporting period.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "reversedCount": 453,
  "reversedAmount": 756.98,
  "inquiryCount": 78,
  "inquiryAmount": 675.34
}
```

