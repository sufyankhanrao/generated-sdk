# Transfers

```python
transfers_controller = client.transfers
```

## Class Name

`TransfersController`

## Methods

* [Get Transfer by Id](../../doc/controllers/transfers.md#get-transfer-by-id)
* [Get Transfers](../../doc/controllers/transfers.md#get-transfers)
* [Create Transfer](../../doc/controllers/transfers.md#create-transfer)


# Get Transfer by Id

```python
def get_transfer_by_id(self,
                      transfer_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_id` | `str` | Template, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetTransfer`](../../doc/models/get-transfer.md).

## Example Usage

```python
transfer_id = 'transfer_id6'

result = transfers_controller.get_transfer_by_id(transfer_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Transfers

Gets all transfers

```python
def get_transfers(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListTransfers`](../../doc/models/list-transfers.md).

## Example Usage

```python
result = transfers_controller.get_transfers()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Transfer

```python
def create_transfer(self,
                   request)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request` | [`CreateTransfer`](../../doc/models/create-transfer.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetTransfer`](../../doc/models/get-transfer.md).

## Example Usage

```python
request = CreateTransfer(
    amount=242,
    source_id='source_id0',
    target_id='target_id6'
)

result = transfers_controller.create_transfer(request)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

