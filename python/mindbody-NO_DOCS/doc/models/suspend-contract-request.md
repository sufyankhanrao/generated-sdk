
# Suspend Contract Request

## Structure

`SuspendContractRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Required | The ID of the client. |
| `client_contract_id` | `int` | Required | The unique ID of the sale of the contract. |
| `suspension_type` | `str` | Optional | ex. Illness, Injury, Vacation. (Note this can be customized by each studio).<br>If provided, then Duration, DurationUnit, and SuspensionFee (if applicable) are automatically applied. Restrict Days are not supported. |
| `suspension_start` | `datetime` | Optional | The contract suspension start date.<br>Default: *today’s date* |
| `duration` | `int` | Optional | The number of (DurationUnit) the suspension lasts. |
| `duration_unit` | `int` | Optional | The unit applied to Duration. |
| `open_ended` | `bool` | Optional | When `true`, indicates that suspension is open ended. Also, when `true`, then Duration and DurationUnit are ignored.<br>Default: *false* |
| `suspension_notes` | `str` | Optional | The comments for suspending a contract. |
| `suspension_fee` | `float` | Optional | An optional charge that clients who wish to pause a contract for a set period of time can be charged. |

## Example (as JSON)

```json
{
  "ClientId": "ClientId6",
  "ClientContractId": 122,
  "SuspensionType": "SuspensionType6",
  "SuspensionStart": "2016-03-13T12:52:32.123Z",
  "Duration": 228,
  "DurationUnit": 106,
  "OpenEnded": false
}
```

