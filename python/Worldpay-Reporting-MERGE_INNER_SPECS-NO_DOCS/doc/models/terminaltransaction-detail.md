
# Terminaltransaction Detail

## Structure

`TerminaltransactionDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `terminal_number` | `int` | Optional | The Unique identification number for every terminal of a merchant |
| `iias_certified` | `bool` | Optional | Inventory Information Approval System |
| `terminal_type` | `str` | Optional | Refer to device used in payments to process card transactions and authorize payments.<br><br>**Constraints**: *Maximum Length*: `2` |
| `terminal_application` | `str` | Optional | Software for managing transactions, payments, or data in a specific location or device like a point-of-sale system.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `255` |
| `register_number` | `str` | Optional | Unique id of point-of-sale terminals to identify and track transactions securely and accurately<br><br>**Constraints**: *Maximum Length*: `4` |

## Example (as JSON)

```json
{
  "terminalNumber": 5,
  "iiasCertified": false,
  "terminalType": "03",
  "terminalApplication": "ABC Software Inc",
  "registerNumber": "1111"
}
```

