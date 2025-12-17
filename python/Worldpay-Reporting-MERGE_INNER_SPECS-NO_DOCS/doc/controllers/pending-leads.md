# Pending Leads

```python
pending_leads_controller = client.pending_leads
```

## Class Name

`PendingLeadsController`


# Post Pending Leads Summary Merchant

Retrieves pending leads summary for merchants.

```python
def post_pending_leads_summary_merchant(self,
                                       body,
                                       v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PendingLeadsSummaryMerchantRequest`](../../doc/models/pending-leads-summary-merchant-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PendingLeadsSummaryMerchantResponse`](../../doc/models/pending-leads-summary-merchant-response.md).

## Example Usage

```python
body = PendingLeadsSummaryMerchantRequest(
    independent_sales_channel_codes=[
        'MTBCON',
        'MTBNEW'
    ],
    month_range=MonthRange1(
        start_month='2022-01',
        end_month='2022-06'
    )
)

v_correlation_id = '3fcb1437-4e52-4946-9ae1-e618351b6d16'

result = pending_leads_controller.post_pending_leads_summary_merchant(
    body,
    v_correlation_id=v_correlation_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "totalEstimatedRevenueAmount": 1564263.0,
  "totalMerchantCount": 125,
  "totalLeadCount": 125,
  "summaries": [
    {
      "merchantName": "MANNA FARM AND GARDEN INC",
      "referringBanker": "Eric Kaveny",
      "branchName": "Downtown Branch",
      "closedDate": "2022-03-01",
      "estimatedRevenueAmount": 4520000.0
    },
    {
      "merchantName": "CVS Payflex - Prepaid Card Pro",
      "referringBanker": "Samuel Merkle",
      "branchName": "City Center Branch",
      "closedDate": "2022-04-01",
      "estimatedRevenueAmount": 1290000.0
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError4Exception`](../../doc/models/error-response-error-4-exception.md) |

