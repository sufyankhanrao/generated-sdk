
# Disbursements Response

## Structure

`DisbursementsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `entity` | `str` | Optional | The identifier of the Entity that owns this Disbursement. |
| `account` | `str` | Optional | The token of the accounts resource used for this Disbursement. |
| `payment` | `str` | Optional | A reference to the actual account or card data used for this disbursement. If someone changes the details in their bank account within Payrix Pro, the account token will point to a new account but the payment will always point to the data used for this disbursement. |
| `payout` | `str` | Optional | The identifier of the Payout that represents the schedule for this Disbursement. |
| `settlement` | `str` | Optional | The settlement record for this disbursement. |
| `statement` | `str` | Optional | The identifier of the Statement being paid by this Disbursement. |
| `description` | `str` | Optional | A description of this Disbursement. |
| `secondary_descriptor` | `str` | Optional | A secondary descriptor for the ACH transaction sent to the receiving bank. |
| `amount` | `int` | Optional | The total amount of this Disbursement. |
| `returned_amount` | `int` | Optional | The amount that has been returned within the disbursement. |
| `status` | [`DisbursementStatusEnum`](../../doc/models/disbursement-status-enum.md) | Optional | The current status of this Disbursement.<br><br><details><summary>Valid Values</summary><br>- `1` - **Requested.** The request for this Disbursement has been received.<br>- `2` - **Processing.** This Disbursement is being processed to be paid out.<br><br>- `3` - **Processed.** This Disbursement has been paid by ACH to the bank account referenced in the Disbursement data.<br><br>- `4` - **Failed.** A problem occurred and the payment processor has failed to process this Disbursement.<br><br>- `5` - **Denied.** This Disbursement has been refused.<br><br>- `6` - **Returned.** This Disbursement has been returned.<br><br> </details><br> |
| `funding_status` | [`FundingStatusEnum`](../../doc/models/funding-status-enum.md) | Optional | Indicates if entries were processed for this Disbursement. <details><summary>Valid Values</summary><br><br>- `pending` - **Pending entry creation and processing.**<br><br>- `processed` - **Entry created and processed.**<br><br> </details><br> |
| `processed` | `str` | Optional | A timestamp indicating when the Disbursement was processed. The format should be YYYY-MM-DD HH:MM:SS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}` |
| `disbursement_entries_status` | [`DisbursementEntriesStatusEnum`](../../doc/models/disbursement-entries-status-enum.md) | Optional | The current status of disbursementEntries creation.<br><br><details><br><summary>Valid Values</summary><br>- `pending` - **Pending entry creation and processing.**<br>- `processing` - **Entry is still processing.**<br><br>- `processed` - **Entry created and processed.**<br><br></details><br> |
| `last_negative_entry` | `str` | Optional | The last negative Entry processed included in the disbursement. |
| `last_negative_pending_entry` | `str` | Optional | The last negative PendingEntry processed included in the disbursement. |
| `last_positive_reserve_entry` | `str` | Optional | The last positive ReserveEntry processed included in the disbursement. |
| `last_positive_entry` | `str` | Optional | The last positive Entry processed included in the disbursement. |
| `last_positive_pending_entry` | `str` | Optional | The last positive PendingEntry processed included in the disbursement. |
| `last_negative_reserve_entry` | `str` | Optional | The last negative ReserveEntry processed included in the disbursement. |
| `currency` | [`CurrencyEnum`](../../doc/models/currency-enum.md) | Optional | The currency of this Disbursement. See <a href="https://www.iban.com/currency-codes" target="_blank">Currency codes</a>  for all valid values. |
| `expiration` | `str` | Optional | The expiration date of the related debit account. |
| `same_day` | [`DisbursementsSameDayEnum`](../../doc/models/disbursements-same-day-enum.md) | Optional | Whether sameDay funding is enabled or disabled for this disbursement.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Disabled.**<br>- `1` - **Enabled.**<br><br></details><br> |

## Example (as JSON)

```json
{
  "currency": "USD",
  "id": "id8",
  "created": "created8",
  "modified": "modified6",
  "creator": "String7",
  "modifier": "modifier2"
}
```

