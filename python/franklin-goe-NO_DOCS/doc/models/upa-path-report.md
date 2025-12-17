
# Upa Path Report

*This model accepts additional fields of type Any.*

## Structure

`UpaPathReport`

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
    209,
    210,
    211
  ],
  "wealthPath": [
    185.43
  ],
  "worstCasePath": [
    172.46,
    172.47,
    172.48
  ],
  "bestCasePath": [
    236.32,
    236.33,
    236.34
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

