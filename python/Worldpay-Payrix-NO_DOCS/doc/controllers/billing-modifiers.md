# Billing Modifiers

```python
billing_modifiers_controller = client.billing_modifiers
```

## Class Name

`BillingModifiersController`

## Methods

* [Get Billing Modifiers Id](../../doc/controllers/billing-modifiers.md#get-billing-modifiers-id)
* [Put Billing Modifiers Id](../../doc/controllers/billing-modifiers.md#put-billing-modifiers-id)
* [Delete Billing Modifiers Id](../../doc/controllers/billing-modifiers.md#delete-billing-modifiers-id)
* [Get Billing Modifiers](../../doc/controllers/billing-modifiers.md#get-billing-modifiers)
* [Post Billing Modifiers](../../doc/controllers/billing-modifiers.md#post-billing-modifiers)


# Get Billing Modifiers Id

Query a Billing Modifier that can change the total amount of the billing or whoever will pay it, such as applying a 10% markup on the fee total for a specific org.

```python
def get_billing_modifiers_id(self,
                            id,
                            request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this billing modifer. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BillingModifiersResponseResult`](../../doc/models/billing-modifiers-response-result.md).

## Example Usage

```python
id = 't1_blm_67d9c9f74881eb511220000'

request_token = '20250423-yourmerchant-refunds-001'

result = billing_modifiers_controller.get_billing_modifiers_id(
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
        "id": "t1_blm_67d9c9f74881eb511220000",
        "created": "2025-03-18 15:31:03.3269",
        "modified": "2025-03-18 15:31:03.3269",
        "creator": "t1_log_605e14227eb0a0b1c1d2b12",
        "modifier": "t1_log_605e14227eb0a0b1c1d2b12",
        "billing": "t1_bil_67d9c8a7df33cf77a3e5e4a",
        "entity": "t1_ent_5cd987a735c33bab09e7570",
        "org": "t1_org_5b0e08025ec790d3f9b8c00",
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_666834d4d504f21414970z0",
        "fromentity": "t1_ent_67d851660b5836731a89ee3",
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


# Put Billing Modifiers Id

Update a Billing Modifier that can change the total amount of the billing or whoever will pay it, such as applying a 10% markup on the fee total for a specific org.

```python
def put_billing_modifiers_id(self,
                            id,
                            body,
                            request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this billing modifer. |
| `body` | [`BillingModifiersPutRequest`](../../doc/models/billing-modifiers-put-request.md) | Body, Required | Update Billing Modifer Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BillingModifiersResponseResult`](../../doc/models/billing-modifiers-response-result.md).

## Example Usage

```python
id = 't1_blm_67d9c9f74881eb511220000'

body = BillingModifiersPutRequest(
    billing='t1_bil_67d9c8a7df33cf77a3e5e4a',
    entity='t1_ent_5cd987a735c33bab09e7570',
    org='t1_org_67d9c6a866e5d47dca276c3',
    division='t1_div_67c56806728fbbf0bae0b00',
    partition='t1_ptn_666834d4d504f21414970z0',
    fromentity='t1_ent_67d851660b5836731a89ee3',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = billing_modifiers_controller.put_billing_modifiers_id(
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
        "id": "t1_blm_67d9c9f74881eb511220000",
        "created": "2025-03-18 15:31:03.3269",
        "modified": "2025-03-18 15:31:03.3269",
        "creator": "t1_log_605e14227eb0a0b1c1d2b12",
        "modifier": "t1_log_605e14227eb0a0b1c1d2b12",
        "billing": "t1_bil_67d9c8a7df33cf77a3e5e4a",
        "entity": "t1_ent_5cd987a735c33bab09e7570",
        "org": "t1_org_5b0e08025ec790d3f9b8c00",
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_666834d4d504f21414970z0",
        "fromentity": "t1_ent_67d851660b5836731a89ee3",
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


# Delete Billing Modifiers Id

Delete a Billing Modifier that can change the total amount of the billing or whoever will pay it.

```python
def delete_billing_modifiers_id(self,
                               id,
                               request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this billing modifer. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BillingModifiersResponseResult`](../../doc/models/billing-modifiers-response-result.md).

## Example Usage

```python
id = 't1_blm_67d9c9f74881eb511220000'

request_token = '20250423-yourmerchant-refunds-001'

result = billing_modifiers_controller.delete_billing_modifiers_id(
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
        "id": "t1_blm_67d9c9f74881eb511220000",
        "created": "2025-03-18 15:31:03.3269",
        "modified": "2025-03-18 15:31:03.3269",
        "creator": "t1_log_605e14227eb0a0b1c1d2b12",
        "modifier": "t1_log_605e14227eb0a0b1c1d2b12",
        "billing": "t1_bil_67d9c8a7df33cf77a3e5e4a",
        "entity": "t1_ent_5cd987a735c33bab09e7570",
        "org": "t1_org_5b0e08025ec790d3f9b8c00",
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_666834d4d504f21414970z0",
        "fromentity": "t1_ent_67d851660b5836731a89ee3",
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


# Get Billing Modifiers

Query a Billing Modifier that can change the total amount of the billing or determine who will pay it. For example, a Billing Modifier may apply a 10% markup on the fee total for a specific organization.

```python
def get_billing_modifiers(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BillingModifiersResponseResult`](../../doc/models/billing-modifiers-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = billing_modifiers_controller.get_billing_modifiers(
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
        "id": "t1_blm_67d9c9f74881eb511220000",
        "created": "2025-03-18 15:31:03.3269",
        "modified": "2025-03-18 15:31:03.3269",
        "creator": "t1_log_605e14227eb0a0b1c1d2b12",
        "modifier": "t1_log_605e14227eb0a0b1c1d2b12",
        "billing": "t1_bil_67d9c8a7df33cf77a3e5e4a",
        "entity": "t1_ent_5cd987a735c33bab09e7570",
        "org": "t1_org_5b0e08025ec790d3f9b8c00",
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_666834d4d504f21414970z0",
        "fromentity": "t1_ent_67d851660b5836731a89ee3",
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


# Post Billing Modifiers

Create a Billing Modifier that can change the total amount of the billing or adjust who will pay it, such as applying a 10% markup on the fee total for a specific organization.

```python
def post_billing_modifiers(self,
                          body,
                          request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`BillingModifiersPostRequest`](../../doc/models/billing-modifiers-post-request.md) | Body, Required | Create Billing Modifier Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BillingModifiersResponseResult`](../../doc/models/billing-modifiers-response-result.md).

## Example Usage

```python
body = BillingModifiersPostRequest(
    billing='t1_bil_67d9c8a7df33cf77a3e5e4a',
    fromentity='t1_ent_67d851660b5836731a89ee3',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    entity='t1_ent_5cd987a735c33bab09e7570',
    org='t1_org_67d9c6a866e5d47dca276c3',
    division='t1_div_67c56806728fbbf0bae0b00',
    partition='t1_ptn_666834d4d504f21414970z0'
)

request_token = '20250423-yourmerchant-refunds-001'

result = billing_modifiers_controller.post_billing_modifiers(
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
        "id": "t1_blm_67d9c9f74881eb511220000",
        "created": "2025-03-18 15:31:03.3269",
        "modified": "2025-03-18 15:31:03.3269",
        "creator": "t1_log_605e14227eb0a0b1c1d2b12",
        "modifier": "t1_log_605e14227eb0a0b1c1d2b12",
        "billing": "t1_bil_67d9c8a7df33cf77a3e5e4a",
        "entity": "t1_ent_5cd987a735c33bab09e7570",
        "org": "t1_org_5b0e08025ec790d3f9b8c00",
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_666834d4d504f21414970z0",
        "fromentity": "t1_ent_67d851660b5836731a89ee3",
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

