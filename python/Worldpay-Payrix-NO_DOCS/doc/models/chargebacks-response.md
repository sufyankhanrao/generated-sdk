
# Chargebacks Response

## Structure

`ChargebacksResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `merchant` | `str` | Optional | The ID of the Merchant associated with the Chargeback. |
| `txn` | `str` | Optional | The ID of the Transaction associated with the Chargeback. |
| `mid` | `str` | Optional | The Merchant's processing MID. |
| `description` | `str` | Optional | Description of the chargeback. |
| `total` | `int` | Optional | The total amount of the Chargeback. |
| `represented_total` | `int` | Optional | The representedTotal for this Chargeback if it has been represented. |
| `cycle` | [`CycleEnum`](../../doc/models/cycle-enum.md) | Optional | <details><summary>Valid Values</summary><br>- `retrieval` - **Initial request from the issuer for more information on this Transaction.**<br>- `first` - **First Chargeback from issuer for this Transaction.**<br><br>- `arbitration` - **Arbitration is being sought for this Chargeback.**<br><br>- `reversal` - **Chargeback was reversed.**<br><br>- `representment` - **Merchant is being represented to the issuer with the Chargeback response posted.**<br><br>- `preArbitration` - **Chargeback is no longer representable. Merchant must choose to accept or arbitrate with the card brand.**<br><br>- `arbitrationLost` - **Arbitration lost.**<br><br>- `arbitrationSplit` - **Arbitration split.**<br><br>- `arbitrationWon` - **Arbitration won.**<br><br>- `issuerAcceptPreArbitration` - **Issuer accepted the pre-arbitration response.**<br><br>- `issuerDeclinedPreArbitration` - **Issuer declined pre-arbitration.**<br><br>- `responseToIssuerPreArbitration` - **Response to issuer pre-arbitration.**<br><br>- `merchantAcceptedPreArbitration` - **Merchant accepted the pre-arbitration response.**<br><br>- `merchantDeclinedPreArbitration` - **Merchant declined the pre-arbitration response.**<br><br>- `preCompliance` - **Pre-compliance.**<br><br>- `compliance` - **Compliance.** </details> |
| `currency` | [`CurrencyEnum`](../../doc/models/currency-enum.md) | Optional | The currency for this statement. See <a href="https://www.iban.com/currency-codes" target="_blank">Currency codes</a>  for all valid values. |
| `platform` | [`ChargebackPlatformEnum`](../../doc/models/chargeback-platform-enum.md) | Optional | The platform used for the adjustment. This field is required if the adjustment is not between entities. |
| `payment_method` | [`ChargebackPaymentMethodEnum`](../../doc/models/chargeback-payment-method-enum.md) | Optional | The type of payment method used for the transaction.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **No payment method specified.**<br>- `1` - **American Express.**<br>- `2` - **Visa.**<br>- `3` - **MasterCard.**<br>- `4` - **Diners Club.**<br>- `5` - **Discover.**<br>- `6` - **PayPal.**<br>- `7` - **Debit card.**<br>- `8` - **Checking account.**<br>- `9` - **Savings account.**<br>- `10` - **Corporate checking account.**<br>- `11` - **Corporate savings account.**<br>- `12` - **Gift card.**<br>- `13` - **EBT card.**<br>- `14` - **WIC card.**<br></details><br> |
| `ref` | `str` | Optional | The processing reference number for this Chargeback. |
| `reason` | `str` | Optional | The reason description for this Chargeback. |
| `reason_code` | `str` | Optional | The reason code for this Chargeback. |
| `issued` | `int` | Optional | The date when the Chargeback was issued. |
| `received` | `int` | Optional | The date when the Chargeback was received. |
| `reply` | `int` | Optional | The deadline to submit a reply for the Chargeback. |
| `bank_ref` | `str` | Optional | The issuing bank's reference number for this Chargeback. |
| `chargeback_ref` | `str` | Optional | Chargeback reference number. |
| `status` | [`ChargebackStatusEnum`](../../doc/models/chargeback-status-enum.md) | Optional | The Chargeback's status.<br><br><details><br><summary>Valid Values</summary><br>- `open` - **Chargeback is open, responses may be submitted.**<br>- `closed` - **Chargeback is closed, responses may no longer be submitted.**<br>- `won` - **Chargeback won.**<br>- `lost` - **Chargeback lost.**<br></details><br>**Default**: `"open"`<br> |
| `last_status_change` | `str` | Optional | The ID of the ChargebackStatus representing the latest status change for this Chargeback. |
| `actionable` | [`ActionableEnum`](../../doc/models/actionable-enum.md) | Optional | Whether the Chargeback is actionable and can be responded to.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not actionable**<br>- `1` - **Actionable**<br><br></details><br> |
| `shadow` | [`ShadowEnum`](../../doc/models/shadow-enum.md) | Optional | <details><br><summary>Valid Values</summary><br>- `0` - **Not shadowed.**<br>- `1` - **Shadowed.**<br><br></details><br> |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "currency": "USD",
  "platform": "VCORE",
  "status": "open",
  "inactive": 0,
  "frozen": 0,
  "id": "id2",
  "created": "created2",
  "modified": "modified0",
  "creator": "String1",
  "modifier": "modifier6"
}
```

