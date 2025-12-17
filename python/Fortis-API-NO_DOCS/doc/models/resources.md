
# Resources

Resource Information on `expand`

## Structure

`Resources`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `title` | `str` | Optional | Resource Title<br><br>**Constraints**: *Maximum Length*: `64` |
| `priv` | `str` | Optional | Priv<br><br>**Constraints**: *Maximum Length*: `64` |
| `resource_name` | `str` | Optional | Resource Name<br><br>**Constraints**: *Maximum Length*: `64` |
| `id` | `int` | Optional | Resource ID |
| `last_used_date` | `int` | Optional | Last Used Date |
| `created_ts` | `int` | Optional | Created Time Stamp |
| `modified_ts` | `int` | Optional | Modified Time Stamp |

## Example (as JSON)

```json
{
  "title": "My terminal",
  "resource_name": "v2.addons.iframe.get",
  "id": 5693,
  "last_used_date": 1422040992,
  "created_ts": 1422040992,
  "modified_ts": 1422040992,
  "priv": "priv0"
}
```

