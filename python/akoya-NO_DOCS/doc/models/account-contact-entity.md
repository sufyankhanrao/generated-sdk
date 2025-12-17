
# Account Contact Entity

Contact information for the account

*This model accepts additional fields of type Any.*

## Structure

`AccountContactEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `holders` | [`List[AccountHolderEntity]`](../../doc/models/account-holder-entity.md) | Optional | Owners of the account |
| `emails` | `List[str]` | Optional | Email addresses associated with the account |
| `addresses` | [`List[DeliveryAddress]`](../../doc/models/delivery-address.md) | Optional | - |
| `telephones` | [`List[TelephoneNumber]`](../../doc/models/telephone-number.md) | Optional | Telephone numbers associated with the account. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "holders": [
    {
      "customerId": "customerId0",
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
        },
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
        "telephones0"
      ],
      "email": [
        "email8",
        "email7"
      ],
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    {
      "customerId": "customerId0",
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
        },
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
        "telephones0"
      ],
      "email": [
        "email8",
        "email7"
      ],
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "emails": [
    "emails1"
  ],
  "addresses": [
    {
      "line1": "line16",
      "line2": "line28",
      "line3": "line36",
      "city": "city4",
      "region": "region0",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "telephones": [
    {
      "type": "FAX",
      "country": "GB",
      "number": "number4",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    {
      "type": "FAX",
      "country": "GB",
      "number": "number4",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    {
      "type": "FAX",
      "country": "GB",
      "number": "number4",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

