
# Debit Petro Details

Petro details of debit card transaction.

## Structure

`DebitPetroDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vehicle_id` | `str` | Optional | Unique identification of the vehicle.<br><br>**Constraints**: *Maximum Length*: `32` |
| `driver_id` | `str` | Optional | Provides information of check writer id.<br><br>**Constraints**: *Maximum Length*: `2` |
| `odometer` | `str` | Optional | An odometer is a measuring instrument that allows you to know the distance traveled by a vehicle.<br><br>**Constraints**: *Maximum Length*: `7` |
| `po_number` | `str` | Optional | PO Numbers help to track and reference the orders.<br><br>**Constraints**: *Maximum Length*: `6` |
| `driver_number` | `str` | Optional | Provides information of check writer driver’s license/Id number<br><br>**Constraints**: *Maximum Length*: `6` |

## Example (as JSON)

```json
{
  "vehicleId": "4Y1SL65848Z411439",
  "driverId": "DL",
  "odometer": "N748364",
  "poNumber": "J60673",
  "driverNumber": "AN6374"
}
```

