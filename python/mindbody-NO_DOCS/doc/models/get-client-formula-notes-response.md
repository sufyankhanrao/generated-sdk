
# Get Client Formula Notes Response

Enables to retrieve cross regional formula notes for a client, or for a specific appointment. The two parameters are optional, however at least one must be provided. This endpoint supports pagination.

## Structure

`GetClientFormulaNotesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `formula_notes` | [`List[FormulaNoteResponse]`](../../doc/models/formula-note-response.md) | Optional | Contains details about the client’s formula. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "FormulaNotes": [
    {
      "Id": 244,
      "ClientId": "ClientId8",
      "AppointmentId": 180,
      "EntryDate": "2016-03-13T12:52:32.123Z",
      "Note": "Note4"
    }
  ]
}
```

