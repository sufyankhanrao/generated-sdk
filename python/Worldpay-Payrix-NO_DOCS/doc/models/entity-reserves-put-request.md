
# Entity Reserves Put Request

## Structure

`EntityReservesPutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total` | `int` | Optional | The amount held in this entityReserve.<br>This field is specified as an integer in cents. |
| `name` | `str` | Optional | The name of this EntityReserve.<br>This field is stored as a text string and must be between 0 and 50 characters long. |
| `description` | `str` | Optional | A description of this EntityReserve.<br>This field is stored as a text string and must be between 0 and 100 characters long. |

## Example (as JSON)

```json
{
  "total": 0,
  "name": "EntityReserve1",
  "description": "EntityReserve"
}
```

