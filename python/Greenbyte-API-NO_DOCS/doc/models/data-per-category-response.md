
# Data Per Category Response

An object containing data grouped by contract category and aggregate.

## Structure

`DataPerCategoryResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data_signal` | [`DataSignal`](../../doc/models/data-signal.md) | Required | A data signal. |
| `calculation` | [`CalculationModeEnum`](../../doc/models/calculation-mode-enum.md) | Required | Which operation to use when aggregating data. |
| `data` | [`List[DataPerCategoryItem]`](../../doc/models/data-per-category-item.md) | Required | A list of objects: one per combination of<br><br>* aggregate<br>* contract category |

## Example (as JSON)

```json
{
  "dataSignal": {
    "dataSignalId": 1,
    "title": "Wind Speed",
    "unit": "m/s"
  },
  "calculation": "sum",
  "data": [
    {
      "aggregateId": 6,
      "deviceIds": [
        1,
        2,
        3
      ],
      "contractTitle": "Vestas 1",
      "categoryTitle": "Icing",
      "categoryTime": "available",
      "value": 104.55,
      "duration": 150.0,
      "aggregatePathNames": [
        "aggregatePathNames4"
      ]
    }
  ]
}
```

