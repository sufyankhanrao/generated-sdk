
# Liability

## Structure

`Liability`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `agreement_date` | `datetime` | Optional | The date and time at which the client agreed to the liability waiver for the business. |
| `is_released` | `bool` | Optional | The client’s liability release status.<br /><br>When `true`, indicates that the client has agreed to the liability release for the business.<br /><br>When `false`, indicates that the client has not agreed to the liability release for the business. |
| `released_by` | `int` | Optional | An ID indicating who released liability for the client. If the client agreed to the liability waiver by signing into an account online, this value is `null`. If a staff member marked the waiver as signed on behalf of the client, it is the staff member’s ID. `0` indicates that the business owner marked the liability waiver as signed on behalf of the client. |

## Example (as JSON)

```json
{
  "AgreementDate": "2016-03-13T12:52:32.123Z",
  "IsReleased": false,
  "ReleasedBy": 68
}
```

