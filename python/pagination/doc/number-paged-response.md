
# NumberPagedResponse

This class represents a paginated API response for page based pagination.

## Base Class

[`ApiResponse`](../doc/api-response.md)

## Fields

| Name | Description | Type |
|  --- | --- | --- |
| `page_number` | Represents the page number using which the current paginated response is fetched. | `int` |

## Methods

| Name | Description | Return Type |
|  --- | --- | --- |
| `items()` | Provides the iterator for the items within a page. | `Iterable[T]` |

