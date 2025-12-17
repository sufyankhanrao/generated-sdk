# Non-Real Time Authorizations

```python
non_real_time_authorizations_controller = client.non_real_time_authorizations
```

## Class Name

`NonRealTimeAuthorizationsController`

## Methods

* [Search Authorizations](../../doc/controllers/non-real-time-authorizations.md#search-authorizations)
* [Retrieve Transaction Detals by Credit Transaction Id](../../doc/controllers/non-real-time-authorizations.md#retrieve-transaction-detals-by-credit-transaction-id)
* [Retrieve Transaction Detals by Debit Transaction Id](../../doc/controllers/non-real-time-authorizations.md#retrieve-transaction-detals-by-debit-transaction-id)
* [Retrieve Transaction Detals by Gift Transaction Id](../../doc/controllers/non-real-time-authorizations.md#retrieve-transaction-detals-by-gift-transaction-id)


# Search Authorizations

Endpoint is used to retrieve the authorized transaction (approved or declined) details for a given hierarchy and date range. It provides the non-real time (till previous date) transaction details. It helps the user to perform a search based on optional fields.

```python
def search_authorizations(self,
                         body,
                         v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SearchAuthNonRealTransactionsRequest`](../../doc/models/search-auth-non-real-transactions-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SearchAuthTransactionsResponse`](../../doc/models/search-auth-transactions-response.md).

## Example Usage

```python
body = SearchAuthNonRealTransactionsRequest(
    hierarchy=Entity(
        level=LevelEnum.INDEPENDENT_SALES_ORGANIZATION,
        values=[
            '4445000860700',
            '4445000860702'
        ],
        chain_code='OA1234'
    ),
    date_range=SearchAuthTransactionsRequestTransactionDateRange(
        from_date='2021-12-01',
        to_date='2022-01-01'
    ),
    authorization_code='73994M',
    token='374245111181117',
    transaction_type_code=TransactionTypeCodeEnum.GA,
    transaction_status_code=TransactionStatusCodeEnum.AA,
    reference_number='2444600338440029'
)

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

result = non_real_time_authorizations_controller.search_authorizations(
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


# Retrieve Transaction Detals by Credit Transaction Id

Retrieves individual credit transaction details for supplied transaction id.

```python
def retrieve_transaction_detals_by_credit_transaction_id(self,
                                                        transaction_id,
                                                        v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `str` | Template, Required | Transaction id is a unique identifier generated for every card transaction for tracking purposes. (12-18 digits)<br><br>**Constraints**: *Maximum Length*: `18` |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`NonRealCreditTransactionDetailsResponse`](../../doc/models/non-real-credit-transaction-details-response.md).

## Example Usage

```python
transaction_id = '141710009519'

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

result = non_real_time_authorizations_controller.retrieve_transaction_detals_by_credit_transaction_id(
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


# Retrieve Transaction Detals by Debit Transaction Id

Retrieves individual debit transaction details for supplied transaction id.

```python
def retrieve_transaction_detals_by_debit_transaction_id(self,
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

result = non_real_time_authorizations_controller.retrieve_transaction_detals_by_debit_transaction_id(
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


# Retrieve Transaction Detals by Gift Transaction Id

Retrieves individual gift transaction details for supplied transaction id.

```python
def retrieve_transaction_detals_by_gift_transaction_id(self,
                                                      transaction_id,
                                                      v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `str` | Template, Required | Transaction id is a unique identifier generated for every card transaction for tracking purposes. (12-18 digits)<br><br>**Constraints**: *Maximum Length*: `18` |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GiftTransactionDetailsResponse`](../../doc/models/gift-transaction-details-response.md).

## Example Usage

```python
transaction_id = '141710009519'

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

result = non_real_time_authorizations_controller.retrieve_transaction_detals_by_gift_transaction_id(
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

