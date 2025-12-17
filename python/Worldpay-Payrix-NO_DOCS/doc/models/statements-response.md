
# Statements Response

## Structure

`StatementsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `billing` | `str` | Optional | The identifier of the Billing of this statement resource. |
| `entity` | `str` | Optional | The paying entity for which this statement applies. |
| `start` | `int` | Optional | The date on which this Statement period should start. The date is specified as an eight digit string in YYYYMMDD format, for example, '20160120' for January 20, 2016. |
| `finish` | `int` | Optional | The date on which this Statement period should finish. The date is specified as an eight digit string in YYYYMMDD format, for example, '20160120' for January 20, 2016. |
| `status` | [`StatementStatusEnum`](../../doc/models/statement-status-enum.md) | Optional | The current status of the statement.<br><br><details><br><summary>Valid Values</summary><br>- `pending` - **Statement amount is owed and is pending payment.**<br>- `processing` - **A payment is processing for this statement, pending completion.**<br>- `partiallyPaid` - **The statement was partially paid, some amount is still outstanding.**<br>- `paid` - **The statement was paid in full.**<br>- `partiallyCancelled` - **The statement was partially cancelled, some amount is still outstanding.**<br>- `cancelled` - **The statement was completely cancelled and is no longer due for payment.**<br></details><br>**Default**: `"pending"`<br> |
| `total_paid` | `int` | Optional | The total paid amount for this statement, specified as an integer in cents. |
| `total` | `int` | Optional | The total amount for this statement. This field is specified as an integer in cents. |
| `currency` | [`CurrencyEnum`](../../doc/models/currency-enum.md) | Optional | The currency for this statement. See <a href="https://www.iban.com/currency-codes" target="_blank">Currency codes</a>  for all valid values. |
| `forentity` | `str` | Optional | The payee entity of the statement. |

## Example (as JSON)

```json
{
  "status": "pending",
  "currency": "USD",
  "id": "id8",
  "created": "created8",
  "modified": "modified6",
  "creator": "String7",
  "modifier": "modifier2"
}
```

