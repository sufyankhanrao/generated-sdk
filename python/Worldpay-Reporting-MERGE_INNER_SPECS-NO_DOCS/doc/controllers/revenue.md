# Revenue

```python
revenue_controller = client.revenue
```

## Class Name

`RevenueController`

## Methods

* [Search Summary by Parties](../../doc/controllers/revenue.md#search-summary-by-parties)
* [Search Summary by Verticals](../../doc/controllers/revenue.md#search-summary-by-verticals)
* [Search Summary by Value Added Services](../../doc/controllers/revenue.md#search-summary-by-value-added-services)


# Search Summary by Parties

Amount (USD) to be receive per transaction. Revenue Endpoints provides drill down details contributing to gross revenue and settled volume. It  provides trend of revenue by considering effective rate, revenue earned per transaction and VAS (Value Added Services) for chains that falls under ISCs aligned with the partners.

```python
def search_summary_by_parties(self,
                             body,
                             v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`RevenueByPartyRequest`](../../doc/models/revenue-by-party-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | A unique identifier value attached to a request |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[SummariesInner]`](../../doc/models/summaries-inner.md).

## Example Usage

```python
body = RevenueByPartyRequest(
    independent_sales_channel_codes=[
        'MTBCON',
        'MTBNEW'
    ],
    month_range=MonthRange(
        start_month='2022-01',
        end_month='2022-06'
    )
)

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

result = revenue_controller.search_summary_by_parties(
    body,
    v_correlation_id=v_correlation_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError3Exception`](../../doc/models/error-response-error-3-exception.md) |


# Search Summary by Verticals

Resource is used to get total effective rate and total processing rate by verticals. Revenue Endpoints provides drill down details contributing to gross revenue and settled volume. It  provides trend of revenue by considering effective rate, revenue earned per transaction and VAS (Value Added Services) for chains that falls under ISCs aligned with the partners.

```python
def search_summary_by_verticals(self,
                               body,
                               v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`RevenueByVerticalsRequest`](../../doc/models/revenue-by-verticals-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | A unique identifier value attached to a request |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SummaryVerticals`](../../doc/models/summary-verticals.md).

## Example Usage

```python
body = RevenueByVerticalsRequest(
    independent_sales_channel_codes=[
        'MTBCON',
        'MTBNEW'
    ],
    month_range=MonthRange(
        start_month='2022-01',
        end_month='2022-06'
    )
)

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

result = revenue_controller.search_summary_by_verticals(
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
  "summaries": [
    {
      "vertical": "B2B",
      "processMonth": "2017-06",
      "totalProcessingRate": 5.54,
      "totalEffectiveRate": 1.57
    },
    {
      "vertical": "DRUG_STORES",
      "processMonth": "2017-06",
      "totalProcessingRate": 6.23,
      "totalEffectiveRate": 2.03
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError3Exception`](../../doc/models/error-response-error-3-exception.md) |


# Search Summary by Value Added Services

Resource is used to get revenue summary by value added services. Revenue Endpoints provides drill down details contributing to gross revenue and settled volume. It  provides trend of revenue by considering effective rate, revenue earned per transaction and VAS (Value Added Services) for chains that falls under ISCs aligned with the partners.

```python
def search_summary_by_value_added_services(self,
                                          body,
                                          v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`RevenueVASRequest`](../../doc/models/revenue-vas-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | A unique identifier value attached to a request |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`VASSubscriptionsByGrossRevenue`](../../doc/models/vas-subscriptions-by-gross-revenue.md).

## Example Usage

```python
body = RevenueVASRequest(
    independent_sales_channel_codes=[
        'MTBCON',
        'MTBNEW'
    ],
    month_range=MonthRange(
        start_month='2022-01',
        end_month='2022-06'
    )
)

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

result = revenue_controller.search_summary_by_value_added_services(
    body,
    v_correlation_id=v_correlation_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError3Exception`](../../doc/models/error-response-error-3-exception.md) |

