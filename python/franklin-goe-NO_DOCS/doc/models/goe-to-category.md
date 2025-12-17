
# Goe to Category

*This model accepts additional fields of type Any.*

## Structure

`GoeToCategory`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `category_name` | `str` | Required | Unique name assigned to an asset category in the portfolio |
| `category_id` | `str` | Required | Unique id assigned to an asset category in the portfolio |
| `category_price` | `float` | Required | Price of the security as on the date the request payload is generated. <br>                        For “Cash”, the category Price is assumed to be 1 for the initial call. |
| `quantity` | `float` | Required | Number of units of the underlying fund  <br>                    Note:  <br>                    Amount in a security = categoryPrice x quantity |
| `cost_basis` | `float` | Required | The purchase price of the funds. In the case of multiple lots within the same category, the average cost price is used. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "categoryName": "CASH",
  "categoryID": "10",
  "categoryPrice": 1.0,
  "quantity": 14589.0,
  "costBasis": 14589.0,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

