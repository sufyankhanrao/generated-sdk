
# Items Put Request

## Structure

`ItemsPutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item` | `str` | Optional | This is item resource. |
| `description` | `str` | Optional | A description of this Item.<br>This field is stored as a text string and must be between 0 and 500 characters long. |
| `custom` | `str` | Optional | A custom identifier for this line Item.<br>This field is stored as a text string and must be between 0 and 500 characters long. |
| `quantity` | `int` | Optional | The quantity of this Item included in the Transaction.<br>This field is specified as an integer. |
| `price` | `int` | Optional | The amount charged for this Item.<br>This field is specified as an integer in cents. |
| `um` | `str` | Optional | The unit of measure for this Item.<br>This field is stored as a text string and must be between 0 and 100 characters long.<br>Examples of units of measure may be: each, kilogram, pound, month. |
| `total` | `int` | Optional | The total price for the line item.<br>This field is specified as an integer in cents. |
| `commodity_code` | `str` | Optional | The commodity code for this Item.<br>This field is stored as a text string and must be between 0 and 12 characters long. |
| `product_code` | `str` | Optional | The product code for this Item such as: UPC, catalog number, or inventory number.<br>This field is stored as a text string and must be between 0 and 100 characters long. |
| `discount` | `int` | Optional | The discount for the line item.<br>This field is specified as an integer in cents. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "item": "Line Item 21",
  "description": "A description of Item",
  "custom": "Identifier",
  "quantity": 1,
  "price": 471,
  "um": "EACH",
  "total": 471,
  "commodityCode": "9717123",
  "discount": 0,
  "productCode": "Prorated Tenant Protection Fee",
  "inactive": 0,
  "frozen": 0
}
```

