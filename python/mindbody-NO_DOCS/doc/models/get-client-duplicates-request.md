
# Get Client Duplicates Request

## Structure

`GetClientDuplicatesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Optional | The client first name to match on when searching for duplicates. |
| `last_name` | `str` | Optional | The client last name to match on when searching for duplicates. |
| `email` | `str` | Optional | The client email to match on when searching for duplicates. |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "FirstName": "FirstName6",
  "LastName": "LastName6",
  "Email": "Email6",
  "Limit": 82,
  "Offset": 16
}
```

