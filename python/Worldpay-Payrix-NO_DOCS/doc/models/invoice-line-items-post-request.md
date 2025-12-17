
# Invoice Line Items Post Request

## Structure

`InvoiceLineItemsPostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invoice` | `str` | Required | The identifier of the Invoice that owns this InvoiceLineItem. |
| `invoice_item` | `str` | Required | The identifier of the InvoiceItem associated with this InvoiceLineItem. |
| `quantity` | `int` | Required | The quantity purchased for this line item, specified as an integer.<br><br>**Default**: `1` |
| `price` | `int` | Optional | The price for each item, this field is specified as an integer in cents. |
| `discount` | `int` | Optional | The discount for the line item, this field is specified as an integer in cents. |

## Example (as JSON)

```json
{
  "invoice": "t1_inv_00b62cb82db90057aae7000",
  "invoiceItem": "t1_ini_00b62cb7d3b3a7e6a841000",
  "quantity": 1,
  "price": 50000,
  "discount": 100
}
```

