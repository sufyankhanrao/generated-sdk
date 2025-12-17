
# Summary 21

Retrieve common summary details

## Structure

`Summary21`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `settled_gross_amount` | `float` | Optional | Gross amount settled as per the selection criteria.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `settled_gross_count` | `int` | Optional | Number of transactions settled as Gross amount as per the selection criteria.<br><br>**Constraints**: `>= 0`, `<= 9999999999999` |
| `settled_net_amount` | `float` | Optional | Amount settled after deduction of fees as per the selection criteria.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `settled_net_count` | `int` | Optional | Number of transactions with settled as Net Amount as per the selection criteria.<br><br>**Constraints**: `>= 0`, `<= 9999999999999` |
| `process_month` | `str` | Optional | Month for which the transactions are processed.<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7`, *Pattern*: `^[0-9]{4}-[0-9]{2}$` |
| `messaging_type` | `str` | Optional | Refers to card holder authentication method. Possible Values SIG (Signature); PIN (Pin) base transaction.<br><br>**Constraints**: *Maximum Length*: `3` |
| `card_network` | `str` | Optional | Brand or Network to which the card is associated.<br><br>**Constraints**: *Maximum Length*: `19` |
| `card_present` | `bool` | Optional | Indicates if card was present at the POS. Possible values True or False |

## Example (as JSON)

```json
{
  "settledGrossAmount": 646.5,
  "settledGrossCount": 11700,
  "settledNetAmount": 5496.876,
  "settledNetCount": 13500,
  "processMonth": "2022-01",
  "messagingType": "PIN",
  "cardNetwork": "VISA",
  "cardPresent": true
}
```

