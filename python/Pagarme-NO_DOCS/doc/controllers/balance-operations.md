# Balance Operations

```python
balance_operations_controller = client.balance_operations
```

## Class Name

`BalanceOperationsController`

## Methods

* [Get Balance Operation by Id](../../doc/controllers/balance-operations.md#get-balance-operation-by-id)
* [Get Balance Operations](../../doc/controllers/balance-operations.md#get-balance-operations)


# Get Balance Operation by Id

```python
def get_balance_operation_by_id(self,
                               id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetBalanceOperationResponse`](../../doc/models/get-balance-operation-response.md).

## Example Usage

```python
id = 112

result = balance_operations_controller.get_balance_operation_by_id(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Balance Operations

```python
def get_balance_operations(self,
                          status=None,
                          created_since=None,
                          created_until=None,
                          recipient_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Query, Optional | - |
| `created_since` | `datetime` | Query, Optional | - |
| `created_until` | `datetime` | Query, Optional | - |
| `recipient_id` | `str` | Query, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListBalanceOperationResponse`](../../doc/models/list-balance-operation-response.md).

## Example Usage

```python
result = balance_operations_controller.get_balance_operations()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

