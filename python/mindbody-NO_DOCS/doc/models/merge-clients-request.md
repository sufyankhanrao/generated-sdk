
# Merge Clients Request

Request for clients/mergeclients

## Structure

`MergeClientsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `source_client_id` | `int` | Optional | The client that will be merged into TargetClientId |
| `target_client_id` | `int` | Optional | The client that will remain |

## Example (as JSON)

```json
{
  "SourceClientId": 44,
  "TargetClientId": 222
}
```

