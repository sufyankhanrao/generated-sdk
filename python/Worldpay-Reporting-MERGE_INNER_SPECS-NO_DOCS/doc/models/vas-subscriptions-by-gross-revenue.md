
# VAS Subscriptions by Gross Revenue

Gross revenue by Value added service subscriptions.

## Structure

`VASSubscriptionsByGrossRevenue`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_chains` | `int` | Optional | Total number of chains associated with top hierarchy level<br><br>**Constraints**: `>= 1000000000`, `<= 9999999999` |
| `details` | [`List[Details]`](../../doc/models/details.md) | Optional | Refers to the object details |

## Example (as JSON)

```json
{
  "totalChains": 1000000000,
  "details": [
    {
      "valueAddedService": "valueAddedService0",
      "numberOfChains": 174,
      "grossRevenue": 201.16
    },
    {
      "valueAddedService": "valueAddedService0",
      "numberOfChains": 174,
      "grossRevenue": 201.16
    },
    {
      "valueAddedService": "valueAddedService0",
      "numberOfChains": 174,
      "grossRevenue": 201.16
    }
  ]
}
```

