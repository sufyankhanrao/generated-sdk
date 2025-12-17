# Members

A member represents a control or beneficiary member of the entity. At least one primary member record is required for merchant boarding.

```python
members_controller = client.members
```

## Class Name

`MembersController`

## Methods

* [Get Members Id](../../doc/controllers/members.md#get-members-id)
* [Put Members Id](../../doc/controllers/members.md#put-members-id)
* [Delete Members Id](../../doc/controllers/members.md#delete-members-id)
* [Get Members](../../doc/controllers/members.md#get-members)
* [Post Members](../../doc/controllers/members.md#post-members)


# Get Members Id

Query a Member. A Member is a person who is associated with a Merchant; One Member associated with each Merchant can be the 'primary' Member, meaning the Member with the most share of ownership in the Merchant.

```python
def get_members_id(self,
                  id,
                  request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this member. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`MembersResponseResult`](../../doc/models/members-response-result.md).

## Example Usage

```python
id = 't1_mbr_67d0336c01048ea41c4382z'

request_token = '20250423-yourmerchant-refunds-001'

result = members_controller.get_members_id(
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
        "id": "t1_mbr_67d0336c01048ea41c4382z",
        "created": "2025-03-11 08:58:20.0258",
        "modified": "2025-03-11 08:58:20.0258",
        "creator": "g1577139c2304b7",
        "modifier": "g1577139c2304b7",
        "merchant": "t1_mer_67d033698c234e74c399ddd",
        "title": "CEO",
        "first": "Chad",
        "middle": "",
        "last": "Foster",
        "ssn": "1924",
        "dob": 20160120,
        "dl": "6679",
        "dlstate": "MD",
        "ownership": 10000,
        "email": "Jerrod_Glover@hotmail.com",
        "fax": "",
        "phone": "5106406000",
        "country": "MAR",
        "zip": "60064",
        "state": "MD",
        "city": "East Bettye",
        "address2": "",
        "address1": "83 Dan Ways",
        "primary": 1,
        "inactive": 0,
        "frozen": 0,
        "timezone": "est",
        "gender": "male",
        "creditScore": 334,
        "creditScoreDate": "2025-03-11 08:58:20",
        "significantResponsibility": 0,
        "politicallyExposed": 0,
        "citizenship": "MAR",
        "mailingAddress1": "",
        "mailingAddress2": "",
        "mailingCity": "",
        "mailingState": "MD",
        "mailingPostalCode": "",
        "mailingCountry": "MAR",
        "treasuryPrimeRoles": "",
        "facilitator": "",
        "vendor": "",
        "shareableUrl": "",
        "status": "",
        "createdAt": 1123,
        "completedAt": 1123,
        "plaidIdvId": "",
        "templateId": ""
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


# Put Members Id

Update a Member, A Member is a person who is associated with a Merchant, One Member associated with each Merchant can be the 'primary' Member, meaning the Member with the most share of ownership in the Merchant.

```python
def put_members_id(self,
                  id,
                  body,
                  request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this member. |
| `body` | [`MembersPutRequest`](../../doc/models/members-put-request.md) | Body, Required | Update Member Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`MembersResponseResult`](../../doc/models/members-response-result.md).

## Example Usage

```python
id = 't1_mbr_67d0336c01048ea41c4382z'

body = MembersPutRequest(
    merchant='t1_mer_67d033698c234e74c399ddd',
    title='CEO',
    first='Chad',
    middle='middle name',
    last='Foster',
    ssn='1924',
    citizenship=CitizenshipEnum.MAR,
    dob=20160120,
    gender=GenderEnum.MALE,
    dl='6679',
    dlstate='MD',
    email='Jerrod_Glover@hotmail.com',
    ownership=10000,
    primary=MembersPrimaryEnum.PRIMARYCONTACT,
    credit_score=334,
    credit_score_date='2025-03-11 08:58:20',
    significant_responsibility=SignificantResponsibilityEnum.NOSIGNIFICANTRESPONSIBILITY,
    politically_exposed=PoliticallyExposedEnum.NOTPOLITICALLYEXPOSED,
    mailing_address_1='mailing first line of address',
    mailing_address_2='mailing second line of address',
    mailing_city='mailing name of the city',
    mailing_state='MD',
    mailing_country=MailingCountryEnum.MAR,
    mailing_postal_code='mailing postal code',
    timezone=TimezoneEnum.EST,
    address_1='first line of address',
    address_2='second line of address',
    city='name of city',
    state='MD',
    zip='ZIP code',
    country=CountryEnum.MAR,
    phone='5106406000',
    fax='5106406000',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = members_controller.put_members_id(
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
        "id": "t1_mbr_67d0336c01048ea41c4382z",
        "created": "2025-03-11 08:58:20.0258",
        "modified": "2025-03-11 08:58:20.0258",
        "creator": "g1577139c2304b7",
        "modifier": "g1577139c2304b7",
        "merchant": "t1_mer_67d033698c234e74c399ddd",
        "title": "CEO",
        "first": "Chad",
        "middle": "",
        "last": "Foster",
        "ssn": "1924",
        "dob": 20160120,
        "dl": "6679",
        "dlstate": "MD",
        "ownership": 10000,
        "email": "Jerrod_Glover@hotmail.com",
        "fax": "",
        "phone": "5106406000",
        "country": "MAR",
        "zip": "60064",
        "state": "MD",
        "city": "East Bettye",
        "address2": "",
        "address1": "83 Dan Ways",
        "primary": 1,
        "inactive": 0,
        "frozen": 0,
        "timezone": "est",
        "gender": "male",
        "creditScore": 334,
        "creditScoreDate": "2025-03-11 08:58:20",
        "significantResponsibility": 0,
        "politicallyExposed": 0,
        "citizenship": "MAR",
        "mailingAddress1": "",
        "mailingAddress2": "",
        "mailingCity": "",
        "mailingState": "MD",
        "mailingPostalCode": "",
        "mailingCountry": "MAR",
        "treasuryPrimeRoles": "",
        "facilitator": "",
        "vendor": "",
        "shareableUrl": "",
        "status": "",
        "createdAt": 1123,
        "completedAt": 1123,
        "plaidIdvId": "",
        "templateId": ""
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


# Delete Members Id

Delete a Member. A Member is a person who is associated with a Merchant. One Member associated with each Merchant can be the 'primary' Member, meaning the Member with the most share of ownership in the Merchant.

```python
def delete_members_id(self,
                     id,
                     request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this member. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`MembersResponseResult`](../../doc/models/members-response-result.md).

## Example Usage

```python
id = 't1_mbr_67d0336c01048ea41c4382z'

request_token = '20250423-yourmerchant-refunds-001'

result = members_controller.delete_members_id(
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
        "id": "t1_mbr_67d0336c01048ea41c4382z",
        "created": "2025-03-11 08:58:20.0258",
        "modified": "2025-03-11 08:58:20.0258",
        "creator": "g1577139c2304b7",
        "modifier": "g1577139c2304b7",
        "merchant": "t1_mer_67d033698c234e74c399ddd",
        "title": "CEO",
        "first": "Chad",
        "middle": "",
        "last": "Foster",
        "ssn": "1924",
        "dob": 20160120,
        "dl": "6679",
        "dlstate": "MD",
        "ownership": 10000,
        "email": "Jerrod_Glover@hotmail.com",
        "fax": "",
        "phone": "5106406000",
        "country": "MAR",
        "zip": "60064",
        "state": "MD",
        "city": "East Bettye",
        "address2": "",
        "address1": "83 Dan Ways",
        "primary": 1,
        "inactive": 0,
        "frozen": 0,
        "timezone": "est",
        "gender": "male",
        "creditScore": 334,
        "creditScoreDate": "2025-03-11 08:58:20",
        "significantResponsibility": 0,
        "politicallyExposed": 0,
        "citizenship": "MAR",
        "mailingAddress1": "",
        "mailingAddress2": "",
        "mailingCity": "",
        "mailingState": "MD",
        "mailingPostalCode": "",
        "mailingCountry": "MAR",
        "treasuryPrimeRoles": "",
        "facilitator": "",
        "vendor": "",
        "shareableUrl": "",
        "status": "",
        "createdAt": 1123,
        "completedAt": 1123,
        "plaidIdvId": "",
        "templateId": ""
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


# Get Members

Query a Member, A Member being a person who is associated with a Merchant, and one Member associated with each Merchant can be the 'primary' Member, meaning the Member with the most share of ownership in the Merchant.

```python
def get_members(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`MembersResponseResult`](../../doc/models/members-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = members_controller.get_members(
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
        "id": "t1_mbr_67d0336c01048ea41c4382z",
        "created": "2025-03-11 08:58:20.0258",
        "modified": "2025-03-11 08:58:20.0258",
        "creator": "g1577139c2304b7",
        "modifier": "g1577139c2304b7",
        "merchant": "t1_mer_67d033698c234e74c399ddd",
        "title": "CEO",
        "first": "Chad",
        "middle": "",
        "last": "Foster",
        "ssn": "1924",
        "dob": 20160120,
        "dl": "6679",
        "dlstate": "MD",
        "ownership": 10000,
        "email": "Jerrod_Glover@hotmail.com",
        "fax": "",
        "phone": "5106406000",
        "country": "MAR",
        "zip": "60064",
        "state": "MD",
        "city": "East Bettye",
        "address2": "",
        "address1": "83 Dan Ways",
        "primary": 1,
        "inactive": 0,
        "frozen": 0,
        "timezone": "est",
        "gender": "male",
        "creditScore": 334,
        "creditScoreDate": "2025-03-11 08:58:20",
        "significantResponsibility": 0,
        "politicallyExposed": 0,
        "citizenship": "MAR",
        "mailingAddress1": "",
        "mailingAddress2": "",
        "mailingCity": "",
        "mailingState": "MD",
        "mailingPostalCode": "",
        "mailingCountry": "MAR",
        "treasuryPrimeRoles": "",
        "facilitator": "",
        "vendor": "",
        "shareableUrl": "",
        "status": "",
        "createdAt": 1123,
        "completedAt": 1123,
        "plaidIdvId": "",
        "templateId": ""
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


# Post Members

Create a Member. A Member is a person who is associated with a Merchant, and one Member associated with each Merchant can be the 'primary' Member, meaning the Member with the most share of ownership in the Merchant.

```python
def post_members(self,
                body,
                request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`MembersPostRequest`](../../doc/models/members-post-request.md) | Body, Required | Create Member Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`MembersResponseResult`](../../doc/models/members-response-result.md).

## Example Usage

```python
body = MembersPostRequest(
    merchant='t1_mer_67d033698c234e74c399ddd',
    first='Chad',
    last='Foster',
    dob=20160120,
    email='Jerrod_Glover@hotmail.com',
    ownership=10000,
    primary=MembersPrimaryEnum.PRIMARYCONTACT,
    significant_responsibility=SignificantResponsibilityEnum.NOSIGNIFICANTRESPONSIBILITY,
    politically_exposed=PoliticallyExposedEnum.NOTPOLITICALLYEXPOSED,
    timezone=TimezoneEnum.EST,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    title='CEO',
    middle='middle name',
    ssn='1924',
    citizenship=CitizenshipEnum.MAR,
    gender=GenderEnum.MALE,
    dl='6679',
    dlstate='MD',
    credit_score=334,
    credit_score_date='2025-03-11 08:58:20',
    mailing_address_1='mailing first line of address',
    mailing_address_2='mailing second line of address',
    mailing_city='mailing name of the city',
    mailing_state='MD',
    mailing_country=MailingCountryEnum.MAR,
    mailing_postal_code='mailing postal code',
    address_1='first line of address',
    address_2='second line of address',
    city='name of city',
    state='MD',
    zip='ZIP code',
    country=CountryEnum.MAR,
    phone='5106406000',
    fax='5106406000'
)

request_token = '20250423-yourmerchant-refunds-001'

result = members_controller.post_members(
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
        "id": "t1_mbr_67d0336c01048ea41c4382z",
        "created": "2025-03-11 08:58:20.0258",
        "modified": "2025-03-11 08:58:20.0258",
        "creator": "g1577139c2304b7",
        "modifier": "g1577139c2304b7",
        "merchant": "t1_mer_67d033698c234e74c399ddd",
        "title": "CEO",
        "first": "Chad",
        "middle": "",
        "last": "Foster",
        "ssn": "1924",
        "dob": 20160120,
        "dl": "6679",
        "dlstate": "MD",
        "ownership": 10000,
        "email": "Jerrod_Glover@hotmail.com",
        "fax": "",
        "phone": "5106406000",
        "country": "MAR",
        "zip": "60064",
        "state": "MD",
        "city": "East Bettye",
        "address2": "",
        "address1": "83 Dan Ways",
        "primary": 1,
        "inactive": 0,
        "frozen": 0,
        "timezone": "est",
        "gender": "male",
        "creditScore": 334,
        "creditScoreDate": "2025-03-11 08:58:20",
        "significantResponsibility": 0,
        "politicallyExposed": 0,
        "citizenship": "MAR",
        "mailingAddress1": "",
        "mailingAddress2": "",
        "mailingCity": "",
        "mailingState": "MD",
        "mailingPostalCode": "",
        "mailingCountry": "MAR",
        "treasuryPrimeRoles": "",
        "facilitator": "",
        "vendor": "",
        "shareableUrl": "",
        "status": "",
        "createdAt": 1123,
        "completedAt": 1123,
        "plaidIdvId": "",
        "templateId": ""
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

