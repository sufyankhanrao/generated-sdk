
# Response Locations Collection

## Structure

`ResponseLocationsCollection`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type35Enum`](../../doc/models/type-35-enum.md) | Optional | Resource Type<br><br>**Default**: `'LocationsCollection'` |
| `list` | [`List[List6]`](../../doc/models/list-6.md) | Optional | Resource Members |
| `links` | [`Links`](../../doc/models/links.md) | Optional | Pagination page links |
| `pagination` | [`Pagination`](../../doc/models/pagination.md) | Optional | Pagination info |
| `sort` | [`Sort`](../../doc/models/sort.md) | Optional | Sort information used on the results |

## Example (as JSON)

```json
{
  "type": "LocationsCollection",
  "list": [
    {
      "id": "id2",
      "created_ts": 56,
      "modified_ts": 124,
      "account_number": "account_number2",
      "address": {
        "city": "city6",
        "state": "state2",
        "postal_code": "postal_code8",
        "country": "US",
        "street": "street6"
      }
    },
    {
      "id": "id2",
      "created_ts": 56,
      "modified_ts": 124,
      "account_number": "account_number2",
      "address": {
        "city": "city6",
        "state": "state2",
        "postal_code": "postal_code8",
        "country": "US",
        "street": "street6"
      }
    },
    {
      "id": "id2",
      "created_ts": 56,
      "modified_ts": 124,
      "account_number": "account_number2",
      "address": {
        "city": "city6",
        "state": "state2",
        "postal_code": "postal_code8",
        "country": "US",
        "street": "street6"
      }
    }
  ],
  "links": {
    "type": "Links",
    "first": "first0",
    "previous": "previous2",
    "next": "next2",
    "last": "last4"
  },
  "pagination": {
    "type": "Pagination",
    "total_count": 100,
    "page_count": 212,
    "page_number": 28,
    "page_size": 6
  },
  "sort": {
    "type": "Sorting",
    "fields": [
      {
        "field": "field2",
        "order": "asc"
      },
      {
        "field": "field2",
        "order": "asc"
      },
      {
        "field": "field2",
        "order": "asc"
      }
    ]
  }
}
```

