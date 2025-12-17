
# Get Class Visits Request

Get class visit request.

## Structure

`GetClassVisitsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `class_id` | `int` | Required | The class ID. |
| `last_modified_date` | `datetime` | Optional | When included in the request, only records modified on or after the `LastModifiedDate` specified are included in the response. |

## Example (as JSON)

```json
{
  "ClassID": 200,
  "LastModifiedDate": "2016-03-13T12:52:32.123Z"
}
```

