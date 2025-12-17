# Signed Deals

```python
signed_deals_controller = client.signed_deals
```

## Class Name

`SignedDealsController`

## Methods

* [Post Signed Deals Summary Month](../../doc/controllers/signed-deals.md#post-signed-deals-summary-month)
* [Postsignedmerchantsummary](../../doc/controllers/signed-deals.md#postsignedmerchantsummary)


# Post Signed Deals Summary Month

Retrieves signed deals summary for independendent sales channel code(s) for selected month range.

```python
def post_signed_deals_summary_month(self,
                                   body,
                                   v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SignedDealsSummaryMonthRequest`](../../doc/models/signed-deals-summary-month-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SignedDealsSummaryMonthResponse`](../../doc/models/signed-deals-summary-month-response.md).

## Example Usage

```python
body = SignedDealsSummaryMonthRequest(
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

result = signed_deals_controller.post_signed_deals_summary_month(
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
  "totalSignedDealCount": 368,
  "totalEstimatedAnnualRevenueAmount": 90546.0,
  "totalEstimatedAnnualVolumeAmount": 10001560.0,
  "signedDealRatio": 9.8,
  "summaries": [
    {
      "processMonth": "2021-01",
      "signedDealCount": 168,
      "signedDealRatio": 6.7,
      "estimatedAnnualRevenueAmount": 5492.0,
      "estimatedAnnualVolumeAmount": 60000.0
    },
    {
      "processMonth": "2021-02",
      "signedDealCount": 268,
      "signedDealRatio": 3.1,
      "estimatedAnnualRevenueAmount": 5495.0,
      "estimatedAnnualVolumeAmount": 80000.0
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError4Exception`](../../doc/models/error-response-error-4-exception.md) |


# Postsignedmerchantsummary

Retrieves signed deals summary for merchant

```python
def postsignedmerchantsummary(self,
                             body,
                             v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SignedDealsSummaryMerchantRequest`](../../doc/models/signed-deals-summary-merchant-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SignedDealsSummaryMerchantResponse`](../../doc/models/signed-deals-summary-merchant-response.md).

## Example Usage

```python
body = SignedDealsSummaryMerchantRequest(
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

result = signed_deals_controller.postsignedmerchantsummary(
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
  "totalSignedMerchantCount": 3,
  "totalEstimatedAnnualRevenueAmount": 90265.0,
  "totalEstimatedAnnualVolumeAmount": 15000.0,
  "signedDealRatio": 12.5,
  "summaries": [
    {
      "merchantName": "CRISP AND NUTS",
      "branchName": "NH445 | Hampton Falls",
      "estimatedAnnualRevenueAmount": 43419.0,
      "estimatedAnnualVolumeAmount": 6000.0
    },
    {
      "merchantName": "MANNA FARM AND GARDEN INC",
      "branchName": "NH45 | NEPTUNE FORT",
      "estimatedAnnualRevenueAmount": 24923.0,
      "estimatedAnnualVolumeAmount": 5000.0
    },
    {
      "merchantName": "VICTOR PHARMACY",
      "branchName": "GH45 | HADDOWS ROAD",
      "estimatedAnnualRevenueAmount": 21923.0,
      "estimatedAnnualVolumeAmount": 4000.0
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError4Exception`](../../doc/models/error-response-error-4-exception.md) |

