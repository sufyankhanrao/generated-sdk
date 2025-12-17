
# Invoice Parameters Response

## Structure

`InvoiceParametersResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `login` | `str` | Optional | The identifier of the Login that owns this invoiceParameter resource. |
| `entity` | `str` | Optional | The identifier of the Entity associated with this invoiceParameter. |
| `org` | `str` | Optional | The identifier of the Org associated with this invoiceParameter. |
| `division` | `str` | Optional | The identifier of the Division associated with this invoiceParameter. |
| `partition` | `str` | Optional | The identifier of the Partition associated with this invoiceParameter. |
| `mtype` | [`InvoiceParameterTypeEnum`](../../doc/models/invoice-parameter-type-enum.md) | Optional | The type of Transaction.<br><br><details><br><summary>Valid Values</summary><br>- `1` - **Credit Card Only:** Sale Transaction, processes a sale and charges the customer.<br>- `2` - **Credit Card Only:** Auth Transaction, authorizes and holds the requested total on the credit card.<br>- `3` - **Credit Card Only:** Capture Transaction, finalizes a prior Auth Transaction and charges the customer.<br>- `4` - **Credit Card Only:** Reverse Authorization, reverses a prior Auth or Sale Transaction and releases the credit hold.<br>- `5` - **Credit Card Only:** Refund Transaction, refunds a prior Capture or Sale Transaction (total may be specified for a partial refund).<br>- `7` - **Echeck Only:** Echeck Sale Transaction, sale transaction for ECheck payment.<br>- `8` - **Echeck Only:** ECheck Refund Transaction, refund transaction for prior ECheck Sale Transaction.<br>- `11` - **Echeck Only:** Echeck Redeposit Transaction, attempt to redeposit a prior failed eCheck Sale Transaction.<br>- `12` - **Echeck Only:** Echeck Account Verification Transaction, attempt to verify eCheck payment details.<br></details><br> |
| `value` | `str` | Optional | The value of this type of invoiceParameter. |
| `locked` | [`InvoiceParameterLockedEnum`](../../doc/models/invoice-parameter-locked-enum.md) | Optional | Whether this invoiceParameter is locked. If locked, it defaults to the value of the invoiceParameter.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not locked**<br>- `1` - **Locked**<br></details><br>**Default**: `0`<br> |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "locked": 0,
  "inactive": 0,
  "frozen": 0,
  "id": "id0",
  "created": "created0",
  "modified": "modified8",
  "creator": "String9",
  "modifier": "modifier4"
}
```

