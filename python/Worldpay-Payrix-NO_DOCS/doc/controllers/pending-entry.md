# Pending Entry

```python
pending_entry_controller = client.pending_entry
```

## Class Name

`PendingEntryController`

## Methods

* [Get Pending Entries Id](../../doc/controllers/pending-entry.md#get-pending-entries-id)
* [Get Pending Entries](../../doc/controllers/pending-entry.md#get-pending-entries)


# Get Pending Entries Id

Query a Pending Entry resource.

```python
def get_pending_entries_id(self,
                          id,
                          request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource or The Pending Entry ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PendingEntriesResponseResult`](../../doc/models/pending-entries-response-result.md).

## Example Usage

```python
id = 't1_per_67f51ffc08643b7442a0c0z'

request_token = '20250423-yourmerchant-refunds-001'

result = pending_entry_controller.get_pending_entries_id(
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
        "id": "t1_per_67f51ffc08643b7442a0c0z",
        "created": "2025-04-08 09:09:16.0370",
        "modified": "2025-04-08 09:09:16.0370",
        "creator": "t1_log_673245a79517f80bf2e7738",
        "modifier": "t1_log_673245a79517f80bf2e7738",
        "entity": "t1_ent_5cd31628c78e5ab17b6212c",
        "onentity": "t1_ent_60f8568b429e7dfeff7080z",
        "fromentity": "t1_ent_60f8568b429e7dfeff7080z",
        "fund": "t1_fun_5d1b04ac29d7c9574ea2452",
        "opposingPendingEntry": "t1_per_67f51fd3165c96d3807e89z",
        "entry": "t1_etr_67f51fd3189a9ae55853bzz",
        "adjustment": "",
        "chargeback": "t1_chb_67f51fbe45d45b518e567e0",
        "disbursement": "",
        "fee": "t1_fee_5c9131ea68dbb156b43ed66",
        "refund": "",
        "txn": "t1_txn_67f51ff9cd19ade7a7f372e",
        "event": 7,
        "eventId": "t1_txn_67f51ff9cd19ade7a7f372e",
        "description": "Txn t1_txn_67f51ff9cd19ade7a7f372e",
        "amount": 105,
        "pending": 0,
        "profitShare": "",
        "originalCurrency": "USD",
        "currencyRate": 0,
        "terminalTxn": "",
        "isFee": 0,
        "entityDebt": "t1_edt_5d70b9336042c995df911bc",
        "statement": "",
        "settlement": "",
        "originalEventId": "t1_txn_67f51ff9cd19ade7a7f372e",
        "originalEvent": 7,
        "revShareStatement": "",
        "isEFE": 0
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


# Get Pending Entries

Query a PendingEntry resource.
A PendingEntry resource represents a record of amounts moving in or out of the funds held by an Entity.
For example, this could be a time-based activity such as a weekly or monthly summary, or an event-based activity such as a Capture, a Payout, or a Fee. In the case of an event-based activity, the PendingEntry contains references the activity in the appropriate field. Eventually the PendingEntry will trigger the creation of an Entry resource and its amount will reflect any unsourced amounts for the Entry.

```python
def get_pending_entries(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PendingEntriesResponseResult`](../../doc/models/pending-entries-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = pending_entry_controller.get_pending_entries(
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
        "id": "t1_per_67f51ffc08643b7442a0c0z",
        "created": "2025-04-08 09:09:16.0370",
        "modified": "2025-04-08 09:09:16.0370",
        "creator": "t1_log_673245a79517f80bf2e7738",
        "modifier": "t1_log_673245a79517f80bf2e7738",
        "entity": "t1_ent_5cd31628c78e5ab17b6212c",
        "onentity": "t1_ent_60f8568b429e7dfeff7080z",
        "fromentity": "t1_ent_60f8568b429e7dfeff7080z",
        "fund": "t1_fun_5d1b04ac29d7c9574ea2452",
        "opposingPendingEntry": "t1_per_67f51fd3165c96d3807e89z",
        "entry": "t1_etr_67f51fd3189a9ae55853bzz",
        "adjustment": "",
        "chargeback": "t1_chb_67f51fbe45d45b518e567e0",
        "disbursement": "",
        "fee": "t1_fee_5c9131ea68dbb156b43ed66",
        "refund": "",
        "txn": "t1_txn_67f51ff9cd19ade7a7f372e",
        "event": 7,
        "eventId": "t1_txn_67f51ff9cd19ade7a7f372e",
        "description": "Txn t1_txn_67f51ff9cd19ade7a7f372e",
        "amount": 105,
        "pending": 0,
        "profitShare": "",
        "originalCurrency": "USD",
        "currencyRate": 0,
        "terminalTxn": "",
        "isFee": 0,
        "entityDebt": "t1_edt_5d70b9336042c995df911bc",
        "statement": "",
        "settlement": "",
        "originalEventId": "t1_txn_67f51ff9cd19ade7a7f372e",
        "originalEvent": 7,
        "revShareStatement": "",
        "isEFE": 0
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

