
# Electrical Properties

Electrical Properties of the Connector

## Structure

`ElectricalProperties`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `power_type` | [`ElectricalPropertiesPowerTypeEnum`](../../doc/models/electrical-properties-power-type-enum.md) | Optional | Power Type used in this connector. |
| `voltage` | `float` | Optional | Voltage in Volts for this connector |
| `amperage` | `float` | Optional | Electric Current in Amperes for this connector |
| `max_electric_power` | `float` | Optional | Power in Kilowatts for this connector |

## Example (as JSON)

```json
{
  "powerType": "AC1Phase",
  "voltage": 230.0,
  "amperage": 16.0,
  "maxElectricPower": 3.7
}
```

