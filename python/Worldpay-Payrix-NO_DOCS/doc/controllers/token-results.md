# Token Results

```python
token_results_controller = client.token_results
```

## Class Name

`TokenResultsController`

## Methods

* [Get Token Results Id](../../doc/controllers/token-results.md#get-token-results-id)
* [Get Token Results](../../doc/controllers/token-results.md#get-token-results)


# Get Token Results Id

Query a tokenResults.

```python
def get_token_results_id(self,
                        id,
                        request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TokenResultsResponseResult`](../../doc/models/token-results-response-result.md).

## Example Usage

```python
id = 't1_tkr_681b008f046d4ddae223z00'

request_token = '20250423-yourmerchant-refunds-001'

result = token_results_controller.get_token_results_id(
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
        "id": "t1_tkr_681b008f046d4ddae223z00",
        "created": "2025-05-07 02:41:19.0389",
        "modified": "2025-05-07 02:41:19.0389",
        "creator": "t1_log_632c5bf8960c660a1750a4a",
        "modifier": "t1_log_632c5bf8960c660a1750a4a",
        "txn": "t1_txn_681b008de0ea2d51f42f8db",
        "token": "t1_tok_67f4f42185959a15661d9e4",
        "merchant": "t1_mer_6389ff3793d00800340d742",
        "code": "omnitokenUsage",
        "omnitoken": "5454547474830000"
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


# Get Token Results

Query a Token Results.

```python
def get_token_results(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TokenResultsResponseResult`](../../doc/models/token-results-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = token_results_controller.get_token_results(
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
        "id": "t1_tkr_681b008f046d4ddae223z00",
        "created": "2025-05-07 02:41:19.0389",
        "modified": "2025-05-07 02:41:19.0389",
        "creator": "t1_log_632c5bf8960c660a1750a4a",
        "modifier": "t1_log_632c5bf8960c660a1750a4a",
        "txn": "t1_txn_681b008de0ea2d51f42f8db",
        "token": "t1_tok_67f4f42185959a15661d9e4",
        "merchant": "t1_mer_6389ff3793d00800340d742",
        "code": "omnitokenUsage",
        "omnitoken": "5454547474830000"
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

