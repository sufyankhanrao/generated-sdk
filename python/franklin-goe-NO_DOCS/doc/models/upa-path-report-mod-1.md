
# Upa Path Report Mod 1

<b>For the Modified Plan:</b><br>            GOE’s outputs including estimated portfolio path, wealth path, etc.

*This model accepts additional fields of type Any.*

## Structure

`UpaPathReportMod1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_path` | `List[int]` | Required | GOE’s expected portfolio path across the investment tenure. |
| `wealth_path` | `List[float]` | Required | Priority based path across the investment tenure. |
| `worst_case_path` | `List[float]` | Required | Represents the pessimistic scenario of a wealth path.                     The default value corresponds to 1% probability (99 percentile). This could be customized using the admin portal. |
| `best_case_path` | `List[float]` | Required | Represents the optimistic scenario of a wealth path. The default value corresponds to 1% probability (99 percentile).                     This could be customized using the admin portal. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "portfolioPath": [
    115,
    116,
    117
  ],
  "wealthPath": [
    54.77,
    54.78
  ],
  "worstCasePath": [
    41.8
  ],
  "bestCasePath": [
    145.02,
    145.01
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

