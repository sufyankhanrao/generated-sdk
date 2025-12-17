
# Common Summary Responses

## Structure

`CommonSummaryResponses`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationResponse2`](../../doc/models/pagination-response-2.md) | Optional | Used for pagination. |
| `total_approved_count` | `int` | Optional | Count of Approved Transactions.<br><br>**Constraints**: `<= 10` |
| `total_approved_amount` | `float` | Optional | Sum of Amount of Approved Transactions.<br><br>**Constraints**: `<= 15` |
| `total_declined_count` | `int` | Optional | Count of Declined Transactions.<br><br>**Constraints**: `<= 10` |
| `total_declined_amount` | `float` | Optional | Sum of Amount of Declined Transactions.<br><br>**Constraints**: `<= 15` |
| `total_approved_count_percent` | `float` | Optional | Ratio of Count of Approved Transactions to the Count of Total Transctions.<br><br>**Constraints**: `<= 15` |
| `total_approved_amount_percent` | `float` | Optional | Ratio of the Sum of Amount of Approved Transactions to the Sum of Amount of Total Transctions.<br><br>**Constraints**: `<= 15` |
| `total_declined_count_percent` | `float` | Optional | Ratio of Count of Declined Transactions to the Count of Total Transctions.<br><br>**Constraints**: `<= 15` |
| `total_declined_amount_percent` | `float` | Optional | Ratio of the Sum of Amount of Declined Transactions to the Sum of Amount of Total Transctions.<br><br>**Constraints**: `<= 15` |
| `total_count` | `int` | Optional | Sum of the Count of Approved Transactions and Count of declined Transactions.<br><br>**Constraints**: `<= 10` |
| `total_amount` | `float` | Optional | Sum of the Amount of Approved Transactions and Amount of declined Transactions.<br><br>**Constraints**: `<= 15` |

## Example (as JSON)

```json
{
  "totalApprovedCount": 10,
  "totalDeclinedAmountPercent": 14.65,
  "pagination": {
    "pageNumber": 106,
    "pageSize": 134,
    "totalRowCount": 22,
    "totalReturnedCount": 172
  },
  "totalApprovedAmount": 12.7,
  "totalDeclinedCount": 10,
  "totalDeclinedAmount": 15.0
}
```

