
# EID Document Response

## Structure

`EIDDocumentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `status` | `str` | Optional | Indicates overall status of the request. Allowed values: SUCCESS, FAILED |
| `data` | [`List[EIDDocument]`](../../doc/models/eid-document.md) | Optional | - |
| `page_size` | `int` | Optional | Number of records returned in the response |
| `page` | `int` | Optional | Current page |
| `total_pages` | `int` | Optional | Total number of pages available for the requested data |
| `total_records` | `int` | Optional | Total number of elements corresponding to the request |
| `is_first_page` | `bool` | Optional | True if it is the first page, false otherwise |
| `is_last_page` | `bool` | Optional | True if it is the last page, false, otherwise. |

## Example (as JSON)

```json
{
  "RequestId": "RequestId8",
  "Status": "Status4",
  "Data": [
    {
      "DocumentId": 28,
      "AccountGroupId": "AccountGroupId2",
      "AccountGroupName": "AccountGroupName6",
      "DocumentType": "DocumentType6",
      "DocumentFormat": "DocumentFormat0"
    }
  ],
  "PageSize": 188,
  "Page": 208
}
```

