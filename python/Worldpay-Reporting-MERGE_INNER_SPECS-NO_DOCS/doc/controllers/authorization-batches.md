# Authorization Batches

```python
authorization_batches_controller = client.authorization_batches
```

## Class Name

`AuthorizationBatchesController`

## Methods

* [Search Batches](../../doc/controllers/authorization-batches.md#search-batches)
* [Get Batch Details](../../doc/controllers/authorization-batches.md#get-batch-details)
* [Get Batch Transaction Details](../../doc/controllers/authorization-batches.md#get-batch-transaction-details)


# Search Batches

Endpoint allows users to search for batches of data using specific criteria (date type, date range and merchant id). Refer to the schema object for the filters.

```python
def search_batches(self,
                  body,
                  v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`BatchDetailsSearchRequest`](../../doc/models/batch-details-search-request.md) | Body, Required | - |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation ID |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BatchDetailsResponse`](../../doc/models/batch-details-response.md).

## Example Usage

```python
body = BatchDetailsSearchRequest(
    date_type=DateTypeEnum.RELEASED_DATE,
    date_range=DateRangeSearch(
        from_date='2021-12-01',
        to_date='2021-12-01'
    ),
    merchant_id='1000910955961234',
    batch_number=111002,
    batch_status=BatchStatusEnum.CLOSED,
    terminal_number=5
)

v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'

result = authorization_batches_controller.search_batches(
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
| Default | Default errors | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |


# Get Batch Details

Resource provides to retrieve information about transactions that have been grouped and processed together in a batch. A batch is a collection of related transactions that are processed and managed together for reconciliation.

```python
def get_batch_details(self,
                     merchant_id,
                     batch_number,
                     bank_number,
                     batch_type,
                     open_date,
                     terminal_number,
                     v_correlation_id=None,
                     page_size=None,
                     page_number=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Header, Required | Merchant ID (card acceptor identification code)<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `16` |
| `batch_number` | `str` | Header, Required | Number of the batch<br><br>**Constraints**: *Minimum Length*: `6`, *Maximum Length*: `6` |
| `bank_number` | `int` | Header, Required | the acquiring institution identification code (Bank ID) |
| `batch_type` | [`BatchType2Enum`](../../doc/models/batch-type-2-enum.md) | Query, Required | Type of batch - AUTH, UPLOAD. <br>AUTH - Authorization batches captured by processing system (host). <br>UPLOAD - Batch uploaded by merchant from the terminal. |
| `open_date` | `str` | Query, Required | Batch Opened date<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |
| `terminal_number` | `int` | Query, Required | The Unique identification number for every terminal of a merchant |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation ID |
| `page_size` | `int` | Query, Optional | Number of record that you would want to retrieve per page <br> Default is 25 items per page. |
| `page_number` | `int` | Query, Optional | This is the page number that you would like to retrieve <br> Default is page number 01 |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetBatchDetailsResponse`](../../doc/models/get-batch-details-response.md).

## Example Usage

```python
merchant_id = '1234910955961234'

batch_number = '111002'

bank_number = 1440

batch_type = BatchType2Enum.AUTH

open_date = '2022-12-06'

terminal_number = 5

v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'

page_size = 100

page_number = 4

result = authorization_batches_controller.get_batch_details(
    merchant_id,
    batch_number,
    bank_number,
    batch_type,
    open_date,
    terminal_number,
    v_correlation_id=v_correlation_id,
    page_size=page_size,
    page_number=page_number
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |


# Get Batch Transaction Details

The Resource allows users to retrieve detailed information about a specific transaction within a batch. Users can pass the retrieval reference number in the API request to specify the transaction want to get the details.Specific transaction details within a batch can be used for reconciliation and reporting purposes.

```python
def get_batch_transaction_details(self,
                                 bank_number,
                                 merchant_id,
                                 batch_number,
                                 retrieval_reference_number,
                                 batch_type,
                                 open_date,
                                 v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_number` | `int` | Header, Required | the acquiring institution identification code (Bank ID) |
| `merchant_id` | `str` | Header, Required | Merchant ID (card acceptor identification code)<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `16` |
| `batch_number` | `str` | Header, Required | Number of the batch<br><br>**Constraints**: *Minimum Length*: `6`, *Maximum Length*: `6` |
| `retrieval_reference_number` | `str` | Template, Required | A unique identifier used to reference and locate the batch of transactions.<br><br>**Constraints**: *Minimum Length*: `12`, *Maximum Length*: `12` |
| `batch_type` | [`BatchType2Enum`](../../doc/models/batch-type-2-enum.md) | Query, Required | Type of batch - AUTH, UPLOAD. <br>AUTH - Authorization batches captured by processing system (host). <br>UPLOAD - Batch uploaded by merchant from the terminal. |
| `open_date` | `str` | Query, Required | Batch Opened date<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation ID |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetBatchTransactionDetailsResponse`](../../doc/models/get-batch-transaction-details-response.md).

## Example Usage

```python
bank_number = 3456

merchant_id = '1000910955961234'

batch_number = '111002'

retrieval_reference_number = '111119154359'

batch_type = BatchType2Enum.AUTH

open_date = '2022-12-06'

v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'

result = authorization_batches_controller.get_batch_transaction_details(
    bank_number,
    merchant_id,
    batch_number,
    retrieval_reference_number,
    batch_type,
    open_date,
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
| Default | Default errors | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |

