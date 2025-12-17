
# Invoice Items Post Request

## Structure

`InvoiceItemsPostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `login` | `str` | Required | The identifier of the Login that owns this Invoiceitem. |
| `item` | `str` | Required | The desired name of this InvoiceItem. This field is stored as a text string and must be between 1 and 500 characters long. |
| `description` | `str` | Optional | The description of this InvoiceItem. This field is stored as a text string and must be between 0 and 500 characters long. |
| `custom` | `str` | Optional | A custom field of this InvoiceItem. This field is stored as a text string and must be between 0 and 500 characters long. |
| `price` | `int` | Required | The price of this InvoiceItem is specified as an integer in cents.<br><br>**Default**: `0` |
| `um` | `str` | Optional | The unit of measure of this InvoiceItem is stored as a text string and must be between 0 and 100 characters long; examples of units of measure may be: each, kilogram, pound, month. |
| `commodity_code` | `str` | Optional | The commodity code for this InvoiceItem. This field is stored as a text string and must be between 0 and 12 characters long. |
| `product_code` | `str` | Optional | The product code for this invoice item such as: UPC, catalog number, or inventory number. This field is stored as a text string and must be between 0 and 100 characters long. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Required | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Required | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "login": "t1_log_00d514abedbf6f641b7c2f2",
  "item": "Test Custom Links",
  "description": "Test Custom Links",
  "custom": "Sample custom field 1",
  "um": "kilogram",
  "commodityCode": "03000",
  "productCode": "SKU23456",
  "price": 1666,
  "inactive": 0,
  "frozen": 0
}
```

