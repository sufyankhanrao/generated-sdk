
# Fee Modifiers Response

## Structure

`FeeModifiersResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `fee` | `str` | Optional | The identifier of the Fee that this Fee Modifier applies. |
| `entity` | `str` | Optional | The identifier of the Entity that this Fee Modifier applies for. |
| `org` | `str` | Optional | The identifier of the Org this Fee Modifiers should apply for on behalf of the Entity identified in the value of the 'entity' field.<br>This field is optional. If it is set, then the Fee Modifier is applied to this Org instead. |
| `division` | `str` | Optional | Division ID in which the fee modifiers is associated. |
| `partition` | `str` | Optional | ID of the partition related to this fee modifiers. |
| `fromentity` | `str` | Optional | The identifier of the Entity who should pay this Fee on behalf of the Entity identified in the value of the 'entity' or 'org' field.<br>This field is optional. If it is set, then the Fee is charged to this Entity instead. |
| `markup_um` | [`MarkupUmEnum`](../../doc/models/markup-um-enum.md) | Optional | The unit of measure for the markup amount for the Fee.<br><br><details><br><summary>Valid Values</summary><br>- `1` - **Fixed Amount.** Specified in the 'markupAmount' field as an integer in cents.<br>- `2` - **Percentage.** Specified in the 'markupAmount' field in basis points.<br></details><br> |
| `markup_amount` | `int` | Optional | The total amount of the markup value for this Fee.<br>The units used in this field are determined by the value of the 'markupUm' field on the Fee. If the 'markupUm' field is set to 'percentage', then this field specifies the Fee percentage to levy in basis points. If the 'markupUm' field is set to 'actual', then this field specifies the markup amount in cents. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "inactive": 0,
  "frozen": 0,
  "id": "id8",
  "created": "created8",
  "modified": "modified6",
  "creator": "String7",
  "modifier": "modifier2"
}
```

