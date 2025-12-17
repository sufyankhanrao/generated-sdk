
# Delete Client Formula Note Request

## Structure

`DeleteClientFormulaNoteRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Required | The client ID of the client whose formula note needs to be deleted. |
| `formula_note_id` | `int` | Required | The formula note ID for the note to be deleted. |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ClientId": "ClientId2",
  "FormulaNoteId": 76,
  "Limit": 196,
  "Offset": 130
}
```

