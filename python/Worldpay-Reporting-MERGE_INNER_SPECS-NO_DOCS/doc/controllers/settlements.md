# Settlements

Resources to retrieve the settlement transactions

```python
settlements_controller = client.settlements
```

## Class Name

`SettlementsController`

## Methods

* [Search Settlements Summary](../../doc/controllers/settlements.md#search-settlements-summary)
* [Search Settlements](../../doc/controllers/settlements.md#search-settlements)
* [Retrieve Transaction Details by Credit Transaction Id](../../doc/controllers/settlements.md#retrieve-transaction-details-by-credit-transaction-id)
* [Retrieve Transaction Details by Debit Transaction Id](../../doc/controllers/settlements.md#retrieve-transaction-details-by-debit-transaction-id)
* [Retrieve Transaction Details by Gift Transaction Id](../../doc/controllers/settlements.md#retrieve-transaction-details-by-gift-transaction-id)
* [Getsettlementssummary](../../doc/controllers/settlements.md#getsettlementssummary)
* [Getsettlementssummarybycardnetwork](../../doc/controllers/settlements.md#getsettlementssummarybycardnetwork)
* [Getsettlementssummarybycardtype](../../doc/controllers/settlements.md#getsettlementssummarybycardtype)
* [Getsettlementssummarybyprocessdate](../../doc/controllers/settlements.md#getsettlementssummarybyprocessdate)
* [Getsettlementssummarybymerchant](../../doc/controllers/settlements.md#getsettlementssummarybymerchant)
* [Getsettlementssummarybystore](../../doc/controllers/settlements.md#getsettlementssummarybystore)
* [Getsettlementssummarybydivision](../../doc/controllers/settlements.md#getsettlementssummarybydivision)
* [Getsettlementssummarybychain](../../doc/controllers/settlements.md#getsettlementssummarybychain)
* [Get Settlements Summary Bysuperchain](../../doc/controllers/settlements.md#get-settlements-summary-bysuperchain)
* [Getsettlementssummarybymonths](../../doc/controllers/settlements.md#getsettlementssummarybymonths)
* [Getsettlementssummarybydate](../../doc/controllers/settlements.md#getsettlementssummarybydate)
* [Getsettlementssummarybymonth](../../doc/controllers/settlements.md#getsettlementssummarybymonth)


# Search Settlements Summary

Resource is used to get settled gross and net amount for card network by process month.

```python
def search_settlements_summary(self,
                              body,
                              v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`NetSettledAmountCardTypeRequest`](../../doc/models/net-settled-amount-card-type-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | A unique identifier value attached to a request |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`NetSettledAmountCardTypeResponse`](../../doc/models/net-settled-amount-card-type-response.md).

## Example Usage

```python
body = NetSettledAmountCardTypeRequest(
    independent_sales_channel_codes=[
        'MTBCON',
        'MTBNEW'
    ],
    month_range=MonthRange(
        start_month='2022-01',
        end_month='2022-06'
    ),
    messaging_types=[
        'PIN',
        'SIG'
    ],
    card_present=True
)

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

result = settlements_controller.search_settlements_summary(
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
  "totalSettledGrossAmount": 775.65,
  "totalSettledGrossCount": 25,
  "totalSettledNetAmount": 1083.69,
  "totalSettledNetCount": 57,
  "summaries": [
    {
      "processMonth": "2017-06",
      "settledGrossAmount": 433.09,
      "settledGrossCount": 17,
      "settledNetAmount": 719.02,
      "settledNetCount": 34,
      "messagingType": "PIN",
      "cardNetwork": "VISA",
      "cardPresent": true
    },
    {
      "processMonth": "2017-07",
      "settledGrossAmount": 342.56,
      "settledGrossCount": 13,
      "settledNetAmount": 364.67,
      "settledNetCount": 23,
      "messagingType": "PIN",
      "cardNetwork": "MASTERCARD",
      "cardPresent": true
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError3Exception`](../../doc/models/error-response-error-3-exception.md) |


# Search Settlements

Endpoint is used to retrieve the settled transaction details for a given hierarchy and date range. It helps the user to perform a search based on optional fields.

```python
def search_settlements(self,
                      body,
                      v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SearchSettleTransactionsRequest`](../../doc/models/search-settle-transactions-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SearchSettledTransactionsResponse`](../../doc/models/search-settled-transactions-response.md).

## Example Usage

```python
body = SearchSettleTransactionsRequest(
    hierarchy=Entity(
        level=LevelEnum.INDEPENDENT_SALES_ORGANIZATION,
        values=[
            '4445000860700',
            '4445000860702'
        ],
        chain_code='OA1234'
    ),
    date_range=Processdaterange(
        from_date='2021-12-01',
        to_date='2021-12-01'
    ),
    date_type=DateType1Enum.PROCESS_DATE,
    token=123456789056789,
    network_token='3434343',
    reference_number='2444600338440029',
    transaction_id='141710009519',
    transaction_type_code=TransactionTypeCode1Enum.GA,
    transaction_status_code=TransactionStatusEnum.AA
)

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

result = settlements_controller.search_settlements(
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


# Retrieve Transaction Details by Credit Transaction Id

Endpoint is used to retrieve the details for a individual transaction.

```python
def retrieve_transaction_details_by_credit_transaction_id(self,
                                                         transaction_id,
                                                         v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `str` | Template, Required | Transaction id is a unique identifier generated for every card transaction for tracking purposes. (12-18 digits)<br><br>**Constraints**: *Maximum Length*: `18` |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CreditTransactionDetailsResponse1`](../../doc/models/credit-transaction-details-response-1.md).

## Example Usage

```python
transaction_id = '141710009519'

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

result = settlements_controller.retrieve_transaction_details_by_credit_transaction_id(
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
| Default | Default errors | [`ErrorError2Exception`](../../doc/models/error-error-2-exception.md) |


# Retrieve Transaction Details by Debit Transaction Id

Endpoint is used to retrieve the details for an individual transaction.

```python
def retrieve_transaction_details_by_debit_transaction_id(self,
                                                        transaction_id,
                                                        v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `str` | Template, Required | Transaction id is a unique identifier generated for every card transaction for tracking purposes. (12-18 digits)<br><br>**Constraints**: *Maximum Length*: `18` |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DebitTransactionDetailsResponse1`](../../doc/models/debit-transaction-details-response-1.md).

## Example Usage

```python
transaction_id = '141710009519'

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

result = settlements_controller.retrieve_transaction_details_by_debit_transaction_id(
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
| Default | Default errors | [`ErrorError2Exception`](../../doc/models/error-error-2-exception.md) |


# Retrieve Transaction Details by Gift Transaction Id

Endpoint is used to retrieve the details for an individual transaction.

```python
def retrieve_transaction_details_by_gift_transaction_id(self,
                                                       transaction_id,
                                                       v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `str` | Template, Required | Transaction id is a unique identifier generated for every card transaction for tracking purposes. (12-18 digits)<br><br>**Constraints**: *Maximum Length*: `18` |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GiftTransactionDetailsResponse1`](../../doc/models/gift-transaction-details-response-1.md).

## Example Usage

```python
transaction_id = '141710009519'

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

result = settlements_controller.retrieve_transaction_details_by_gift_transaction_id(
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
| Default | Default errors | [`ErrorError2Exception`](../../doc/models/error-error-2-exception.md) |


# Getsettlementssummary

Resource to get total summary of settlements for given hierarchy and date range with card type and card network being optional parameters. Refer to the  schema object for the allowed hierarchies and specifications.

```python
def getsettlementssummary(self,
                         v_correlation_id=None,
                         body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |
| `body` | [`SettlementsRequest`](../../doc/models/settlements-request.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SummaryResponses2`](../../doc/models/summary-responses-2.md).

## Example Usage

```python
body = SettlementsRequest(
    hierarchy=Entity4(
        level=Level1Enum.MERCHANT,
        values=[
            '4445000123456',
            '4345023507756'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2019-07-27',
        to_date='2019-09-13'
    )
)

result = settlements_controller.getsettlementssummary(
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
  "totalSaleCount": 200,
  "totalSaleAmount": 2000.11,
  "totalReturnCount": 218,
  "totalReturnAmount": 844.28,
  "totalNetAmount": 1155.72
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |


# Getsettlementssummarybycardnetwork

Resource to get summary of settlements grouped by card network for given hierarchy and date range with card type and card network being optional parameters. Refer to the schema object for the allowed hierarchies and specifications.

```python
def getsettlementssummarybycardnetwork(self,
                                      v_correlation_id=None,
                                      body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |
| `body` | [`SettlementsSummaryRequest`](../../doc/models/settlements-summary-request.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SettlementSummaryByCardNetworkResponse`](../../doc/models/settlement-summary-by-card-network-response.md).

## Example Usage

```python
body = SettlementsSummaryRequest(
    hierarchy=Entity4(
        level=Level1Enum.MERCHANT,
        values=[
            '4445000123456',
            '4345023507756'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2019-07-27',
        to_date='2019-09-13'
    ),
    pagination=PaginationType2(
        page_number=1,
        page_size=25
    )
)

result = settlements_controller.getsettlementssummarybycardnetwork(
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
  "pagination": {
    "pageNumber": 1,
    "pageSize": 25,
    "totalRowCount": 85,
    "totalReturnedCount": 25
  },
  "totalSaleCount": 25,
  "totalSaleAmount": 257.35,
  "totalReturnCount": 20,
  "totalReturnAmount": 36.43,
  "totalNetAmount": 236.79,
  "summaries": [
    {
      "saleCount": 10,
      "saleAmount": 120.34,
      "returnCount": 9,
      "returnAmount": 20.56,
      "netAmount": 99.78,
      "cardType": "CREDIT",
      "cardNetwork": {
        "code": "L,",
        "shortDescription": "BILL_ME_LATER",
        "longDescription": "BILL_ME_LATER"
      }
    },
    {
      "saleCount": 15,
      "saleAmount": 137.01,
      "returnCount": 11,
      "returnAmount": 15.87,
      "netAmount": 137.01,
      "cardType": "DEBIT",
      "cardNetwork": {
        "code": "07",
        "shortDescription": "EBT",
        "longDescription": "EBT"
      }
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |


# Getsettlementssummarybycardtype

Resource to get summary of settlements grouped by card type for given hierarchy and date range with card type and card network being optional parameters. Refer to the schema object for the allowed hierarchies and specifications.

```python
def getsettlementssummarybycardtype(self,
                                   v_correlation_id=None,
                                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |
| `body` | [`SettlementsSummaryRequest`](../../doc/models/settlements-summary-request.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SettlementSummaryByCardTypeResponse`](../../doc/models/settlement-summary-by-card-type-response.md).

## Example Usage

```python
body = SettlementsSummaryRequest(
    hierarchy=Entity4(
        level=Level1Enum.MERCHANT,
        values=[
            '4445000123456',
            '4345023507756'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2019-07-27',
        to_date='2019-09-13'
    ),
    pagination=PaginationType2(
        page_number=1,
        page_size=25
    )
)

result = settlements_controller.getsettlementssummarybycardtype(
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
  "pagination": {
    "pageNumber": 1,
    "pageSize": 25,
    "totalRowCount": 85,
    "totalReturnedCount": 25
  },
  "totalSaleCount": 25,
  "totalSaleAmount": 257.35,
  "totalReturnCount": 20,
  "totalReturnAmount": 36.43,
  "totalNetAmount": 236.79,
  "summaries": [
    {
      "saleCount": 10,
      "saleAmount": 120.34,
      "returnCount": 9,
      "returnAmount": 20.56,
      "netAmount": 99.78,
      "cardType": "CREDIT"
    },
    {
      "saleCount": 15,
      "saleAmount": 137.01,
      "returnCount": 11,
      "returnAmount": 15.87,
      "netAmount": 137.01,
      "cardType": "DEBIT"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |


# Getsettlementssummarybyprocessdate

Resource to get summary of settlements grouped by process dates for given hierarchy and date range with card type and card network being optional parameters. Refer to the schema object for the allowed hierarchies and specifications.

```python
def getsettlementssummarybyprocessdate(self,
                                      v_correlation_id=None,
                                      body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |
| `body` | [`SettlementsSummaryRequest`](../../doc/models/settlements-summary-request.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SettlementSummaryByProcessDateResponse`](../../doc/models/settlement-summary-by-process-date-response.md).

## Example Usage

```python
body = SettlementsSummaryRequest(
    hierarchy=Entity4(
        level=Level1Enum.MERCHANT,
        values=[
            '4445000123456',
            '4345023507756'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2019-07-27',
        to_date='2019-09-13'
    ),
    pagination=PaginationType2(
        page_number=1,
        page_size=25
    )
)

result = settlements_controller.getsettlementssummarybyprocessdate(
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
  "pagination": {
    "pageNumber": 1,
    "pageSize": 25,
    "totalRowCount": 85,
    "totalReturnedCount": 25
  },
  "totalSaleCount": 25,
  "totalSaleAmount": 257.35,
  "totalReturnCount": 20,
  "totalReturnAmount": 36.43,
  "totalNetAmount": 236.79,
  "summaries": [
    {
      "saleCount": 10,
      "saleAmount": 120.34,
      "returnCount": 9,
      "returnAmount": 20.56,
      "netAmount": 99.78,
      "processDate": "2019-07-27"
    },
    {
      "saleCount": 15,
      "saleAmount": 137.01,
      "returnCount": 11,
      "returnAmount": 15.87,
      "netAmount": 137.01,
      "processDate": "2019-07-28"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |


# Getsettlementssummarybymerchant

Resource to get summary of settlements grouped by merchants for given hierarchy and date range with card type and card network being optional parameters. Refer to the schema object for the allowed hierarchies and specifications.

```python
def getsettlementssummarybymerchant(self,
                                   v_correlation_id=None,
                                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |
| `body` | [`SettlementsRequestByMERCHANT`](../../doc/models/settlements-request-by-merchant.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SettlementSummaryByMERCHANTResponse`](../../doc/models/settlement-summary-by-merchant-response.md).

## Example Usage

```python
body = SettlementsRequestByMERCHANT(
    hierarchy=EntityMerchant2(
        level=Level11Enum.MERCHANT,
        values=[
            '4445000123456',
            '4345023507756'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2019-07-27',
        to_date='2019-09-13'
    ),
    pagination=PaginationType2(
        page_number=1,
        page_size=25
    )
)

result = settlements_controller.getsettlementssummarybymerchant(
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
  "pagination": {
    "pageNumber": 1,
    "pageSize": 25,
    "totalRowCount": 85,
    "totalReturnedCount": 25
  },
  "totalSaleCount": 25,
  "totalSaleAmount": 257.35,
  "totalReturnCount": 20,
  "totalReturnAmount": 36.43,
  "totalNetAmount": 236.79,
  "summaries": [
    {
      "saleCount": 10,
      "saleAmount": 120.34,
      "returnCount": 9,
      "returnAmount": 20.56,
      "netAmount": 99.78,
      "merchantId": "4445000123456"
    },
    {
      "saleCount": 15,
      "saleAmount": 137.01,
      "returnCount": 11,
      "returnAmount": 15.87,
      "netAmount": 137.01,
      "merchantId": "4345023507756"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |


# Getsettlementssummarybystore

Resource to get summary of settlements grouped by stores for given hierarchy and date range with card type and card network being optional parameters. Refer to the schema object for the allowed hierarchies and specifications.

```python
def getsettlementssummarybystore(self,
                                v_correlation_id=None,
                                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |
| `body` | [`SettlementsRequestBySTORE`](../../doc/models/settlements-request-by-store.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SettlementSummaryBySTOREResponse`](../../doc/models/settlement-summary-by-store-response.md).

## Example Usage

```python
body = SettlementsRequestBySTORE(
    hierarchy=EntityParentTypeStore2(
        level=Level51Enum.CHAIN,
        values=[
            'AB1234',
            '111217'
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

result = settlements_controller.getsettlementssummarybystore(
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
  "pagination": {
    "pageNumber": 1,
    "pageSize": 25,
    "totalRowCount": 85,
    "totalReturnedCount": 25
  },
  "totalSaleCount": 25,
  "totalSaleAmount": 257.35,
  "totalReturnCount": 20,
  "totalReturnAmount": 36.43,
  "totalNetAmount": 236.79,
  "summaries": [
    {
      "saleCount": 10,
      "saleAmount": 120.34,
      "returnCount": 9,
      "returnAmount": 20.56,
      "netAmount": 99.78,
      "chainCode": "AB1234",
      "storeNumber": "000000012"
    },
    {
      "saleCount": 15,
      "saleAmount": 137.01,
      "returnCount": 11,
      "returnAmount": 15.87,
      "netAmount": 137.01,
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


# Getsettlementssummarybydivision

Resource to get summary of settlements grouped by divisions for given hierarchy and date range with card type and card network being optional parameters. Refer to the schema object for the allowed hierarchies and specifications.

```python
def getsettlementssummarybydivision(self,
                                   v_correlation_id=None,
                                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |
| `body` | [`SettlementsRequestByDIVISION`](../../doc/models/settlements-request-by-division.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SettlementSummaryByDIVISIONResponse`](../../doc/models/settlement-summary-by-division-response.md).

## Example Usage

```python
body = SettlementsRequestByDIVISION(
    hierarchy=EntityParentTypeDivision2(
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
    pagination=PaginationType2(
        page_number=1,
        page_size=25
    )
)

result = settlements_controller.getsettlementssummarybydivision(
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


# Getsettlementssummarybychain

Resource to get summary of settlements grouped by chain for given hierarchy and date range with card type and card network being optional parameters. Refer to the schema object for the allowed hierarchies and specifications.

```python
def getsettlementssummarybychain(self,
                                v_correlation_id=None,
                                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |
| `body` | [`SettlementsRequestByCHAIN`](../../doc/models/settlements-request-by-chain.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SettlementSummaryByCHAINResponse`](../../doc/models/settlement-summary-by-chain-response.md).

## Example Usage

```python
body = SettlementsRequestByCHAIN(
    hierarchy=EntityChain2(
        level=Level2Enum.CHAIN,
        values=[
            'AB1234',
            '111217'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2019-07-27',
        to_date='2019-09-12'
    ),
    pagination=PaginationType2(
        page_number=1,
        page_size=25
    ),
    card_type=CardType1Enum.CREDIT,
    card_networks=[
        CardNetwork2Enum.VISA,
        CardNetwork2Enum.MASTERCARD,
        CardNetwork2Enum.DISCOVER,
        CardNetwork2Enum.AMEX
    ]
)

result = settlements_controller.getsettlementssummarybychain(
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
  "pagination": {
    "pageNumber": 1,
    "pageSize": 25,
    "totalRowCount": 85,
    "totalReturnedCount": 25
  },
  "totalSaleCount": 25,
  "totalSaleAmount": 257.35,
  "totalReturnCount": 20,
  "totalReturnAmount": 36.43,
  "totalNetAmount": 236.79,
  "summaries": [
    {
      "saleCount": 10,
      "saleAmount": 120.34,
      "returnCount": 9,
      "returnAmount": 20.56,
      "netAmount": 99.78,
      "chainCode": "AB1234"
    },
    {
      "saleCount": 15,
      "saleAmount": 137.01,
      "returnCount": 11,
      "returnAmount": 15.87,
      "netAmount": 137.01,
      "chainCode": "111217"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |


# Get Settlements Summary Bysuperchain

Resource to get summary of settlements grouped by super chain for given hierarchy and date range with card type and card network being optional parameters. Refer to the schema object for the allowed hierarchies and specifications.

```python
def get_settlements_summary_bysuperchain(self,
                                        v_correlation_id=None,
                                        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |
| `body` | [`SettlementsRequestBySuperChain`](../../doc/models/settlements-request-by-super-chain.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SettlementSummaryBySuperChainResponse`](../../doc/models/settlement-summary-by-super-chain-response.md).

## Example Usage

```python
body = SettlementsRequestBySuperChain(
    hierarchy=EntitySuperChain1(
        level=Level4Enum.SUPERCHAIN,
        values=[
            'SCNPCB6111',
            'SCNPCB8811'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2019-07-27',
        to_date='2019-08-02'
    ),
    pagination=PaginationType2(
        page_number=1,
        page_size=25
    ),
    card_type=CardType1Enum.CREDIT,
    card_networks=[
        CardNetwork2Enum.VISA,
        CardNetwork2Enum.MASTERCARD,
        CardNetwork2Enum.DISCOVER,
        CardNetwork2Enum.AMEX
    ]
)

result = settlements_controller.get_settlements_summary_bysuperchain(
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
  "pagination": {
    "pageNumber": 1,
    "pageSize": 25,
    "totalRowCount": 85,
    "totalReturnedCount": 25
  },
  "totalSaleCount": 25,
  "totalSaleAmount": 257.35,
  "totalReturnCount": 20,
  "totalReturnAmount": 36.43,
  "totalNetAmount": 236.79,
  "summaries": [
    {
      "saleCount": 10,
      "saleAmount": 120.34,
      "returnCount": 9,
      "returnAmount": 20.56,
      "netAmount": 99.78,
      "superChainCode": "SCNPCB6111"
    },
    {
      "saleCount": 15,
      "saleAmount": 137.01,
      "returnCount": 11,
      "returnAmount": 15.87,
      "netAmount": 137.01,
      "superChainCode": "SCNPCB8811"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |


# Getsettlementssummarybymonths

Resource to get summary of settlements for given merchant and chain with month range. Refer to the schema object for the allowed hierarchies and specifications.

```python
def getsettlementssummarybymonths(self,
                                 v_correlation_id=None,
                                 body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |
| `body` | [`MonthlyTranSummaryInput`](../../doc/models/monthly-tran-summary-input.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TransactionSummaryByMonth`](../../doc/models/transaction-summary-by-month.md).

## Example Usage

```python
v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

body = MonthlyTranSummaryInput(
    merchant_id='4445191034215',
    chain_code='070110'
)

result = settlements_controller.getsettlementssummarybymonths(
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


# Getsettlementssummarybydate

Resource to get summary of settlements for given merchant and chain with date range. Refer to the schema object for the allowed hierarchies and specifications.

```python
def getsettlementssummarybydate(self,
                               v_correlation_id=None,
                               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |
| `body` | [`DailyTranSummaryInput`](../../doc/models/daily-tran-summary-input.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TransactionSummaryByDate`](../../doc/models/transaction-summary-by-date.md).

## Example Usage

```python
body = DailyTranSummaryInput(
    sort_results_by=OrderByForDateSummaryType(
        field_name=FieldName16Enum.PROCESS_DATE,
        order_by=OrderByEnum.ASC
    ),
    merchant_id='4445000860874',
    date_range=SearchAuthTransactionsRequestRealTimeTransactionDateRange(
        from_date='2023-05-05',
        to_date='2023-07-24'
    )
)

result = settlements_controller.getsettlementssummarybydate(
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


# Getsettlementssummarybymonth

API to return settled transaction summary details by month for a single chain.

```python
def getsettlementssummarybymonth(self,
                                v_correlation_id=None,
                                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id. |
| `body` | [`MonthlyTranSummaryInputCHAIN`](../../doc/models/monthly-tran-summary-input-chain.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TransactionSummaryByMonthCHAIN`](../../doc/models/transaction-summary-by-month-chain.md).

## Example Usage

```python
body = MonthlyTranSummaryInputCHAIN(
    chain_code='111186',
    date_range=MonthRange(
        start_month='2023-03',
        end_month='2023-06'
    )
)

result = settlements_controller.getsettlementssummarybymonth(
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
  "details": {
    "chainCode": "111186",
    "totalChargebackSalesCount": 116,
    "totalChargebackSalesAmount": 158624.05,
    "totalTransactionAmount": 8.87,
    "totalTransactionCount": 7,
    "processMonthStart": "2023-03",
    "processMonthEnd": "2023-06"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |

