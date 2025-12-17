
# Contact Log Type

A contact log type.

## Structure

`ContactLogType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The Id of the contactlog Type. |
| `name` | `str` | Optional | The name of the contactlog Type. |
| `sub_types` | [`List[ContactLogSubType]`](../../doc/models/contact-log-sub-type.md) | Optional | Contains the SubType objects, each of which describes the subtypes for a contactlog Type. |

## Example (as JSON)

```json
{
  "Id": 80,
  "Name": "Name6",
  "SubTypes": [
    {
      "Id": 102,
      "Name": "Name6"
    },
    {
      "Id": 102,
      "Name": "Name6"
    },
    {
      "Id": 102,
      "Name": "Name6"
    }
  ]
}
```

