
# Valutec

## Structure

`Valutec`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `group_id` | `str` | Required | GroupId<br><br>**Constraints**: *Maximum Length*: `4` |
| `billing_account_number` | `str` | Optional | Billing Account Number<br><br>**Constraints**: *Maximum Length*: `17` |
| `billing_routing_number` | `str` | Optional | Billing Routing Number<br><br>**Constraints**: *Maximum Length*: `9` |
| `settlement_account_number` | `str` | Optional | Settlement Account Number<br><br>**Constraints**: *Maximum Length*: `17` |
| `settlement_routing_number` | `str` | Optional | Settlement Routing Number<br><br>**Constraints**: *Maximum Length*: `9` |
| `last_updated_date_time` | `str` | Optional | Record created date & timestamp in system<br><br>**Constraints**: *Maximum Length*: `29`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}:[0-9]{6}` |
| `enrollment_date` | `str` | Optional | VCS gift card enrollment date<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-2]{2}-[0-2]{2}` |
| `processing_date` | `str` | Optional | VCS go live first transaction processing date<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-2]{2}-[0-2]{2}` |
| `close_date` | `str` | Optional | VCS Valutec optout date<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-2]{2}-[0-2]{2}` |

## Example (as JSON)

```json
{
  "groupId": "1010",
  "billingAccountNumber": "********2311",
  "billingRoutingNumber": "*****2111",
  "settlementAccountNumber": "********4500",
  "settlementRoutingNumber": "*****4511",
  "processingDate": "2021-10-12",
  "closeDate": "2021-11-21",
  "lastUpdatedDateTime": "lastUpdatedDateTime8"
}
```

