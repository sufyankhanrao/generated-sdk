
# Items Response

## Structure

`ItemsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `txn` | `str` | Optional | The txn in which these items have been sold, A single txn may have many items. |
| `item` | `str` | Optional | The SKU, short name or title of the item sold. |
| `description` | `str` | Optional | A description of this Item. This field is stored as a text string and must be between 0 and 500 characters long. |
| `custom` | `str` | Optional | A custom identifier for this line Item. This field is stored as a text string and must be between 0 and 500 characters long. |
| `um` | `str` | Optional | The unit of measure for this Item. This field is stored as a text string and must be between 0 and 100 characters long. Examples of units of measure may be: each, kilogram, pound, month. |
| `commodity_code` | `str` | Optional | The commodity code for this Item. This field is stored as a text string and must be between 0 and 12 characters long. |
| `product_code` | `str` | Optional | The product code for this Item such as: UPC, catalog number, or inventory number. This field is stored as a text string and must be between 0 and 100 characters long. |
| `quantity` | `int` | Optional | The quantity of this Item included in the Transaction. This field is specified as an integer. |
| `price` | `int` | Optional | The amount charged for this Item. This field is specified as an integer in cents. |
| `total` | `int` | Optional | The total price for the line item. This field is specified as an integer in cents. |
| `discount` | `int` | Optional | The discount for the line item. This field is specified as an integer in cents. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "inactive": 0,
  "frozen": 0,
  "id": "id2",
  "created": "created8",
  "modified": "modified0",
  "creator": "String1",
  "modifier": "modifier4"
}
```

