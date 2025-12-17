
# Details Properties

Where the response lists multiple resources, the API splits the response into several 'pages'.
This object indicates the current and last available pages in the list.

## Structure

`DetailsProperties`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `current` | `int` | Optional | The current page in the paginated resource list. |
| `last` | `int` | Optional | The last available page in the paginated resource list. |
| `has_more` | `bool` | Optional | Indicates if another page of results is available. |

## Example (as JSON)

```json
{
  "current": 44,
  "last": 214,
  "hasMore": false
}
```

