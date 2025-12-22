
# NumberPagedResponse

This class represents a paginated API response for page based pagination.

## Fields

| Name | Description | Type |
|  --- | --- | --- |
| `page_number` | Represents the page number using which the current paginated response is fetched. | `int` |
| `body` | The content associated with the Page instance. | `Any` |

## Methods

| Name | Description | Return Type |
|  --- | --- | --- |
| `items()` | Provides the iterator for the items within a page. | `Iterable[T]` |

