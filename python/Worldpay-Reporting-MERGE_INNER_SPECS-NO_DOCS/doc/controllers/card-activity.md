# Card Activity

```python
card_activity_controller = client.card_activity
```

## Class Name

`CardActivityController`

## Methods

* [Getsettlementssummarybycardnetworks](../../doc/controllers/card-activity.md#getsettlementssummarybycardnetworks)
* [Getcardactivitysummarybydebit](../../doc/controllers/card-activity.md#getcardactivitysummarybydebit)
* [Getcardactivitysummarybygift](../../doc/controllers/card-activity.md#getcardactivitysummarybygift)


# Getsettlementssummarybycardnetworks

Endpoint is used to get the summaries for different card networks for the respective card numbers. Optional fields are used to filter the search criteria.

```python
def getsettlementssummarybycardnetworks(self,
                                       v_correlation_id=None,
                                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |
| `body` | [`CreditCardActivitySummaryRequest`](../../doc/models/credit-card-activity-summary-request.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CreditActivitySummaryResponse`](../../doc/models/credit-activity-summary-response.md).

## Example Usage

```python
body = CreditCardActivitySummaryRequest(
    hierarchy=Hierarchy(
        level=Level12Enum.CHAIN,
        values=[
            'AB1234',
            '111217'
        ]
    ),
    card_network=CardNetwork2Enum.MASTERCARD,
    card_number='634527',
    date_range=SearchAuthTransactionsRequestRealTimeTransactionDateRange(
        from_date='2019-07-27',
        to_date='2019-09-13'
    )
)

result = card_activity_controller.getsettlementssummarybycardnetworks(
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "authorizationActivity": {
    "authorizationCount": 335594,
    "authorizationAmount": 12349.62,
    "approvedCount": 6357,
    "approvedAmount": 5374.65,
    "declinedCount": 7564,
    "declinedAmount": 4583.56,
    "merchantSurchargeCount": 32,
    "merchantSurchargeAmount": 327.97
  },
  "settlementActivity": {
    "settledCount": 84532,
    "settledAmount": 93657.54,
    "salesCount": 9673,
    "salesAmount": 93657.54,
    "returnsCount": 4356,
    "returnsAmount": 43848.87,
    "merchantSurchargeCount": 22,
    "merchantSurchargeAmount": 345.65
  },
  "disputeActivity": {
    "retrievalsCount": 7453,
    "retrievalsAmount": 7543725.34,
    "chargebacksCount": 38465,
    "chargebacksAmount": 933748.56
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |


# Getcardactivitysummarybydebit

Endpoint is used to get the summaries for different card networks for the respective card numbers. Optional fields are used to filter the search criteria.

```python
def getcardactivitysummarybydebit(self,
                                 v_correlation_id=None,
                                 body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |
| `body` | [`DebitCardActivitySummaryRequest`](../../doc/models/debit-card-activity-summary-request.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DebitActivitySummaryResponse`](../../doc/models/debit-activity-summary-response.md).

## Example Usage

```python
v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

body = DebitCardActivitySummaryRequest(
    hierarchy=Hierarchy(
        level=Level12Enum.MERCHANT,
        values=[
            '4445000123456',
            '4445191034215'
        ],
        chain_code='AB1234'
    ),
    card_network=DebitCardNetworkEnum.WIC,
    card_number='************4353',
    date_range=SearchAuthTransactionsRequestRealTimeTransactionDateRange(
        from_date='2021-12-01',
        to_date='2021-12-01'
    )
)

result = card_activity_controller.getcardactivitysummarybydebit(
    v_correlation_id=v_correlation_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "authorizationActivity": {
    "approvedCount": 6357,
    "approvedAmount": 5374.65,
    "declinedCount": 7564,
    "declinedAmount": 4583.56
  },
  "settlementActivity": {
    "settledCount": 84532,
    "settledAmount": 93657.54
  },
  "otherActivity": {
    "reversedCount": 453,
    "reversedAmount": 756.98,
    "inquiryCount": 78,
    "inquiryAmount": 675.34
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |


# Getcardactivitysummarybygift

Endpoint is used to get the summaries for different card networks for the respective card numbers. Optional fields are used to filter the search criteria.

```python
def getcardactivitysummarybygift(self,
                                v_correlation_id=None,
                                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |
| `body` | [`GiftCardActivitySummaryRequest`](../../doc/models/gift-card-activity-summary-request.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GiftActivitySummaryResponse`](../../doc/models/gift-activity-summary-response.md).

## Example Usage

```python
v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

body = GiftCardActivitySummaryRequest(
    hierarchy=Hierarchy(
        level=Level12Enum.MERCHANT,
        values=[
            '4445000123456',
            '4445191034215'
        ],
        chain_code='AB1234'
    ),
    card_network=GiftCardNetworkEnum.GIFT,
    card_number='************4353',
    date_range=SearchAuthTransactionsRequestRealTimeTransactionDateRange(
        from_date='2021-12-01',
        to_date='2021-12-01'
    )
)

result = card_activity_controller.getcardactivitysummarybygift(
    v_correlation_id=v_correlation_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |

