
# Petro Details

Petro details.

## Structure

`PetroDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vehicle_id` | `str` | Optional | Identification number of vehicle<br><br>**Constraints**: *Maximum Length*: `6` |
| `driver_id` | `str` | Optional | Identification of driver<br><br>**Constraints**: *Maximum Length*: `2` |
| `odometer` | `str` | Optional | An odometer is a measuring instrument that allows you to know the distance traveled by a vehicle.<br><br>**Constraints**: *Maximum Length*: `7` |
| `po_number` | `str` | Optional | PO Numbers help to track and reference the orders.<br><br>**Constraints**: *Maximum Length*: `6` |
| `driver_number` | `str` | Optional | Provides information of check writer driver’s license/Id number<br><br>**Constraints**: *Maximum Length*: `6` |

## Example (as JSON)

```json
{
  "vehicleId": "AN8735",
  "driverId": "DL",
  "odometer": "N748364",
  "poNumber": "J60673",
  "driverNumber": "AN6374"
}
```

