# Entities

Entities are portion of a single facilitator, vendor or merchant. Common business-related details for each type of entity are stored here (like name and address) as well as management details (like which login the entity belongs to). ny kind of business within the Payrix Pro API (like board merchants as a facilitator, capture fees as a vendor or accept payments as a merchant) an entity record is required.

```python
entities_controller = client.entities
```

## Class Name

`EntitiesController`

## Methods

* [Get Entities](../../doc/controllers/entities.md#get-entities)
* [Post Entities](../../doc/controllers/entities.md#post-entities)
* [Get Entities Id](../../doc/controllers/entities.md#get-entities-id)
* [Put Entities Id](../../doc/controllers/entities.md#put-entities-id)
* [Delete Entities Id](../../doc/controllers/entities.md#delete-entities-id)


# Get Entities

Query entities. An Entity is the top-level resource of a business in the API, describing the details of that business in its fields. Each entity can describe a Merchant, a Partner, or a Facilitator (payment facilitator).

```python
def get_entities(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`EntitiesResponseResult`](../../doc/models/entities-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = entities_controller.get_entities(
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
        "id": "t1_ent_6733015a977c2cdd6277d00",
        "created": "2024-11-12 02:18:50.6207",
        "modified": "2024-11-12 02:22:57.3301",
        "creator": "t1_log_5f875c53ed397f57c0afc90",
        "modifier": "t1_log_6733015a79f48410904564b",
        "ipCreated": "134.238.16.164",
        "ipModified": "134.238.16.164",
        "clientIp": "",
        "login": "t1_log_6733015a79f48410904564b",
        "parameter": "",
        "type": 6,
        "name": "Splash LLC",
        "address1": "1234 Rivver Lane",
        "address2": "San house Fremont",
        "city": "Frisco",
        "state": "NB",
        "zip": "75034",
        "country": "USA",
        "timezone": "cst",
        "phone": "995685660000",
        "fax": "",
        "email": "ankit0911@gmail.com",
        "website": "http://payrix.com",
        "ein": "678912345",
        "tcVersion": "1.0",
        "tcDate": "2024-11-12 02:18:50",
        "tcIp": "134.238.16.164",
        "tcAcceptDate": "202204281403",
        "tcAcceptIp": "162.250.123.158",
        "custom": "62",
        "inactive": 0,
        "frozen": 0,
        "tinStatus": 0,
        "reserved": 0,
        "checkStage": "postboard",
        "public": 1,
        "customerPhone": "",
        "locations": 1,
        "industry": "",
        "displayName": "",
        "totalCreditDisbursements": 0,
        "payoutSecondaryDescriptor": "",
        "einType": "ssn",
        "irsFilingName": "",
        "currency": "USD",
        "globalBusinessId": "678912345",
        "globalBusinessType": "ssn",
        "pendingRiskCheck": "pending"
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


# Post Entities

Create an Entity, the top-level resource of a business in the API, describing its details through fields. An entity can represent a Merchant, a Partner, or a Facilitator (payment facilitator).

```python
def post_entities(self,
                 body,
                 request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`EntitiesPostRequest`](../../doc/models/entities-post-request.md) | Body, Required | Create Entity Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`EntitiesResponseResult`](../../doc/models/entities-response-result.md).

## Example Usage

```python
body = EntitiesPostRequest(
    client_ip='152.58.83.44',
    login='t1_log_6733015a79f48410904564b',
    mtype=EntityTypeEnum.GOV,
    name='Splash LLC',
    address_1='1234 Rivver Lane',
    city='Frisco',
    state='TX',
    zip='75034',
    country=EntityCountryEnum.USA,
    timezone=TimezoneEnum.CST,
    phone='995685662566',
    email='rawatankit0911@gmail.com',
    ein='678912345',
    locations=1,
    public=EntitiesPublicEnum.PUBLICENTITY,
    global_business_id='678912345',
    frozen=FrozenEnum.NOTFROZEN,
    inactive=InactiveEnum.ACTIVE,
    display_name='John',
    address_2='San house Fremont',
    customer_phone='995685662566',
    fax='995685662566',
    website='http://payrix.com',
    ein_type=EinTypeEnum.SSN,
    irs_filing_name='Integration Test 2025-02-21T09:12:15.332',
    tc_version='1.0',
    tc_accept_date='202204281403',
    tc_accept_ip='162.250.123.158',
    custom='voluptatibus et accusamus',
    payout_secondary_descriptor='Apex Leadership',
    industry='Residential Painting',
    global_business_type=GlobalBusinessTypeEnum.SSN
)

request_token = '20250423-yourmerchant-refunds-001'

result = entities_controller.post_entities(
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
        "id": "t1_ent_6733015a977c2cdd6277d00",
        "created": "2024-11-12 02:18:50.6207",
        "modified": "2024-11-12 02:22:57.3301",
        "creator": "t1_log_5f875c53ed397f57c0afc90",
        "modifier": "t1_log_6733015a79f48410904564b",
        "ipCreated": "134.238.16.164",
        "ipModified": "134.238.16.164",
        "clientIp": "",
        "login": "t1_log_6733015a79f48410904564b",
        "parameter": "",
        "type": 6,
        "name": "Splash LLC",
        "address1": "1234 Rivver Lane",
        "address2": "San house Fremont",
        "city": "Frisco",
        "state": "NB",
        "zip": "75034",
        "country": "USA",
        "timezone": "cst",
        "phone": "995685660000",
        "fax": "",
        "email": "ankit0911@gmail.com",
        "website": "http://payrix.com",
        "ein": "678912345",
        "tcVersion": "1.0",
        "tcDate": "2024-11-12 02:18:50",
        "tcIp": "134.238.16.164",
        "tcAcceptDate": "202204281403",
        "tcAcceptIp": "162.250.123.158",
        "custom": "62",
        "inactive": 0,
        "frozen": 0,
        "tinStatus": 0,
        "reserved": 0,
        "checkStage": "postboard",
        "public": 1,
        "customerPhone": "",
        "locations": 1,
        "industry": "",
        "displayName": "",
        "totalCreditDisbursements": 0,
        "payoutSecondaryDescriptor": "",
        "einType": "ssn",
        "irsFilingName": "",
        "currency": "USD",
        "globalBusinessId": "678912345",
        "globalBusinessType": "ssn",
        "pendingRiskCheck": "pending"
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


# Get Entities Id

Query an Entity, which is the top-level resource of a business in the API and describes the details of that business in its fields. An Entity can describe a Merchant, a Partner, or a Facilitator (payment facilitator).

```python
def get_entities_id(self,
                   id,
                   request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this entity. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`EntitiesResponseResult`](../../doc/models/entities-response-result.md).

## Example Usage

```python
id = 't1_ent_6733015a977c2cdd6277d89'

request_token = '20250423-yourmerchant-refunds-001'

result = entities_controller.get_entities_id(
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
        "id": "t1_ent_6733015a977c2cdd6277d00",
        "created": "2024-11-12 02:18:50.6207",
        "modified": "2024-11-12 02:22:57.3301",
        "creator": "t1_log_5f875c53ed397f57c0afc90",
        "modifier": "t1_log_6733015a79f48410904564b",
        "ipCreated": "134.238.16.164",
        "ipModified": "134.238.16.164",
        "clientIp": "",
        "login": "t1_log_6733015a79f48410904564b",
        "parameter": "",
        "type": 6,
        "name": "Splash LLC",
        "address1": "1234 Rivver Lane",
        "address2": "San house Fremont",
        "city": "Frisco",
        "state": "NB",
        "zip": "75034",
        "country": "USA",
        "timezone": "cst",
        "phone": "995685660000",
        "fax": "",
        "email": "ankit0911@gmail.com",
        "website": "http://payrix.com",
        "ein": "678912345",
        "tcVersion": "1.0",
        "tcDate": "2024-11-12 02:18:50",
        "tcIp": "134.238.16.164",
        "tcAcceptDate": "202204281403",
        "tcAcceptIp": "162.250.123.158",
        "custom": "62",
        "inactive": 0,
        "frozen": 0,
        "tinStatus": 0,
        "reserved": 0,
        "checkStage": "postboard",
        "public": 1,
        "customerPhone": "",
        "locations": 1,
        "industry": "",
        "displayName": "",
        "totalCreditDisbursements": 0,
        "payoutSecondaryDescriptor": "",
        "einType": "ssn",
        "irsFilingName": "",
        "currency": "USD",
        "globalBusinessId": "678912345",
        "globalBusinessType": "ssn",
        "pendingRiskCheck": "pending"
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


# Put Entities Id

Update an Entity, which is the top-level resource of a business in the API and describes the details of that business in its fields. An Entity can be a Merchant, a Partner, or a Facilitator (payment facilitator).

```python
def put_entities_id(self,
                   id,
                   body,
                   request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this entity. |
| `body` | [`EntitiesPutRequest`](../../doc/models/entities-put-request.md) | Body, Required | Update Entity Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`EntitiesResponseResult`](../../doc/models/entities-response-result.md).

## Example Usage

```python
id = 't1_ent_6733015a977c2cdd6277d89'

body = EntitiesPutRequest(
    client_ip='152.58.83.44',
    login='t1_log_6733015a79f48410904564b',
    mtype=EntityTypeEnum.GOV,
    name='Splash LLC',
    display_name='John',
    address_1='1234 Rivver Lane',
    address_2='San house Fremont',
    city='Frisco',
    state='TX',
    zip='75034',
    country=EntityCountryEnum.USA,
    timezone=TimezoneEnum.CST,
    phone='995685662566',
    customer_phone='995685662566',
    fax='995685662566',
    email='rawatankit0911@gmail.com',
    website='http://payrix.com',
    ein_type=EinTypeEnum.SSN,
    irs_filing_name='Integration Test 2025-02-21T09:12:15.332',
    ein='678912345',
    locations=1,
    public=EntitiesPublicEnum.PUBLICENTITY,
    tc_version='1.0',
    tc_accept_date='202204281403',
    tc_accept_ip='162.250.123.158',
    custom='voluptatibus et accusamus',
    payout_secondary_descriptor='Apex Leadership',
    industry='Residential Painting',
    global_business_type=GlobalBusinessTypeEnum.SSN,
    global_business_id='678912345',
    frozen=FrozenEnum.NOTFROZEN,
    inactive=InactiveEnum.ACTIVE
)

request_token = '20250423-yourmerchant-refunds-001'

result = entities_controller.put_entities_id(
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
        "id": "t1_ent_6733015a977c2cdd6277d00",
        "created": "2024-11-12 02:18:50.6207",
        "modified": "2024-11-12 02:22:57.3301",
        "creator": "t1_log_5f875c53ed397f57c0afc90",
        "modifier": "t1_log_6733015a79f48410904564b",
        "ipCreated": "134.238.16.164",
        "ipModified": "134.238.16.164",
        "clientIp": "",
        "login": "t1_log_6733015a79f48410904564b",
        "parameter": "",
        "type": 6,
        "name": "Splash LLC",
        "address1": "1234 Rivver Lane",
        "address2": "San house Fremont",
        "city": "Frisco",
        "state": "NB",
        "zip": "75034",
        "country": "USA",
        "timezone": "cst",
        "phone": "995685660000",
        "fax": "",
        "email": "ankit0911@gmail.com",
        "website": "http://payrix.com",
        "ein": "678912345",
        "tcVersion": "1.0",
        "tcDate": "2024-11-12 02:18:50",
        "tcIp": "134.238.16.164",
        "tcAcceptDate": "202204281403",
        "tcAcceptIp": "162.250.123.158",
        "custom": "62",
        "inactive": 0,
        "frozen": 0,
        "tinStatus": 0,
        "reserved": 0,
        "checkStage": "postboard",
        "public": 1,
        "customerPhone": "",
        "locations": 1,
        "industry": "",
        "displayName": "",
        "totalCreditDisbursements": 0,
        "payoutSecondaryDescriptor": "",
        "einType": "ssn",
        "irsFilingName": "",
        "currency": "USD",
        "globalBusinessId": "678912345",
        "globalBusinessType": "ssn",
        "pendingRiskCheck": "pending"
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


# Delete Entities Id

Delete an Entity, which is the top-level resource of a business in the API and describes the details of that business in its fields, including a Merchant, a Partner, or a Facilitator (payment facilitator).

```python
def delete_entities_id(self,
                      id,
                      request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this entity. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`EntitiesResponseResult`](../../doc/models/entities-response-result.md).

## Example Usage

```python
id = 't1_ent_6733015a977c2cdd6277d89'

request_token = '20250423-yourmerchant-refunds-001'

result = entities_controller.delete_entities_id(
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
        "id": "t1_ent_6733015a977c2cdd6277d00",
        "created": "2024-11-12 02:18:50.6207",
        "modified": "2024-11-12 02:22:57.3301",
        "creator": "t1_log_5f875c53ed397f57c0afc90",
        "modifier": "t1_log_6733015a79f48410904564b",
        "ipCreated": "134.238.16.164",
        "ipModified": "134.238.16.164",
        "clientIp": "",
        "login": "t1_log_6733015a79f48410904564b",
        "parameter": "",
        "type": 6,
        "name": "Splash LLC",
        "address1": "1234 Rivver Lane",
        "address2": "San house Fremont",
        "city": "Frisco",
        "state": "NB",
        "zip": "75034",
        "country": "USA",
        "timezone": "cst",
        "phone": "995685660000",
        "fax": "",
        "email": "ankit0911@gmail.com",
        "website": "http://payrix.com",
        "ein": "678912345",
        "tcVersion": "1.0",
        "tcDate": "2024-11-12 02:18:50",
        "tcIp": "134.238.16.164",
        "tcAcceptDate": "202204281403",
        "tcAcceptIp": "162.250.123.158",
        "custom": "62",
        "inactive": 0,
        "frozen": 0,
        "tinStatus": 0,
        "reserved": 0,
        "checkStage": "postboard",
        "public": 1,
        "customerPhone": "",
        "locations": 1,
        "industry": "",
        "displayName": "",
        "totalCreditDisbursements": 0,
        "payoutSecondaryDescriptor": "",
        "einType": "ssn",
        "irsFilingName": "",
        "currency": "USD",
        "globalBusinessId": "678912345",
        "globalBusinessType": "ssn",
        "pendingRiskCheck": "pending"
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

