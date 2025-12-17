
# Quick Invoice View

## Structure

`QuickInvoiceView`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Quick Invoice Views Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `quick_invoice_id` | `str` | Optional | Quick Invoice ID<br><br>**Constraints**: *Maximum Length*: `24` |
| `remote_ip` | `str` | Optional | Remote Ip<br><br>**Constraints**: *Maximum Length*: `45` |
| `created_ts` | `int` | Optional | Created Time Stamp |

## Example (as JSON)

```json
{
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "quick_invoice_id": "Quick Invoice ID",
  "created_ts": 1422040992,
  "remote_ip": "remote_ip8"
}
```

