
# Spot

Contains information about the spot details.

## Structure

`Spot`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reserved_spot_numbers` | `List[int]` | Optional | Contains information about the collection of reserved spot numbers. |
| `available_spot_numbers` | `List[int]` | Optional | Contains information about the collection of available spot numbers. |
| `unavailable_spot_numbers` | `List[int]` | Optional | Contains information about the collection of Unavailable spot numbers. |

## Example (as JSON)

```json
{
  "ReservedSpotNumbers": [
    164,
    165
  ],
  "AvailableSpotNumbers": [
    68
  ],
  "UnavailableSpotNumbers": [
    83,
    82,
    81
  ]
}
```

