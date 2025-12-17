
# Site With Data

## Structure

`SiteWithData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `int` | Optional | The id of a site.<br><br>**Constraints**: `>= 1` |
| `title` | `str` | Optional | - |
| `country` | `str` | Optional | - |
| `identity` | `str` | Optional | - |
| `metadata` | [`List[MetadataField]`](../../doc/models/metadata-field.md) | Optional | A list of metadata fields and their values. |

## Example (as JSON)

```json
{
  "siteId": 32,
  "title": "title8",
  "country": "country0",
  "identity": "identity0",
  "metadata": [
    {
      "key": "key6",
      "value": "value8"
    },
    {
      "key": "key6",
      "value": "value8"
    }
  ]
}
```

