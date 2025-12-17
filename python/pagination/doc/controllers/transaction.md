# Transaction

```python
transaction_controller = client.transaction
```

## Class Name

`TransactionController`

## Methods

* [Fetch With Offset](../../doc/controllers/transaction.md#fetch-with-offset)
* [Fetch With Cursor](../../doc/controllers/transaction.md#fetch-with-cursor)
* [Fetch With Link](../../doc/controllers/transaction.md#fetch-with-link)
* [Fetch With Page](../../doc/controllers/transaction.md#fetch-with-page)


# Fetch With Offset

Fetch transactions using Offset-based Pagination

```python
def fetch_with_offset(self,
                     offset=None,
                     limit=None,
                     success_on_empty_page=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `offset` | `int` | Query, Optional | The number of records to skip before selecting transactions.<br><br>**Constraints**: `>= 0` |
| `limit` | `int` | Query, Optional | Number of transactions per page.<br><br>**Constraints**: `>= 1`, `<= 100` |
| `success_on_empty_page` | `bool` | Query, Optional | Should return 200 success code on the calls after the last batch of paginated data. |

## Response Type

This method returns an instance of [`PagedIterable`](../../doc/paged-iterable.md), where each item is of type [`Transaction`](../../doc/models/transaction.md) and each page is of type [`TransactionsOffset`](../../doc/models/transactions-offset.md).

## Example Usage

```python
result = transaction_controller.fetch_with_offset()

# Iterating over items in all pages.
try:
    for _item in result:
        print(_item)
except APIException as e:
    print(e)

# Iterating over pages in the paginated response.
try:
    for _page in result.pages():
        print(_page.body)
        # Iterating over items in the current page.
        for _item in _page.items():
            print(_item)
except APIException as e:
    print(e)
```


# Fetch With Cursor

Fetch transactions using Cursor-based Pagination

```python
def fetch_with_cursor(self,
                     cursor=None,
                     limit=10,
                     success_on_empty_page=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cursor` | `str` | Query, Optional | The unique identifier (cursor) to fetch the next set of results. |
| `limit` | `int` | Query, Optional | Number of transactions per page.<br><br>**Default**: `10`<br><br>**Constraints**: `>= 1`, `<= 100` |
| `success_on_empty_page` | `bool` | Query, Optional | Should return 200 success code on the calls after the last batch of paginated data. |

## Response Type

This method returns an instance of [`PagedIterable`](../../doc/paged-iterable.md), where each item is of type [`Transaction`](../../doc/models/transaction.md) and each page is of type [`TransactionsCursored`](../../doc/models/transactions-cursored.md).

## Example Usage

```python
cursor = 'txn_abc123'

limit = 10

result = transaction_controller.fetch_with_cursor(
    cursor=cursor,
    limit=limit
)

# Iterating over items in all pages.
try:
    for _item in result:
        print(_item)
except APIException as e:
    print(e)

# Iterating over pages in the paginated response.
try:
    for _page in result.pages():
        print(_page.body)
        # Iterating over items in the current page.
        for _item in _page.items():
            print(_item)
except APIException as e:
    print(e)
```


# Fetch With Link

Fetch transactions using Link-based Pagination

```python
def fetch_with_link(self,
                   page=1,
                   size=10,
                   success_on_empty_page=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | The page number to fetch.<br><br>**Default**: `1`<br><br>**Constraints**: `>= 1` |
| `size` | `int` | Query, Optional | Number of transactions per page.<br><br>**Default**: `10`<br><br>**Constraints**: `>= 1`, `<= 100` |
| `success_on_empty_page` | `bool` | Query, Optional | Should return 200 success code on the calls after the last batch of paginated data. |

## Response Type

This method returns an instance of [`PagedIterable`](../../doc/paged-iterable.md), where each item is of type [`Transaction`](../../doc/models/transaction.md) and each page is of type [`Transactions`](../../doc/models/transactions.md).

## Example Usage

```python
page = 1

size = 10

result = transaction_controller.fetch_with_link(
    page=page,
    size=size
)

# Iterating over items in all pages.
try:
    for _item in result:
        print(_item)
except APIException as e:
    print(e)

# Iterating over pages in the paginated response.
try:
    for _page in result.pages():
        print(_page.body)
        # Iterating over items in the current page.
        for _item in _page.items():
            print(_item)
except APIException as e:
    print(e)
```


# Fetch With Page

Fetch transactions using Page-based Pagination

```python
def fetch_with_page(self,
                   page=None,
                   size=None,
                   success_on_empty_page=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | The page number to fetch.<br><br>**Constraints**: `>= 1` |
| `size` | `int` | Query, Optional | Number of transactions per page.<br><br>**Constraints**: `>= 1`, `<= 100` |
| `success_on_empty_page` | `bool` | Query, Optional | Should return 200 success code on the calls after the last batch of paginated data. |

## Response Type

This method returns an instance of [`PagedIterable`](../../doc/paged-iterable.md), where each item is of type [`Transaction`](../../doc/models/transaction.md) and each page is of type [`Transactions`](../../doc/models/transactions.md).

## Example Usage

```python
result = transaction_controller.fetch_with_page()

# Iterating over items in all pages.
try:
    for _item in result:
        print(_item)
except APIException as e:
    print(e)

# Iterating over pages in the paginated response.
try:
    for _page in result.pages():
        print(_page.body)
        # Iterating over items in the current page.
        for _item in _page.items():
            print(_item)
except APIException as e:
    print(e)
```

