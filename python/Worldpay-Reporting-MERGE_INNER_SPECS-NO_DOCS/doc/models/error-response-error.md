
# Error Response Error

## Structure

`ErrorResponseError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | Worldpay generated Correlation Id<br><br>**Constraints**: *Maximum Length*: `36` |
| `error_code` | `str` | Optional | Code of error<br><br>**Constraints**: *Maximum Length*: `256` |
| `error_message` | `str` | Optional | Error Message<br><br>**Constraints**: *Maximum Length*: `256` |

## Example (as JSON)

```json
{
  "correlationId": "3fcb1437-4e52-4946-9ae1-e618351b6d16",
  "errorCode": "ERROR_CODE",
  "errorMessage": "Error message here."
}
```

