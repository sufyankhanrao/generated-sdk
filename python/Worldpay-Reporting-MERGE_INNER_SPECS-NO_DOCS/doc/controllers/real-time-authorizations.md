# Real Time Authorizations

```python
real_time_authorizations_controller = client.real_time_authorizations
```

## Class Name

`RealTimeAuthorizationsController`

## Methods

* [Search Real Authorizations](../../doc/controllers/real-time-authorizations.md#search-real-authorizations)
* [Retrieve Real Time Transaction Detals by Credit Transaction Id](../../doc/controllers/real-time-authorizations.md#retrieve-real-time-transaction-detals-by-credit-transaction-id)
* [Retrieve Real Time Transaction Detals by Debit Transaction Id](../../doc/controllers/real-time-authorizations.md#retrieve-real-time-transaction-detals-by-debit-transaction-id)
* [Retrieve Real Time Transaction Detals by Gift Transaction Id](../../doc/controllers/real-time-authorizations.md#retrieve-real-time-transaction-detals-by-gift-transaction-id)


# Search Real Authorizations

Endpoint is used to retrieve the authorized transaction (approved or declined) details for a given hierarchy and date range. It provides the real time (current date) transaction details. It helps the user to perform a search based on optional fields.

:information_source: **Note** This endpoint does not require authentication.

```python
def search_real_authorizations(self,
                              body,
                              v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SearchAuthRealTransactionsRequest`](../../doc/models/search-auth-real-transactions-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SearchAuthRealTimeTransactionsResponse`](../../doc/models/search-auth-real-time-transactions-response.md).

## Example Usage

```python
body = SearchAuthRealTransactionsRequest(
    hierarchy=Entity(
        level=LevelEnum.INDEPENDENT_SALES_ORGANIZATION,
        values=[
            '4445000860700',
            '4445000860702'
        ],
        chain_code='OA1234'
    ),
    transaction_date_range=SearchAuthTransactionsRequestRealTimeTransactionDateRange(
        from_date='2021-12-01',
        to_date='2021-12-01'
    ),
    authorization_code='73994M',
    card_type=CardTypeEnum.CREDIT,
    card_number='************4353',
    token='374245111181117',
    transaction_type=TransactionTypeEnum.GA,
    transaction_status=TransactionStatusEnum.AA,
    fraud_response_code=FraudResponseCodeEnum.FRAUD_SYSTEM_APPROVED,
    fraud_rule_result=FraudRuleResultEnum.MANUAL_REVIEW
)

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

result = real_time_authorizations_controller.search_real_authorizations(
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
| Default | Default errors | [`ErrorException`](../../doc/models/error-exception.md) |


# Retrieve Real Time Transaction Detals by Credit Transaction Id

Retrieves individual credit transaction details for supplied transaction id.

```python
def retrieve_real_time_transaction_detals_by_credit_transaction_id(self,
                                                                  transaction_id,
                                                                  v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `str` | Template, Required | Transaction id is a unique identifier generated for every card transaction for tracking purposes. (12-18 digits)<br><br>**Constraints**: *Maximum Length*: `18` |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CreditTransactionDetailsResponse`](../../doc/models/credit-transaction-details-response.md).

## Example Usage

```python
transaction_id = '141710009519'

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

result = real_time_authorizations_controller.retrieve_real_time_transaction_detals_by_credit_transaction_id(
    transaction_id,
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
| Default | Default errors | [`ErrorException`](../../doc/models/error-exception.md) |


# Retrieve Real Time Transaction Detals by Debit Transaction Id

Retrieves individual debit transaction details  for supplied transaction id.

```python
def retrieve_real_time_transaction_detals_by_debit_transaction_id(self,
                                                                 transaction_id,
                                                                 v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `str` | Template, Required | Transaction id is a unique identifier generated for every card transaction for tracking purposes. (12-18 digits)<br><br>**Constraints**: *Maximum Length*: `18` |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DebitTransactionDetailsResponse`](../../doc/models/debit-transaction-details-response.md).

## Example Usage

```python
transaction_id = '141710009519'

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

result = real_time_authorizations_controller.retrieve_real_time_transaction_detals_by_debit_transaction_id(
    transaction_id,
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
| Default | Default errors | [`ErrorException`](../../doc/models/error-exception.md) |


# Retrieve Real Time Transaction Detals by Gift Transaction Id

Retrieves individual gift transaction details  for supplied transaction id.

```python
def retrieve_real_time_transaction_detals_by_gift_transaction_id(self,
                                                                transaction_id,
                                                                v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `str` | Template, Required | Transaction id is a unique identifier generated for every card transaction for tracking purposes. (12-18 digits)<br><br>**Constraints**: *Maximum Length*: `18` |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GiftRealTransactionDetailsResponse`](../../doc/models/gift-real-transaction-details-response.md).

## Example Usage

```python
transaction_id = '141710009519'

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

result = real_time_authorizations_controller.retrieve_real_time_transaction_detals_by_gift_transaction_id(
    transaction_id,
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
| Default | Default errors | [`ErrorException`](../../doc/models/error-exception.md) |

