
# Orgs Put Request

## Structure

`OrgsPutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `login` | `str` | Optional | The Login that owns this Org. |
| `name` | `str` | Optional | The name of this Org.<br>This field is stored as a text string and must be between 0 and 100 characters long. |
| `description` | `str` | Optional | A description of this Org.<br>This field is stored as a text string and must be between 0 and 100 characters long. |

## Example (as JSON)

```json
{
  "login": "t1_log_656d51cd565edf13a27c494",
  "name": "Leora44",
  "description": "description of Org"
}
```

