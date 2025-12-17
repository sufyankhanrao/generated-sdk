# Contacts

A contact reflects a known, valid individual registered as a contact for the entity. It is purely informational and not a required record.

```python
contacts_controller = client.contacts
```

## Class Name

`ContactsController`

## Methods

* [Get Contacts Id](../../doc/controllers/contacts.md#get-contacts-id)
* [Put Contacts Id](../../doc/controllers/contacts.md#put-contacts-id)
* [Delete Contacts Id](../../doc/controllers/contacts.md#delete-contacts-id)
* [Get Contacts](../../doc/controllers/contacts.md#get-contacts)
* [Post Contacts](../../doc/controllers/contacts.md#post-contacts)


# Get Contacts Id

Query a Contact, which represents an individual who is associated with an Entity.

```python
def get_contacts_id(self,
                   id,
                   request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this contact. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ContactsResponseResult`](../../doc/models/contacts-response-result.md).

## Example Usage

```python
id = 't1_con_665f696f0d66c3281d00000'

request_token = '20250423-yourmerchant-refunds-001'

result = contacts_controller.get_contacts_id(
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
        "id": "t1_con_665f696f0d66c3281d00000",
        "created": "2024-06-04 15:22:23.0592",
        "modified": "2024-06-04 15:22:23.0592",
        "creator": "t1_log_5d263a0050fcc8fb784a957",
        "modifier": "t1_log_5d263a0050fcc8fb784a957",
        "entity": "t1_ent_665e13ff8b2e613134b9273",
        "first": "John",
        "middle": "",
        "last": "Doe",
        "description": "",
        "email": "JohnD@payr.com",
        "fax": "",
        "phone": "",
        "country": "USA",
        "zip": "",
        "state": "AK",
        "city": "",
        "address2": "",
        "address1": "",
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


# Put Contacts Id

Update a Contact, A Contact resource represents an individual who is associated with an Entity.

```python
def put_contacts_id(self,
                   id,
                   body,
                   request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this contact. |
| `body` | [`ContactsPutRequest`](../../doc/models/contacts-put-request.md) | Body, Required | Update Contact Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ContactsResponseResult`](../../doc/models/contacts-response-result.md).

## Example Usage

```python
id = 't1_con_665f696f0d66c3281d00000'

body = ContactsPutRequest(
    entity='t1_ent_665e13ff8b2e613134b9273',
    first='first name',
    middle='middle name',
    last='last name',
    description='description of Contact',
    email='fewafehwuohfewafewafewa@payrjfhuiweafewa.com',
    address_1='first line of the address',
    address_2='second line of the address',
    city='Anchorage',
    state='AK',
    zip='99501',
    country=CountryEnum.USA,
    phone='1234567890',
    fax='1234567890',
    frozen=FrozenEnum.NOTFROZEN,
    inactive=InactiveEnum.ACTIVE
)

request_token = '20250423-yourmerchant-refunds-001'

result = contacts_controller.put_contacts_id(
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
        "id": "t1_con_665f696f0d66c3281d00000",
        "created": "2024-06-04 15:22:23.0592",
        "modified": "2024-06-04 15:22:23.0592",
        "creator": "t1_log_5d263a0050fcc8fb784a957",
        "modifier": "t1_log_5d263a0050fcc8fb784a957",
        "entity": "t1_ent_665e13ff8b2e613134b9273",
        "first": "John",
        "middle": "",
        "last": "Doe",
        "description": "",
        "email": "JohnD@payr.com",
        "fax": "",
        "phone": "",
        "country": "USA",
        "zip": "",
        "state": "AK",
        "city": "",
        "address2": "",
        "address1": "",
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


# Delete Contacts Id

Delete a Contact. A Contact resource represents an individual who is associated with an Entity.

```python
def delete_contacts_id(self,
                      id,
                      request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this contact. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ContactsResponseResult`](../../doc/models/contacts-response-result.md).

## Example Usage

```python
id = 't1_con_665f696f0d66c3281d00000'

request_token = '20250423-yourmerchant-refunds-001'

result = contacts_controller.delete_contacts_id(
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
        "id": "t1_con_665f696f0d66c3281d00000",
        "created": "2024-06-04 15:22:23.0592",
        "modified": "2024-06-04 15:22:23.0592",
        "creator": "t1_log_5d263a0050fcc8fb784a957",
        "modifier": "t1_log_5d263a0050fcc8fb784a957",
        "entity": "t1_ent_665e13ff8b2e613134b9273",
        "first": "John",
        "middle": "",
        "last": "Doe",
        "description": "",
        "email": "JohnD@payr.com",
        "fax": "",
        "phone": "",
        "country": "USA",
        "zip": "",
        "state": "AK",
        "city": "",
        "address2": "",
        "address1": "",
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


# Get Contacts

Query a Contact, which represents an individual who is associated with an Entity.

```python
def get_contacts(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ContactsResponseResult`](../../doc/models/contacts-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = contacts_controller.get_contacts(
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
        "id": "t1_con_665f696f0d66c3281d00000",
        "created": "2024-06-04 15:22:23.0592",
        "modified": "2024-06-04 15:22:23.0592",
        "creator": "t1_log_5d263a0050fcc8fb784a957",
        "modifier": "t1_log_5d263a0050fcc8fb784a957",
        "entity": "t1_ent_665e13ff8b2e613134b9273",
        "first": "John",
        "middle": "",
        "last": "Doe",
        "description": "",
        "email": "JohnD@payr.com",
        "fax": "",
        "phone": "",
        "country": "USA",
        "zip": "",
        "state": "AK",
        "city": "",
        "address2": "",
        "address1": "",
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


# Post Contacts

Create a Contact.
A Contact resource represents an individual who is associated with an Entity.

```python
def post_contacts(self,
                 body,
                 request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ContactsPostRequest`](../../doc/models/contacts-post-request.md) | Body, Required | Create Contact Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ContactsResponseResult`](../../doc/models/contacts-response-result.md).

## Example Usage

```python
body = ContactsPostRequest(
    entity='t1_ent_665e13ff8b2e613134b9273',
    first='first name',
    last='last name',
    email='fewafehwuohfewafewafewa@payrjfhuiweafewa.com',
    frozen=FrozenEnum.NOTFROZEN,
    inactive=InactiveEnum.ACTIVE,
    middle='middle name',
    description='description of Contact',
    address_1='first line of the address',
    address_2='second line of the address',
    city='Anchorage',
    state='AK',
    zip='99501',
    country=CountryEnum.USA,
    phone='1234567890',
    fax='1234567890'
)

request_token = '20250423-yourmerchant-refunds-001'

result = contacts_controller.post_contacts(
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
        "id": "t1_con_665f696f0d66c3281d00000",
        "created": "2024-06-04 15:22:23.0592",
        "modified": "2024-06-04 15:22:23.0592",
        "creator": "t1_log_5d263a0050fcc8fb784a957",
        "modifier": "t1_log_5d263a0050fcc8fb784a957",
        "entity": "t1_ent_665e13ff8b2e613134b9273",
        "first": "John",
        "middle": "",
        "last": "Doe",
        "description": "",
        "email": "JohnD@payr.com",
        "fax": "",
        "phone": "",
        "country": "USA",
        "zip": "",
        "state": "AK",
        "city": "",
        "address2": "",
        "address1": "",
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

