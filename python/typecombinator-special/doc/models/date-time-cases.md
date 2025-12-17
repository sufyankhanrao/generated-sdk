
# Date Time Cases

This class contains datetime types in oneOf/anyOf cases.

## Structure

`DateTimeCases`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `rfc_3339_vs_string` | datetime \| str | Required | This is a container for any-of cases. |
| `all_one_of` | date \| datetime | Required | This is a container for one-of cases. |
| `all_outer_array` | List[date \| datetime] | Required | This is List of a container for one-of cases. |
| `datevs_array` | List[datetime] \| datetime | Required | This is a container for any-of cases. |
| `mapvs_array` | List[datetime] \| Dict[str, datetime] | Required | This is a container for any-of cases. |

## Example (as JSON)

```json
{
  "rfc3339vsString": "2016-03-13T12:52:32.123Z",
  "allOneOf": "2016-03-13",
  "allOuterArray": [
    "2016-03-13"
  ],
  "datevsArray": [
    "Mon, 15 Jun 2009 20:45:30 GMT"
  ],
  "mapvsArray": [
    "Mon, 15 Jun 2009 20:45:30 GMT"
  ]
}
```

