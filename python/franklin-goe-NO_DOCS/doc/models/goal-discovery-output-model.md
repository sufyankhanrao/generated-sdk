
# Goal Discovery Output Model

*This model accepts additional fields of type Any.*

## Structure

`GoalDiscoveryOutputModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status_code` | `int` | Required | Status code for the response. |
| `request_id` | `str` | Required | 32-byte string that uniquely identifies a set of (investor preferences, scenario results). Used to GET later pages of scenarios corresponding to a set of investor preferences that an investor has sent to the Goal Discovery Service. |
| `data` | [`List[Scenario]`](../../doc/models/scenario.md) | Required | Array of scenario objects (refer to the Swagger documentation for Scenario objects for more details). The length of this array is equal to `perPage` (refer to the Swagger documentation for Page objects for more details). |
| `page` | [`Page2`](../../doc/models/page-2.md) | Required | Contains details about the number of scenarios returned, the current page, and the total number of scenarios and pages that pertain to these investors preferences. Refer to the Swagger documentation for Page objects for more details. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "statusCode": 200,
  "requestId": "d02f19c5cde34443b97ed81a59417dca",
  "data": [
    {
      "initialInvestment": 100000.0,
      "targetWealth": 200000.2,
      "goalTenure": 8,
      "irr": 2.9,
      "infusions": 24000.3,
      "goalProbability": 158,
      "portfolioId": 2,
      "goalPriority": 96,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "page": {
    "perPage": 200,
    "id": 1,
    "totalRecords": 67380,
    "totalPages": 33690,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

