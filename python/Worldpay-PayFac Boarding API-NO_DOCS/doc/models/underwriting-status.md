
# Underwriting Status

## Structure

`UnderwritingStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `status` | [`StatusEnum`](../../doc/models/status-enum.md) | Optional | Underwriting status of the submerchant |
| `reason` | `str` | Optional | Underwriting pending reason |

## Example (as JSON)

```json
{
  "id": "id2",
  "status": "Pending",
  "reason": "reason8"
}
```

