# Tickets

The tickets endpoint is used as a single use cc only token generation endpoint. If there is a need to store card numbers with cvv for a one time use, then this is the endpoint to perform that task.  Transactions run with the generated ticket_id can save card information for later with save_account.

```python
tickets_controller = client.tickets
```

## Class Name

`TicketsController`

## Methods

* [Create a Ticket Record](../../doc/controllers/tickets.md#create-a-ticket-record)
* [List All Tickets Related](../../doc/controllers/tickets.md#list-all-tickets-related)
* [View Single Ticket Record](../../doc/controllers/tickets.md#view-single-ticket-record)


# Create a Ticket Record

```python
def create_a_ticket_record(self,
                          body,
                          expand=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`V1TicketsRequest`](../../doc/models/v1-tickets-request.md) | Body, Required | - |
| `expand` | [`List[Expand41Enum]`](../../doc/models/expand-41-enum.md) | Query, Optional | Most endpoints in the API have a way to retrieve extra data related to the current record being retrieved. For example, if the API request is for the accountvaults endpoint, and the end user also needs to know which contact the token belongs to, this data can be returned in the accountvaults endpoint request.<br><br>**Constraints**: *Unique Items Required*, *Pattern*: `^[\w]+$` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ResponseTicket`](../../doc/models/response-ticket.md).

## Example Usage

```python
body = V1TicketsRequest(
    exp_date='0722',
    account_number='545454545454545',
    account_holder_name='John Smith',
    contact_id='11e95f8ec39de8fbdb0a4f1a'
)

result = tickets_controller.create_a_ticket_record(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "type": "Ticket",
  "data": {
    "account_holder_name": "John Smith",
    "exp_date": "0722",
    "cvv": null,
    "account_number": "545454545454545",
    "billing_address": {
      "postal_code": "48375"
    },
    "contact_id": "11e95f8ec39de8fbdb0a4f1a",
    "location_api_id": null,
    "id": "11e95f8ec39de8fbdb0a4f1a",
    "created_ts": 1422040992,
    "created_user_id": "11e95f8ec39de8fbdb0a4f1a"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`Response401tokenException`](../../doc/models/response-401-token-exception.md) |
| 412 | Precondition Failed | [`Response412Exception`](../../doc/models/response-412-exception.md) |


# List All Tickets Related

```python
def list_all_tickets_related(self,
                            page=None,
                            order=None,
                            filter_by=None,
                            expand=None,
                            format=None,
                            typeahead=None,
                            fields=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | [`Page`](../../doc/models/page.md) | Query, Optional | Use this field to specify paginate your results, by using page size and number. You can use one of the following methods:<br><br>> /endpoint?page={ "number": 1, "size": 50 }<br>> <br>> /endpoint?page[number]=1&page[size]=50 |
| `order` | [`List[Order19]`](../../doc/models/order-19.md) | Query, Optional | Criteria used in query string parameters to order results.  Most fields from the endpoint results can be used as a `key`.  Unsupported fields or operators will return a `412`.  Must be encoded, or use syntax that does not require encoding.<br><br>> /endpoint?order[0][key]=created_ts&order[0][operator]=asc<br>> <br>> /endpoint?order=[{ "key": "created_ts", "operator": "asc"}]<br>> <br>> /endpoint?order=[{ "key": "balance", "operator": "desc"},{ "key": "created_ts", "operator": "asc"}]<br><br>**Constraints**: *Minimum Items*: `1` |
| `filter_by` | [`List[FilterBy]`](../../doc/models/filter-by.md) | Query, Optional | Filter criteria that can be used in query string parameters.  Most fields from the endpoint results can be used as a `key`.  Unsupported fields or operators will return a `412`. Must be encoded, or use syntax that does not require encoding.<br><br>> ?filter_by[0][key]=first_name&filter_by[0][operator]==&filter_by[0][value]=Steve<br>> <br>> /endpoint?filter_by=[{ "key": "first_name", "operator": "=", "value": "Fred" }]<br>> <br>> /endpoint?filter_by=[{ "key": "account_type", "operator": "=", "value": "VISA" }]<br>> <br>> /endpoint?filter_by=[{ "key": "created_ts", "operator": ">=", "value": "946702799" }, { "key": "created_ts", "operator": "<=", value: "1695061891" }]<br>> <br>> /endpoint?filter_by=[{ "key": "last_name", "operator": "IN", "value": "Williams,Brown,Allman" }]<br><br>**Constraints**: *Minimum Items*: `1` |
| `expand` | [`List[Expand41Enum]`](../../doc/models/expand-41-enum.md) | Query, Optional | Most endpoints in the API have a way to retrieve extra data related to the current record being retrieved. For example, if the API request is for the accountvaults endpoint, and the end user also needs to know which contact the token belongs to, this data can be returned in the accountvaults endpoint request.<br><br>**Constraints**: *Unique Items Required*, *Pattern*: `^[\w]+$` |
| `format` | [`Format1Enum`](../../doc/models/format-1-enum.md) | Query, Optional | Reporting format, valid values: csv, tsv |
| `typeahead` | `str` | Query, Optional | You can use any `field_name` from this endpoint results to order the list using the value provided as filter for the same `field_name`. It will be ordered using the following rules: 1) Exact match, 2) Starts with, 3) Contains. |
| `fields` | [`List[Field47Enum]`](../../doc/models/field-47-enum.md) | Query, Optional | You can use any `field_name` from this endpoint results to filter the list of fields returned on the response. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ResponseTicketsCollection`](../../doc/models/response-tickets-collection.md).

## Example Usage

```python
page = Page(
    number=1,
    size=50
)

