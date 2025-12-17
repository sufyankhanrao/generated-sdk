
# PagedIterable

An iterable wrapper for paginated data that allows iteration over pages or individual items. It can fetch and iterate over each individual element in all the pages lazily.

This class defines the '__iter__` method that provides it with the iterator functionality.

## Methods

| Name | Description | Type |
|  --- | --- | --- |
| `__iter__` | Provides iterator functionality to sequentially access all items across all pages. It will loop through all items by fetching next pages lazily. | `Iterable[T]` |
| `pages` | Retrieve an iterable collection of all pages in the paginated data, which can be used to loop through all pages lazily. | <code>Iterable[[`LinkPagedResponse`](../doc/link-paged-response.md) \| [`NumberPagedResponse`](../doc/number-paged-response.md) \| [`CursorPagedResponse`](../doc/cursor-paged-response.md) \| [`OffsetPagedResponse`](../doc/offset-paged-response.md)]</code> |

## Usage Example

```python
# Iterating over items in all pages.
for item in pagedIterable:
    print(item)

# Iterating over pages in the paginated response.
for page in pagedIterable.pages():
    if isinstance(page, CursorPagedResponse):
        print(page.next_cursor)
    elif isinstance(page, NumberPagedResponse):
        print(page.page_number)
    elif isinstance(page, LinkPagedResponse):
        print(page.next_link)
    elif isinstance(page, OffsetPagedResponse):
        print(page.offset)
    else:
        print("Unknown Pagination Metadata Type")

    print(page.body)
    # Iterating over items in the current page.
    for item in page.items():
        print(item)
```

