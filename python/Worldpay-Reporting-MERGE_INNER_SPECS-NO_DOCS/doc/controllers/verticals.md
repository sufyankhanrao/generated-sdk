# Verticals

```python
verticals_controller = client.verticals
```

## Class Name

`VerticalsController`


# Retrieve Summary by Verticals

Resource is used to get settled transactions summary for respective independent sales channel and months and group by verticals.

```python
def retrieve_summary_by_verticals(self,
                                 body,
                                 v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`VerticalsRequest`](../../doc/models/verticals-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | A unique identifier value attached to a request |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SummaryByVerticals`](../../doc/models/summary-by-verticals.md).

## Example Usage

```python
body = VerticalsRequest(
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

result = verticals_controller.retrieve_summary_by_verticals(
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
      "numberOfChains": 6500,
      "numberOfMerchants": 5500,
      "grossRevenue": 500.87,
      "processRevenue": 200.09,
      "settledTransactionAmount": 6579.98,
      "settledTransactionCount": 500,
      "settledAverageTicket": 23.87,
      "totalEffectiveRate": 4.67
    },
    {
      "vertical": "DRUG_STORES",
      "processMonth": "2017-06",
      "numberOfChains": 6503,
      "numberOfMerchants": 5510,
      "grossRevenue": 607.12,
      "processRevenue": 223.19,
      "settledTransactionAmount": 5679.88,
      "settledTransactionCount": 390,
      "settledAverageTicket": 33.27,
      "totalEffectiveRate": 2.89
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError3Exception`](../../doc/models/error-response-error-3-exception.md) |

