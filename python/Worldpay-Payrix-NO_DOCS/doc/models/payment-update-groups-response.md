
# Payment Update Groups Response

## Structure

`PaymentUpdateGroupsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `entity` | `str` | Optional | The identifier of the Entity that this resource belongs to. |
| `processing` | `int` | Optional | Whether payment is processing. |
| `processed` | `int` | Optional | Whether payment is processed. |
| `number_updated` | [`NumberUpdatedEnum`](../../doc/models/number-updated-enum.md) | Optional | Whether payment number changes.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Updated**<br>- `1` - **Updated**<br></details><br> |
| `expiration_updated` | [`ExpirationUpdatedEnum`](../../doc/models/expiration-updated-enum.md) | Optional | Whether token expiration date changes.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Updated**<br>- `1` - **Updated**<br></details><br> |

## Example (as JSON)

```json
{
  "id": "id0",
  "created": "created0",
  "modified": "modified2",
  "creator": "String9",
  "modifier": "modifier6"
}
```

