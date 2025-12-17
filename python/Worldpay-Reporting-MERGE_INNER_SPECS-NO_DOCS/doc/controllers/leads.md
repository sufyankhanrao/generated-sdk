# Leads

```python
leads_controller = client.leads
```

## Class Name

`LeadsController`

## Methods

* [Post Leads Summary Month](../../doc/controllers/leads.md#post-leads-summary-month)
* [Post Leads Count Category](../../doc/controllers/leads.md#post-leads-count-category)
* [Post Leads Count Source](../../doc/controllers/leads.md#post-leads-count-source)
* [Post Leads Count Disqualified](../../doc/controllers/leads.md#post-leads-count-disqualified)
* [Post Leads Count Closed Lost](../../doc/controllers/leads.md#post-leads-count-closed-lost)


# Post Leads Summary Month

Retrieves leads summary for independent sales channel code(s) for selected month range.

```python
def post_leads_summary_month(self,
                            body,
                            v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LeadsSummaryMonthRequest`](../../doc/models/leads-summary-month-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`LeadsSummaryMonthResponse`](../../doc/models/leads-summary-month-response.md).

## Example Usage

```python
body = LeadsSummaryMonthRequest(
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

result = leads_controller.post_leads_summary_month(
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
  "totalLeadCount": 94145,
  "totalActionableLeadCount": 47329,
  "totalSignedDealCount": 5503,
  "totalSignedDealAverageAmount": 62.37,
  "totalSignedDealPercentage": 35.52,
  "totalActivatedAccounts": 3866,
  "summaries": [
    {
      "processMonth": "2021-04",
      "leadCount": 7300,
      "actionableLeadCount": 5000,
      "signedDealCount": 315,
      "signedDealAverageAmount": 579.0,
      "signedDealPercentage": 4.29,
      "activatedAccounts": 171
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError4Exception`](../../doc/models/error-response-error-4-exception.md) |


# Post Leads Count Category

Retrieves leads category and its counts for independent sales channel code(s) for selected month range.

```python
def post_leads_count_category(self,
                             body,
                             v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LeadsCountCategoryRequest`](../../doc/models/leads-count-category-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`LeadsCountCategoryResponse`](../../doc/models/leads-count-category-response.md).

## Example Usage

```python
body = LeadsCountCategoryRequest(
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

result = leads_controller.post_leads_count_category(
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
  "totalCount": 94145,
  "counts": [
    {
      "category": "IN_PROGRESS_LEADS",
      "count": 91446
    },
    {
      "category": "ACTIVATED",
      "count": 1916
    },
    {
      "category": "MERCHANT_NOT_INTERESTED",
      "count": 686
    },
    {
      "category": "APPROVED_BUT_NOT_ACTIVATED",
      "count": 68
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError4Exception`](../../doc/models/error-response-error-4-exception.md) |


# Post Leads Count Source

Retrieves leads counts and its source for independendent sales channel code(s) for selected month range lead source.

```python
def post_leads_count_source(self,
                           body,
                           v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LeadsCountSourceRequest`](../../doc/models/leads-count-source-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`LeadsCountSourceResponse`](../../doc/models/leads-count-source-response.md).

## Example Usage

```python
body = LeadsCountSourceRequest(
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

result = leads_controller.post_leads_count_source(
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
  "totalCount": 94145,
  "counts": [
    {
      "source": "List - Bank",
      "count": 82945
    },
    {
      "source": "Marketing",
      "count": 11200
    },
    {
      "source": "Referral - Bank",
      "count": 1120
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError4Exception`](../../doc/models/error-response-error-4-exception.md) |


# Post Leads Count Disqualified

Retrieves leads counts with its disqualification reason for independendent sales channel code(s) for selected month range.

```python
def post_leads_count_disqualified(self,
                                 body,
                                 v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LeadsCountDisqualifiedRequest`](../../doc/models/leads-count-disqualified-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`LeadsCountDisqualifiedResponse`](../../doc/models/leads-count-disqualified-response.md).

## Example Usage

```python
body = LeadsCountDisqualifiedRequest(
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

result = leads_controller.post_leads_count_disqualified(
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
  "totalCount": 94145,
  "counts": [
    {
      "disqualificationReason": "Invalid Contact Information",
      "count": 82945
    },
    {
      "disqualificationReason": "Out of Business",
      "count": 11200
    },
    {
      "disqualificationReason": "Unable to Contact",
      "count": 1120
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError4Exception`](../../doc/models/error-response-error-4-exception.md) |


# Post Leads Count Closed Lost

Retrieves leads count with its closed lost reason for independendent sales channel code(s) for selected month range.

```python
def post_leads_count_closed_lost(self,
                                body,
                                v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LeadsCountClosedlostreasonsRequest`](../../doc/models/leads-count-closedlostreasons-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`LeadsCountClosedLostReasonResponse`](../../doc/models/leads-count-closed-lost-reason-response.md).

## Example Usage

```python
body = LeadsCountClosedlostreasonsRequest(
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

result = leads_controller.post_leads_count_closed_lost(
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
  "totalCount": 94145,
  "counts": [
    {
      "disqualificationReason": "Change in customer priorities / circumstances",
      "count": 82945
    },
    {
      "disqualificationReason": "Disqualified opportunity",
      "count": 11200
    },
    {
      "disqualificationReason": "Solution fit to Customer's needs",
      "count": 1120
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError4Exception`](../../doc/models/error-response-error-4-exception.md) |

