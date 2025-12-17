
# Response 416 Date Range

## Structure

`Response416dateRange`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status_code` | `int` | Optional | Response code |
| `error` | `str` | Optional | Requested Range Not Satisfiable |
| `message` | `str` | Optional | The "fieldDate" should be less or equal to "ISODate". |

## Example (as JSON)

```json
{
  "statusCode": 416,
  "error": "Requested Range Not Satisfiable",
  "message": "The \"startDate\" should be less or equal \"2019-08-20T03:00:00.000Z\"."
}
```

