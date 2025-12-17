
# Holds Put Request

## Structure

`HoldsPutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `login` | `str` | Optional | The identifier of the Login that owns this holds resource. |
| `verification_ref` | `str` | Optional | If this hold resource was triggered through Payrix Integration Risk, then this field stores the identifier of the VerificationRef. |
| `released` | `str` | Optional | If this hold was released, this will contain the timestamp for when it was released. (YYYY-MM-DD HH:II:SS)<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$` |
| `reviewed` | `str` | Optional | If this hold was reviewed, this will contain the timestamp for when it was reviewed. (YYYY-MM-DD HH:II:SS)<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$` |
| `release_action` | [`ReleaseActionEnum`](../../doc/models/release-action-enum.md) | Optional | The final action taken on the hold while it's been released.<br><br><details><br><summary>Valid Values</summary><br>- `1` - **Holds released because the hold resource was approved.**<br>- `2` - **Holds released because the hold resource was cancelled.**<br>- `3` - **Holds released because the hold resource was refunded.**<br>- `4` - **Holds released because the hold resource was failed.**<br>- `5` - **Expired.**<br></details><br> |
| `hold_source` | [`HoldSourceEnum`](../../doc/models/hold-source-enum.md) | Optional | Field created to know the reason for why a hold was created.<br><br><details><br><summary>Valid Values</summary><br>- `DS_MODEL_POLICY_RUN` - **DS_MODEL_POLICY_RUN**<br>- `API_DECISION` - **API_DECISION**<br>- `POLICY_RUN` - **POLICY_RUN**<br>- `RISK_ALERT` - **RISK_ALERT**<br>- `MANUAL` - **MANUAL**<br>- `ERROR` - **ERROR**<br></details><br> |
| `hold_source_id` | `str` | Optional | reasonid for why a hold was created. |
| `delayed_funding_start_date` | `str` | Optional | The timestamp when hold was considered to be delaying funding. (YYYY-MM-DD HH:II:SS)<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$` |
| `delayed_funding_end_date` | `str` | Optional | The timestamp when hold stopped delaying funding, this might be due to the hold been released, cancelled or funded. (YYYY-MM-DD HH:II:SS)<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$` |
| `analyst` | `str` | Optional | The person who review the hold applied. |
| `claimed` | `str` | Optional | The timestamp for the most recent update of the analyst field. (YYYY-MM-DD HH:II:SS)<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$` |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "login": "t1_hld_0000fc11df8e4c00000e00c",
  "verificationRef": "t1_xyz_12345eb00f0cf1bfc00be0f",
  "released": "2025-01-31 08:42:16",
  "reviewed": "2025-01-31 08:42:16",
  "releaseAction": 2,
  "holdSource": "API_DECISION",
  "holdSourceId": "5a9bba34-38eb-489e-abd8-765e18562a08",
  "delayedFundingStartDate": "2025-01-31 08:42:16",
  "delayedFundingEndDate": "2025-01-31 08:42:16",
  "analyst": "name",
  "claimed": "2025-01-31 08:42:16",
  "inactive": 0,
  "frozen": 0
}
```

