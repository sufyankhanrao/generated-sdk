
# Token Results Response

## Structure

`TokenResultsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `txn` | `str` | Optional | The identifier of the Txn resource that this tokenResult relates to. |
| `token` | `str` | Optional | The identifier of the Token resource that this tokenResult relates to. |
| `merchant` | `str` | Optional | The identifier of the Merchant resource that this tokenResult relates to. |
| `code` | [`CodeEnum`](../../doc/models/code-enum.md) | Optional | The code type of the tokenResult.<br><br><details><br><summary>Valid Values</summary><br>- `omnitokenMinting` - **Indicates omnitoken minting event**<br>- `omnitokenLookup` - **Indicates omnitoken lookup event**<br>- `omnitokenUsage` - **Indicates omnitoken usage event**<br></details><br> |
| `omni_token` | `str` | Optional | The omniToken value. |

## Example (as JSON)

```json
{
  "id": "id0",
  "created": "created0",
  "modified": "modified8",
  "creator": "String9",
  "modifier": "modifier4"
}
```

