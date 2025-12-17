# Profit Share Results

```python
profit_share_results_controller = client.profit_share_results
```

## Class Name

`ProfitShareResultsController`

## Methods

* [Get Profit Share Results Id](../../doc/controllers/profit-share-results.md#get-profit-share-results-id)
* [Get Profit Share Results](../../doc/controllers/profit-share-results.md#get-profit-share-results)


# Get Profit Share Results Id

Query a ProfitShareResult or Profit Share Result.

```python
def get_profit_share_results_id(self,
                               id,
                               request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource, The Profit Share Result ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ProfitShareResultsResponseResult`](../../doc/models/profit-share-results-response-result.md).

## Example Usage

```python
id = 't1_psr_655c21ba778461b81b98b00'

request_token = '20250423-yourmerchant-refunds-001'

result = profit_share_results_controller.get_profit_share_results_id(
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
        "id": "t1_psr_655c21ba778461b81b98b00",
        "created": "2023-11-20 22:19:22.4970",
        "modified": "2023-11-20 22:19:22.4970",
        "creator": "t1_log_673245a79517f80bf2e0000",
        "modifier": "t1_log_673245a79517f80bf2e0000",
        "profitShare": "t1_psh_65369bffac4c88d0d3df1f0",
        "entry": "t1_etr_655c21ba5e65de16142b2c3",
        "amount": 434,
        "message": "Could not share income"
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


# Get Profit Share Results

Query a ProfitShareResult or Profit Share Result resource, which holds a message regarding a failed ProfitShare process.

```python
def get_profit_share_results(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ProfitShareResultsResponseResult`](../../doc/models/profit-share-results-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = profit_share_results_controller.get_profit_share_results(
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
        "id": "t1_psr_655c21ba778461b81b98b00",
        "created": "2023-11-20 22:19:22.4970",
        "modified": "2023-11-20 22:19:22.4970",
        "creator": "t1_log_673245a79517f80bf2e0000",
        "modifier": "t1_log_673245a79517f80bf2e0000",
        "profitShare": "t1_psh_65369bffac4c88d0d3df1f0",
        "entry": "t1_etr_655c21ba5e65de16142b2c3",
        "amount": 434,
        "message": "Could not share income"
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

