
# Page

*This model accepts additional fields of type Any.*

## Structure

`Page`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `per_page` | `int` | Required | The number of scenarios returned in this response (equal to the number of elements in the data array). Each scenario is returned as a JSON object. Typically, a larger page size lowers the time taken to receive all the results, but increases the time to receive each page of data. |
| `id` | `int` | Required | A 1-indexed number that identifies the page being returned: for example, a pageIndex of 1 returns the first page of scenarios from the Goal Discovery Service |
| `total_records` | `int` | Required | The total number of scenarios corresponding to this request that can be returned by the Goal Discovery service. This corresponds to the number of JSON elements in the data array. |
| `total_pages` | `int` | Required | The total number of pages corresponding to this request that can be returned by the Goal Discovery service. Each page has `perPage` scenarios on it. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "perPage": 200,
  "id": 1,
  "totalRecords": 67380,
  "totalPages": 33690,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

