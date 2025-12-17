# Disbursements

A disbursement represents a movement of funds in an entity's payment account. Records of an occasion where money is either paid to a bank account or received from a bank account.

```python
disbursements_controller = client.disbursements
```

## Class Name

`DisbursementsController`

## Methods

* [Get Disbursements Id](../../doc/controllers/disbursements.md#get-disbursements-id)
* [Get Disbursements](../../doc/controllers/disbursements.md#get-disbursements)


# Get Disbursements Id

Query a Disbursement, which represents a record of an occasion where money is either paid to a bank account or received from a bank account.

```python
def get_disbursements_id(self,
                        id,
                        request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this disbursement. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DisbursementsResponseResult`](../../doc/models/disbursements-response-result.md).

## Example Usage

```python
id = 't1_dbm_67b7b9b69fca00a9685674f'

request_token = '20250423-yourmerchant-refunds-001'

result = disbursements_controller.get_disbursements_id(
    id,
    request_token=request_token
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "response": {
    "data": [
      {
        "id": "t1_dbm_67b7b9a27c0771be7e9157c",
        "created": "2024-02-20 18:24:18.5096",
        "modified": "2024-02-20 20:30:08.9457",
        "creator": "t1_log_67b7b9a1234771be7e9157c",
        "modifier": "t1_log_67b7b9a1234771be7e9157c",
        "entity": "t1_ent_6744c2ebece01009406db29",
        "account": "90e8b943cf752ffe0ba77c0d2bc8b4c1",
        "payout": "t1_pay_67b7b0d13d70006226d27ff",
        "description": "Disbursement for payout t1_pay_67b7b0d13d70006226d27ff",
        "amount": 23400,
        "status": 3,
        "processed": "2024-02-20 19:41:52",
        "currency": "USD",
        "payment": "t1_pmt_6765c49660f8e2f40424d91",
        "expiration": "1235",
        "sameDay": 0,
        "returnedAmount": 1200,
        "statement": "t1_stm_67bc033e4rt5dd88aa4b9973",
        "settlement": "",
        "lastNegativeEntry": "t1_etr_67b69cfdaf0abd231d9a151",
        "lastNegativePendingEntry": "t1_per_67b50120226e12c1205bee3",
        "lastPositiveReserveEntry": "",
        "disbursementEntriesStatus": "processed",
        "lastPositiveEntry": "t1_etr_67b69b65ac20bbcfdf42478",
        "lastPositivePendingEntry": "",
        "lastNegativeReserveEntry": "",
        "fundingStatus": "pending",
        "secondaryDescriptor": "SGH Bank"
      }
    ],
    "details": {
      "requestId": "1",
      "totals": [],
      "page": {
        "current": 1,
        "last": 1,
        "hasMore": false
      }
    },
    "errors": []
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ErrorFourHundredException`](../../doc/models/error-four-hundred-exception.md) |


# Get Disbursements

Query Disbursements, each of which represents a record of an occasion where money is either paid to a bank account or received from a bank account.

```python
def get_disbursements(self,
                     request_token=None,
                     search=None,
                     totals=None,
                     page_number=None,
                     page_limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |
| `search` | `str` | Header, Optional | Set this header to filter or sort the list of resources that the method returns.<br>See [Searches](page:welcome#searches) for detailed information and examples on how to use search header. |
| `totals` | `str` | Header, Optional | To configure a request to return a total for all instances of a field in a result set,  use the totals header in the format `totals={operator}[]={key}`.  This will calculate the desired total and return it in the `details > totals` object of the response.  For instance, if you want to sum the `total` field of all transactions,  you would use the `sum` operator. The response will include the result set,  along with the calculated total in the `details` section. See [Collection Operators](page:welcome#collection-operators) for detailed information and examples on how to use totals header. |
| `page_number` | `int` | Query, Optional | Set this path parameter to request a specific page of records.<br>For example, set `?page[number]=2` to retrieve the second page of records for this request. |
| `page_limit` | `int` | Query, Optional | Set this path parameter to request up to a specific amount of records. By default 30 records are retrieved per page. The maximum limit that can be set is 100.<br>For example, set `?page[limit]=50` to retrieve up to 50 records for this request. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DisbursementsResponseResult`](../../doc/models/disbursements-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = disbursements_controller.get_disbursements(
    request_token=request_token,
    search=search,
    totals=totals,
    page_number=page_number,
    page_limit=page_limit
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "response": {
    "data": [
      {
        "id": "t1_dbm_67b7b9a27c0771be7e9157c",
        "created": "2024-02-20 18:24:18.5096",
        "modified": "2024-02-20 20:30:08.9457",
        "creator": "t1_log_67b7b9a1234771be7e9157c",
        "modifier": "t1_log_67b7b9a1234771be7e9157c",
        "entity": "t1_ent_6744c2ebece01009406db29",
        "account": "90e8b943cf752ffe0ba77c0d2bc8b4c1",
        "payout": "t1_pay_67b7b0d13d70006226d27ff",
        "description": "Disbursement for payout t1_pay_67b7b0d13d70006226d27ff",
        "amount": 23400,
        "status": 3,
        "processed": "2024-02-20 19:41:52",
        "currency": "USD",
        "payment": "t1_pmt_6765c49660f8e2f40424d91",
        "expiration": "1235",
        "sameDay": 0,
        "returnedAmount": 1200,
        "statement": "t1_stm_67bc033e4rt5dd88aa4b9973",
        "settlement": "",
        "lastNegativeEntry": "t1_etr_67b69cfdaf0abd231d9a151",
        "lastNegativePendingEntry": "t1_per_67b50120226e12c1205bee3",
        "lastPositiveReserveEntry": "",
        "disbursementEntriesStatus": "processed",
        "lastPositiveEntry": "t1_etr_67b69b65ac20bbcfdf42478",
        "lastPositivePendingEntry": "",
        "lastNegativeReserveEntry": "",
        "fundingStatus": "pending",
        "secondaryDescriptor": "SGH Bank"
      }
    ],
    "details": {
      "requestId": "1",
      "totals": [],
      "page": {
        "current": 1,
        "last": 1,
        "hasMore": false
      }
    },
    "errors": []
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ErrorFourHundredException`](../../doc/models/error-four-hundred-exception.md) |

