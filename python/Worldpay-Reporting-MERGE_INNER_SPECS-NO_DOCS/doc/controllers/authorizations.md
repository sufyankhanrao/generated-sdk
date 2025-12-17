# Authorizations

```python
authorizations_controller = client.authorizations
```

## Class Name

`AuthorizationsController`

## Methods

* [Get Authorizations Summary](../../doc/controllers/authorizations.md#get-authorizations-summary)
* [Get Authorizations Summary by Card Network](../../doc/controllers/authorizations.md#get-authorizations-summary-by-card-network)
* [Get Authorizations Summary by Transaction Date](../../doc/controllers/authorizations.md#get-authorizations-summary-by-transaction-date)
* [Get Authorizations Summary by Merchant](../../doc/controllers/authorizations.md#get-authorizations-summary-by-merchant)
* [Get Authorizations Summary by Division](../../doc/controllers/authorizations.md#get-authorizations-summary-by-division)
* [Get Authorizations Summary by Store](../../doc/controllers/authorizations.md#get-authorizations-summary-by-store)
* [Get Authorizations Summary by Chain](../../doc/controllers/authorizations.md#get-authorizations-summary-by-chain)
* [Get Authorizations Summary by Super Chain](../../doc/controllers/authorizations.md#get-authorizations-summary-by-super-chain)


# Get Authorizations Summary

Resource to get total summary of authorizations for given hierarchy and date range with card type and card network being optional parameters. Refer to the  schema object for the allowed hierarchies and specifications.

```python
def get_authorizations_summary(self,
                              body,
                              v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AuthTransactionsRequest`](../../doc/models/auth-transactions-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SummaryResponses`](../../doc/models/summary-responses.md).

## Example Usage

```python
body = AuthTransactionsRequest(
    hierarchy=Entity1(
        level=Level1Enum.MERCHANT,
        values=[
            '4445000123456',
            '4345023507756'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2019-07-27',
        to_date='2019-09-12'
    )
)

result = authorizations_controller.get_authorizations_summary(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |


# Get Authorizations Summary by Card Network

Resource to get summary of authorizations grouped by card networks for given hierarchy and date range with card type and card network being optional parameters. Refer to the schema object for the allowed hierarchies and specifications.

```python
def get_authorizations_summary_by_card_network(self,
                                              v_correlation_id=None,
                                              body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |
| `body` | [`AuthTransactionsSummaryRequestByCardNetwork`](../../doc/models/auth-transactions-summary-request-by-card-network.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SummaryCardNetwork`](../../doc/models/summary-card-network.md).

## Example Usage

```python
body = AuthTransactionsSummaryRequestByCardNetwork(
    hierarchy=Entity1(
        level=Level1Enum.MERCHANT,
        values=[
            '4445000123456',
            '4345023507756'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2019-07-27',
        to_date='2019-09-12'
    ),
    pagination=PaginationType2(
        page_number=1,
        page_size=25
    )
)

result = authorizations_controller.get_authorizations_summary_by_card_network(
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


# Get Authorizations Summary by Transaction Date

Resource to get summary of authorizations grouped by transaction dates for given hierarchy and date range with card type and card network being optional parameters. Refer to the schema object for the allowed hierarchies and specifications.

```python
def get_authorizations_summary_by_transaction_date(self,
                                                  v_correlation_id=None,
                                                  body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |
| `body` | [`AuthTransactionsSummaryRequestByTransactionDate`](../../doc/models/auth-transactions-summary-request-by-transaction-date.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SummaryTransactionDate`](../../doc/models/summary-transaction-date.md).

## Example Usage

```python
body = AuthTransactionsSummaryRequestByTransactionDate(
    hierarchy=Entity1(
        level=Level1Enum.MERCHANT,
        values=[
            '4445000123456',
            '4345023507756'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2019-07-27',
        to_date='2019-09-12'
    )
)

result = authorizations_controller.get_authorizations_summary_by_transaction_date(
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


# Get Authorizations Summary by Merchant

Resource to get summary of authorizations for given parameters grouped by merchants for given hierarchy and date range with card type and card network being optional parameters. Refer to the schema object for the allowed hierarchies and specifications.

```python
def get_authorizations_summary_by_merchant(self,
                                          v_correlation_id=None,
                                          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |
| `body` | [`AuthTransactionsSummaryRequestByMerchant`](../../doc/models/auth-transactions-summary-request-by-merchant.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SummaryDetailMerchant`](../../doc/models/summary-detail-merchant.md).

## Example Usage

```python
body = AuthTransactionsSummaryRequestByMerchant(
    hierarchy=EntityMerchant(
        level=Level11Enum.MERCHANT,
        values=[
            '4445000123456',
            '4345023507756'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2019-07-27',
        to_date='2019-09-12'
    )
)

result = authorizations_controller.get_authorizations_summary_by_merchant(
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


# Get Authorizations Summary by Division

Resource to get summary of authorizations grouped by divisions for given hierarchy and date range with card type and card network being optional parameters. Refer to the schema object for the allowed hierarchies and specifications.

```python
def get_authorizations_summary_by_division(self,
                                          v_correlation_id=None,
                                          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |
| `body` | [`AuthTransactionsRequestByDivision`](../../doc/models/auth-transactions-request-by-division.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SummaryDetailDivision`](../../doc/models/summary-detail-division.md).

## Example Usage

```python
body = AuthTransactionsRequestByDivision(
    hierarchy=EntityParentTypeDivision(
        level=Level5Enum.CHAIN,
        values=[
            'OA1234',
            '1X0010'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2019-07-27',
        to_date='2019-09-12'
    )
)

result = authorizations_controller.get_authorizations_summary_by_division(
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


# Get Authorizations Summary by Store

Resource to get summary of authorizations grouped by stores for given hierarchy and date range with card type and card network being optional parameters. Refer to the schema object for the allowed hierarchies and specifications.

```python
def get_authorizations_summary_by_store(self,
                                       v_correlation_id=None,
                                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |
| `body` | [`AuthTransactionsRequestByStore`](../../doc/models/auth-transactions-request-by-store.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SummaryDetailStore`](../../doc/models/summary-detail-store.md).

## Example Usage

```python
body = AuthTransactionsRequestByStore(
    hierarchy=EntityParentTypeStore(
        level=Level3Enum.CHAIN,
        values=[
            'OA1234',
            '1X0010'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2019-07-27',
        to_date='2019-09-12'
    )
)

result = authorizations_controller.get_authorizations_summary_by_store(
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


# Get Authorizations Summary by Chain

Resource to get summary of authorizations grouped by chains for given hierarchy and date range with card type and card network being optional parameters. Refer to the schema object for the allowed hierarchies and specifications.

```python
def get_authorizations_summary_by_chain(self,
                                       v_correlation_id=None,
                                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |
| `body` | [`AuthTransactionsRequestByChain`](../../doc/models/auth-transactions-request-by-chain.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SummaryDetailChain`](../../doc/models/summary-detail-chain.md).

## Example Usage

```python
body = AuthTransactionsRequestByChain(
    hierarchy=EntityChain(
        level=Level2Enum.CHAIN,
        values=[
            'OA1234',
            '1X0010'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2019-07-27',
        to_date='2019-09-12'
    )
)

result = authorizations_controller.get_authorizations_summary_by_chain(
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


# Get Authorizations Summary by Super Chain

Resource to get summary of authorizations grouped by superchains for given hierarchy and date range with card type and card network being optional parameters. Refer to the schema object for the allowed hierarchies and specifications.

```python
def get_authorizations_summary_by_super_chain(self,
                                             v_correlation_id=None,
                                             body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |
| `body` | [`AuthTransactionsRequestBySuperChain`](../../doc/models/auth-transactions-request-by-super-chain.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SummaryDetailSuperChain`](../../doc/models/summary-detail-super-chain.md).

## Example Usage

```python
body = AuthTransactionsRequestBySuperChain(
    hierarchy=EntitySuperChain(
        level=Level4Enum.SUPERCHAIN,
        values=[
            'SCABCB6111',
            'SCABCB1777'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2019-07-27',
        to_date='2019-09-12'
    )
)

result = authorizations_controller.get_authorizations_summary_by_super_chain(
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

