
# Class Client Detail

Class Client Detail Object

## Structure

`ClassClientDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_ids` | `List[str]` | Required | The RSSID of the clients to remove from the specified classes. |
| `class_id` | `int` | Required | The ID of the classes that you want to remove the clients from. |

## Example (as JSON)

```json
{
  "ClientIds": [
    "ClientIds1"
  ],
  "ClassId": 120
}
```

