
# Holds Response

## Structure

`HoldsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `login` | `str` | Optional | The identifier of the Login that owns this holds resource. |
| `entity` | `str` | Optional | The Entity id in which this Hold belongs to. |
| `txn` | `str` | Optional | The identifier of the Txn that is being held with this hold. |
| `terminal_txn` | `str` | Optional | The TerminalTxn id in which this Hold belongs to. |
| `account` | `str` | Optional | The identifier of the Account that owns this holds resource. |
| `verification` | `str` | Optional | If this hold resource was triggered through a verification, then this field stores the identifier of the Verification. |
| `verification_ref` | `str` | Optional | If this hold resource was triggered through Payrix Integration Risk, then this field stores the identifier of the VerificationRef. |
| `decision_action` | `str` | Optional | The DecisionAction id in which this Hold belongs to. |
| `action` | [`HoldActionEnum`](../../doc/models/hold-action-enum.md) | Optional | The action taken on the referenced Txn. Block, Hold, or Reserve it.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **NONE**<br>- `1` - **Block.** Block the Transaction from proceeding. This returns an error.<br>- `3` - **Hold.** Hold the Transaction. It will not be captured until it is manually released.<br>- `4` - **Reserve** Reserve the Transaction. The funds for the transaction will not be released until the Transaction is manually reviewed.<br>- `5` - **LIMIT** Block current activity.<br>- `6` - **PASS** Passed decision(s).<br>- `8` - **POSTREVIEWONLY** Passed decision(s).<br></details><br> |
| `released` | `str` | Optional | If this hold was released, this will contain the timestamp for when it was released. The format should be YYYY-MM-DD HH:MM:SS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$` |
| `reviewed` | `str` | Optional | If this hold was reviewed, this will contain the timestamp for when it was reviewed. The format should be YYYY-MM-DD HH:MM:SS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$` |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |
| `release_action` | [`ReleaseActionEnum`](../../doc/models/release-action-enum.md) | Optional | The final action taken on the hold while it's been released.<br><br><details><br><summary>Valid Values</summary><br>- `1` - **Holds released because the hold resource was approved.**<br>- `2` - **Holds released because the hold resource was cancelled.**<br>- `3` - **Holds released because the hold resource was refunded.**<br>- `4` - **Holds released because the hold resource was failed.**<br>- `5` - **Expired.**<br></details><br> |
| `delayed_funding_start_date` | `str` | Optional | The timestamp when hold was considered to be delaying funding. The format should be YYYY-MM-DD HH:MM:SS.<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$` |
| `delayed_funding_end_date` | `str` | Optional | The timestamp when hold stopped delaying funding, this might be due to the hold been released, cancelled or funded. The format should be YYYY-MM-DD HH:MM:SS.<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$` |
| `analyst` | `str` | Optional | The person who review the hold applied. |
| `claimed` | `str` | Optional | The timestamp for the most recent update of the analyst field. The format should be YYYY-MM-DD HH:MM:SS.<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$` |
| `hold_source` | [`HoldSourceEnum`](../../doc/models/hold-source-enum.md) | Optional | Field created to know the reason for why a hold was created.<br><br><details><br><summary>Valid Values</summary><br>- `DS_MODEL_POLICY_RUN` - **DS_MODEL_POLICY_RUN**<br>- `API_DECISION` - **API_DECISION**<br>- `POLICY_RUN` - **POLICY_RUN**<br>- `RISK_ALERT` - **RISK_ALERT**<br>- `MANUAL` - **MANUAL**<br>- `ERROR` - **ERROR**<br></details><br> |
| `hold_source_id` | `str` | Optional | Reason id for why a hold was created. |
| `hold_source_details` | `str` | Optional | It adds details to hold source. |
| `division` | `str` | Optional | ID of the division associated with this vendor |

## Example (as JSON)

```json
{
  "inactive": 0,
  "frozen": 0,
  "holdSource": "ERROR",
  "id": "id4",
  "created": "created4",
  "modified": "modified2",
  "creator": "String3",
  "modifier": "modifier8"
}
```

