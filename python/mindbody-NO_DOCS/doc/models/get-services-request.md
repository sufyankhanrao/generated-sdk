
# Get Services Request

## Structure

`GetServicesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `program_ids` | `List[int]` | Optional | Filters to pricing options with the specified program IDs. |
| `session_type_ids` | `List[int]` | Optional | Filters to the pricing options with the specified session types IDs. |
| `service_ids` | `List[str]` | Optional | Filters to the pricing options with the specified IDs. In this context, service and pricing option are used interchangeably. These are the `PurchasedItems[].Id` returned from GET Sales. |
| `class_id` | `int` | Optional | Filters to the pricing options for the specified class ID. |
| `class_schedule_id` | `int` | Optional | Filters to the pricing options for the specified class schedule ID. |
| `sell_online` | `bool` | Optional | When `true`, filters to the pricing options that can be sold online.<br /><br>Default: **false** |
| `location_id` | `int` | Optional | When specified, for each returned pricing option, `TaxRate` and `TaxIncluded` are calculated according to the specified location. Note that this does not filter results to only services provided at the given location, and for locations where Value-Added Tax (VAT) rules apply, the `TaxRate` is set to zero. |
| `hide_related_programs` | `bool` | Optional | When `true`, indicates that pricing options of related programs are omitted from the response.<br /><br>Default: **false** |
| `staff_id` | `int` | Optional | Sets `Price` and `OnlinePrice` to the particular pricing of a specific staff member, if allowed by the business. |
| `include_discontinued` | `bool` | Optional | When `true`, indicates that the filtered pricing option list includes discontinued pricing options.<br /><br>Default: **false** |
| `include_sale_in_contract_only` | `bool` | Optional | When `true`, indicates that the filtered pricing option list includes sale in contract only pricing options.<br /><br>Default: **false** |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ProgramIds": [
    54
  ],
  "SessionTypeIds": [
    68
  ],
  "ServiceIds": [
    "ServiceIds3"
  ],
  "ClassId": 162,
  "ClassScheduleId": 108
}
```

