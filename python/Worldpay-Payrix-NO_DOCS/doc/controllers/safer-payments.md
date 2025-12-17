# Safer Payments

```python
safer_payments_controller = client.safer_payments
```

## Class Name

`SaferPaymentsController`

## Methods

* [Get Safer Payments Id](../../doc/controllers/safer-payments.md#get-safer-payments-id)
* [Put Safer Payments Id](../../doc/controllers/safer-payments.md#put-safer-payments-id)
* [Get Safer Payments](../../doc/controllers/safer-payments.md#get-safer-payments)
* [Post Safer Payments](../../doc/controllers/safer-payments.md#post-safer-payments)


# Get Safer Payments Id

Query Safer Payment.

```python
def get_safer_payments_id(self,
                         id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource, or the (unknown) ID associated with the Safer Payments. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SaferPaymentsResponseResult`](../../doc/models/safer-payments-response-result.md).

## Example Usage

```python
id = 't1_saf_67f4d59664ed122a5915300'

result = safer_payments_controller.get_safer_payments_id(id)

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
        "id": "t1_vas_65de13bb68f138dc751dc0z",
        "created": "2024-02-27 11:54:19.4389",
        "modified": "2024-02-27 11:54:19.4389",
        "creator": "t1_log_633455983e5e7fe16fb078b",
        "modifier": "t1_log_633455983e5e7fe16fb078b",
        "entity": "t1_ent_65de12aabb1f58e2a3441f7",
        "status": "compliance",
        "enablementDate": "2024-02-27 11:54:19",
        "pciNonValidationFeeEnabled": 0,
        "org": "t1_org_00b2ac11ed8bed97fb80000",
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_666834d4d504f21414978z5",
        "program": "basic",
        "deleted": "2024-02-27 11:54:19",
        "deleter": "",
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


# Put Safer Payments Id

Update Safer Payment.

```python
def put_safer_payments_id(self,
                         id,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource, or the (unknown) ID associated with the Safer Payment. |
| `body` | [`SaferPaymentsPutRequest`](../../doc/models/safer-payments-put-request.md) | Body, Required | Update Safer Payment Request |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SaferPaymentsResponseResult`](../../doc/models/safer-payments-response-result.md).

## Example Usage

```python
id = 't1_saf_67f4d59664ed122a5915300'

body = SaferPaymentsPutRequest(
    entity='t1_ent_65de12aabb1f58e2a3441f7',
    status=SaferPaymentStatusEnum.COMPLIANCE,
    enablement_date='2024-02-27 11:54:19',
    pci_non_validation_fee_enabled=SaferPaymentPciNonValidationFeeEnabledEnum.ENUM_0,
    org='t1_org_00b2ac11ed8bed97fb80000',
    division='t1_div_67c56806728fbbf0bae0b00',
    partition='t1_ptn_666834d4d504f21414978z5',
    program=SaferPaymentProgramEnum.BASIC,
    deleted='2024-02-27 11:54:19',
    deleter='',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

result = safer_payments_controller.put_safer_payments_id(
    id,
    body
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
        "id": "t1_vas_65de13bb68f138dc751dc0z",
        "created": "2024-02-27 11:54:19.4389",
        "modified": "2024-02-27 11:54:19.4389",
        "creator": "t1_log_633455983e5e7fe16fb078b",
        "modifier": "t1_log_633455983e5e7fe16fb078b",
        "entity": "t1_ent_65de12aabb1f58e2a3441f7",
        "status": "compliance",
        "enablementDate": "2024-02-27 11:54:19",
        "pciNonValidationFeeEnabled": 0,
        "org": "t1_org_00b2ac11ed8bed97fb80000",
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_666834d4d504f21414978z5",
        "program": "basic",
        "deleted": "2024-02-27 11:54:19",
        "deleter": "",
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


# Get Safer Payments

Query Safer Payments.

```python
def get_safer_payments(self,
                      search=None,
                      totals=None,
                      page_number=None,
                      page_limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `search` | `str` | Header, Optional | Set this header to filter or sort the list of resources that the method returns.<br>See [Searches](page:welcome#searches) for detailed information and examples on how to use search header. |
| `totals` | `str` | Header, Optional | To configure a request to return a total for all instances of a field in a result set,  use the totals header in the format `totals={operator}[]={key}`.  This will calculate the desired total and return it in the `details > totals` object of the response.  For instance, if you want to sum the `total` field of all transactions,  you would use the `sum` operator. The response will include the result set,  along with the calculated total in the `details` section. See [Collection Operators](page:welcome#collection-operators) for detailed information and examples on how to use totals header. |
| `page_number` | `int` | Query, Optional | Set this path parameter to request a specific page of records.<br>For example, set `?page[number]=2` to retrieve the second page of records for this request. |
| `page_limit` | `int` | Query, Optional | Set this path parameter to request up to a specific amount of records. By default 30 records are retrieved per page. The maximum limit that can be set is 100.<br>For example, set `?page[limit]=50` to retrieve up to 50 records for this request. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SaferPaymentsResponseResult`](../../doc/models/safer-payments-response-result.md).

## Example Usage

```python
search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = safer_payments_controller.get_safer_payments(
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
        "id": "t1_vas_65de13bb68f138dc751dc0z",
        "created": "2024-02-27 11:54:19.4389",
        "modified": "2024-02-27 11:54:19.4389",
        "creator": "t1_log_633455983e5e7fe16fb078b",
        "modifier": "t1_log_633455983e5e7fe16fb078b",
        "entity": "t1_ent_65de12aabb1f58e2a3441f7",
        "status": "compliance",
        "enablementDate": "2024-02-27 11:54:19",
        "pciNonValidationFeeEnabled": 0,
        "org": "t1_org_00b2ac11ed8bed97fb80000",
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_666834d4d504f21414978z5",
        "program": "basic",
        "deleted": "2024-02-27 11:54:19",
        "deleter": "",
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


# Post Safer Payments

Create a Safer Payment.

```python
def post_safer_payments(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SaferPaymentsPostRequest`](../../doc/models/safer-payments-post-request.md) | Body, Required | Create Safer Payment Request |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SaferPaymentsResponseResult`](../../doc/models/safer-payments-response-result.md).

## Example Usage

```python
body = SaferPaymentsPostRequest(
    entity='t1_ent_65de12aabb1f58e2a3441f7',
    status=SaferPaymentStatusEnum.COMPLIANCE,
    enablement_date='2024-02-27 11:54:19',
    pci_non_validation_fee_enabled=SaferPaymentPciNonValidationFeeEnabledEnum.ENUM_0,
    org='t1_org_00b2ac11ed8bed97fb80000',
    division='t1_div_67c56806728fbbf0bae0b00',
    partition='t1_ptn_666834d4d504f21414978z5',
    program=SaferPaymentProgramEnum.BASIC,
    deleted='2024-02-27 11:54:19',
    deleter='',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

result = safer_payments_controller.post_safer_payments(body)

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
        "id": "t1_vas_65de13bb68f138dc751dc0z",
        "created": "2024-02-27 11:54:19.4389",
        "modified": "2024-02-27 11:54:19.4389",
        "creator": "t1_log_633455983e5e7fe16fb078b",
        "modifier": "t1_log_633455983e5e7fe16fb078b",
        "entity": "t1_ent_65de12aabb1f58e2a3441f7",
        "status": "compliance",
        "enablementDate": "2024-02-27 11:54:19",
        "pciNonValidationFeeEnabled": 0,
        "org": "t1_org_00b2ac11ed8bed97fb80000",
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_666834d4d504f21414978z5",
        "program": "basic",
        "deleted": "2024-02-27 11:54:19",
        "deleter": "",
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

