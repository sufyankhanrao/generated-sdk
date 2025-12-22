
# OffsetPagedResponse

This class represents a paginated API response for offset based pagination.

## Fields

| Name | Description | Type |
|  --- | --- | --- |
| `offset` | Represents the offset using which the current paginated response is fetched. | `int` |
| `body` | The content associated with the Page instance. | `Any` |

## Methods

| Name | Description | Return Type |
|  --- | --- | --- |
| `items()` | Provides the iterator for the items within a page. | `Iterable[T]` |

