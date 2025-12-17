
# Tokens Response

## Structure

`TokensResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `customer` | `str` | Optional | The Customer that this Token is associated with. |
| `payment` | `str` | Optional | The payment method that is associated with this Token. |
| `status` | [`TokenStatusEnum`](../../doc/models/token-status-enum.md) | Optional | Indicates if this token is ready for use in transactions and subscriptions or not.<br>A token without complete payment details will be marked as 'pending'.<br><br><details><br><summary>Valid Values</summary><br>- `pending` - **The payment data is not yet available, Token is not ready for use.**<br>- `ready` - **The payment data is available, Token is ready for use.**<br><br></details><br> |
| `token` | `str` | Optional | The auto-generated token identifier. |
| `track` | `str` | Optional | The magnetic stripe track data for the payment record for use in a transaction. |
| `cvv` | `str` | Optional | The CVV (Card Verification Value) for the payment record for use in a transaction |
| `expiration` | `str` | Optional | The expiry month for the payment method associated with this Token.<br>This field is stored as a text string in 'MMYY' format, where 'MM' is the number of a month and 'YY' is the last two digits of a year. For example, '0623' for June 2023.<br>The value must reflect a future date. |
| `name` | `str` | Optional | The name of this Token.<br>This field is stored as a text string and must be between 0 and 100 characters long. |
| `description` | `str` | Optional | A description of this Token.<br>This field is stored as a text string and must be between 0 and 100 characters long. |
| `custom` | `str` | Optional | Custom, free-form field for client-supplied text, must be between 0 and 1000 characters long. |
| `auth_token_customer` | `str` | Optional | The customer reference from the authToken used for user authentication |
| `origin` | `str` | Optional | The origin of the token. |
| `entry_mode` | `int` | Optional | Entry mode set to the token. |
| `omnitoken` | `str` | Optional | The omnitoken value. If this field has a value, the whole record is treated as an omnitoken. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "inactive": 0,
  "frozen": 0,
  "id": "id2",
  "created": "created2",
  "modified": "modified0",
  "creator": "String1",
  "modifier": "modifier6"
}
```

