
# Update Odometer

## Structure

`UpdateOdometer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sales_item_id` | `str` | Required | Unique SalesItemId (Either Billed on Unbilled)<br>Mandatory |
| `new_odometer_value` | `int` | Required | NewOdometerValue that needs to be updated |

## Example (as JSON)

```json
{
  "SalesItemId": "SalesItemId2",
  "NewOdometerValue": 158
}
```

