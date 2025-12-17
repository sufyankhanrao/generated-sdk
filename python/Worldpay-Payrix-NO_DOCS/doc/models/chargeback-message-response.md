
# Chargeback Message Response

## Structure

`ChargebackMessageResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `chargeback` | `str` | Optional | The identifier of the Chargeback resource that this chargebackMessage relates to. |
| `date` | `str` | Optional | The date of this chargebackMessage.<br>The date is specified as an eight digit string in YYYYMMDD format, for example, '20160120' for January 20, 2016. |
| `mtype` | [`ChargebackMessageTypeEnum`](../../doc/models/chargeback-message-type-enum.md) | Optional | The type of this chargebackMessage.<br><br><details><br><summary>Valid Values</summary><br>- `assign` - **Assign the chargeback.**<br>- `notate` - **Add a note to the chargeback.**<br>- `acceptLiability` - **Accept Liability for the Chargeback amount.**<br>- `createPreArbitration` - **Create a pre-arbitration case.**<br>- `represent` - **Represent the chargeback.**<br>- `respond` - **Respond to the chargeback.**<br>- `requestArbitration` - **Request Arbitration. The Merchant wishes to enter arbitration to determine the outcome of the Chargeback.**<br>- `createArbitration` - **Create an arbitration case.**<br>- `requestPreArbitration` - **Request a pre-arbitration case.**<br>- `requestResolutionToPreArbitration` - **Request resolution to a pre-arbitration case.**<br>- `respondToDispute` - **Respond to a dispute.**<br>- `respondToPreArbitration` - **Respond to a pre-arbitration case.**<br>- `unaccept` - **Unaccept the chargeback.**<br></details><br> |
| `from_queue` | `str` | Optional | The fromQueue element that specifies the queue in which the chargeback resided prior to the performance of the specified activity. |
| `to_queue` | `str` | Optional | The toQueue element that specifies queue to which the chargeback moved after the performance of the specified activity. |
| `contact` | `str` | Optional | The identifier of the Contact for this chargebackMessage. |
| `amount` | `int` | Optional | The amount that this chargebackMessage corresponds to.<br>For example, if the 'type' is set to '3' (Accept Liability), then this amount indicates that the liability should be for this amount.<br>This field is specified as an integer in cents. |
| `currency` | [`CurrencyEnum`](../../doc/models/currency-enum.md) | Optional | The currency of the amount. See <a href="https://www.iban.com/currency-codes" target="_blank">Currency codes</a>  for all valid values. |
| `note` | `str` | Optional | A free-text note relating to this chargebackMessage. |
| `status` | [`ChargebackMessageStatusEnum`](../../doc/models/chargeback-message-status-enum.md) | Optional | The current status of the Chargeback.<br><br><details><br><summary>Valid Values</summary><br>- `requested` - **The chargeback has been requested.**<br>- `processing` - **The chargeback is currently being processed.**<br>- `failed` - **The chargeback process has failed.**<br>- `denied` - **The chargeback has been denied.**<br>- `processed` - **The chargeback has been successfully processed.**<br></details><br> |
| `imported` | [`ImportedEnum`](../../doc/models/imported-enum.md) | Optional | Whether the chargeback message was imported.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not imported.**<br>- `1` - **Imported.**<br></details><br> |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "currency": "USD",
  "inactive": 0,
  "frozen": 0,
  "id": "id2",
  "created": "created2",
  "modified": "modified0",
  "creator": "String1",
  "modifier": "modifier6"
}
```

