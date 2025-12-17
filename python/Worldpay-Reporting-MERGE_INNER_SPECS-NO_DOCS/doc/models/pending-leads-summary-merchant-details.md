
# Pending Leads Summary Merchant Details

Pending leads summary grouped by merchant.

## Structure

`PendingLeadsSummaryMerchantDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_name` | `str` | Optional | Name of the merchant in pipeline.<br><br>**Constraints**: *Maximum Length*: `10000` |
| `referring_banker` | `str` | Optional | Name of the referring banker.<br><br>**Constraints**: *Maximum Length*: `10000` |
| `branch_name` | `str` | Optional | Name of the branch.<br><br>**Constraints**: *Maximum Length*: `10000` |
| `closed_date` | `str` | Optional | Opportunity closed date.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |
| `estimated_revenue_amount` | `float` | Optional | Estimated revenue amount for the merchant.<br><br>**Constraints**: `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "merchantName": "MANNA FARM AND GARDEN INC",
  "referringBanker": "Eric Kaveny",
  "branchName": "Downtown Branch",
  "closedDate": "2022-06-30",
  "estimatedRevenueAmount": 4520000.0
}
```

