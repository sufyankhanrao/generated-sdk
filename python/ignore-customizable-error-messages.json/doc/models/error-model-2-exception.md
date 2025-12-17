
# Error Model 2 Exception

## Structure

`ErrorModel2Exception`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_description` | `str` | Required | - |
| `caught` | `str` | Required | - |
| `exception` | `str` | Required | - |
| `inner_exception` | `str` | Required | - |

## Example (as JSON)

```json
{
  "error description": "error description8",
  "caught": "Error in CatchInner caused by calling the ThrowInner method.",
  "Exception": "In catch block of Main method.",
  "Inner Exception": "AppException: Exception in ThrowInner method."
}
```

