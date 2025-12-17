# Bins

Bins Holds information about the issuer of a card. (Bank Issuer Number).

```python
bins_controller = client.bins
```

## Class Name

`BinsController`

## Methods

* [Get Bins Id](../../doc/controllers/bins.md#get-bins-id)
* [Get Bins](../../doc/controllers/bins.md#get-bins)


# Get Bins Id

Query a BIN, which holds information about the issuer of a card.

```python
def get_bins_id(self,
               id,
               request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The BIN ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BinsResponseResult`](../../doc/models/bins-response-result.md).

## Example Usage

```python
id = 't1_bil_67dbdc94ee1b1a43e6ab000'

request_token = '20250423-yourmerchant-refunds-001'

result = bins_controller.get_bins_id(
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
        "id": "t1_bil_67dbdc94ee1b1a43e6ab000",
        "created": "2025-03-20 05:15:00.9831",
        "modified": "2025-03-20 05:15:00.9831",
        "creator": "t1_log_5cd987a73478a6179b95008",
        "modifier": "t1_log_5cd987a73478a6179b95008",
        "bin": "472509",
        "method": 2,
        "type": "credit",
        "name": "Bank Name",
        "country": "USA",
        "website": "",
        "phone": "",
        "address": "address1",
        "city": "city1",
        "state": "AK",
        "zip": "",
        "locationType": "branch",
        "newBin": "",
        "category": "classic",
        "transferEnabled": 0,
        "numberLength": 0,
        "debitOverCreditEnabled": 0,
        "billPayEnabled": 0,
        "pinlessSupport": "none",
        "inactive": 0,
        "frozen": 0
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


# Get Bins

Querying a BIN resource, which holds information about the issuer of a card.

```python
def get_bins(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BinsResponseResult`](../../doc/models/bins-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = bins_controller.get_bins(
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
        "id": "t1_bil_67dbdc94ee1b1a43e6ab000",
        "created": "2025-03-20 05:15:00.9831",
        "modified": "2025-03-20 05:15:00.9831",
        "creator": "t1_log_5cd987a73478a6179b95008",
        "modifier": "t1_log_5cd987a73478a6179b95008",
        "bin": "472509",
        "method": 2,
        "type": "credit",
        "name": "Bank Name",
        "country": "USA",
        "website": "",
        "phone": "",
        "address": "address1",
        "city": "city1",
        "state": "AK",
        "zip": "",
        "locationType": "branch",
        "newBin": "",
        "category": "classic",
        "transferEnabled": 0,
        "numberLength": 0,
        "debitOverCreditEnabled": 0,
        "billPayEnabled": 0,
        "pinlessSupport": "none",
        "inactive": 0,
        "frozen": 0
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

