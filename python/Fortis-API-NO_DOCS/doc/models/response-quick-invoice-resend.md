
# Response Quick Invoice Resend

## Structure

`ResponseQuickInvoiceResend`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type53Enum`](../../doc/models/type-53-enum.md) | Optional | Resource Type<br><br>**Default**: `"QuickInvoiceResend"` |
| `data` | [`Data15`](../../doc/models/data-15.md) | Optional | - |

## Example (as JSON)

```json
{
  "type": "QuickInvoiceResend",
  "data": {
    "id": "id0",
    "email_log_id": "email_log_id2",
    "sms_log_id": "sms_log_id4",
    "success": false,
    "sms_success": false
  }
}
```

