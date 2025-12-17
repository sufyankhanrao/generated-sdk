
# Wealth Path

*This model accepts additional fields of type Any.*

## Structure

`WealthPath`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `default` | `List[float]` | Required | Wealth paths corresponding to the priority-based probability level are returned. |
| `pessimistic` | `List[float]` | Required | Wealth paths corresponding to the Pessimistic probability level are returned |
| `optimistic` | `List[float]` | Required | Wealth paths corresponding to the Optimistic probability level are returned |
| `default_percentile` | `str` | Required | Percentile values corresponding to default path. |
| `pessimistic_percentile` | `str` | Required | Percentile values corresponding to Pessimistic path. |
| `optimistic_percentile` | `str` | Required | Percentile values corresponding to Optimistic path. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "default": [
    37.22,
    37.23,
    37.24
  ],
  "pessimistic": [
    134.6
  ],
  "optimistic": [
    153.78
  ],
  "defaultPercentile": "defaultPercentile6",
  "pessimisticPercentile": "pessimisticPercentile8",
  "optimisticPercentile": "optimisticPercentile8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

