# Fund Origins

```python
fund_origins_controller = client.fund_origins
```

## Class Name

`FundOriginsController`

## Methods

* [Get Fund Origins Id](../../doc/controllers/fund-origins.md#get-fund-origins-id)
* [Get Fund Origins](../../doc/controllers/fund-origins.md#get-fund-origins)


# Get Fund Origins Id

Query a Fund Origin.

```python
def get_fund_origins_id(self,
                       id,
                       request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Fund Origin ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`FundOriginsResponseResult`](../../doc/models/fund-origins-response-result.md).

## Example Usage

```python
id = 't1_fon_67e54d049d19a73f57449b0'

request_token = '20250423-yourmerchant-refunds-001'

result = fund_origins_controller.get_fund_origins_id(
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
        "id": "t1_fon_67e54d049d19a73f57449b0",
        "created": "2025-03-27 09:05:08.6436",
        "modified": "2025-03-27 12:00:28.3183",
        "creator": "t1_log_003ae6ec24a9357ace75ebf",
        "modifier": "t1_log_003ae6ec24a9357ace75ebf",
        "fund": "t1_fun_67e5159729ac5309dcf591d",
        "disbursement": "",
        "amount": 0,
        "funding": "APPLE",
        "platform": "VANTIV",
        "fbo": ""
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


# Get Fund Origins

Query fundOrigins.

```python
def get_fund_origins(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`FundOriginsResponseResult`](../../doc/models/fund-origins-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = fund_origins_controller.get_fund_origins(
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
        "id": "t1_fon_67e54d049d19a73f57449b0",
        "created": "2025-03-27 09:05:08.6436",
        "modified": "2025-03-27 12:00:28.3183",
        "creator": "t1_log_003ae6ec24a9357ace75ebf",
        "modifier": "t1_log_003ae6ec24a9357ace75ebf",
        "fund": "t1_fun_67e5159729ac5309dcf591d",
        "disbursement": "",
        "amount": 0,
        "funding": "APPLE",
        "platform": "VANTIV",
        "fbo": ""
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

