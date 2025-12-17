
# Commission Payroll Purchase Event

## Structure

`CommissionPayrollPurchaseEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `staff_id` | `int` | Optional | The ID of the staff member who earned commissions. |
| `sale_date_time` | `datetime` | Optional | The date and time when the sale occurred. |
| `sale_id` | `int` | Optional | The sale’s ID. |
| `sale_type` | `str` | Optional | The Sales type. When this is "Purchase" indicates that this sale paid commission to a staff. When this is "Return" |
| `product_id` | `int` | Optional | The product ID of the item for which the staff earned commissions. |
| `earnings_details` | [`List[CommissionDetail]`](../../doc/models/commission-detail.md) | Optional | Contains information about which commissions the staff earned for this item. |
| `earnings` | `float` | Optional | The total commissions earned by the staff for this item. |

## Example (as JSON)

```json
{
  "StaffId": 230,
  "SaleDateTime": "2016-03-13T12:52:32.123Z",
  "SaleId": 136,
  "SaleType": "SaleType8",
  "ProductId": 178
}
```

