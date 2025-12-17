
# Decision Actions Post Request

## Structure

`DecisionActionsPostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `decision` | `str` | Required | The identifier of the Decision to which this resource applies |
| `action` | [`DescisionActionsActionEnum`](../../doc/models/descision-actions-action-enum.md) | Optional | The action to take when this check fails.<br><br><details><br><summary>Valid Values</summary><br>- `1` - **Block txn, will never be processed. The Entity is sent to the manual review queue.**<br>- `3` - **Hold txn, will not be captured.**<br>- `4` - **Reserve txn, funds should be reserved.**<br>- `5` - **Block current activity, no change for merchant.**<br>- `8` - **We onboard the merchant and wait for manual check later.**<br></details><br> |
| `application` | [`ApplicationEnum`](../../doc/models/application-enum.md) | Optional | Where the action defined by this DecisionAction should apply.<br><br><details><br><summary>Valid Values</summary><br>- `account` - **Account type Decision.**<br>- `txn` - **Txn type Decision.**<br>- `entity` - **Entity type Decision.**<br></details><br> |
| `score_type` | [`ScoreTypeEnum`](../../doc/models/score-type-enum.md) | Optional | The type of score result on the related Decision.<br><br><details><br><summary>Valid Values</summary><br>- `low` - **Only applies if the check hit the low of the parent decision.**<br>- `high` - **Only applies if the check hit the high of the parent decision.**<br>- `none` - **Only applies if the check did not hit the high or low of the parent decision.**<br></details><br> |
| `mtype` | [`DecisionActionTypeEnum`](../../doc/models/decision-action-type-enum.md) | Optional | The type of DecisionAction.<br><br><details><br><summary>Valid Values</summary><br>- `equal` - **Equal.**<br>- `notEqual` - **Not Equal.**<br>- `contains` - **Contains.**<br>- `greater` - **Greater.**<br>- `less` - **Less.**<br></details><br> |
| `field` | `str` | Optional | The result field to check. |
| `score` | `str` | Optional | The score to check. |
| `data` | `str` | Optional | The decisionAction data will be matched with verificationReuslts data. |
| `message` | `str` | Optional | The decisionAction message will be matched with verificationReuslts message. |
| `code` | `str` | Optional | The decisionAction code will be matched with verificationReuslts code. |
| `grouping` | `str` | Optional | A name for a group of decisionActions to be applied in conjunction when evaluating this DecisionAction; when grouping is used, the DecisionActions will not apply unless they all match. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Required | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Required | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "decision": "t1_dcs_67ddc0163a32ae0c5c33bfc",
  "action": 1,
  "application": "account",
  "scoreType": "low",
  "type": "less",
  "field": "score",
  "score": "20",
  "data": "dummy@dummy.neoncrm.com",
  "message": "Required",
  "code": "I602",
  "grouping": "bademail",
  "inactive": 0,
  "frozen": 0
}
```

