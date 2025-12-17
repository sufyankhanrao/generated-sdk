
# Adjustments Response

## Structure

`AdjustmentsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `login` | `str` | Optional | The Login that owns this Adjustment. |
| `entity` | `str` | Optional | The Entity that will receive the set amount. |
| `fromentity` | `str` | Optional | The Entity that will pay for the adjustment.<br>This is an optional field and should only be used when the amount is being transfered from the fromentity to the entity. |
| `onentity` | `str` | Optional | The applicable Entity for this Adjustment.<br>This field is an optional field. |
| `disbursement` | `str` | Optional | Related disbursement ID. |
| `description` | `str` | Optional | The description of this Decision Rule.<br>This field is stored as a text string and must be between 0 and 100 characters long. |
| `amount` | `float` | Optional | The amount of the Adjustment, This field is specified in cents(up to three decimal points). |
| `currency` | [`CurrencyEnum`](../../doc/models/currency-enum.md) | Optional | The currency for the amount of this resource. See <a href="https://www.iban.com/currency-codes" target="_blank">Currency codes</a>  for all valid values. |
| `funding` | `str` | Optional | The ID of the fund which the disbursement’s movement applies. |
| `platform` | `str` | Optional | The processor that issued this terminalTxnRef.<br><br><details><br><summary>Valid Values</summary><br>- `APPLE` - **Apple Payment Processor**<br>- `ELAVON` - **ELAVON Payment Processor**<br>- `FIRSTDATA` - **FirstData Payment Processor**<br>- `GOOGLE` - **Google Payment Processor**<br>- `VANTIV` - **WorldPay / Vantiv eComm Payment Processor (VAP)**<br>- `VCORE` - **WorldPay / Vantiv Core Payment Processor**<br>- `WELLSACH` - **Wells Fargo Merchant Services Payment Processor (ACH)**<br>- `WELLSFARGO` - **Wells Fargo Merchant Services Payment Processor**<br>- `WFSINGLE` - **Wells Fargo Single Payment Processor**<br>- `WORLDPAY` - **WORLDPAY**<br>- `TDBANKCA` - **TDBANKCA**<br></details><br> |
| `fbo` | `str` | Optional | FBO account (For-Benefit-Of account) identifier. |

## Example (as JSON)

```json
{
  "currency": "USD",
  "id": "id6",
  "created": "created6",
  "modified": "modified4",
  "creator": "String5",
  "modifier": "modifier0"
}
```

