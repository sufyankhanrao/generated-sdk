
# Token Post Request

## Structure

`TokenPostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer` | `str` | Required | The Customer that this Token is associated with. |
| `payment` | [`TokenPaymentParam`](../../doc/models/token-payment-param.md) | Required | The payment method that is associated with this Token. |
| `expiration` | `str` | Optional | The expiry month for the payment method associated with this Token.In This field is stored as a text string in 'MMYY' format, where 'MM' is the number of a month and 'YY' is the last two digits of a year. For example, '0623' for June 2023. The value must reflect a future date. |
| `name` | `str` | Optional | The name of this Token. This field is stored as a text string and must be between 0 and 100 characters long. |
| `description` | `str` | Optional | A description of this Token. This field is stored as a text string and must be between 0 and 100 characters long. |
| `custom` | `str` | Optional | Custom, free-form field for client-supplied text, must be between 0 and 1000 characters long. |
| `auth_token_customer` | `str` | Optional | The customer reference from the authToken used for user authentication |
| `origin` | `int` | Optional | The origin of the token. |
| `entry_mode` | `int` | Optional | Entry mode set to the token. |
| `omnitoken` | `str` | Optional | The omnitoken value. If this field has a value, the whole record is treated as an omnitoken. |
| `status` | [`TokenStatusEnum`](../../doc/models/token-status-enum.md) | Required | Indicates if this token is ready for use in transactions and subscriptions or not.<br>A token without complete payment details will be marked as 'pending'.<br><br><details><br><summary>Valid Values</summary><br>- `pending` - **The payment data is not yet available, Token is not ready for use.**<br>- `ready` - **The payment data is available, Token is ready for use.**<br><br></details><br> |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Required | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Required | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "customer": "t1_cus_00c82eb304b0067620c7",
  "status": "pending",
  "payment": {
    "method": 1,
    "number": "378734493671000",
    "routing": "code"
  },
  "expiration": "0123",
  "name": "test",
  "description": "test Token",
  "custom": "Custom Token Processor 2",
  "authTokenCustomer": "authToken",
  "origin": 2,
  "entryMode": 2,
  "omnitoken": "123",
  "inactive": 0,
  "frozen": 0
}
```

