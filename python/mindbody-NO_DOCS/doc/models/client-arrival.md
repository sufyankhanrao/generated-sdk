
# Client Arrival

## Structure

`ClientArrival`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `arrival_program_id` | `int` | Optional | Arrival program id |
| `arrival_program_name` | `str` | Optional | Arrival program name |
| `can_access` | `bool` | Optional | Property to check client can access arrival service. |
| `locations_i_ds` | `List[int]` | Optional | List of locations where arrival service can availed |

## Example (as JSON)

```json
{
  "ArrivalProgramID": 208,
  "ArrivalProgramName": "ArrivalProgramName2",
  "CanAccess": false,
  "LocationsIDs": [
    231,
    232,
    233
  ]
}
```