order = [
    Order19(
        key='first_name',
        operator=OperatorEnum.ASC
    )
]

filter_by = [
    FilterBy(
        key='first_name',
        operator=Operator1Enum.ENUM_1,
        value='Fred'
    )
]

result = tickets_controller.list_all_tickets_related(
    page=page,
    order=order,
    filter_by=filter_by
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "type": "TicketsCollection",
  "list": [
    {
      "account_holder_name": "John Smith",
      "exp_date": "0722",
      "cvv": null,
      "account_number": "545454545454545",
      "billing_address": {
        "postal_code": "48375"
      },
      "contact_id": "11e95f8ec39de8fbdb0a4f1a",
      "location_api_id": null,
      "id": "11e95f8ec39de8fbdb0a4f1a",
      "created_ts": 1422040992,
      "created_user_id": "11e95f8ec39de8fbdb0a4f1a"
    }
  ],
  "links": {
    "type": "Links",
    "first": "/v1/endpoint?page[size]=10&page[number]=1",
    "previous": "/v1/endpoint?page[size]=10&page[number]=5",
    "next": "/v1/endpoint?page[size]=10&page[number]=7",
    "last": "/v1/endpoint?page[size]=10&page[number]=42"
  },
  "pagination": {
    "type": "Pagination",
    "total_count": 423,
    "page_count": 42,
    "page_number": 6,
    "page_size": 10
  },
  "sort": {
    "type": "Sorting",
    "fields": [
      {
        "field": "last_name",
        "order": "asc"
      }
    ]
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`Response401tokenException`](../../doc/models/response-401-token-exception.md) |


# View Single Ticket Record

```python
def view_single_ticket_record(self,
                             ticket_id,
                             expand=None,
                             fields=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ticket_id` | `str` | Template, Required | A unique, system-generated identifier for the Ticket.<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `expand` | [`List[Expand41Enum]`](../../doc/models/expand-41-enum.md) | Query, Optional | Most endpoints in the API have a way to retrieve extra data related to the current record being retrieved. For example, if the API request is for the accountvaults endpoint, and the end user also needs to know which contact the token belongs to, this data can be returned in the accountvaults endpoint request.<br><br>**Constraints**: *Unique Items Required*, *Pattern*: `^[\w]+$` |
| `fields` | [`List[Field47Enum]`](../../doc/models/field-47-enum.md) | Query, Optional | You can use any `field_name` from this endpoint results to filter the list of fields returned on the response. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ResponseTicket`](../../doc/models/response-ticket.md).

## Example Usage

```python
ticket_id = '11e95f8ec39de8fbdb0a4f1a'

result = tickets_controller.view_single_ticket_record(ticket_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "type": "Ticket",
  "data": {
    "account_holder_name": "John Smith",
    "exp_date": "0722",
    "cvv": null,
    "account_number": "545454545454545",
    "billing_address": {
      "postal_code": "48375"
    },
    "contact_id": "11e95f8ec39de8fbdb0a4f1a",
    "location_api_id": null,
    "id": "11e95f8ec39de8fbdb0a4f1a",
    "created_ts": 1422040992,
    "created_user_id": "11e95f8ec39de8fbdb0a4f1a"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`Response401tokenException`](../../doc/models/response-401-token-exception.md) |

