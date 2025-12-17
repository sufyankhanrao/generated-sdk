
# Checkout Item Wrapper

## Structure

`CheckoutItemWrapper`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item` | [`CheckoutItem`](../../doc/models/checkout-item.md) | Optional | - |
| `discount_amount` | `float` | Optional | The amount the item is discounted. This parameter is ignored for packages. |
| `appointment_booking_requests` | [`List[CheckoutAppointmentBookingRequest]`](../../doc/models/checkout-appointment-booking-request.md) | Optional | A list of appointments to be booked then paid for by this item. This parameter applies only to pricing option items. |
| `enrollment_ids` | `List[int]` | Optional | A list of enrollment IDs that this item is to pay for. This parameter applies only to pricing option items. |
| `class_ids` | `List[int]` | Optional | A list of class IDs that this item is to pay for. This parameter applies only to pricing option items. |
| `course_ids` | `List[int]` | Optional | A list of course IDs that this item is to pay for. This parameter applies only to pricing option items. |
| `visit_ids` | `List[int]` | Optional | A list of visit IDs that this item is to pay for. This parameter applies only to pricing option items. |
| `appointment_ids` | `List[int]` | Optional | A list of appointment IDs that this item is to reconcile. |
| `id` | `int` | Optional | The item’s unique ID within the cart. |
| `quantity` | `int` | Optional | The number of this item to be purchased. |

## Example (as JSON)

```json
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
  "DiscountAmount": 177.3,
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
    },
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
    },
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
    19
  ],
  "ClassIds": [
    179,
    180
  ]
}
```

