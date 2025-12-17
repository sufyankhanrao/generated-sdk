
# Invoice Line Items Response

## Structure

`InvoiceLineItemsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `invoice` | `str` | Optional | The identifier of the Invoice that owns this InvoiceLineItem. |
| `invoice_item` | `str` | Optional | The identifier of the InvoiceItem associated with this InvoiceLineItem. |
| `quantity` | `int` | Optional | The quantity purchased for this line item, specified as an integer. |
| `price` | `int` | Optional | The price for each item, this field is specified as an integer in cents. |
| `discount` | `int` | Optional | The discount for the line item, this field is specified as an integer in cents. |
| `total` | `int` | Optional | The total price for the line item, which is specified as an integer in cents. |

## Example (as JSON)

```json
{
  "id": "id8",
  "created": "created8",
  "modified": "modified6",
  "creator": "String7",
  "modifier": "modifier2"
}
```

