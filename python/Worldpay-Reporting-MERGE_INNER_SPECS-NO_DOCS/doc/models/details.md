
# Details

Details.

## Structure

`Details`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value_added_service` | `str` | Optional | Additional services provided to customer. VAS are performed to meet customer demands.<br><br>**Constraints**: *Maximum Length*: `256` |
| `number_of_chains` | `int` | Optional | Number of chains associated with top hierarchy level.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `gross_revenue` | `float` | Optional | Overall cost incurred for merchant for a specific value added service.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "valueAddedService": "pciNonValidation",
  "numberOfChains": 6500,
  "grossRevenue": 21844.32
}
```

