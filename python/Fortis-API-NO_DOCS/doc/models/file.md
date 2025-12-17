
# File

## Structure

`File`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `file` | `Any` | Optional | File Object |
| `resource_id` | `str` | Optional | Resource Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `resource` | [`Resource2Enum`](../../doc/models/resource-2-enum.md) | Optional | Resource |
| `product_file_id` | `str` | Optional | Product File Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `file_category_id` | `str` | Optional | File Category Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `visibility_group_id` | `str` | Optional | Visibility Group Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `file_description` | `str` | Optional | File Description<br><br>**Constraints**: *Maximum Length*: `128` |
| `id` | `str` | Optional | Resource<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `file_name` | `str` | Optional | File Name |
| `file_extension` | `str` | Optional | File Extension<br><br>**Constraints**: *Maximum Length*: `4` |
| `file_size_bytes` | `int` | Optional | File Size Bytes |
| `created_ts` | `int` | Optional | Created Time Stamp |
| `modified_ts` | `int` | Optional | Modified Time Stamp |
| `created_user_id` | `str` | Optional | User ID Created the register<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |

## Example (as JSON)

```json
{
  "resource_id": "11e95f8ec39de8fbdb0a4f1a",
  "resource": "Contact",
  "product_file_id": "11e95f8ec39de8fbdb0a4f1a",
  "file_category_id": "11e95f8ec39de8fbdb0a4f1a",
  "visibility_group_id": "11e95f8ec39de8fbdb0a4f1a",
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "created_ts": 1422040992,
  "modified_ts": 1422040992,
  "created_user_id": "11e95f8ec39de8fbdb0a4f1a",
  "file": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

