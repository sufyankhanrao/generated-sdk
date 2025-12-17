# Settlement Errors

```python
settlement_errors_controller = client.settlement_errors
```

## Class Name

`SettlementErrorsController`

## Methods

* [Search Settlement Rejects](../../doc/controllers/settlement-errors.md#search-settlement-rejects)
* [Search Bank Card Rejects](../../doc/controllers/settlement-errors.md#search-bank-card-rejects)


# Search Settlement Rejects

Resource to search settlement rejects

```python
def search_settlement_rejects(self,
                             body,
                             v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SettlementRejectsSearchRequest`](../../doc/models/settlement-rejects-search-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SettlementRejectsSearchResponse`](../../doc/models/settlement-rejects-search-response.md).

## Example Usage

```python
body = SettlementRejectsSearchRequest(
    hierarchy=Entity(
        level=LevelEnum.INDEPENDENT_SALES_ORGANIZATION,
        values=[
            '4445000860700',
            '4445000860702'
        ],
        chain_code='OA1234'
    ),
    date_range=SearchAuthTransactionsRequestRealTimeTransactionDateRange(
        from_date='2021-12-01',
        to_date='2021-12-01'
    )
)

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

result = settlement_errors_controller.search_settlement_rejects(
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
  "details": [
    {
      "processedDate": "2017-07-20",
      "transactionDate": "2017-07-20",
      "resubmitDate": "2017-07-21",
      "accountNumber": "************0081",
      "ddaNumber": "******7790",
      "amount": 120.01,
      "code": "D",
      "shortDescription": "BAD MCC CODE",
      "longDescription": "INVALID MCC CODE",
      "hierarchy": {
        "chainCode": "0F1286",
        "storeNumber": "000000001",
        "divisionNumber": "002",
        "merchantName": "ABC SOLUTIONS",
        "merchantId": "4445492391789"
      }
    },
    {
      "processedDate": "2017-07-21",
      "transactionDate": "2017-07-21",
      "resubmitDate": "2017-07-22",
      "accountNumber": "************8823",
      "ddaNumber": "******6689",
      "amount": 120.01,
      "code": "D",
      "shortDescription": "BAD MCC CODE",
      "longDescription": "INVALID MCC CODE",
      "hierarchy": {
        "chainCode": "0F1286",
        "storeNumber": "000000001",
        "divisionNumber": "002",
        "merchantName": "ABC SOLUTIONS",
        "merchantId": "4555492491790"
      }
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorError2Exception`](../../doc/models/error-error-2-exception.md) |


# Search Bank Card Rejects

Resource to search bank card rejects

```python
def search_bank_card_rejects(self,
                            body,
                            v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`BankCardRejectsSearchRequest`](../../doc/models/bank-card-rejects-search-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BankCardRejectsSearchResponse`](../../doc/models/bank-card-rejects-search-response.md).

## Example Usage

```python
body = BankCardRejectsSearchRequest(
    hierarchy=Entity(
        level=LevelEnum.INDEPENDENT_SALES_ORGANIZATION,
        values=[
            '4445000860700',
            '4445000860702'
        ],
        chain_code='OA1234'
    ),
    date_range=SearchAuthTransactionsRequestRealTimeTransactionDateRange(
        from_date='2021-12-01',
        to_date='2021-12-01'
    ),
    batch_hold_status='RELEASE BATCH '
)

v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'

result = settlement_errors_controller.search_bank_card_rejects(
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
| Default | Default errors | [`ErrorError2Exception`](../../doc/models/error-error-2-exception.md) |

