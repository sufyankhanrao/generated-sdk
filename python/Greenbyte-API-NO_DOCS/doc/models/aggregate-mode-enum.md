
# Aggregate Mode Enum

How data is aggregated in the asset structure.

## Enumeration

`AggregateModeEnum`

## Fields

| Name | Description |
|  --- | --- |
| `DEVICE` | The data is aggregated by device. |
| `DEVICELEVEL` | The data is aggregated by top-level device. |
| `SITE` | The data is aggregated by site. |
| `PORTFOLIO` | All data is aggregated into a single group. |
| `SITELEVEL` | The data is aggregated by site hierarchy level. When this mode is used the parameter AggregateLevel controls down to which level in the hierarchy to aggregate. |

## Example

```
device
```

