# Deposit Details

```python
deposit_details_controller = client.deposit_details
```

## Class Name

`DepositDetailsController`

## Methods

* [Search Deposit Details](../../doc/controllers/deposit-details.md#search-deposit-details)
* [Searchdepositerrors](../../doc/controllers/deposit-details.md#searchdepositerrors)


# Search Deposit Details

Endpoint is used to get the deposit details at different hierarchy levels for respective date range. Optionals fields is used to filter the serach criteria.

```python
def search_deposit_details(self,
                          body,
                          v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DepositSearchRequest`](../../doc/models/deposit-search-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SearchByCategoryResponse`](../../doc/models/search-by-category-response.md).

## Example Usage

```python
body = DepositSearchRequest(
    hierarchy=Entity2(
        level=Level1Enum.MERCHANT,
        values=[
            '4445000860700',
            '4445000860702'
        ],
        chain_code='OA1234'
    ),
    date_range=DateRange(
        from_date='2019-10-27',
        to_date='2019-11-27'
    ),
    settlement_category=SettlementCategoryEnum.FEES
)

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

result = deposit_details_controller.search_deposit_details(
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
| Default | Default errors | [`ErrorError1Exception`](../../doc/models/error-error-1-exception.md) |


# Searchdepositerrors

Endpoint is used to get the deposit error details at different hierarchy levels for respective date range. Optionals fields is used to filter the serach criteria.

```python
def searchdepositerrors(self,
                       body,
                       v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ACHRejectsSearchRequest`](../../doc/models/ach-rejects-search-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ACHRejectsSearchResponse`](../../doc/models/ach-rejects-search-response.md).

## Example Usage

```python
body = ACHRejectsSearchRequest(
    hierarchy=Entity2(
        level=Level1Enum.MERCHANT,
        values=[
            '4445000860700',
            '4445000860702'
        ],
        chain_code='OA1234'
    ),
    date_range=DateRange(
        from_date='2019-10-27',
        to_date='2019-11-27'
    ),
    funding_method=FundingMethodEnum.PREPAID_CARD
)

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

result = deposit_details_controller.searchdepositerrors(
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
| Default | Default errors | [`ErrorError1Exception`](../../doc/models/error-error-1-exception.md) |

