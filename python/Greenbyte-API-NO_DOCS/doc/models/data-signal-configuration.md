
# Data Signal Configuration

Your data signal configuration. These only apply to wind devices.

## Structure

`DataSignalConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `availability_time_data_signal_id` | `int` | Required | The id of the data signal used for time-based availability data.<br><br>**Constraints**: `>= 1` |
| `availability_production_data_signal_id` | `int` | Required | The id of the data signal used for production-based availability data.<br><br>**Constraints**: `>= 1` |
| `lost_production_data_signal_id` | `int` | Required | The id of the data signal used for lost production data.<br><br>**Constraints**: `>= 1` |
| `performance_data_signal_id` | `int` | Required | The id of the data signal used for performance data.<br><br>**Constraints**: `>= 1` |

## Example (as JSON)

```json
{
  "availabilityTimeDataSignalId": 100,
  "availabilityProductionDataSignalId": 176,
  "lostProductionDataSignalId": 232,
  "performanceDataSignalId": 184
}
```

