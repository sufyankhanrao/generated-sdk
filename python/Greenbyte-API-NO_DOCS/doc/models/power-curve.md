
# Power Curve

## Structure

`PowerCurve`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `int` | Required | The id of a device.<br><br>**Constraints**: `>= 1` |
| `title` | `str` | Required | The title of the power curve. |
| `values` | [`List[PowerCurveValue]`](../../doc/models/power-curve-value.md) | Required | - |

## Example (as JSON)

```json
{
  "deviceId": 96,
  "title": "title4",
  "values": [
    {
      "windSpeed": 28.46,
      "power": 248.04
    }
  ]
}
```

