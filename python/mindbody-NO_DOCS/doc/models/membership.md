
# Membership

## Structure

`Membership`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `membership_id` | `int` | Optional | The membership id. |
| `membership_name` | `str` | Optional | The membership name. |
| `priority` | `int` | Optional | The priority/sort order. |
| `member_retail_discount` | `float` | Optional | The membership discount for retail as a percentage. |
| `member_service_discount` | `float` | Optional | The membership discount for services as a percentage. |
| `allow_clients_to_schedule_unpaid` | `bool` | Optional | Allow clients in this membership to schedule unpaid. |
| `online_booking_restricted_to_members_only` | [`List[ProgramMembership]`](../../doc/models/program-membership.md) | Optional | List of programs that are restricted to clients in this membership only. |
| `day_of_month_scheduling_opens_for_next_month` | `int` | Optional | Day of month scheduling opens for next month.  Unrestricted is a null value. |
| `restrict_self_sign_in_to_members_only` | `bool` | Optional | Restrict self sign in to members only. |
| `allow_members_to_book_appointments_without_paying` | `bool` | Optional | Allow members to book appointments without paying. |
| `allow_members_to_purchase_non_members_services` | `bool` | Optional | Allow members to purchase non-members services. |
| `allow_members_to_purchase_non_members_products` | `bool` | Optional | Allow members to purchase non-members products. |
| `is_active` | `bool` | Optional | Indicates if the membership is active. |

## Example (as JSON)

```json
{
  "MembershipId": 228,
  "MembershipName": "MembershipName0",
  "Priority": 178,
  "MemberRetailDiscount": 155.74,
  "MemberServiceDiscount": 84.46
}
```

