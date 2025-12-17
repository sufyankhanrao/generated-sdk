
# Fault Response Fault

## Structure

`FaultResponseFault`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `faultstring` | `str` | Optional | The description of the error. |
| `detail` | [`FaultResponseFaultDetail`](../../doc/models/fault-response-fault-detail.md) | Optional | - |

## Example (as JSON)

```json
{
  "faultstring": "Invalid ApiKey for given resource",
  "detail": {
    "errorcode": "errorcode6"
  }
}
```

