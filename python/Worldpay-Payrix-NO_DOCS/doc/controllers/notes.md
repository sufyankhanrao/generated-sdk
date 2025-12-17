# Notes

Notes handles  risk management notes, reviews and releases for a Hold, Transaction and Entity specific data.

```python
notes_controller = client.notes
```

## Class Name

`NotesController`

## Methods

* [Get Notes Id](../../doc/controllers/notes.md#get-notes-id)
* [Put Notes Id](../../doc/controllers/notes.md#put-notes-id)
* [Delete Notes Id](../../doc/controllers/notes.md#delete-notes-id)
* [Get Notes](../../doc/controllers/notes.md#get-notes)
* [Post Notes](../../doc/controllers/notes.md#post-notes)


# Get Notes Id

Query a Notes resource that represents risk management notes, reviews, and releases for a Hold, Txn, and Entity specific data.

```python
def get_notes_id(self,
                id,
                request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this note. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`NotesResponseResult`](../../doc/models/notes-response-result.md).

## Example Usage

```python
id = 'p1_not_00c7145c4daae43427e0d91'

request_token = '20250423-yourmerchant-refunds-001'

result = notes_controller.get_notes_id(
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
        "id": "p1_not_00c5a2ff6ba148fbfd20acc",
        "created": "2025-03-03 07:39:27.4554",
        "modified": "2025-03-03 07:39:27.4554",
        "creator": "p1_log_00fad7e7a567603f45e13ab",
        "modifier": "p1_log_00fad7e7a567603f45e13ab",
        "login": "p1_log_00c59f2b74896e4086c2fe6",
        "hold": "",
        "txn": "",
        "terminalTxn": "",
        "entity": "p1_ent_00c1ff2d61b43ffab63cec5",
        "type": "release",
        "note": "Raised HT limit",
        "data": "",
        "inactive": 0,
        "frozen": 0,
        "pinned": 0,
        "pinnedDate": "2025-03-04 09:55:27"
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


# Put Notes Id

Update a Note.

```python
def put_notes_id(self,
                id,
                body,
                request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this note. |
| `body` | [`NotesPutRequest`](../../doc/models/notes-put-request.md) | Body, Required | Update Note Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`NotesResponseResult`](../../doc/models/notes-response-result.md).

## Example Usage

```python
id = 'p1_not_00c7145c4daae43427e0d91'

body = NotesPutRequest(
    login='p1_log_00c59f2b74896e4086c2fe6',
    txn='t1_txn_67ea9ac271f195a95059550',
    terminal_txn='identifier',
    hold='t1_hld_67e08f086e275ddcc8820e1',
    entity='p1_ent_00c1ff2d61b43ffab63cec5',
    mtype=NoteTypeEnum.NOTE,
    data='amexSales',
    note='Raised HT limit',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = notes_controller.put_notes_id(
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
        "id": "p1_not_00c5a2ff6ba148fbfd20acc",
        "created": "2025-03-03 07:39:27.4554",
        "modified": "2025-03-03 07:39:27.4554",
        "creator": "p1_log_00fad7e7a567603f45e13ab",
        "modifier": "p1_log_00fad7e7a567603f45e13ab",
        "login": "p1_log_00c59f2b74896e4086c2fe6",
        "hold": "",
        "txn": "",
        "terminalTxn": "",
        "entity": "p1_ent_00c1ff2d61b43ffab63cec5",
        "type": "release",
        "note": "Raised HT limit",
        "data": "",
        "inactive": 0,
        "frozen": 0,
        "pinned": 0,
        "pinnedDate": "2025-03-04 09:55:27"
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


# Delete Notes Id

Delete a Note.

```python
def delete_notes_id(self,
                   id,
                   request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this note. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`NotesResponseResult`](../../doc/models/notes-response-result.md).

## Example Usage

```python
id = 'p1_not_00c7145c4daae43427e0d91'

request_token = '20250423-yourmerchant-refunds-001'

result = notes_controller.delete_notes_id(
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
        "id": "p1_not_00c5a2ff6ba148fbfd20acc",
        "created": "2025-03-03 07:39:27.4554",
        "modified": "2025-03-03 07:39:27.4554",
        "creator": "p1_log_00fad7e7a567603f45e13ab",
        "modifier": "p1_log_00fad7e7a567603f45e13ab",
        "login": "p1_log_00c59f2b74896e4086c2fe6",
        "hold": "",
        "txn": "",
        "terminalTxn": "",
        "entity": "p1_ent_00c1ff2d61b43ffab63cec5",
        "type": "release",
        "note": "Raised HT limit",
        "data": "",
        "inactive": 0,
        "frozen": 0,
        "pinned": 0,
        "pinnedDate": "2025-03-04 09:55:27"
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


# Get Notes

Query a Notes resource that represents risk management notes, reviews, and releases for a Hold, Txn, and Entity specific data.

```python
def get_notes(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`NotesResponseResult`](../../doc/models/notes-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = notes_controller.get_notes(
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
        "id": "p1_not_00c5a2ff6ba148fbfd20acc",
        "created": "2025-03-03 07:39:27.4554",
        "modified": "2025-03-03 07:39:27.4554",
        "creator": "p1_log_00fad7e7a567603f45e13ab",
        "modifier": "p1_log_00fad7e7a567603f45e13ab",
        "login": "p1_log_00c59f2b74896e4086c2fe6",
        "hold": "",
        "txn": "",
        "terminalTxn": "",
        "entity": "p1_ent_00c1ff2d61b43ffab63cec5",
        "type": "release",
        "note": "Raised HT limit",
        "data": "",
        "inactive": 0,
        "frozen": 0,
        "pinned": 0,
        "pinnedDate": "2025-03-04 09:55:27"
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


# Post Notes

Create a Notes resource that represents risk management notes, reviews, and releases for a Hold, Txn, and Entity-specific data.

```python
def post_notes(self,
              body,
              request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`NotesPostRequest`](../../doc/models/notes-post-request.md) | Body, Required | Create Note Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`NotesResponseResult`](../../doc/models/notes-response-result.md).

## Example Usage

```python
body = NotesPostRequest(
    mtype=NoteTypeEnum.NOTE,
    login='p1_log_00c59f2b74896e4086c2fe6',
    txn='t1_txn_67ea9ac271f195a95059550',
    terminal_txn='identifier',
    hold='t1_hld_67e08f086e275ddcc8820e1',
    entity='p1_ent_00c1ff2d61b43ffab63cec5',
    data='amexSales',
    note='Raised HT limit',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = notes_controller.post_notes(
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
        "id": "p1_not_00c5a2ff6ba148fbfd20acc",
        "created": "2025-03-03 07:39:27.4554",
        "modified": "2025-03-03 07:39:27.4554",
        "creator": "p1_log_00fad7e7a567603f45e13ab",
        "modifier": "p1_log_00fad7e7a567603f45e13ab",
        "login": "p1_log_00c59f2b74896e4086c2fe6",
        "hold": "",
        "txn": "",
        "terminalTxn": "",
        "entity": "p1_ent_00c1ff2d61b43ffab63cec5",
        "type": "release",
        "note": "Raised HT limit",
        "data": "",
        "inactive": 0,
        "frozen": 0,
        "pinned": 0,
        "pinnedDate": "2025-03-04 09:55:27"
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

