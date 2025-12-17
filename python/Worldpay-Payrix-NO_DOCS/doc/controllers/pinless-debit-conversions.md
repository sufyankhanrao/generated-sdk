# Pinless Debit Conversions

```python
pinless_debit_conversions_controller = client.pinless_debit_conversions
```

## Class Name

`PinlessDebitConversionsController`

## Methods

* [Get Pinless Debit Conversions Id](../../doc/controllers/pinless-debit-conversions.md#get-pinless-debit-conversions-id)
* [Put Pinless Debit Conversions Id](../../doc/controllers/pinless-debit-conversions.md#put-pinless-debit-conversions-id)
* [Get Pinless Debit Conversions](../../doc/controllers/pinless-debit-conversions.md#get-pinless-debit-conversions)
* [Post Pinless Debit Conversions](../../doc/controllers/pinless-debit-conversions.md#post-pinless-debit-conversions)


# Get Pinless Debit Conversions Id

Query a pinlessDebitConversion.

```python
def get_pinless_debit_conversions_id(self,
                                    id,
                                    request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this pinlessDebitConversion. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PinlessDebitConversionsResponseResult`](../../doc/models/pinless-debit-conversions-response-result.md).

## Example Usage

```python
id = 't1_pdc_684c7ec770b6d462c4cd000'

request_token = '20250423-yourmerchant-refunds-001'

result = pinless_debit_conversions_controller.get_pinless_debit_conversions_id(
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
        "id": "t1_pdc_684c7ec770b6d462c4cd000",
        "entity": "t1_ent_684c79a47671985f15621c0",
        "created": "2025-06-13 15:40:55.4761",
        "modified": "2025-06-13 15:43:09.6391",
        "creator": "t1_log_67a4e72ad2ccca060a2fzzz",
        "modifier": "t1_log_67a4e72ad2ccca060a2fzzz",
        "enablementDate": "2025-06-16 11:15:47",
        "org": "t1_org_684c7ae33b2d4f98520a79a",
        "division": "t1_div_684c7ae33b2d4f98520a00b",
        "partition": "t1_ptn_666834d4d504f11234578f0",
        "platform": "VCORE",
        "inactive": 1,
        "frozen": 0,
        "deleted": "2025-06-13 15:43:09",
        "deleter": "t1_log_67a4e72ad2ccca060a2fcfb"
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


# Put Pinless Debit Conversions Id

Update a pinlessDebitConversion.

```python
def put_pinless_debit_conversions_id(self,
                                    id,
                                    body,
                                    request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this Pinless Debit Conversions. |
| `body` | [`PinlessDebitConversionsPutRequest`](../../doc/models/pinless-debit-conversions-put-request.md) | Body, Required | Update Pinless Debit Conversions |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PinlessDebitConversionsResponseResult`](../../doc/models/pinless-debit-conversions-response-result.md).

## Example Usage

```python
id = 't1_pdc_684c7ec770b6d462c4cd000'

body = PinlessDebitConversionsPutRequest(
    enablement_date='2023-06-01 01:00:00',
    org='t1_org_684c7ae33b2d4f98520a79a',
    division='t1_div_684c7ae33b2d4f98520a00b',
    partition='t1_ptn_666834d4d504f11234578f0',
    platform=Platform2Enum.VCORE,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    deleted='2023-06-01 01:00:00',
    deleter='t1_log_67a4e72ad2ccca060a2fcfb'
)

request_token = '20250423-yourmerchant-refunds-001'

result = pinless_debit_conversions_controller.put_pinless_debit_conversions_id(
    id,
    body,
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
        "id": "t1_pdc_684c7ec770b6d462c4cd000",
        "entity": "t1_ent_684c79a47671985f15621c0",
        "created": "2025-06-13 15:40:55.4761",
        "modified": "2025-06-13 15:43:09.6391",
        "creator": "t1_log_67a4e72ad2ccca060a2fzzz",
        "modifier": "t1_log_67a4e72ad2ccca060a2fzzz",
        "enablementDate": "2025-06-16 11:15:47",
        "org": "t1_org_684c7ae33b2d4f98520a79a",
        "division": "t1_div_684c7ae33b2d4f98520a00b",
        "partition": "t1_ptn_666834d4d504f11234578f0",
        "platform": "VCORE",
        "inactive": 1,
        "frozen": 0,
        "deleted": "2025-06-13 15:43:09",
        "deleter": "t1_log_67a4e72ad2ccca060a2fcfb"
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


# Get Pinless Debit Conversions

Query a pinlessDebitConversions.

```python
def get_pinless_debit_conversions(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PinlessDebitConversionsResponseResult`](../../doc/models/pinless-debit-conversions-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = pinless_debit_conversions_controller.get_pinless_debit_conversions(
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
        "id": "t1_pdc_684c7ec770b6d462c4cd000",
        "entity": "t1_ent_684c79a47671985f15621c0",
        "created": "2025-06-13 15:40:55.4761",
        "modified": "2025-06-13 15:43:09.6391",
        "creator": "t1_log_67a4e72ad2ccca060a2fzzz",
        "modifier": "t1_log_67a4e72ad2ccca060a2fzzz",
        "enablementDate": "2025-06-16 11:15:47",
        "org": "t1_org_684c7ae33b2d4f98520a79a",
        "division": "t1_div_684c7ae33b2d4f98520a00b",
        "partition": "t1_ptn_666834d4d504f11234578f0",
        "platform": "VCORE",
        "inactive": 1,
        "frozen": 0,
        "deleted": "2025-06-13 15:43:09",
        "deleter": "t1_log_67a4e72ad2ccca060a2fcfb"
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


# Post Pinless Debit Conversions

Create a pinlessDebitConversions.

```python
def post_pinless_debit_conversions(self,
                                  body,
                                  request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PinlessDebitConversionsPostRequest`](../../doc/models/pinless-debit-conversions-post-request.md) | Body, Required | Create Pinless Debit Conversions Request. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PinlessDebitConversionsResponseResult`](../../doc/models/pinless-debit-conversions-response-result.md).

## Example Usage

```python
body = PinlessDebitConversionsPostRequest(
    enablement_date='2023-06-01 01:00:00',
    org='t1_org_684c7ae33b2d4f98520a79a',
    division='t1_div_684c7ae33b2d4f98520a00b',
    partition='t1_ptn_666834d4d504f11234578f0',
    platform=Platform2Enum.VCORE,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    deleted='2023-06-01 01:00:00',
    deleter='t1_log_67a4e72ad2ccca060a2fcfb'
)

request_token = '20250423-yourmerchant-refunds-001'

result = pinless_debit_conversions_controller.post_pinless_debit_conversions(
    body,
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
        "id": "t1_pdc_684c7ec770b6d462c4cd000",
        "entity": "t1_ent_684c79a47671985f15621c0",
        "created": "2025-06-13 15:40:55.4761",
        "modified": "2025-06-13 15:43:09.6391",
        "creator": "t1_log_67a4e72ad2ccca060a2fzzz",
        "modifier": "t1_log_67a4e72ad2ccca060a2fzzz",
        "enablementDate": "2025-06-16 11:15:47",
        "org": "t1_org_684c7ae33b2d4f98520a79a",
        "division": "t1_div_684c7ae33b2d4f98520a00b",
        "partition": "t1_ptn_666834d4d504f11234578f0",
        "platform": "VCORE",
        "inactive": 1,
        "frozen": 0,
        "deleted": "2025-06-13 15:43:09",
        "deleter": "t1_log_67a4e72ad2ccca060a2fcfb"
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

