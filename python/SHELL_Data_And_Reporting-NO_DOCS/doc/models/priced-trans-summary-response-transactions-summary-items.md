
# Priced Trans Summary Response Transactions Summary Items

## Structure

`PricedTransSummaryResponseTransactionsSummaryItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `int` | Optional | Product Id |
| `product_code` | `str` | Optional | Product Code<br>Examples:<br>10	TMF Charges<br>11	Tunnel/Bridges<br>12	Motorway toll<br>13	Ferries |
| `product_name` | `str` | Optional | Product Name<br>Examples:<br>Unleaded - High octane<br>Unleaded - Medium octane<br>Unleaded - Low octane<br>Unleaded Environmental |
| `product_group_id` | `int` | Optional | Product Group Id<br>Example:<br>1	Parent Product Group<br>2	All Fuels<br>3	Motor gasoline<br>4	2 stroke<br>5	Autogas<br>6	CNG |
| `product_group_name` | `str` | Optional | Product Group Name<br>Example:<br>1	Parent Product Group<br>2	All Fuels<br>3	Motor gasoline<br>4	2 stroke<br>5	Autogas<br>6	CNG<br>7	Automotive Gas Oil |
| `site_group_id` | `int` | Optional | Site Group Id<br>Example: 202 |
| `site_group_name` | `str` | Optional | Site Group Name<br>Example: CZ 9100 ECONOMY NETWORK |
| `total_fuel_quantity` | `int` | Optional | Total Fuel Quantity |
| `total_net_amount` | `int` | Optional | Total Net amount in invoice currency |
| `total_gross_amount` | `int` | Optional | Total Gross amount in invoice currency |
| `invoice_currency_code` | `str` | Optional | ISO currency code<br>Example: GBP |
| `invoice_currency_symbol` | `str` | Optional | Currency symbol of the Invoice Currency Code<br>Example: £, $ |
| `customer_retail_value_total_net` | `float` | Optional | Sum of the retail net price |
| `customer_retail_value_total_gross` | `float` | Optional | Sum of the retail gross price |

## Example (as JSON)

```json
{
  "ProductId": 164,
  "ProductCode": "ProductCode2",
  "ProductName": "ProductName8",
  "ProductGroupId": 92,
  "ProductGroupName": "ProductGroupName4"
}
```

