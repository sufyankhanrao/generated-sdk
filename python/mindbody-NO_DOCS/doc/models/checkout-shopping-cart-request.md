
# Checkout Shopping Cart Request

## Structure

`CheckoutShoppingCartRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cart_id` | `str` | Optional | The unique ID of the shopping cart to be processed. You can use this value to maintain a persistent cart. If you do not specify a cart ID, the MINDBODY software generates one. |
| `client_id` | `str` | Required | The RSSID of the client making the purchase. A cart can be validated without a client ID, but a client ID must be specified to complete a sale. |
| `test` | `bool` | Optional | When `true`, indicates that the contents of the cart are validated, but the transaction does not take place. You should use this parameter during testing and when checking the calculated totals of the items in the cart.<br /><br>When `false`, the transaction takes place and the database is affected.<br /><br>Default: **false** |
| `items` | [`List[CheckoutItemWrapper]`](../../doc/models/checkout-item-wrapper.md) | Required | A list of the items in the cart. |
| `in_store` | `bool` | Optional | When `true`, indicates that the cart is to be completed by a staff member and is to take place at one of the business’ physical locations.<br /><br>When `false`, indicates that the cart is to be completed by a client from the business’ online store.<br /><br>Default: **false** |
| `calculate_tax` | `bool` | Optional | When `true`, indicates that the tax should be calculated.<br>When `false`, indicates that the tax should not be calculated.<br>Default: **true** |
| `promotion_code` | `str` | Optional | Promotion code to be applied to the cart. |
| `payments` | [`List[CheckoutPaymentInfo]`](../../doc/models/checkout-payment-info.md) | Required | A list of payment information objects to be applied to payment against the items in the cart. |
| `send_email` | `bool` | Optional | When `true`, sends a purchase receipt email to the client. Note that all appropriate permissions and settings must be enabled for the client to receive an email.<br /><br>Default: **false** |
| `location_id` | `int` | Optional | The location ID to be used for pulling business mode prices and taxes. If no location ID is supplied, it defaults to the online store, represented by a null value.<br>Default: **null** (the online store) |
| `image` | `str` | Optional | The byte array data of the signature image. |
| `image_file_name` | `str` | Optional | The name of the signature image being uploaded. |
| `consumer_present` | `bool` | Optional | When `true`, indicates that the consumer is present or otherwise able to successfully negotiate an SCA challenge. It is not a good idea to have this always be `false` as that could very likely lead to a bank declining all transactions for the merchant.<br>Defaults to `false`. |
| `payment_authentication_callback_url` | `str` | Optional | The URL consumer is redirected to if the bank requests SCA. This field is only needed if ConsumerPresent is `true` |
| `transaction_ids` | `List[int]` | Optional | The list of TransactionIds provided with initial response containing SCA Challenge URLs for ConsumerPresent transactions |
| `is_billing_postal_code_required` | `bool` | Optional | the flag to check billing post code is required or not. |
| `enforce_location_restrictions` | `bool` | Optional | When `true`, enforces "sell at" location restrictions on the cart items.<br>When `false`, "sell at" location restrictions are not enforced.<br>Default: **false** |

## Example (as JSON)

```json
{
  "CartId": "CartId4",
  "ClientId": "ClientId4",
  "Test": false,
  "Items": [
    {
      "Item": {
        "Type": "Type2",
        "Metadata": {
          "key0": {
            "key1": "val1",
            "key2": "val2"
          }
        }
      },
      "DiscountAmount": 41.36,
      "AppointmentBookingRequests": [
        {
          "StaffId": 16,
          "LocationId": 66,
          "SessionTypeId": 166,
          "Resources": [
            {
              "Id": 216,
              "Name": "Name6"
            },
            {
              "Id": 216,
              "Name": "Name6"
            },
            {
              "Id": 216,
              "Name": "Name6"
            }
          ],
          "StartDateTime": "2016-03-13T12:52:32.123Z"
        }
      ],
      "EnrollmentIds": [
        249,
        250
      ],
      "ClassIds": [
        153,
        154,
        155
      ]
    },
    {
      "Item": {
        "Type": "Type2",
        "Metadata": {
          "key0": {
            "key1": "val1",
            "key2": "val2"
          }
        }
      },
      "DiscountAmount": 41.36,
      "AppointmentBookingRequests": [
        {
          "StaffId": 16,
          "LocationId": 66,
          "SessionTypeId": 166,
          "Resources": [
            {
              "Id": 216,
              "Name": "Name6"
            },
            {
              "Id": 216,
              "Name": "Name6"
            },
            {
              "Id": 216,
              "Name": "Name6"
            }
          ],
          "StartDateTime": "2016-03-13T12:52:32.123Z"
        }
      ],
      "EnrollmentIds": [
        249,
        250
      ],
      "ClassIds": [
        153,
        154,
        155
      ]
    }
  ],
  "InStore": false,
  "CalculateTax": false,
  "PromotionCode": "PromotionCode6",
  "Payments": [
    {
      "Type": "Type8",
      "Metadata": {
        "key0": {
          "key1": "val1",
          "key2": "val2"
        },
        "key1": {
          "key1": "val1",
          "key2": "val2"
        }
      }
    },
    {
      "Type": "Type8",
      "Metadata": {
        "key0": {
          "key1": "val1",
          "key2": "val2"
        },
        "key1": {
          "key1": "val1",
          "key2": "val2"
        }
      }
    }
  ]
}
```

