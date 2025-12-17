# Statements

Resources for dealing with billing statements for entities. Statements are generated from billing configurations and represent the amount billed for a given period of time.

```python
statements_controller = client.statements
```

## Class Name

`StatementsController`

## Methods

* [Get Statements Id](../../doc/controllers/statements.md#get-statements-id)
* [Get Statements](../../doc/controllers/statements.md#get-statements)


# Get Statements Id

Query a Statement. A Statement resource represents the total collection of funds owed for a Billing period.

```python
def get_statements_id(self,
                     id,
                     request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Statement ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`StatementsResponseResult`](../../doc/models/statements-response-result.md).

## Example Usage

```python
id = 'p1_stm_00ce6abbac436354cd82bba'

request_token = '20250423-yourmerchant-refunds-001'

result = statements_controller.get_statements_id(
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
        "id": "p1_stm_00ce6abbac436354cd82bba",
        "created": "2025-03-10 00:29:47.7087",
        "modified": "2025-03-10 00:29:50.7845",
        "creator": "p1_log_000444ad99da5eb18e00207",
        "modifier": "p1_log_000444ad99da5eb18e00207",
        "billing": "p1_bil_00585dd2654581aaa5f9993",
        "status": "pending",
        "totalPaid": 0,
        "total": 78687,
        "currency": "USD",
        "forentity": "p1_ent_0acb282c487aa4bf1477e0f",
        "entity": "p1_ent_0051dcf88fee4617e5e38d5",
        "start": 20250201,
        "finish": 20250228
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


# Get Statements

Query a Statement.
A Statement resource represents the total collection of funds owed for a Billing period.

```python
def get_statements(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`StatementsResponseResult`](../../doc/models/statements-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = statements_controller.get_statements(
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
        "id": "p1_stm_00ce6abbac436354cd82bba",
        "created": "2025-03-10 00:29:47.7087",
        "modified": "2025-03-10 00:29:50.7845",
        "creator": "p1_log_000444ad99da5eb18e00207",
        "modifier": "p1_log_000444ad99da5eb18e00207",
        "billing": "p1_bil_00585dd2654581aaa5f9993",
        "status": "pending",
        "totalPaid": 0,
        "total": 78687,
        "currency": "USD",
        "forentity": "p1_ent_0acb282c487aa4bf1477e0f",
        "entity": "p1_ent_0051dcf88fee4617e5e38d5",
        "start": 20250201,
        "finish": 20250228
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

