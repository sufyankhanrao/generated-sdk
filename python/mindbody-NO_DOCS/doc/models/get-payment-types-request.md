
# Get Payment Types Request

Get Payment Types Request Model

## Structure

`GetPaymentTypesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `active` | `bool` | Optional | When `true`, the response only contains payment types which are activated.<br>When `false`, only deactivated payment types are returned.<br>Default: **All Payment Types** |

## Example (as JSON)

```json
{
  "Active": false
}
```

