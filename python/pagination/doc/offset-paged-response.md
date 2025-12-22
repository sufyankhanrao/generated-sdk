
# OffsetPagedResponse

This class represents a paginated API response for offset based pagination.

## Base Class

[`ApiResponse`](../doc/api-response.md)

## Fields

| Name | Description | Type |
|  --- | --- | --- |
| `offset` | Represents the offset using which the current paginated response is fetched. | `int` |

## Methods

| Name | Description | Return Type |
|  --- | --- | --- |
| `items()` | Provides the iterator for the items within a page. | `Iterable[T]` |

