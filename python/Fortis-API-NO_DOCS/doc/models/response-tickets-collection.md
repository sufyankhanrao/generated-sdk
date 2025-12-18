
# Response Tickets Collection

## Structure

`ResponseTicketsCollection`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type80Enum`](../../doc/models/type-80-enum.md) | Optional | Resource Type<br><br>**Default**: `'TicketsCollection'` |
| `list` | [`List[List14]`](../../doc/models/list-14.md) | Optional | Resource Members |
| `links` | [`Links`](../../doc/models/links.md) | Optional | Pagination page links |
| `pagination` | [`Pagination`](../../doc/models/pagination.md) | Optional | Pagination info |
| `sort` | [`Sort`](../../doc/models/sort.md) | Optional | Sort information used on the results |

## Example (as JSON)

```json
{
  "type": "TicketsCollection",
  "list": [
    {
      "account_holder_name": "account_holder_name8",
      "exp_date": "exp_date0",
      "cvv": "cvv0",
      "account_number": "account_number2",
      "billing_address": {
        "postal_code": "postal_code0",
        "street": "street8"
      }
    },
    {
      "account_holder_name": "account_holder_name8",
      "exp_date": "exp_date0",
      "cvv": "cvv0",
      "account_number": "account_number2",
      "billing_address": {
        "postal_code": "postal_code0",
        "street": "street8"
      }
    },
    {
      "account_holder_name": "account_holder_name8",
      "exp_date": "exp_date0",
      "cvv": "cvv0",
      "account_number": "account_number2",
      "billing_address": {
        "postal_code": "postal_code0",
        "street": "street8"
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

