
# CursorPagedResponse

This class represents a paginated API response for cursor based pagination.

## Base Class

[`ApiResponse`](../doc/api-response.md)

## Fields

| Name | Description | Type |
|  --- | --- | --- |
| `next_cursor` | Represents the next cursor using which the current paginated response is fetched. | `str` |

## Methods

| Name | Description | Return Type |
|  --- | --- | --- |
| `items()` | Provides the iterator for the items within a page. | `Iterable[T]` |

