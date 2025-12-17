# Statement Entry

```python
statement_entry_controller = client.statement_entry
```

## Class Name

`StatementEntryController`

## Methods

* [Get Statement Entries Id](../../doc/controllers/statement-entry.md#get-statement-entries-id)
* [Get Statement Entries](../../doc/controllers/statement-entry.md#get-statement-entries)


# Get Statement Entries Id

Query a StatementEntry resource. A StatementEntry resource represents a record of funds owed for a billing schedule.

```python
def get_statement_entries_id(self,
                            id,
                            request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this statement entry. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`StatementEntriesResponseResult`](../../doc/models/statement-entries-response-result.md).

## Example Usage

```python
id = 't1_ste_67a18bcde1a1b2ec3d9c9az'

request_token = '20250423-yourmerchant-refunds-001'

result = statement_entry_controller.get_statement_entries_id(
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
        "id": "t1_ste_67a18bcde1a1b2ec3d9c9az",
        "created": "2025-01-31 08:42:16.7318",
        "modified": "2025-01-31 08:42:16.7318",
        "creator": "t1_log_0092b50e8812b18e41d511s",
        "modifier": "t1_log_0092b50e8812b18e41d511s",
        "onentity": "t1_ent_5603d7c605d246c48c43fb5",
        "billing": "t1_bil_09506bd083f5dc8539d3a4f",
        "statement": "p1_stm_0088a64f48d47e4e0c8012c",
        "fee": "t1_fee_90fafb488200de80848de1e",
        "profitShare": "",
        "event": 6,
        "eventId": "t1_txn_98ca80b33efecf1b1c5f807",
        "description": "AUTH fee schedule",
        "amount": 30,
        "deductedFromBalance": 0,
        "entity": "t1_ent_1103d7c605d246c48c43fb5",
        "forentity": "t1_ent_110d5f86c965eb277f498d8",
        "originalEventId": "t1_txn_00ca80b33efecf1b1c5d807",
        "originalEvent": 7,
        "revShareStatement": ""
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


# Get Statement Entries

Query a StatementEntry resource.
A StatementEntry resource represents a record of funds owed for a billing schedule.
For example, this could be a scheduled weekly or monthly fee, or an event-based activity such as a capture or payout fee.

```python
def get_statement_entries(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`StatementEntriesResponseResult`](../../doc/models/statement-entries-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = statement_entry_controller.get_statement_entries(
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
        "id": "t1_ste_67a18bcde1a1b2ec3d9c9az",
        "created": "2025-01-31 08:42:16.7318",
        "modified": "2025-01-31 08:42:16.7318",
        "creator": "t1_log_0092b50e8812b18e41d511s",
        "modifier": "t1_log_0092b50e8812b18e41d511s",
        "onentity": "t1_ent_5603d7c605d246c48c43fb5",
        "billing": "t1_bil_09506bd083f5dc8539d3a4f",
        "statement": "p1_stm_0088a64f48d47e4e0c8012c",
        "fee": "t1_fee_90fafb488200de80848de1e",
        "profitShare": "",
        "event": 6,
        "eventId": "t1_txn_98ca80b33efecf1b1c5f807",
        "description": "AUTH fee schedule",
        "amount": 30,
        "deductedFromBalance": 0,
        "entity": "t1_ent_1103d7c605d246c48c43fb5",
        "forentity": "t1_ent_110d5f86c965eb277f498d8",
        "originalEventId": "t1_txn_00ca80b33efecf1b1c5d807",
        "originalEvent": 7,
        "revShareStatement": ""
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

