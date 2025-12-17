# Transactions

```python
transactions_controller = client.transactions
```

## Class Name

`TransactionsController`


# Get Transaction

```python
def get_transaction(self,
                   transaction_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `str` | Template, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetTransactionResponse`](../../doc/models/get-transaction-response.md).

## Example Usage

```python
transaction_id = 'transaction_id8'

result = transactions_controller.get_transaction(transaction_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

