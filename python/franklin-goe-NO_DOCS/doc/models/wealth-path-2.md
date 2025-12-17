
# Wealth Path 2

Priority based path of wealth across the investment tenure <br>        (corresponding to the end of each reallocation date).  If additional wealth paths are <br>        requested, a dictionary of 3 wealth paths and wealth path percentiles is returned – covered in the next 2 rows<br>         The probability levels can be configured.

*This model accepts additional fields of type Any.*

## Structure

`WealthPath2`

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
    78.6,
    78.61
  ],
  "pessimistic": [
    51.54,
    51.55
  ],
  "optimistic": [
    195.16,
    195.17,
    195.18
  ],
  "defaultPercentile": "defaultPercentile6",
  "pessimisticPercentile": "pessimisticPercentile4",
  "optimisticPercentile": "optimisticPercentile6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

