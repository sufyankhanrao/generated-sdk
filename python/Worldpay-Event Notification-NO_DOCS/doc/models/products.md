
# Products

## Structure

`Products`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `review_trackers` | [`ReviewTrackers`](../../doc/models/review-trackers.md) | Optional | Information on review trackers |
| `discount_program` | [`DiscountProgram`](../../doc/models/discount-program.md) | Optional | Information on discount program |
| `recruiting_manager` | [`RecruitingManager`](../../doc/models/recruiting-manager.md) | Optional | Information on recruting manager |
| `get_upside` | [`GetUpside`](../../doc/models/get-upside.md) | Optional | Information on get upside |

## Example (as JSON)

```json
{
  "reviewTrackers": {
    "enabled": false,
    "program": "REVIEW TRACKERS",
    "optInDate": "optInDate8",
    "optOutDate": "optOutDate6",
    "billingStartDate": "billingStartDate4"
  },
  "discountProgram": {
    "enabled": false,
    "program": "FIS DISCOUNT PROGRAM",
    "optInDate": "optInDate4",
    "optOutDate": "optOutDate2",
    "billingStartDate": "billingStartDate0"
  },
  "recruitingManager": {
    "enabled": false,
    "program": "FIS RECRUITING MANAGER",
    "optInDate": "optInDate2",
    "optOutDate": "optOutDate0",
    "billingStartDate": "billingStartDate8"
  },
  "getUpside": {
    "enabled": false,
    "program": "GETUPSIDE",
    "optInDate": "optInDate2",
    "optOutDate": "optOutDate0",
    "billingStartDate": "billingStartDate8"
  }
}
```

