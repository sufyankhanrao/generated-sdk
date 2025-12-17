
# Current Customer

*This model accepts additional fields of type Any.*

## Structure

`CurrentCustomer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer` | [`Customer`](../../doc/models/customer.md) | Optional | Represents a customer (end-user) |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "customer": {
    "customerId": "customerId4",
    "name": {
      "first": "first6",
      "middle": "middle6",
      "last": "last0",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "addresses": [
      {
        "line1": "line16",
        "city": "city4",
        "state": "state0",
        "postalCode": "postalCode4",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      }
    ],
    "telephones": [
      "telephones4",
      "telephones5",
      "telephones6"
    ],
    "email": [
      "email8",
      "email9",
      "email0"
    ],
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

