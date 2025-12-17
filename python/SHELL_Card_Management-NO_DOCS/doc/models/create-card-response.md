
# Create Card Response

This entity models the data that is sent in the http response body for this operation.

## Structure

`CreateCardResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `driver_and_vrn` | `str` | Optional | Driver and VRN of the card. ;( semicolon) is used as delimiter |
| `order_card_reference` | `int` | Optional | Reference number for each individual card in the order |

## Example (as JSON)

```json
{
  "DriverAndVRN": "Robert:MV65YLH",
  "OrderCardReference": 488351
}
```

