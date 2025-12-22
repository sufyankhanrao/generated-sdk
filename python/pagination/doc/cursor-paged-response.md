
# CursorPagedResponse

This class represents a paginated API response for cursor based pagination.

## Fields

| Name | Description | Type |
|  --- | --- | --- |
| `next_cursor` | Represents the next cursor using which the current paginated response is fetched. | `str` |
| `body` | The content associated with the Page instance. | `Any` |

## Methods

| Name | Description | Return Type |
|  --- | --- | --- |
| `items()` | Provides the iterator for the items within a page. | `Iterable[T]` |

