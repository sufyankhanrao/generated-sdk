
# Alert Actions Response

## Structure

`AlertActionsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `mtype` | [`AlertActionTypeEnum`](../../doc/models/alert-action-type-enum.md) | Optional | The medium to use to deliver this Alert.<br><br><details><br><summary>Valid Values</summary><br>- `email` - **Deliver the Alert to an email address.**<br>- `web` - **Deliver the Alert through a web site notification.**<br>- `app` - **Deliver the Alert through a mobile application notification.**<br>- `sms` - **Deliver the Alert through an SMS message to a mobile device.**<br></details><br> |
| `options` | `str` | Optional | When the 'type' field of this resource is set to 'web', this field determines the format that the Alert data should be sent in. |
| `value` | `str` | Optional | A value used to deliver the alert. The field should be set to an email address if the type is email, an endpoint if the type is web, etc. |
| `header_name` | `str` | Optional | The request header name for authentication to the endpoint. |
| `header_value` | `str` | Optional | The request header value for authentication to the endpoint. |
| `retries` | `int` | Optional | The number of times an alert should be resent in case of a failure. This fields can only be set for web type alertActions. |
| `max_attempts_temp_disabled` | [`MaxAttemptsTempDisabledEnum`](../../doc/models/max-attempts-temp-disabled-enum.md) | Optional | Whether it was temporarily disabled for reaching the maximum number of failed attempts.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Temporarily Disabled**<br>- `1` - **Temporarily Disabled**<br></details><br> |
| `alert` | `str` | Optional | The identifier of the Alert resource that defines this alertAction. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "inactive": 0,
  "frozen": 0,
  "id": "id0",
  "created": "created0",
  "modified": "modified8",
  "creator": "String9",
  "modifier": "modifier4"
}
```

