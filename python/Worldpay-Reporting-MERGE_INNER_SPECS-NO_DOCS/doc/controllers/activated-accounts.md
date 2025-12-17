# Activated Accounts

```python
activated_accounts_controller = client.activated_accounts
```

## Class Name

`ActivatedAccountsController`


# Post Activated Accounts Summary Month

Retrieves activated accounts summary for independendent sales channel code(s) for selected month range.

```python
def post_activated_accounts_summary_month(self,
                                         body,
                                         v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ActivationsSummaryMonthRequest`](../../doc/models/activations-summary-month-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ActivationsSummaryMonthResponse`](../../doc/models/activations-summary-month-response.md).

## Example Usage

```python
body = ActivationsSummaryMonthRequest(
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

result = activated_accounts_controller.post_activated_accounts_summary_month(
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
  "totalActivatedAccounts": 3866,
  "totalActivationPercentage": 89.3,
  "averageDaysToActivate": 51.0,
  "summaries": [
    {
      "processMonth": "2021-02",
      "activatedAccounts": 134,
      "activationPercentage": 28.75,
      "averageDaysToActivate": 31.0
    },
    {
      "processMonth": "2021-03",
      "activatedAccounts": 224,
      "activationPercentage": 60.55,
      "averageDaysToActivate": 20.0
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError4Exception`](../../doc/models/error-response-error-4-exception.md) |

