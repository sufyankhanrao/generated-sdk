
# Subscriptions Post Request

## Structure

`SubscriptionsPostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plan` | `str` | Required | The identifier of the Plan that this Subscription is associated with. The Plan determines the frequency and amount of each payment. |
| `statement_entity` | `str` | Optional | For a plan that is attached to a billing, this is the paying entity to match to the generated statements of that billing for which the recurring payments will be made. |
| `first_txn` | `str` | Optional | The identification of the first transaction processed through this subscription. This is used internally to process subsequent transactions. |
| `start` | `int` | Required | The date on which the Subscription should start. The date is specified as an eight digit string in YYYYMMDD format, for example, '20160120' for January 20, 2016. The value of this field must represent a date in the future. |
| `finish` | `int` | Optional | The date on which the Subscription should finish. The date is specified as an eight digit string in YYYYMMDD format, for example, '20160120' for January 20, 2016. The value of this field must represent a date in the future. |
| `tax` | `int` | Optional | The amount of the total sum of this Subscription that is made up of tax. This field is specified as an integer in cents. |
| `descriptor` | `str` | Optional | The descriptor used in this Subscription. This field is stored as a text string and must be between 1 and 50 characters long. If a value is not set, an attempt is made to set a default value from the merchant information. |
| `txn_description` | `str` | Optional | The description of the Txn that will be created through this Subscription. |
| `order` | `str` | Optional | The order of the Txn that will be created through this Subscription. |
| `origin` | [`SubscriptionOriginEnum`](../../doc/models/subscription-origin-enum.md) | Required | The origin of the Txn that will be created through this Subscription.<br><br><details><br><summary>Valid Values</summary><br>- `2` - **Customer will be subscribing through eCommerce.**<br>- `3` - **Customer will be subscribing by Mail Order/Telephone.**<br>- `4` - **Originated with Apple Pay.**<br>- `5` - **Originated as a Successful 3D Secure transaction.**<br>- `6` - **Originated as an Attempted 3D Secure transaction.**<br>- `8` - **Originated in a Payframe.**<br></details><br>**Default**: `2`<br> |
| `authentication` | `str` | Required | Authentication token for 3D Secure transactions. |
| `authentication_id` | `str` | Optional | Authentication reference ID for 3D Secure transactions. |
| `failures` | `int` | Required | The current count of consecutive payment failures for this subscription. |
| `max_failures` | `int` | Optional | The maximum consecutive amount of payment failures to allow for this subscription before inactivating it. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Required | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Required | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "plan": "t1_pln_680064c9e9920768c5f7156",
  "statementEntity": "paying entity",
  "firstTxn": "t1_txn_680064d333e8a4e6cc85903",
  "start": 20250416,
  "finish": 20250416,
  "tax": 0,
  "descriptor": "Subscription Descriptor",
  "txnDescription": "subscription1",
  "order": "t183l8nsmsiq",
  "origin": 2,
  "authentication": "Authentication token",
  "authenticationId": "Authentication reference ID",
  "failures": 0,
  "maxFailures": 0,
  "inactive": 0,
  "frozen": 0
}
```

