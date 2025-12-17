
# Cashflow Details 2

Details of infusions i.e., money deposited in an account

*This model accepts additional fields of type Any.*

## Structure

`CashflowDetails2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_date` | `str` | Required | The date associated with the first infusion in the account.<br>                     Valid Date Format: 'DD-MM-YYYY' |
| `end_date` | `str` | Required | The date corresponding to the last infusion in the account. |
| `cashflow_amt` | `List[float]` | Optional | List of infusions associated with an account.<br>            The first element of the list denotes the infusion as on “startDate”. The last element corresponds to infusion on the “endDate”. <br>            The start date should be greater current date. If there is an infusion on the current date, it is accounted for in the currentBalance field.<br>            Important<br>            All infusions b/w “startDate” and “endDate” are assumed to occur, yearly, on the “cashflowDate”. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "startDate": "01-03-2024",
  "endDate": "01-11-2032",
  "cashflowAmt": [
    2500.0,
    2575.0
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

