
# Update Client Contract Autopays Request

## Structure

`UpdateClientContractAutopaysRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_contract_id` | `int` | Optional | Client Contract Id |
| `autopay_start_date` | `datetime` | Optional | Autopay start date |
| `autopay_end_date` | `datetime` | Optional | (optional) - Indefinite if not provided |
| `product_id` | `int` | Optional | Product Id to update (optional if contract has only one product) |
| `replace_with_product_id` | `int` | Optional | (optional) - Replaces the product with this product |
| `amount` | `float` | Optional | Overrides autopay amount or amount that would come from ProductId |
| `overwrite_all_product_i_ds` | `bool` | Optional | (optional) - If true, will update autopays with any productID |

## Example (as JSON)

```json
{
  "ClientContractId": 182,
  "AutopayStartDate": "2016-03-13T12:52:32.123Z",
  "AutopayEndDate": "2016-03-13T12:52:32.123Z",
  "ProductId": 200,
  "ReplaceWithProductId": 120
}
```

