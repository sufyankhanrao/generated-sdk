# Reserve Entry

```python
reserve_entry_controller = client.reserve_entry
```

## Class Name

`ReserveEntryController`

## Methods

* [Get Reserve Entries Id](../../doc/controllers/reserve-entry.md#get-reserve-entries-id)
* [Get Reserve Entries](../../doc/controllers/reserve-entry.md#get-reserve-entries)
* [Post Reserve Entries](../../doc/controllers/reserve-entry.md#post-reserve-entries)


# Get Reserve Entries Id

Query a Reserve Entry resource that describes a record of funds moving in or out of reserve and can be associated with either a Transaction, a Reserve, an entityReserve, or another reserveEntry resource.

```python
def get_reserve_entries_id(self,
                          id,
                          request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this reserve entry. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ReserveEntriesResponseResult`](../../doc/models/reserve-entries-response-result.md).

## Example Usage

```python
id = 't1_rer_6800d1df0a777412aa4c8c3'

request_token = '20250423-yourmerchant-refunds-001'

result = reserve_entry_controller.get_reserve_entries_id(
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
        "id": "t1_rer_6800d1df0a777412aa4c8c3",
        "created": "2025-04-17 06:03:11.0593",
        "modified": "2025-04-17 06:03:11.1237",
        "creator": "t1_log_673245a79517f80bf2e7738",
        "modifier": "t1_log_673245a79517f80bf2e7738",
        "login": "t1_log_5d652e3c9bb91623e859e02",
        "fund": "t1_fun_5e6186054d4dbe2416bca5c",
        "txn": "t1_txn_67caef0a014c280a6caa5zz",
        "hold": "t1_hld_67ef5bad3be038935902200",
        "reserve": "t1_rsv_5e21064368e32ef4d38f8d4",
        "entityReserve": "",
        "reserveEntry": "",
        "description": "description1",
        "release": "20160120",
        "amount": 15,
        "onentity": "",
        "entry": "t1_etr_6800d1dee193517e5d6ce91",
        "event": 6,
        "eventId": "t1_txn_6800d1dd114238a04f4e608",
        "status": "processed",
        "statusMessage": "",
        "processed": "2025-04-17 06:03:11.1237",
        "processingId": "t1_rer_6800d1df1e3d47d69bd1cd4"
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


# Get Reserve Entries

Query a reserveEntry resource.
A reserveEntry resource describes a record of funds moving in or out of reserve. It can be associated with either a Transaction, a Reserve, an entityReserve, or another reserveEntry resource.

```python
def get_reserve_entries(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ReserveEntriesResponseResult`](../../doc/models/reserve-entries-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = reserve_entry_controller.get_reserve_entries(
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
        "id": "t1_rer_6800d1df0a777412aa4c8c3",
        "created": "2025-04-17 06:03:11.0593",
        "modified": "2025-04-17 06:03:11.1237",
        "creator": "t1_log_673245a79517f80bf2e7738",
        "modifier": "t1_log_673245a79517f80bf2e7738",
        "login": "t1_log_5d652e3c9bb91623e859e02",
        "fund": "t1_fun_5e6186054d4dbe2416bca5c",
        "txn": "t1_txn_67caef0a014c280a6caa5zz",
        "hold": "t1_hld_67ef5bad3be038935902200",
        "reserve": "t1_rsv_5e21064368e32ef4d38f8d4",
        "entityReserve": "",
        "reserveEntry": "",
        "description": "description1",
        "release": "20160120",
        "amount": 15,
        "onentity": "",
        "entry": "t1_etr_6800d1dee193517e5d6ce91",
        "event": 6,
        "eventId": "t1_txn_6800d1dd114238a04f4e608",
        "status": "processed",
        "statusMessage": "",
        "processed": "2025-04-17 06:03:11.1237",
        "processingId": "t1_rer_6800d1df1e3d47d69bd1cd4"
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


# Post Reserve Entries

Create a Reserve Entry resource that describes a record of funds moving in or out of reserve and can be associated with either a Transaction, a Reserve, an entityReserve, or another reserveEntry resource.

```python
def post_reserve_entries(self,
                        body,
                        request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ReserveEntriesPostRequest`](../../doc/models/reserve-entries-post-request.md) | Body, Required | Create Reserve Entry Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ReserveEntriesResponseResult`](../../doc/models/reserve-entries-response-result.md).

## Example Usage

```python
body = ReserveEntriesPostRequest(
    login='t1_log_5d652e3c9bb91623e859e02',
    fund='t1_fun_5e6186054d4dbe2416bca5c',
    event=ReserveEntryEventEnum.AUTH,
    amount=15,
    entry='t1_etr_6800d1dee193517e5d6ce91',
    hold='t1_hld_67ef5bad3be038935902200',
    txn='t1_txn_67caef0a014c280a6caa5zz',
    reserve='t1_rsv_5e21064368e32ef4d38f8d4',
    entity_reserve='identifier',
    reserve_entry='identifier',
    onentity='t1_ent_00c2b1a6102ffdd33f11000',
    event_id='t1_txn_6800d1dd114238a04f4e608',
    description='description1',
    release='20160120'
)

request_token = '20250423-yourmerchant-refunds-001'

result = reserve_entry_controller.post_reserve_entries(
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
        "id": "t1_rer_6800d1df0a777412aa4c8c3",
        "created": "2025-04-17 06:03:11.0593",
        "modified": "2025-04-17 06:03:11.1237",
        "creator": "t1_log_673245a79517f80bf2e7738",
        "modifier": "t1_log_673245a79517f80bf2e7738",
        "login": "t1_log_5d652e3c9bb91623e859e02",
        "fund": "t1_fun_5e6186054d4dbe2416bca5c",
        "txn": "t1_txn_67caef0a014c280a6caa5zz",
        "hold": "t1_hld_67ef5bad3be038935902200",
        "reserve": "t1_rsv_5e21064368e32ef4d38f8d4",
        "entityReserve": "",
        "reserveEntry": "",
        "description": "description1",
        "release": "20160120",
        "amount": 15,
        "onentity": "",
        "entry": "t1_etr_6800d1dee193517e5d6ce91",
        "event": 6,
        "eventId": "t1_txn_6800d1dd114238a04f4e608",
        "status": "processed",
        "statusMessage": "",
        "processed": "2025-04-17 06:03:11.1237",
        "processingId": "t1_rer_6800d1df1e3d47d69bd1cd4"
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

