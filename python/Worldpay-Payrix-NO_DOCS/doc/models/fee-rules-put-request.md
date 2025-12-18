
# Fee Rules Put Request

## Structure

`FeeRulesPutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fee` | `str` | Optional | The identifier of the Fee that this Fee Rule applies. |
| `name` | `str` | Optional | The name of this Fee Rule.<br>This field is stored as a text string and must be between 0 and 100 characters long. |
| `description` | `str` | Optional | The description of this Fee Rule. |
| `mtype` | [`FeeRuleTypeEnum`](../../doc/models/fee-rule-type-enum.md) | Optional | The type of Transaction.<br><br><details><br><summary>Valid Values</summary><br>- `1` - **Credit Card Only: Sale Transaction.** Processes a sale and charges the customer.<br>- `2` - **Credit Card Only: Auth Transaction.** Authorizes and holds the requested total on the credit card.<br>- `3` - **Credit Card Only: Capture Transaction.** Finalizes a prior Auth Transaction and charges the customer.<br>- `4` - **Credit Card Only: Reverse Authorization.** Reverses a prior Auth or Sale Transaction and releases the credit hold.<br>- `5` - **Credit Card Only: Refund Transaction.** Refunds a prior Capture or Sale Transaction (total may be specified for a partial refund).<br>- `7` - **Echeck Only: Echeck Sale Transaction.** Sale Transaction for ECheck payment.<br>- `8` - **Echeck Only: ECheck Refund Transaction.** Refund Transaction for prior ECheck Sale Transaction.<br>- `11` - **Echeck Only: Echeck Redeposit Transaction.** Attempt to redeposit a prior failed eCheck Sale Transaction.<br>- `12` - **Echeck Only: Echeck Account Verification Transaction.** Attempt to verify eCheck payment details.<br></details><br> |
| `application` | [`FeeApplicationEnum`](../../doc/models/fee-application-enum.md) | Optional | Where the feeRule should apply.<br><br><details><br><summary>Valid Values</summary><br>- `both` - **Both.** The rule should apply to the fee and to the calculation of collections.<br>- `fee` - **Fee.** The rule should apply only to the fee itself.<br>- `collection` - **Collection.** The fee should be only used when calculating a collection.<br></details><br>**Default**: `'both'`<br> |
| `value` | `str` | Optional | The value to compare against when evaluating this Fee Rule. |
| `grouping` | `str` | Optional | A name for a group of rules to be applied in conjunction when evaluating this Fee Rule.<br>When grouping is used, the Fee will be allowed to be processed if at least one of the rules are matched. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "fee": "t1_fee_67ce8623b048d0d5284a886",
  "type": 1,
  "application": "both",
  "value": "1",
  "name": "Fee Rule1",
  "description": "Fee Rule",
  "grouping": "Fee Rule Group1",
  "inactive": 0,
  "frozen": 0
}
```

