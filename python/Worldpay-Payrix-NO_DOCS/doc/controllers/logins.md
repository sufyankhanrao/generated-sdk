# Logins

Logins resources deal with individual user details like name and email as well as management details like which partition and division the user belongs to.

```python
logins_controller = client.logins
```

## Class Name

`LoginsController`

## Methods

* [Get Logins Id](../../doc/controllers/logins.md#get-logins-id)
* [Put Logins Id](../../doc/controllers/logins.md#put-logins-id)
* [Delete Logins Id](../../doc/controllers/logins.md#delete-logins-id)
* [Get Logins](../../doc/controllers/logins.md#get-logins)
* [Post Logins](../../doc/controllers/logins.md#post-logins)


# Get Logins Id

Query a Login. A Login is a user of the API and has a unique username and password.

```python
def get_logins_id(self,
                 id,
                 request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Login ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`LoginsResponseResult`](../../doc/models/logins-response-result.md).

## Example Usage

```python
id = 't1_log_67c56806038bb4eb85a0000'

request_token = '20250423-yourmerchant-refunds-001'

result = logins_controller.get_logins_id(
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
        "id": "t1_log_67c56806038bb4eb85a0000",
        "created": "2025-03-03 03:27:50.0511",
        "modified": "2025-03-03 03:38:26.1424",
        "creator": "g1577139c2304b0",
        "modifier": "t1_log_67c56806038bb4eb85a0000",
        "login": "g15967a6e0d7cf6",
        "lastLogin": "2025-03-03 03:38:26",
        "username": "user9287347954",
        "password": "myPassword",
        "first": "John",
        "middle": "",
        "last": "Doe",
        "email": "user2118145526@example.com",
        "fax": "",
        "phone": "0028106820",
        "country": "USA",
        "zip": "77379",
        "state": "TX",
        "city": "Spring",
        "address2": "",
        "address1": "9337 SPRING CYPRESS RD STE A413",
        "confirmed": 0,
        "roles": 64,
        "partition": "g157713aff9b946",
        "division": "t1_div_67c56806728fbbf0bae0b10",
        "inactive": 0,
        "frozen": 0,
        "allowedResources": "",
        "restrictedResources": "",
        "parentDivision": "",
        "portalAccess": 1,
        "ssoId": "",
        "mfaEnabled": 1,
        "mfaSecret": "",
        "mfaEnrolledDate": "2025-06-16 08:02:53",
        "mfaType": "",
        "mfaSmsCodesCount": 0,
        "mfaSmsWindow": 0,
        "loginAsEnabled": 1,
        "effectiveRoles": 1550314
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


# Put Logins Id

Update a Login, which is a user of the API having a unique username and password.

```python
def put_logins_id(self,
                 id,
                 body,
                 request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Login ID. |
| `body` | [`LoginsPutRequest`](../../doc/models/logins-put-request.md) | Body, Required | Update Login Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`LoginsResponseResult`](../../doc/models/logins-response-result.md).

## Example Usage

```python
id = 't1_log_67c56806038bb4eb85a0000'

body = LoginsPutRequest(
    login='g15967a6e0d7cf6',
    partition='g157713aff9b946',
    division='t1_div_67c56806728fbbf0bae0b10',
    parent_division='t1_div_67c56806728fbbf0bae0b10',
    roles=64,
    confirmed=ConfirmedEnum.NOTCONFIRMED,
    username='user9287347954',
    password='****',
    first='John',
    last='Doe',
    email='user2118145526@example.com',
    allowed_resources='{"create":["accounts","payouts"],"read":["disbursements","disbursementResults"],"update":["accounts","payouts"],"delete":["accounts","payouts"],"totals":["disbursements","disbursementResults"]}',
    restricted_resources='{"create":["ltxns"],"read":["txnResults"],"update":["txns"],"delete":["txns"],"totals":["txns"]}',
    portal_access=PortalAccessEnum.HASACCESS,
    mfa_enabled=MfaEnabledEnum.DISABLED,
    mfa_secret='****',
    mfa_enrolled_date='2025-06-16 08:02:53',
    mfa_type='totp',
    address_1='9337 SPRING CYPRESS RD STE A413',
    address_2='Suite 403',
    city='Spring',
    state='TX',
    zip='77379',
    country=CountryEnum.USA,
    phone='1028106820',
    fax='1085069293',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = logins_controller.put_logins_id(
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
        "id": "t1_log_67c56806038bb4eb85a0000",
        "created": "2025-03-03 03:27:50.0511",
        "modified": "2025-03-03 03:38:26.1424",
        "creator": "g1577139c2304b0",
        "modifier": "t1_log_67c56806038bb4eb85a0000",
        "login": "g15967a6e0d7cf6",
        "lastLogin": "2025-03-03 03:38:26",
        "username": "user9287347954",
        "password": "myPassword",
        "first": "John",
        "middle": "",
        "last": "Doe",
        "email": "user2118145526@example.com",
        "fax": "",
        "phone": "0028106820",
        "country": "USA",
        "zip": "77379",
        "state": "TX",
        "city": "Spring",
        "address2": "",
        "address1": "9337 SPRING CYPRESS RD STE A413",
        "confirmed": 0,
        "roles": 64,
        "partition": "g157713aff9b946",
        "division": "t1_div_67c56806728fbbf0bae0b10",
        "inactive": 0,
        "frozen": 0,
        "allowedResources": "",
        "restrictedResources": "",
        "parentDivision": "",
        "portalAccess": 1,
        "ssoId": "",
        "mfaEnabled": 1,
        "mfaSecret": "",
        "mfaEnrolledDate": "2025-06-16 08:02:53",
        "mfaType": "",
        "mfaSmsCodesCount": 0,
        "mfaSmsWindow": 0,
        "loginAsEnabled": 1,
        "effectiveRoles": 1550314
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


# Delete Logins Id

Delete a Login. A Login is a user of the API and has a unique username and password.

```python
def delete_logins_id(self,
                    id,
                    request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Login ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`LoginsResponseResult`](../../doc/models/logins-response-result.md).

## Example Usage

```python
id = 't1_log_67c56806038bb4eb85a0000'

request_token = '20250423-yourmerchant-refunds-001'

result = logins_controller.delete_logins_id(
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
        "id": "t1_log_67c56806038bb4eb85a0000",
        "created": "2025-03-03 03:27:50.0511",
        "modified": "2025-03-03 03:38:26.1424",
        "creator": "g1577139c2304b0",
        "modifier": "t1_log_67c56806038bb4eb85a0000",
        "login": "g15967a6e0d7cf6",
        "lastLogin": "2025-03-03 03:38:26",
        "username": "user9287347954",
        "password": "myPassword",
        "first": "John",
        "middle": "",
        "last": "Doe",
        "email": "user2118145526@example.com",
        "fax": "",
        "phone": "0028106820",
        "country": "USA",
        "zip": "77379",
        "state": "TX",
        "city": "Spring",
        "address2": "",
        "address1": "9337 SPRING CYPRESS RD STE A413",
        "confirmed": 0,
        "roles": 64,
        "partition": "g157713aff9b946",
        "division": "t1_div_67c56806728fbbf0bae0b10",
        "inactive": 0,
        "frozen": 0,
        "allowedResources": "",
        "restrictedResources": "",
        "parentDivision": "",
        "portalAccess": 1,
        "ssoId": "",
        "mfaEnabled": 1,
        "mfaSecret": "",
        "mfaEnrolledDate": "2025-06-16 08:02:53",
        "mfaType": "",
        "mfaSmsCodesCount": 0,
        "mfaSmsWindow": 0,
        "loginAsEnabled": 1,
        "effectiveRoles": 1550314
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


# Get Logins

Query Logins. Retrieves the list of all users details like name and email as well as management details like which partition and division the user belongs to. A Login represents the unique ID of the user making an API request. Each user has a unique username and password

```python
def get_logins(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`LoginsResponseResult`](../../doc/models/logins-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = logins_controller.get_logins(
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
        "id": "t1_log_67c56806038bb4eb85a0000",
        "created": "2025-03-03 03:27:50.0511",
        "modified": "2025-03-03 03:38:26.1424",
        "creator": "g1577139c2304b0",
        "modifier": "t1_log_67c56806038bb4eb85a0000",
        "login": "g15967a6e0d7cf6",
        "lastLogin": "2025-03-03 03:38:26",
        "username": "user9287347954",
        "password": "myPassword",
        "first": "John",
        "middle": "",
        "last": "Doe",
        "email": "user2118145526@example.com",
        "fax": "",
        "phone": "0028106820",
        "country": "USA",
        "zip": "77379",
        "state": "TX",
        "city": "Spring",
        "address2": "",
        "address1": "9337 SPRING CYPRESS RD STE A413",
        "confirmed": 0,
        "roles": 64,
        "partition": "g157713aff9b946",
        "division": "t1_div_67c56806728fbbf0bae0b10",
        "inactive": 0,
        "frozen": 0,
        "allowedResources": "",
        "restrictedResources": "",
        "parentDivision": "",
        "portalAccess": 1,
        "ssoId": "",
        "mfaEnabled": 1,
        "mfaSecret": "",
        "mfaEnrolledDate": "2025-06-16 08:02:53",
        "mfaType": "",
        "mfaSmsCodesCount": 0,
        "mfaSmsWindow": 0,
        "loginAsEnabled": 1,
        "effectiveRoles": 1550314
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


# Post Logins

Create a Login. A Login represents the unique ID of the user making an API request. Each user has a unique username and password.

```python
def post_logins(self,
               body,
               request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LoginsPostRequest`](../../doc/models/logins-post-request.md) | Body, Required | Create Login Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`LoginsResponseResult`](../../doc/models/logins-response-result.md).

## Example Usage

```python
body = LoginsPostRequest(
    partition='g157713aff9b946',
    roles=64,
    username='user9287347954',
    password='****',
    first='John',
    last='Doe',
    email='user2118145526@example.com',
    allowed_resources='{"create":["accounts","payouts"],"read":["disbursements","disbursementResults"],"update":["accounts","payouts"],"delete":["accounts","payouts"],"totals":["disbursements","disbursementResults"]}',
    restricted_resources='{"create":["ltxns"],"read":["txnResults"],"update":["txns"],"delete":["txns"],"totals":["txns"]}',
    portal_access=PortalAccessEnum.HASACCESS,
    mfa_enabled=MfaEnabledEnum.DISABLED,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    login='g15967a6e0d7cf6',
    division='t1_div_67c56806728fbbf0bae0b10',
    parent_division='Login belongs to',
    mfa_secret='****',
    mfa_enrolled_date='2025-06-16 08:02:53',
    mfa_type='totp',
    address_1='9337 SPRING CYPRESS RD STE A413',
    address_2='Suite 403',
    city='Spring',
    state='TX',
    zip='77379',
    country=CountryEnum.USA,
    phone='1028106820',
    fax='1085069293'
)

request_token = '20250423-yourmerchant-refunds-001'

result = logins_controller.post_logins(
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
        "id": "t1_log_67c56806038bb4eb85a0000",
        "created": "2025-03-03 03:27:50.0511",
        "modified": "2025-03-03 03:38:26.1424",
        "creator": "g1577139c2304b0",
        "modifier": "t1_log_67c56806038bb4eb85a0000",
        "login": "g15967a6e0d7cf6",
        "lastLogin": "2025-03-03 03:38:26",
        "username": "user9287347954",
        "password": "myPassword",
        "first": "John",
        "middle": "",
        "last": "Doe",
        "email": "user2118145526@example.com",
        "fax": "",
        "phone": "0028106820",
        "country": "USA",
        "zip": "77379",
        "state": "TX",
        "city": "Spring",
        "address2": "",
        "address1": "9337 SPRING CYPRESS RD STE A413",
        "confirmed": 0,
        "roles": 64,
        "partition": "g157713aff9b946",
        "division": "t1_div_67c56806728fbbf0bae0b10",
        "inactive": 0,
        "frozen": 0,
        "allowedResources": "",
        "restrictedResources": "",
        "parentDivision": "",
        "portalAccess": 1,
        "ssoId": "",
        "mfaEnabled": 1,
        "mfaSecret": "",
        "mfaEnrolledDate": "2025-06-16 08:02:53",
        "mfaType": "",
        "mfaSmsCodesCount": 0,
        "mfaSmsWindow": 0,
        "loginAsEnabled": 1,
        "effectiveRoles": 1550314
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

