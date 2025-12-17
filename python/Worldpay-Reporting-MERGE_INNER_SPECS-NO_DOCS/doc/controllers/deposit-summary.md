# Deposit Summary

```python
deposit_summary_controller = client.deposit_summary
```

## Class Name

`DepositSummaryController`

## Methods

* [Summary](../../doc/controllers/deposit-summary.md#summary)
* [Summary by Date](../../doc/controllers/deposit-summary.md#summary-by-date)
* [Summary by Settlement Type](../../doc/controllers/deposit-summary.md#summary-by-settlement-type)
* [Summary by Account Number](../../doc/controllers/deposit-summary.md#summary-by-account-number)
* [Summary by Merchant](../../doc/controllers/deposit-summary.md#summary-by-merchant)
* [Summary by Store](../../doc/controllers/deposit-summary.md#summary-by-store)
* [Summary by Division](../../doc/controllers/deposit-summary.md#summary-by-division)
* [Summary by Chain](../../doc/controllers/deposit-summary.md#summary-by-chain)
* [Summary by Super Chain](../../doc/controllers/deposit-summary.md#summary-by-super-chain)


# Summary

Resource to get total summary of deposits for given hierarchy and date range. Refer to the  schema object for the allowed hierarchies and specifications.

```python
def summary(self,
           body,
           v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SummaryRequest`](../../doc/models/summary-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SummaryResponses1`](../../doc/models/summary-responses-1.md).

## Example Usage

```python
body = SummaryRequest(
    hierarchy=Entity3(
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

result = deposit_summary_controller.summary(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "totalCreditsCount": 7346,
  "totalCreditedAmount": 2353785.11,
  "totalDebitsCount": 3574,
  "totalDebitedAmount": 84464.28,
  "totalNetAmount": 2269320.83
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |


# Summary by Date

Resource to get summary of deposits grouped by dates for given hierarchy and date range. Refer to the schema object for the allowed hierarchies and specifications.

```python
def summary_by_date(self,
                   body,
                   v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DepositSummaryRequest`](../../doc/models/deposit-summary-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DepositSummaryByDate`](../../doc/models/deposit-summary-by-date.md).

## Example Usage

```python
body = DepositSummaryRequest(
    hierarchy=Entity3(
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
    pagination=PaginationType1(
        page_number=1,
        page_size=25
    )
)

result = deposit_summary_controller.summary_by_date(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "pagination": {
    "pageNumber": 1,
    "pageSize": 25,
    "totalRowCount": 85,
    "totalReturnedCount": 25
  },
  "totalCreditsCount": 25,
  "totalCreditedAmount": 257.35,
  "totalDebitsCount": 20,
  "totalDebitedAmount": 36.43,
  "totalNetAmount": 220.92,
  "summaries": [
    {
      "creditsCount": 10,
      "creditedAmount": 120.34,
      "debitsCount": 9,
      "debitedAmount": 20.56,
      "netAmount": 99.78,
      "date": "2019-07-27"
    },
    {
      "creditsCount": 15,
      "creditedAmount": 137.01,
      "debitsCount": 11,
      "debitedAmount": 15.87,
      "netAmount": 121.14,
      "date": "2019-07-28"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |


# Summary by Settlement Type

Resource to get summary of deposits grouped by settlement types for given hierarchy and date range with settlement type being an optional parameters. Refer to the schema object for the allowed hierarchies and specifications.

```python
def summary_by_settlement_type(self,
                              body,
                              v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DepositSettlementSummaryRequest`](../../doc/models/deposit-settlement-summary-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SummarySettlementType`](../../doc/models/summary-settlement-type.md).

## Example Usage

```python
body = DepositSettlementSummaryRequest(
    hierarchy=Entity3(
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
    pagination=PaginationType1(
        page_number=1,
        page_size=25
    )
)

result = deposit_summary_controller.summary_by_settlement_type(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "pagination": {
    "pageNumber": 1,
    "pageSize": 25,
    "totalRowCount": 85,
    "totalReturnedCount": 25
  },
  "totalCreditsCount": 25,
  "totalCreditedAmount": 257.35,
  "totalDebitsCount": 20,
  "totalDebitedAmount": 36.43,
  "totalNetAmount": 220.92,
  "summaries": [
    {
      "creditsCount": 10,
      "creditedAmount": 120.34,
      "debitsCount": 9,
      "debitedAmount": 20.56,
      "netAmount": 99.78,
      "code": "F",
      "description": "FEES"
    },
    {
      "creditsCount": 15,
      "creditedAmount": 137.01,
      "debitsCount": 11,
      "debitedAmount": 15.87,
      "netAmount": 121.14,
      "code": "D",
      "description": "DEPOSIT"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |


# Summary by Account Number

Resource to get summary of deposits grouped by account number for given hierarchy and date range with account number being an optional parameters. Refer to the schema object for the allowed hierarchies and specifications.

```python
def summary_by_account_number(self,
                             body,
                             v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DepositAccountNumberRequest`](../../doc/models/deposit-account-number-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SummaryAccountNumber`](../../doc/models/summary-account-number.md).

## Example Usage

```python
body = DepositAccountNumberRequest(
    hierarchy=Entity3(
        level=Level1Enum.CHAIN,
        values=[
            'AB1234'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2021-02-18',
        to_date='2021-02-18'
    )
)

result = deposit_summary_controller.summary_by_account_number(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "pagination": {
    "pageNumber": 1,
    "pageSize": 25,
    "totalRowCount": 1,
    "totalReturnedCount": 1
  },
  "totalCreditsCount": 22,
  "totalCreditedAmount": 5524735.1,
  "totalDebitsCount": 0,
  "totalDebitedAmount": 0,
  "totalNetAmount": 5524735.1,
  "summaries": [
    {
      "creditsCount": 12,
      "creditedAmount": 5524734.1,
      "debitsCount": 0,
      "debitedAmount": 0,
      "netAmount": 5524734.1,
      "accountNumber": "******1811",
      "accountType": "ACH"
    },
    {
      "creditsCount": 10,
      "creditedAmount": 1.0,
      "debitsCount": 0,
      "debitedAmount": 0,
      "netAmount": 1.0,
      "accountNumber": "******2001",
      "accountType": "ACH"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |


# Summary by Merchant

Resource to get summary of deposits grouped by merchants for given hierarchy and date range. Refer to the schema object for the allowed hierarchies and specifications.

```python
def summary_by_merchant(self,
                       body,
                       v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DepositSummaryMerchantRequest`](../../doc/models/deposit-summary-merchant-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DepositSummaryMerchantResponse`](../../doc/models/deposit-summary-merchant-response.md).

## Example Usage

```python
body = DepositSummaryMerchantRequest(
    hierarchy=EntityMerchant1(
        level=Level11Enum.MERCHANT,
        values=[
            '4445000123456',
            '4345023507756'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2019-07-27',
        to_date='2019-09-12'
    ),
    pagination=PaginationType1(
        page_number=1,
        page_size=25
    )
)

result = deposit_summary_controller.summary_by_merchant(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "pagination": {
    "pageNumber": 1,
    "pageSize": 25,
    "totalRowCount": 85,
    "totalReturnedCount": 25
  },
  "totalCreditsCount": 25,
  "totalCreditedAmount": 257.35,
  "totalDebitsCount": 20,
  "totalDebitedAmount": 36.43,
  "totalNetAmount": 220.92,
  "summaries": [
    {
      "creditsCount": 10,
      "creditedAmount": 120.34,
      "debitsCount": 9,
      "debitedAmount": 20.56,
      "netAmount": 99.78,
      "merchantId": "4445000123456"
    },
    {
      "creditsCount": 15,
      "creditedAmount": 137.01,
      "debitsCount": 11,
      "debitedAmount": 15.87,
      "netAmount": 121.14,
      "merchantId": "4345023507756"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |


# Summary by Store

Resource to get summary of deposits grouped by stores for given hierarchy and date range. Refer to the schema object for the allowed hierarchies and specifications.

```python
def summary_by_store(self,
                    body,
                    v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DepositSummaryStoreRequest`](../../doc/models/deposit-summary-store-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DepositSummaryStoreResponse`](../../doc/models/deposit-summary-store-response.md).

## Example Usage

```python
body = DepositSummaryStoreRequest(
    hierarchy=EntityParentTypeStore1(
        level=Level3Enum.CHAIN,
        values=[
            'AB1234',
            '111217'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2019-07-27',
        to_date='2019-09-12'
    ),
    pagination=PaginationType1(
        page_number=1,
        page_size=25
    )
)

result = deposit_summary_controller.summary_by_store(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "pagination": {
    "pageNumber": 1,
    "pageSize": 25,
    "totalRowCount": 85,
    "totalReturnedCount": 25
  },
  "totalCreditsCount": 25,
  "totalCreditedAmount": 257.35,
  "totalDebitsCount": 20,
  "totalDebitedAmount": 36.43,
  "totalNetAmount": 220.92,
  "summaries": [
    {
      "creditsCount": 10,
      "creditedAmount": 120.34,
      "debitsCount": 9,
      "debitedAmount": 20.56,
      "netAmount": 99.78,
      "chainCode": "AB1234",
      "storeNumber": "000000012"
    },
    {
      "creditsCount": 15,
      "creditedAmount": 137.01,
      "debitsCount": 11,
      "debitedAmount": 15.87,
      "netAmount": 121.14,
      "chainCode": "AB1234",
      "storeNumber": "000000023"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |


# Summary by Division

Resource to get summary of deposits grouped by divisions for given hierarchy and date range. Refer to the schema object for the allowed hierarchies and specifications.

```python
def summary_by_division(self,
                       body,
                       v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DepositSummaryDivisionRequest`](../../doc/models/deposit-summary-division-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DepositSummaryDivisionResponse`](../../doc/models/deposit-summary-division-response.md).

## Example Usage

```python
body = DepositSummaryDivisionRequest(
    hierarchy=EntityParentTypeDivision1(
        level=Level5Enum.CHAIN,
        values=[
            'AB1234',
            '111217'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2019-07-27',
        to_date='2019-09-12'
    ),
    pagination=PaginationType1(
        page_number=1,
        page_size=25
    )
)

result = deposit_summary_controller.summary_by_division(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "pagination": {
    "pageNumber": 1,
    "pageSize": 25,
    "totalRowCount": 85,
    "totalReturnedCount": 25
  },
  "totalCreditsCount": 25,
  "totalCreditedAmount": 257.35,
  "totalDebitsCount": 20,
  "totalDebitedAmount": 36.43,
  "totalNetAmount": 220.92,
  "summaries": [
    {
      "creditsCount": 10,
      "creditedAmount": 120.34,
      "debitsCount": 9,
      "debitedAmount": 20.56,
      "netAmount": 99.78,
      "chainCode": "AB1234",
      "divisionNumber": "356"
    },
    {
      "creditsCount": 15,
      "creditedAmount": 137.01,
      "debitsCount": 11,
      "debitedAmount": 15.87,
      "netAmount": 121.14,
      "chainCode": "AB1234",
      "divisionNumber": "453"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |


# Summary by Chain

Resource to get summary of deposits grouped by chains for given hierarchy and date range. Refer to the schema object for the allowed hierarchies and specifications.

```python
def summary_by_chain(self,
                    body,
                    v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DepositSummaryChainRequest`](../../doc/models/deposit-summary-chain-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DepositSummaryChainResponse`](../../doc/models/deposit-summary-chain-response.md).

## Example Usage

```python
body = DepositSummaryChainRequest(
    hierarchy=EntityChain1(
        level=Level2Enum.CHAIN,
        values=[
            '0B2345',
            'AB1234'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2021-12-01',
        to_date='2021-12-01'
    )
)

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

result = deposit_summary_controller.summary_by_chain(
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
  "pagination": {
    "pageNumber": 1,
    "pageSize": 25,
    "totalRowCount": 85,
    "totalReturnedCount": 25
  },
  "totalCreditsCount": 25,
  "totalCreditedAmount": 257.35,
  "totalDebitsCount": 20,
  "totalDebitedAmount": 36.43,
  "totalNetAmount": 220.92,
  "summaries": [
    {
      "creditsCount": 10,
      "creditedAmount": 120.34,
      "debitsCount": 9,
      "debitedAmount": 20.56,
      "netAmount": 99.78,
      "chainCode": "AB1234"
    },
    {
      "creditsCount": 15,
      "creditedAmount": 137.01,
      "debitsCount": 11,
      "debitedAmount": 15.87,
      "netAmount": 121.14,
      "chainCode": "111217"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |


# Summary by Super Chain

Resource to get summary of deposits grouped by superchains for given hierarchy and date range. Refer to the schema object for the allowed hierarchies and specifications.

```python
def summary_by_super_chain(self,
                          body,
                          v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DepositSummarySuperChainRequest`](../../doc/models/deposit-summary-super-chain-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DepositSummarySuperChainResponse`](../../doc/models/deposit-summary-super-chain-response.md).

## Example Usage

```python
body = DepositSummarySuperChainRequest(
    hierarchy=EntityListTypeSuperChain(
        level=Level4Enum.SUPERCHAIN,
        values=[
            'SCNPCB6111',
            'SCNPCB8811'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2019-07-27',
        to_date='2019-09-12'
    ),
    pagination=PaginationType1(
        page_number=1,
        page_size=25
    )
)

result = deposit_summary_controller.summary_by_super_chain(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "pagination": {
    "pageNumber": 1,
    "pageSize": 25,
    "totalRowCount": 85,
    "totalReturnedCount": 25
  },
  "totalCreditsCount": 25,
  "totalCreditedAmount": 257.35,
  "totalDebitsCount": 20,
  "totalDebitedAmount": 36.43,
  "totalNetAmount": 220.92,
  "summaries": [
    {
      "creditsCount": 10,
      "creditedAmount": 120.34,
      "debitsCount": 9,
      "debitedAmount": 20.56,
      "netAmount": 99.78,
      "superChainCode": "SCNPCB6111"
    },
    {
      "creditsCount": 15,
      "creditedAmount": 137.01,
      "debitsCount": 11,
      "debitedAmount": 15.87,
      "netAmount": 121.14,
      "superChainCode": "SCNPCB8811"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |

