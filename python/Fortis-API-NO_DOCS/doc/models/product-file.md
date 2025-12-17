
# Product File

## Structure

`ProductFile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `title` | `str` | Optional | Title<br><br>**Constraints**: *Maximum Length*: `64` |
| `product_file_credential_id` | `str` | Optional | Product File Credential Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `free_bytes` | `float` | Optional | Free Bytes |
| `byte_increment` | `float` | Optional | Byte Increment |
| `max_file_size_bytes` | `float` | Optional | Max File Size Bytes |
| `increment_cost` | `float` | Optional | Increment Cost |
| `monthly_fee` | `int` | Optional | Monthly Fee |
| `file_ext_allowed` | `str` | Optional | File Ext Allowed<br><br>**Constraints**: *Maximum Length*: `64` |
| `container` | `str` | Optional | Container<br><br>**Constraints**: *Maximum Length*: `128` |
| `id` | `str` | Optional | Product File Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `created_ts` | `int` | Optional | Created Time Stamp |
| `modified_ts` | `int` | Optional | Modified Time Stamp |
| `active` | `bool` | Optional | Active |
| `created_user_id` | `str` | Optional | User ID Created the register<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |

## Example (as JSON)

```json
{
  "title": "My terminal",
  "product_file_credential_id": "11e95f8ec39de8fbdb0a4f1a",
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "created_ts": 1422040992,
  "modified_ts": 1422040992,
  "active": true,
  "created_user_id": "11e95f8ec39de8fbdb0a4f1a",
  "free_bytes": 216.62,
  "byte_increment": 219.94,
  "max_file_size_bytes": 237.34
}
```

