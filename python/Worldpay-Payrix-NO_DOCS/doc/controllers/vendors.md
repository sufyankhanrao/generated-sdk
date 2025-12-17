# Vendors

Resources that deal with third-party entities (non-facilitators and non-merchants) that are involved with the merchant processing and provide a service (or set of services) to the merchant, for which they usually take a fee.

```python
vendors_controller = client.vendors
```

## Class Name

`VendorsController`

## Methods

* [Get Vendors Id](../../doc/controllers/vendors.md#get-vendors-id)
* [Put Vendors Id](../../doc/controllers/vendors.md#put-vendors-id)
* [Delete Vendors Id](../../doc/controllers/vendors.md#delete-vendors-id)
* [Get Vendors](../../doc/controllers/vendors.md#get-vendors)


# Get Vendors Id

Querying a Vendor resource represents a third-party vendor who interacts with the API, for example, a referral platform.

```python
def get_vendors_id(self,
                  id,
                  request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource, The Vendor ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`VendorsResponseResult`](../../doc/models/vendors-response-result.md).

## Example Usage

```python
id = 'p1_ven_00be57c6efdce043adae8a1'

request_token = '20250423-yourmerchant-refunds-001'

result = vendors_controller.get_vendors_id(
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
        "id": "p1_ven_00be57c6efdce043adae8a1",
        "created": "2025-02-25 18:52:38.9990",
        "modified": "2025-02-25 18:52:43.4509",
        "creator": "g1577d7719644a9",
        "modifier": "g1577d7719644a9",
        "entity": "p1_ent_67be57c6a1d97f564021b6b",
        "division": "p1_div_67be57c6d34928c1ee16155",
        "inactive": 0,
        "frozen": 0,
        "dealId": "",
        "onboardingContactEmails": "",
        "riskContactEmails": ""
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


# Put Vendors Id

Manage a Vendor resource.

Details:
Update a Vendor resource. A Vendor resource represents a third-party vendor who interacts with the API, for example, a referral platform.
Query a Vendor resource.

```python
def put_vendors_id(self,
                  id,
                  body,
                  request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Vendor ID. |
| `body` | [`VendorsPutRequest`](../../doc/models/vendors-put-request.md) | Body, Required | Update Vendor Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`VendorsResponseResult`](../../doc/models/vendors-response-result.md).

## Example Usage

```python
id = 'p1_ven_00be57c6efdce043adae8a1'

body = VendorsPutRequest(
    entity='p1_ent_67be57c6a1d97f564021b6b',
    division='p1_div_67be57c6d34928c1ee16155',
    onboarding_contact_emails='robert@example.com',
    risk_contact_emails='robert.j@example.com',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = vendors_controller.put_vendors_id(
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
        "id": "p1_ven_00be57c6efdce043adae8a1",
        "created": "2025-02-25 18:52:38.9990",
        "modified": "2025-02-25 18:52:43.4509",
        "creator": "g1577d7719644a9",
        "modifier": "g1577d7719644a9",
        "entity": "p1_ent_67be57c6a1d97f564021b6b",
        "division": "p1_div_67be57c6d34928c1ee16155",
        "inactive": 0,
        "frozen": 0,
        "dealId": "",
        "onboardingContactEmails": "",
        "riskContactEmails": ""
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


# Delete Vendors Id

Delete a Vendor or Vendors resource that represents a third-party vendor who interacts with the API, for example, a referral platform.

```python
def delete_vendors_id(self,
                     id,
                     request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource, The Vendor ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`VendorsResponseResult`](../../doc/models/vendors-response-result.md).

## Example Usage

```python
id = 'p1_ven_00be57c6efdce043adae8a1'

request_token = '20250423-yourmerchant-refunds-001'

result = vendors_controller.delete_vendors_id(
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
        "id": "p1_ven_00be57c6efdce043adae8a1",
        "created": "2025-02-25 18:52:38.9990",
        "modified": "2025-02-25 18:52:43.4509",
        "creator": "g1577d7719644a9",
        "modifier": "g1577d7719644a9",
        "entity": "p1_ent_67be57c6a1d97f564021b6b",
        "division": "p1_div_67be57c6d34928c1ee16155",
        "inactive": 0,
        "frozen": 0,
        "dealId": "",
        "onboardingContactEmails": "",
        "riskContactEmails": ""
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


# Get Vendors

Query a Vendor resource. A Vendor resource represents a third-party vendor who interacts with the API, for example, a referral platform.

```python
def get_vendors(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`VendorsResponseResult`](../../doc/models/vendors-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = vendors_controller.get_vendors(
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
        "id": "p1_ven_00be57c6efdce043adae8a1",
        "created": "2025-02-25 18:52:38.9990",
        "modified": "2025-02-25 18:52:43.4509",
        "creator": "g1577d7719644a9",
        "modifier": "g1577d7719644a9",
        "entity": "p1_ent_67be57c6a1d97f564021b6b",
        "division": "p1_div_67be57c6d34928c1ee16155",
        "inactive": 0,
        "frozen": 0,
        "dealId": "",
        "onboardingContactEmails": "",
        "riskContactEmails": ""
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

