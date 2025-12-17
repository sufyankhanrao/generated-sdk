
# Response Users Collection

## Structure

`ResponseUsersCollection`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type111Enum`](../../doc/models/type-111-enum.md) | Optional | Resource Type<br><br>**Default**: `"UsersCollection"` |
| `list` | [`List[List18]`](../../doc/models/list-18.md) | Optional | Resource Members |
| `links` | [`Links`](../../doc/models/links.md) | Optional | Pagination page links |
| `pagination` | [`Pagination`](../../doc/models/pagination.md) | Optional | Pagination info |
| `sort` | [`Sort`](../../doc/models/sort.md) | Optional | Sort information used on the results |

## Example (as JSON)

```json
{
  "type": "UsersCollection",
  "list": [
    {
      "account_number": "account_number2",
      "branding_domain_url": "branding_domain_url8",
      "cell_phone": "cell_phone8",
      "company_name": "company_name8",
      "contact_id": "contact_id2"
    },
    {
      "account_number": "account_number2",
      "branding_domain_url": "branding_domain_url8",
      "cell_phone": "cell_phone8",
      "company_name": "company_name8",
      "contact_id": "contact_id2"
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

