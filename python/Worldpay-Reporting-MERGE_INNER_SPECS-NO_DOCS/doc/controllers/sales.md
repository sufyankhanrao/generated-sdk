# Sales

```python
sales_controller = client.sales
```

## Class Name

`SalesController`


# Post Sales Summary Month

Retrieves sales summary for independendent sales channel code(s) for selected month range.

```python
def post_sales_summary_month(self,
                            body,
                            v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SalesSummaryMonthRequest`](../../doc/models/sales-summary-month-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SalesSummaryMonthResponse`](../../doc/models/sales-summary-month-response.md).

## Example Usage

```python
body = SalesSummaryMonthRequest(
    independent_sales_channel_codes=[
        'MTBCON',
        'MTBNEW'
    ],
    month_range=MonthRange1(
        start_month='2022-01',
        end_month='2022-06'
    )
)

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

result = sales_controller.post_sales_summary_month(
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
| Default | Default errors | [`ErrorResponseError4Exception`](../../doc/models/error-response-error-4-exception.md) |

