
# Substitute Class Teacher Response

## Structure

`SubstituteClassTeacherResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mclass` | [`SubstituteTeacherClass`](../../doc/models/substitute-teacher-class.md) | Optional | Represents a single class instance. Used in SubstituteClassTeacher endpoint. |

## Example (as JSON)

```json
{
  "Class": {
    "ClassScheduleId": 206,
    "Location": {
      "AdditionalImageURLs": [
        "AdditionalImageURLs4"
      ],
      "Address": "Address2",
      "Address2": "Address24",
      "Amenities": [
        {
          "Id": 214,
          "Name": "Name8"
        },
        {
          "Id": 214,
          "Name": "Name8"
        },
        {
          "Id": 214,
          "Name": "Name8"
        }
      ],
      "BusinessDescription": "BusinessDescription8"
    },
    "MaxCapacity": 124,
    "WebCapacity": 170,
    "TotalBooked": 154
  }
}
```

