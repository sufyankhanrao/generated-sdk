
# Fuel Consumption Data

## Structure

`FuelConsumptionData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | Account Name |
| `account_number` | `str` | Optional | Account Number |
| `payer_name` | `str` | Optional | Payment customer Name |
| `payer_number` | `str` | Optional | Payment customer number |
| `card_number` | `str` | Optional | Card PAN |
| `card_group_id` | `int` | Optional | Card group ID |
| `card_group_name` | `str` | Optional | Card group name |
| `driver_name` | `str` | Optional | Driver name |
| `license_number` | `str` | Optional | Vehicle registration number |
| `initial_odometer` | `float` | Optional | First transaction odometer reading |
| `last_odometer` | `float` | Optional | Last transaction odometer reading |
| `distance` | `float` | Optional | Distance in  KM or Miles based on Customer and Colco Settings |
| `fuel_consumption` | `float` | Optional | Total Fuel Consumption. |
| `fuel_net_amount` | `float` | Optional | Net Fuel Amount |
| `discount` | `float` | Optional | Total Discount |
| `fuel_tax` | `float` | Optional | Fuel Tax Amount |
| `fuel_volume` | `float` | Optional | Total Fuel Volume in Litres |
| `gross_non_fuel_expenses` | `float` | Optional | Gross Nonfuel Amount |
| `co_2_produced` | `float` | Optional | Total Co2 produced |
| `transaction_count` | `float` | Optional | Total Transaction Count |

## Example (as JSON)

```json
{
  "AccountName": "AccountName0",
  "AccountNumber": "AccountNumber4",
  "PayerName": "PayerName8",
  "PayerNumber": "PayerNumber2",
  "CardNumber": "CardNumber2"
}
```

