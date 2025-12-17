
# Decision Rules Response

## Structure

`DecisionRulesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `decision` | `str` | Optional | The identifier of the Decision that this Decision Rule applies. |
| `name` | `str` | Optional | The name of this Decision Rule. This field is stored as a text string and must be between 0 and 100 characters long. |
| `description` | `str` | Optional | Description of the Decision Rules. |
| `mtype` | [`DecisionRuleTypeEnum`](../../doc/models/decision-rule-type-enum.md) | Optional | The type of logic to apply with this Decision Rule.<br><br><details><br><summary>Valid Values</summary><br>- `less` - **Less.**<br>- `equal` - **Equal.**<br>- `notEqual` - **Not Equal.**<br>- `greater` - **Greater.**<br>- `swiped` - **Swiped.**<br>- `signed` - **Signed.**<br>- `type` - **Type.**<br>- `origin` - **Origin.**<br>- `method` - **Method.**<br>- `cvvResult` - **CVV Result.**<br>- `avsResult` - **AVS Result.**<br>- `3dsResult` - **3DS Result. The Decision applies based on the results of a 3DS check.**<br>- `related` - **Related.**<br>- `relatedDelay` - **Related Delay.**<br>- `relatedFloor` - **Related Floor.**<br>- `relatedCeil` - **Related Ceil.**<br>- `mcc` - **MCC.**<br>- `merchantCountry` - **Merchant Country.**<br>- `issuerCountry` - **Issuer Country.**<br>- `international` - **International.**<br>- `platform` - **Platform.**<br>- `methodType` - **Method Type.**<br>- `emv` - **EMV.**<br>- `misuse` - **Misuse.**<br>- `bin` - **BIN.**<br>- `primary` - **Primary.**<br>- `fundingCurrencyEqual` - **Funding Currency Equal.**<br>- `fundingCurrencyNotEqual` - **Funding Currency Not Equal.**<br>- `fundingCurrencyMismatch` - **Funding Currency Mismatch.**<br>- `settledCurrencyMismatch` - **Settled Currency Mismatch.**<br>- `imported` - **Imported.**<br>- `subscription` - **Subscription.**<br>- `publicAuth` - **Public Auth.**<br>- `clientIp` - **Client IP.**<br>- `debtRepayment` - **Debt Repayment.**<br>- `cofType` - **COF Type.**<br>- `entryMode` - **Entry Mode.**<br></details><br> |
| `value` | `int` | Optional | The value to compare against when evaluating this Decision Rule. |
| `grouping` | `str` | Optional | A name for a group of rules to be applied in conjunction when evaluating this Decision Rule; When grouping is used, the Decision will be allowed to be processed if at least one of the rules are matched. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "inactive": 0,
  "frozen": 0,
  "id": "id2",
  "created": "created2",
  "modified": "modified0",
  "creator": "String1",
  "modifier": "modifier6"
}
```

