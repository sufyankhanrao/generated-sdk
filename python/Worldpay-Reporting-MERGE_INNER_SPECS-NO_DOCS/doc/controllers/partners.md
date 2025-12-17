# Partners

```python
partners_controller = client.partners
```

## Class Name

`PartnersController`

## Methods

* [Search Partners Summary](../../doc/controllers/partners.md#search-partners-summary)
* [Search Partners Summary by Cardnetworks](../../doc/controllers/partners.md#search-partners-summary-by-cardnetworks)
* [Search Partners Summary by Verticals](../../doc/controllers/partners.md#search-partners-summary-by-verticals)


# Search Partners Summary

Resource is used to get settled transactions summary for respective independent sales channel and months and group by partners.

```python
def search_partners_summary(self,
                           body,
                           v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PartnersRequest`](../../doc/models/partners-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | A unique identifier value attached to a request |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PartnersSummaryResponse`](../../doc/models/partners-summary-response.md).

## Example Usage

```python
body = PartnersRequest(
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

result = partners_controller.search_partners_summary(
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
  "totalGrossRevenue": 775.65,
  "totalProcessRevenue": 587.93,
  "totalSettledAmount": 1083.69,
  "totalSettledCount": 57,
  "summaries": [
    {
      "processMonth": "2017-06",
      "grossRevenue": 433.09,
      "processRevenue": 333.15,
      "settledAmount": 719.02,
      "settledCount": 34,
      "settledAverageTicket": 23.87,
      "totalEffectiveRate": 4.67
    },
    {
      "processMonth": "2017-07",
      "grossRevenue": 342.56,
      "processRevenue": 254.78,
      "settledAmount": 364.67,
      "settledCount": 23,
      "settledAverageTicket": 33.87,
      "totalEffectiveRate": 5.67
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError3Exception`](../../doc/models/error-response-error-3-exception.md) |


# Search Partners Summary by Cardnetworks

Resource is used to get settled transactions summary for respective independent sales channel and months and group by partners and card networks.

```python
def search_partners_summary_by_cardnetworks(self,
                                           body,
                                           v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PartnersCardNetworkRequest`](../../doc/models/partners-card-network-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | A unique identifier value attached to a request |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CardNetworkResponse`](../../doc/models/card-network-response.md).

## Example Usage

```python
body = PartnersCardNetworkRequest(
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

result = partners_controller.search_partners_summary_by_cardnetworks(
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
  "totalGrossRevenue": 745.96,
  "totalProcessRevenue": 533.24,
  "totalSettledAmount": 1299,
  "totalSettledCount": 840,
  "summaries": [
    {
      "cardNetwork": "VISA",
      "grossRevenue": 433.09,
      "processRevenue": 333.15,
      "settledAmount": 719.02,
      "settledCount": 340
    },
    {
      "cardNetwork": "MASTERCARD",
      "grossRevenue": 312.87,
      "processRevenue": 200.09,
      "settledAmount": 579.98,
      "settledCount": 500
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError3Exception`](../../doc/models/error-response-error-3-exception.md) |


# Search Partners Summary by Verticals

Resource is used to get settled transactions summary for respective independent sales channel and months and group by partners and verticals.

```python
def search_partners_summary_by_verticals(self,
                                        body,
                                        v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PartnersVerticalsRequest`](../../doc/models/partners-verticals-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | A unique identifier value attached to a request |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`VerticalsResponse`](../../doc/models/verticals-response.md).

## Example Usage

```python
body = PartnersVerticalsRequest(
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

result = partners_controller.search_partners_summary_by_verticals(
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
  "totalGrossRevenue": 745.96,
  "totalProcessRevenue": 533.24,
  "totalSettledAmount": 1299,
  "totalSettledCount": 840,
  "summaries": [
    {
      "vertical": "B2B",
      "grossRevenue": 433.09,
      "processRevenue": 333.15,
      "settledAmount": 719.02,
      "settledCount": 340
    },
    {
      "vertical": "Drugs",
      "grossRevenue": 312.87,
      "processRevenue": 200.09,
      "settledAmount": 579.98,
      "settledCount": 500
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError3Exception`](../../doc/models/error-response-error-3-exception.md) |

